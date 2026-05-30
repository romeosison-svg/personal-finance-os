Begin or continue Phase 1 (Collect) of the active monthly finance review.

1. Find the most recent folder under `reviews/` (alphabetically last, excluding `2026-06-example`).
2. Read `collect.md` from that folder.
3. Check the phase status. If it is already `Complete`, tell the user collect is locked and suggest running `/reconcile`.
4. Set the phase status to `In Progress` if it was `Not Started`.
5. Present the input checklist to the user and work through it interactively:
   - Ask the user to confirm each item: obtained, not applicable, or pending.
   - Mark each item accordingly in the file.
   - For any item marked pending, ask why and note it.
6. Do not perform any analysis, calculate any balances, or make any observations about what the numbers mean. This phase is collection only.
7. When all checklist items are accounted for, ask the user: "Are you ready to lock Phase 1?"
8. If yes:
   - Set phase status to `Complete` in `collect.md`.
   - Record today's date as the completion date.
   - Update the phase status table in `collect.md` to reflect Collect = Complete.
   - Commit: `git commit -m "collect: phase 1 complete — YYYY-MM"`
   - Instruct the user to run `/reconcile` to begin Phase 2.
