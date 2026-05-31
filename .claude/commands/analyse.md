Begin or continue Phase 5 (Analyse) of the active monthly finance review.

1. Find the most recent folder under `reviews/` (alphabetically last, excluding `2026-06-example`).
2. Read `position.md` and confirm its phase status is `Complete`. If not, tell the user Phase 4 (Position) must be completed first and suggest running `position`.
3. Read `analyse.md` from that folder.
4. Check the phase status. If already `Complete`, tell the user the analysis is locked and suggest running `plan`.
5. Set the phase status to `In Progress` if it was `Not Started`.
6. Locate credit card statement files using the same priority order as collect and reconcile:
   a. Local: `reviews/YYYY-MM/statements/`
   b. Google Drive: folder ID `1D_U5sNk52firQcWsD6K1QBfmcsTCJxP0` (Finance OS / Statements)
7. Read all credit card statements. Focus on credit cards only — do not include current account transactions. Cards to analyse:
   - Romeo: Amex, Barclaycard, Halifax CC
   - Kelly: Amex, Halifax CC
   Note: Kelly's cards are self-funded this month but spending data is still valuable for pattern analysis.
8. For each card, extract all transactions from the statement period.
9. Categorise every transaction into one of the following categories:
   - Groceries
   - Dining & Restaurants
   - Coffee & Cafes
   - Takeaway & Fast Food
   - Transport & Travel
   - EV Charging
   - Entertainment & Events
   - Subscriptions & Streaming
   - Health & Medical
   - Sport & Fitness
   - Clothing & Retail
   - Household & Home
   - Children & Family
   - Business & Professional
   - Charity & Giving
   - Other
10. Produce a spending breakdown:
    - Per card: total spend, itemised by category
    - Household combined: total across all cards by category
    - Grand total household spend
11. Flag notable observations:
    - Highest spend categories
    - Recurring subscriptions (list each with monthly cost)
    - Any single transaction over £100
    - Any category that appears unusually high
    - Patterns worth noting for the plan or strategy phases
12. Do not make recommendations. Do not tell the user to spend less on anything. Surface patterns and facts only.
13. Write the analysis to `analyse.md`.
14. When complete, ask: "Are you ready to lock Phase 5?"
15. If yes:
    - Set phase status to `Complete` in `analyse.md`.
    - Record today's date.
    - Update the phase status table.
    - Commit: `git commit -m "analyse: phase 5 complete — YYYY-MM"`
    - Instruct the user to run `plan` to begin Phase 6.
