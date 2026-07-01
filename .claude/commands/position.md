Begin or continue Phase 4 (Position) of the active monthly finance review.

1. Find the most recent folder under `reviews/` (alphabetically last, excluding `2026-06-example`).
2. Read `reconcile.md` and `assumptions.md` and confirm both phase statuses are `Complete`. If either is not complete, tell the user which phase(s) must be completed first.
3. Read `position.md` from that folder.
4. Check the phase status. If already `Complete`, tell the user the position is locked and suggest running `/handoff`.
5. Set the phase status to `In Progress` if it was `Not Started`.
6. Using only the locked facts from `reconcile.md` and the locked assumptions from `assumptions.md`, calculate and record:
   - Total cash across all accounts
   - Total credit card balances owed
   - Total balance transfer balances owed
   - All known upcoming liabilities (with amounts and due dates)
   - Available funds: total cash minus preferred cash buffer minus known committed liabilities
7. Present the position summary to the user clearly, showing each calculation step.
8. Do not suggest what to pay or recommend any actions. The position describes the current state only.
9. When the position is fully calculated and the user has reviewed it, ask: "Are you ready to lock Phase 4?"
10. If yes:
    - Set phase status to `Complete` in `position.md`.
    - Record today's date.
    - Update the phase status table.
    - Commit: `git commit -m "position: phase 4 complete — YYYY-MM"`
    - Instruct the user to run `/handoff` to begin Phase 5.
