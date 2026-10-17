PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS schema_migrations (
    version TEXT PRIMARY KEY,
    applied_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS balance_observations (
    observation_id INTEGER PRIMARY KEY,
    component_key TEXT NOT NULL,
    source_record_id TEXT NOT NULL,
    as_of_date TEXT NOT NULL CHECK (as_of_date GLOB '????-??-??'),
    owner TEXT NOT NULL,
    component_name TEXT NOT NULL,
    category TEXT NOT NULL,
    balance_kind TEXT NOT NULL CHECK (balance_kind IN ('asset', 'liability')),
    native_currency TEXT NOT NULL,
    native_value_minor INTEGER NOT NULL,
    gbp_value_minor INTEGER NOT NULL,
    inclusion_scope TEXT NOT NULL CHECK (inclusion_scope IN ('financial', 'household')),
    valuation_status TEXT NOT NULL CHECK (valuation_status IN ('verified', 'estimated', 'pending', 'unknown')),
    source_ref TEXT NOT NULL,
    source_date TEXT NOT NULL,
    notes TEXT NOT NULL DEFAULT '',
    imported_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CHECK ((balance_kind = 'asset' AND gbp_value_minor >= 0)
        OR (balance_kind = 'liability' AND gbp_value_minor <= 0)),
    UNIQUE (source_record_id, as_of_date)
);

CREATE INDEX IF NOT EXISTS idx_finance_balance_component_date
    ON balance_observations(component_key, as_of_date DESC);

CREATE VIEW IF NOT EXISTS current_balances AS
WITH ranked AS (
    SELECT *, ROW_NUMBER() OVER (
        PARTITION BY component_key
        ORDER BY as_of_date DESC, observation_id DESC
    ) AS choice_rank
    FROM balance_observations
)
SELECT * FROM ranked WHERE choice_rank = 1;
