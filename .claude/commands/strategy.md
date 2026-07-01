Begin or continue Phase 10 (Strategy) of the active monthly finance review.

1. Find the most recent folder under `reviews/` (alphabetically last, excluding `2026-06-example`).
2. Read `plan.md` and confirm its phase status is `Complete`. If not, tell the user Phase 9 (Plan) must be completed first and suggest running `/plan`.
3. Read `strategy.md` from that folder.
4. Check the phase status. If already `Complete`, tell the user the monthly review is fully complete.
5. Set the phase status to `In Progress` if it was `Not Started`.
6. Read `docs/finance-profile.md` to understand the user's current long-term financial picture.
7. Review all open strategic items. For each item ask:
   - Is a decision needed this month, or can it be deferred?
   - If a decision is needed: what are the options and what does the user decide?
   - If deferred: when should it next be reviewed and why?
8. Common strategic items to check (only raise if relevant based on the profile):
   - Emergency fund progress toward target
   - BT card(s) — are they on pace to clear before promotional rate expires?
   - Vehicle finance — any decisions upcoming?
   - Pension or investment decisions
   - Business financial decisions
9. Record all decisions with reasoning and all deferrals with next review dates in `strategy.md`.
10. If any decisions change a persistent assumption, ask the user whether `docs/finance-profile.md` should be updated. If yes, update it and commit separately: `git commit -m "finance-profile: update [what changed] — YYYY-MM"`
11. When all strategic items are reviewed, ask: "Are you ready to lock Phase 10 and close this monthly review?"
12. If yes:
    - Set phase status to `Complete` in `strategy.md`.
    - Record today's date.
    - Update the phase status table.
    - Commit: `git commit -m "strategy: phase 10 complete — YYYY-MM"`
    - Confirm to the user that the monthly review is complete.
