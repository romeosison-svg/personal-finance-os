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
4. Also create an empty `reviews/YYYY-MM/statements/` subfolder (create a `.gitkeep` file inside it so the folder exists but remains empty in git — the folder itself is gitignored so statement files dropped here will never be committed).
5. Each phase file should contain its corresponding phase template from `docs/monthly-review-template.md`, with the month and year substituted into the heading.
6. All phase statuses should be set to `Not Started`.
7. Confirm to the user that the review folder is ready. Tell them:
   "Drop your bank statements, credit card statements, and any CSVs into reviews/YYYY-MM/statements/ before running collect. PDFs, CSVs, and screenshots all work. Those files stay local and are never committed to git."
   Then instruct them to run `collect` to begin Phase 1.
