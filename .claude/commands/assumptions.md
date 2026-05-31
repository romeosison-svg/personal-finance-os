Begin or continue Phase 3 (Assumptions) of the active monthly finance review.

1. Find the most recent folder under `reviews/` (alphabetically last, excluding `2026-06-example`).
2. Read `reconcile.md` and confirm its phase status is `Complete`. If not, tell the user Phase 2 (Reconcile) must be completed first and suggest running `/reconcile`.
3. Read `assumptions.md` from that folder.
4. Check the phase status. If already `Complete`, tell the user assumptions are locked and suggest running `/position`.
5. Set the phase status to `In Progress` if it was `Not Started`.
6. Read `docs/finance-profile.md` to load the persistent planning assumptions.
7. Present each assumption to the user one at a time and ask: "Is this still correct for this month?"
   - Minimum cash buffer
   - Preferred cash buffer
   - Mortgage split methodology
   - Bill split methodology
   - BT monthly repayment target(s)
   - Emergency fund monthly contribution
8. For each assumption:
   - If confirmed: record as-is in `assumptions.md`.
   - If overridden: record the override value and ask for the reason. Document both the normal value and the override value.
9. Do not apply the assumptions yet. Do not calculate anything. This phase only confirms the rules.
10. When all assumptions are confirmed or overridden, ask: "Are you ready to lock Phase 3?"
11. If yes:
    - Set phase status to `Complete` in `assumptions.md`.
    - Record today's date.
    - Update the phase status table.
    - Commit: `git commit -m "assumptions: phase 3 complete — YYYY-MM"`
    - Instruct the user to run `/position` to begin Phase 4.
