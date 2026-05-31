Begin or continue Phase 5 (Plan) of the active monthly finance review.

1. Find the most recent folder under `reviews/` (alphabetically last, excluding `2026-06-example`).
2. Read `position.md` and confirm its phase status is `Complete`. If not, tell the user Phase 4 (Position) must be completed first and suggest running `/position`.
3. Read `plan.md` from that folder.
4. Check the phase status. If already `Complete`, tell the user the plan is locked and suggest running `/strategy`.
5. Set the phase status to `In Progress` if it was `Not Started`.
6. Read the available funds figure from `position.md` and the locked assumptions from `assumptions.md`.
7. Build the payment plan by working through allocations in priority order (per `docs/finance-profile.md`):
   - Mortgage payment (with split methodology applied)
   - Bill payments (with split methodology applied)
   - Minimum credit card payments
   - BT repayments to hit monthly targets
   - Emergency fund contribution (unless overridden in assumptions)
   - Remaining credit card balance payment if funds allow
8. After each allocation, show the running total of allocated funds and remaining available funds.
9. If allocations exceed available funds, flag the shortfall immediately and ask the user how to resolve it before continuing.
10. When all allocations are complete, show the full plan table and the reconciliation (available funds minus total allocated = surplus or shortfall).
11. Ask the user: "Do you approve this plan?"
12. If approved:
    - Set phase status to `Complete` in `plan.md`.
    - Record today's date.
    - Update the phase status table.
    - Commit: `git commit -m "plan: phase 5 complete — YYYY-MM"`
    - Instruct the user to run `/strategy` to begin Phase 6.
