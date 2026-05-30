Start a new monthly finance review.

1. Ask the user: "Which month is this review for? (e.g. 2026-07)"
2. Create the folder `reviews/YYYY-MM/` using the month they provide.
3. Create six files in that folder by copying the phase templates from `docs/monthly-review-template.md`:
   - `collect.md`
   - `reconcile.md`
   - `assumptions.md`
   - `position.md`
   - `plan.md`
   - `strategy.md`
4. Each file should contain its corresponding phase template from `docs/monthly-review-template.md`, with the month and year substituted into the heading.
5. All phase statuses should be set to `Not Started`.
6. Confirm to the user that the review folder is ready and instruct them to run `/collect` to begin Phase 1.
