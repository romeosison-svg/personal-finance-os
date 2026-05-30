Begin or continue Phase 1 (Collect) of the active monthly finance review.

1. Find the most recent folder under `reviews/` (alphabetically last, excluding `2026-06-example`).
2. Check whether a `statements/` subfolder exists inside that review folder. If it does not, tell the user:
   "Drop your statement files into reviews/YYYY-MM/statements/ — PDFs, CSVs, or screenshots all work. That folder is gitignored so files stay local and are never committed."
   Wait for the user to confirm files are in place before continuing, or let them proceed without files if they prefer to enter figures manually.
3. If statement files are present, list them so the user can see what has been found.
4. Read `collect.md` from that folder.
5. Check the phase status. If it is already `Complete`, tell the user collect is locked and suggest running `reconcile`.
6. Set the phase status to `In Progress` if it was `Not Started`.
7. Present the input checklist to the user and work through it interactively:
   - For each checklist item, check whether a corresponding file exists in `statements/`. If yes, mark it as obtained automatically.
   - For items with no file, ask the user to confirm: obtained (file elsewhere), not applicable, or pending.
   - Mark each item accordingly in the file.
   - For any item marked pending, ask why and note it.
8. Do not perform any analysis, calculate any balances, or make any observations about what the numbers mean. This phase is collection only.
9. When all checklist items are accounted for, ask the user: "Are you ready to lock Phase 1?"
10. If yes:
    - Set phase status to `Complete` in `collect.md`.
    - Record today's date as the completion date.
    - Update the phase status table in `collect.md` to reflect Collect = Complete.
    - Commit: `git commit -m "collect: phase 1 complete — YYYY-MM"`
    - Instruct the user to run `reconcile` to begin Phase 2.
