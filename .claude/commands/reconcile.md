Begin or continue Phase 2 (Reconcile) of the active monthly finance review.

1. Find the most recent folder under `reviews/` (alphabetically last, excluding `2026-06-example`).
2. Read `collect.md` and confirm its phase status is `Complete`. If it is not, tell the user that Phase 1 (Collect) must be completed first and suggest running `/collect`.
3. Read `reconcile.md` from that folder.
4. Check the phase status. If it is already `Complete`, tell the user reconcile is locked and suggest running `/assumptions`.
5. Set the phase status to `In Progress` if it was `Not Started`.
6. Locate statement files using this priority order:
   a. Local: check `reviews/YYYY-MM/statements/` for files.
   b. Google Drive: if local is empty, use the Google Drive MCP to list and read files from folder ID `1D_U5sNk52firQcWsD6K1QBfmcsTCJxP0` (Finance OS / Statements).
   If files are found in either location, read them to extract balances and transactions directly. Supported formats: PDF statements, CSV exports, screenshots.
7. Work through the reconcile file with the user:
   - For each account identified in collect: if a statement file exists, read it and extract the closing balance, statement date, and any payments. Present what you found and ask the user to confirm or correct.
   - If no statement file exists for an account, ask the user to provide the figures manually.
   - Ask for any payments made since the statement date (not captured in the file).
   - Calculate the current outstanding balance (statement balance minus payments since statement).
   - Ask about any pending reimbursements and match them to statement periods.
   - Ask the user to confirm all scheduled direct debits.
   - Note any discrepancies explicitly.
7. Record all facts in `reconcile.md`. Do not make recommendations. Do not suggest what to pay. This phase establishes what is true, not what should happen.
8. When all accounts are reconciled, ask: "Are you ready to lock Phase 2?"
9. If yes:
   - Set phase status to `Complete` in `reconcile.md`.
   - Record today's date.
   - Update the phase status table in `reconcile.md`.
   - Commit: `git commit -m "reconcile: phase 2 complete — YYYY-MM"`
   - Instruct the user to run `/assumptions` to begin Phase 3.
