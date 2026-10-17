# Net Worth Database

FinanceOS stores normalized historical household cash and consumer-debt balances in a local SQLite database. The phase-gated Markdown files and dated CSV exports remain the review audit trail.

The completed handoff phase publishes `reviews/YYYY-MM/net-worth-export.csv` as a derived factual export. It contains no recommendations or planning decisions and must not introduce facts that are absent from the locked Position. PortfolioOS imports this file read-only and remains responsible for the consolidated household net-worth view. New reviews start from `templates/net-worth-export-template.csv`.

The default local database is `private-data/finance.sqlite`; it is ignored by Git because it is a sensitive binary working file. Build or refresh it with:

```bash
python3 scripts/net_worth_db.py refresh
python3 scripts/net_worth_db.py report
python3 scripts/net_worth_db.py reserve-report
```

`refresh` loads the newest locked `reviews/YYYY-MM/net-worth-export.csv`, then applies dated post-lock operational balance observations from `data/current-balance-observations.csv` and imports the operating-reserve ledger. It does not rewrite a locked review artefact.

Stable `component_key` values are the cross-repository identity contract. Amounts are signed: assets are positive and liabilities are negative. Money is stored as integer minor units in SQLite to avoid floating-point rounding.

The September 2026 export intentionally excludes the mortgage because the current FinanceOS handoff contains the monthly mortgage commitment but not a reconciled outstanding mortgage balance. PortfolioOS temporarily remains authoritative for that balance.

## Operating reserves

Operating reserves are designations of cash already included in balance observations. They are not extra assets and must never be added to net worth a second time.

- `data/operating-reserves.csv` defines each reserve and its authority.
- `data/reserve-ledger.csv` is a signed event ledger by physical location.
- `data/reserve-targets.csv` records dated required balances or floors.
- `current_operating_reserves` reports booked, pending and projected balances against the latest target.
- `reserve_location_balances` shows where each reserve is held.
- `reserve_transfer_audit` exposes unbalanced transfer groups; a valid internal transfer has two entries and nets to zero.

A movement such as Cynergy to Lloyds is recorded with equal negative and positive transfer entries, so it changes location but not the reserve total. The later card payment is the event that reduces the reserve. Pending entries remain separate from booked cash.
