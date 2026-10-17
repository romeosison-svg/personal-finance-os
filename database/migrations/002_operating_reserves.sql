PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS operating_reserves (
    reserve_key TEXT PRIMARY KEY,
    reserve_name TEXT NOT NULL,
    owner TEXT NOT NULL,
    currency TEXT NOT NULL DEFAULT 'GBP',
    purpose TEXT NOT NULL,
    authoritative_source TEXT NOT NULL CHECK (authoritative_source IN ('finance_os', 'portfolio_os')),
    status TEXT NOT NULL CHECK (status IN ('active', 'released', 'closed')),
    linked_component_key TEXT,
    notes TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS reserve_entries (
    entry_key TEXT PRIMARY KEY,
    reserve_key TEXT NOT NULL REFERENCES operating_reserves(reserve_key),
    effective_date TEXT NOT NULL CHECK (effective_date GLOB '????-??-??'),
    location_key TEXT NOT NULL,
    entry_type TEXT NOT NULL CHECK (entry_type IN (
        'opening_balance', 'funding', 'transfer', 'spend', 'release', 'interest', 'adjustment'
    )),
    amount_minor INTEGER NOT NULL,
    verification_status TEXT NOT NULL CHECK (verification_status IN ('verified', 'estimated', 'pending', 'unknown')),
    source_system TEXT NOT NULL CHECK (source_system IN ('finance_os', 'portfolio_os')),
    source_ref TEXT NOT NULL,
    source_date TEXT,
    transfer_group_key TEXT,
    notes TEXT NOT NULL DEFAULT '',
    imported_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_reserve_entries_reserve_date
    ON reserve_entries(reserve_key, effective_date, entry_key);

CREATE INDEX IF NOT EXISTS idx_reserve_entries_location
    ON reserve_entries(location_key, effective_date, entry_key);

CREATE TABLE IF NOT EXISTS reserve_target_observations (
    target_key TEXT PRIMARY KEY,
    reserve_key TEXT NOT NULL REFERENCES operating_reserves(reserve_key),
    as_of_date TEXT NOT NULL CHECK (as_of_date GLOB '????-??-??'),
    target_minor INTEGER NOT NULL CHECK (target_minor >= 0),
    verification_status TEXT NOT NULL CHECK (verification_status IN ('verified', 'estimated', 'pending', 'unknown')),
    source_system TEXT NOT NULL CHECK (source_system IN ('finance_os', 'portfolio_os')),
    source_ref TEXT NOT NULL,
    source_date TEXT,
    notes TEXT NOT NULL DEFAULT '',
    imported_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_reserve_targets_reserve_date
    ON reserve_target_observations(reserve_key, as_of_date DESC, target_key);

CREATE VIEW IF NOT EXISTS current_reserve_targets AS
WITH ranked AS (
    SELECT *, ROW_NUMBER() OVER (
        PARTITION BY reserve_key
        ORDER BY as_of_date DESC, target_key DESC
    ) AS choice_rank
    FROM reserve_target_observations
)
SELECT * FROM ranked WHERE choice_rank = 1;

CREATE VIEW IF NOT EXISTS reserve_location_balances AS
SELECT
    reserve_key,
    location_key,
    SUM(CASE WHEN verification_status = 'verified' THEN amount_minor ELSE 0 END) AS booked_minor,
    SUM(CASE WHEN verification_status = 'pending' THEN amount_minor ELSE 0 END) AS pending_minor
FROM reserve_entries
GROUP BY reserve_key, location_key;

CREATE VIEW IF NOT EXISTS current_operating_reserves AS
WITH balances AS (
    SELECT
        reserve_key,
        SUM(CASE WHEN verification_status = 'verified' THEN amount_minor ELSE 0 END) AS booked_minor,
        SUM(CASE WHEN verification_status = 'pending' THEN amount_minor ELSE 0 END) AS pending_minor
    FROM reserve_entries
    GROUP BY reserve_key
)
SELECT
    r.reserve_key,
    r.reserve_name,
    r.owner,
    r.currency,
    r.purpose,
    r.authoritative_source,
    r.status,
    r.linked_component_key,
    COALESCE(b.booked_minor, 0) AS booked_minor,
    COALESCE(b.pending_minor, 0) AS pending_minor,
    COALESCE(b.booked_minor, 0) + COALESCE(b.pending_minor, 0) AS projected_minor,
    t.target_minor,
    CASE WHEN t.target_minor IS NULL THEN NULL ELSE COALESCE(b.booked_minor, 0) - t.target_minor END AS variance_minor,
    t.as_of_date AS target_as_of_date,
    r.notes
FROM operating_reserves r
LEFT JOIN balances b USING (reserve_key)
LEFT JOIN current_reserve_targets t USING (reserve_key);

CREATE VIEW IF NOT EXISTS reserve_transfer_audit AS
SELECT
    transfer_group_key,
    COUNT(*) AS entry_count,
    SUM(amount_minor) AS net_minor,
    MIN(verification_status) AS first_status,
    MAX(verification_status) AS last_status
FROM reserve_entries
WHERE transfer_group_key IS NOT NULL
GROUP BY transfer_group_key;
