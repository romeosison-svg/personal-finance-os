Begin or continue Phase 1 (Collect) of the active monthly finance review.

1. Find the most recent folder under `reviews/` (alphabetically last, excluding `2026-06-example`).
2. Locate statement files using this priority order:
   a. Local: check whether a `statements/` subfolder exists inside that review folder and list any files found.
   b. Google Drive: if local statements/ is empty or absent, use the Google Drive MCP to list files in folder ID `1D_U5sNk52firQcWsD6K1QBfmcsTCJxP0` (Finance OS / Statements).
   c. If neither has files, tell the user: "No statement files found locally or in Google Drive (Finance OS / Statements). You can drop files into either location, or proceed and enter figures manually."
3. Build the statements map:
   - For each file found, read its contents to determine: statement period (YYYY-MM), account holder name, institution, and account type (e.g. current, savings, credit, mortgage).
   - For any file where the contents are ambiguous, flag it and ask the user to supply the missing detail.
   - Derive a normalised name for each file using the convention: `YYYY-MM_<person>_<institution>_<account-type>`
     Examples: `2026-06_Kelly_Halifax_current`, `2026-06_Kelly_Amex_credit`
   - Write (or overwrite) `reviews/YYYY-MM/statements.md` with a mapping table in this format:

     | Normalised name | Original filename | Source |
     |---|---|---|
     | 2026-06_Kelly_Halifax_current | Jun2026_statement_012345.pdf | Google Drive |
     | 2026-06_Kelly_Amex_credit | AMEX_eStatement_2026-06-01.pdf | Google Drive |

   - Do not rename or move any files. The original files stay exactly as they are.
4. Present the statements map to the user and ask them to confirm it is correct before continuing.
5. Read `collect.md` from that folder.
6. Check the phase status. If it is already `Complete`, tell the user collect is locked and suggest running `reconcile`.
7. Set the phase status to `In Progress` if it was `Not Started`.
8. Present the input checklist to the user and work through it interactively:
   - For each checklist item, check whether a corresponding entry exists in `statements.md`. If yes, mark it as obtained automatically.
   - For items with no entry, ask the user to confirm: obtained (file elsewhere), not applicable, or pending.
   - Mark each item accordingly in the file.
   - For any item marked pending, ask why and note it.
9. Do not perform any analysis, calculate any balances, or make any observations about what the numbers mean. This phase is collection only.
10. When all checklist items are accounted for, ask the user: "Are you ready to lock Phase 1?"
11. If yes:
    - Set phase status to `Complete` in `collect.md`.
    - Record today's date as the completion date.
    - Update the phase status table in `collect.md` to reflect Collect = Complete.
    - Commit: `git commit -m "collect: phase 1 complete — YYYY-MM"`
    - Instruct the user to run `reconcile` to begin Phase 2.
