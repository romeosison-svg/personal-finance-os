Report the current status of the active monthly finance review.

1. Find the most recent folder under `reviews/` (by folder name, alphabetically last — this is the active review).
2. Read the phase status table from each of the ten phase files: `collect.md`, `reconcile.md`, `assumptions.md`, `position.md`, `handoff.md`, `analyse.md`, `budget-calibration.md`, `affordability-check.md`, `plan.md`, `strategy.md`.
3. Report a single consolidated status table:

| Phase       | Status      | Completed  |
| ----------- | ----------- | ---------- |
| Collect     | ...         | ...        |
| Reconcile   | ...         | ...        |
| Assumptions | ...         | ...        |
| Position    | ...         | ...        |
| Handoff     | ...         | ...        |
| Analyse     | ...         | ...        |
| Budget Calibration | ...  | ...        |
| Affordability Check | ... | ...        |
| Plan        | ...         | ...        |
| Strategy    | ...         | ...        |

4. State clearly:
   - Which phase was last completed
   - Which phase is currently active
   - Any phases marked Blocked and why
   - What command to run next

If no review folder exists under `reviews/` (other than the example), tell the user to run `/finance-start` to begin a new review.
