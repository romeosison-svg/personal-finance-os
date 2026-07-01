Begin or continue Phase 5 (Handoff) of the active monthly finance review.

This phase exports verified facts and transaction data. It is the formal boundary between factual work and judgement work.

1. Find the most recent folder under `reviews/` (alphabetically last, excluding `2026-06-example`).
2. Read `position.md` and confirm phase status is `Complete`. If not complete, tell the user position must be completed first.
3. Check whether `handoff.md` exists in the review folder. If not, create it from the `handoff.md` section in `docs/monthly-review-template.md`.
4. Check whether `position-handoff.md` exists in the review folder. If not, copy from `templates/position-handoff-template.md`.
5. Check whether `transactions.csv` exists in the review folder. If not, copy from `templates/transactions-template.csv`.
6. Populate `position-handoff.md` using verified data from `reconcile.md`, `assumptions.md`, and `position.md`:
   - Section 1: list source artefacts used
   - Section 2: confirm phase statuses (collect, reconcile, assumptions, position all Complete)
   - Section 3: populate locked planning assumptions from `assumptions.md`
   - Section 4: populate current financial position from `position.md` and `reconcile.md`
   - Section 5: populate balance transfer position from `position.md`
   - Section 6: populate credit card position from `position.md` and `reconcile.md`
   - Section 7: populate known monthly obligations from `position.md`
   - Section 8: include open questions (standard questions plus any month-specific questions)
   - Section 9: constraints for later phases (use template defaults)
7. Do NOT include any categorisation, analysis, recommendations, or strategic advice in `position-handoff.md`.
8. Populate `transactions.csv` with raw transaction data from the statements:
   - Columns: date, owner, account, card_provider, merchant, description, amount, type, statement_period, notes
   - Do not categorise transactions. Preserve raw merchant/description text.
   - If transaction type is unclear, set type to `unknown`.
   - If ownership cannot be determined, set owner to `unknown` and note in notes column.
   - If statement data is not available in the repo or Drive, create the file with headers only and document the gap in `position-handoff.md`.
9. Present all handoff artefacts to the user for review. Confirm completeness.
10. When the user confirms all files are complete and accurate, ask: "Are you ready to lock Phase 5 and commit the handoff artefacts?"
11. If yes:
    - Stage all files: `handoff.md`, `position-handoff.md`, and `transactions.csv`
    - Commit: `git commit -m "handoff: phase 5 complete — YYYY-MM"`
    - Tell the user: "Handoff complete. Run `analyse` to begin Phase 6."
