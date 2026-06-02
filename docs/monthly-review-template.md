# Monthly Review Template

Copy this structure into a new folder under `/reviews/YYYY-MM/` when starting a new monthly review.

Create phase files:
- `collect.md`
- `reconcile.md`
- `assumptions.md`
- `position.md`
- `analyse.md`
- `budget-calibration.md`
- `affordability-check.md`
- `plan.md`
- `strategy.md`

Create handoff artefacts (populated during the handoff phase):
- `position-handoff.md` — from `templates/position-handoff-template.md`
- `transactions.csv` — from `templates/transactions-template.csv`

---

## Phase Status Dashboard

Copy this table into each phase file header and update as phases complete.

| Phase                | Owner       | Status      | Completed  |
| -------------------- | ----------- | ----------- | ---------- |
| Collect              | Claude Code | Not Started |            |
| Reconcile            | Claude Code | Not Started |            |
| Assumptions          | Claude Code | Not Started |            |
| Position             | Claude Code | Not Started |            |
| Handoff              | Claude Code | Not Started |            |
| Analyse              | ChatGPT     | Not Started |            |
| Budget Calibration   | ChatGPT     | Not Started |            |
| Affordability Check  | ChatGPT     | Not Started |            |
| Plan                 | ChatGPT     | Not Started |            |
| Strategy             | ChatGPT     | Not Started |            |

---

---

## collect.md Template

```markdown
# Collect — [Month] [Year]

## Phase Status

| Phase                | Status      | Completed  |
| -------------------- | ----------- | ---------- |
| Collect              | In Progress |            |
| Reconcile            | Not Started |            |
| Assumptions          | Not Started |            |
| Position             | Not Started |            |
| Handoff              | Not Started |            |
| Analyse              | Not Started |            |
| Budget Calibration   | Not Started |            |
| Affordability Check  | Not Started |            |
| Plan                 | Not Started |            |
| Strategy             | Not Started |            |

---

## Input Checklist

### Bank Accounts

- [ ] Current account statement — [Bank Name]
- [ ] Savings account statement — [Bank Name]
- [ ] Joint account statement — [Bank Name]
- [ ] Any other accounts

### Credit Cards

- [ ] Credit card statement — [Card Name]
- [ ] Credit card statement — [Card Name]
- [ ] Balance transfer card statement — [Card Name]

### Other Inputs

- [ ] Reimbursement spreadsheet (if applicable)
- [ ] Upcoming direct debits list confirmed
- [ ] Any known one-off payments this month
- [ ] Any expected income beyond regular salary

---

## Notes

<!-- Document anything unusual about inputs this month:
     missing statements, delays, anomalies, items to chase -->

---

## Phase Lock

Status: <!-- Not Started / In Progress / Complete / Blocked -->
Completed: <!-- YYYY-MM-DD -->
Locked by: <!-- Your name -->

All inputs confirmed present. Proceeding to Reconcile.
```

---

---

## reconcile.md Template

```markdown
# Reconcile — [Month] [Year]

> Requires: Collect complete

## Phase Status

| Phase                | Status      | Completed  |
| -------------------- | ----------- | ---------- |
| Collect              | Complete    | YYYY-MM-DD |
| Reconcile            | In Progress |            |
| Assumptions          | Not Started |            |
| Position             | Not Started |            |
| Handoff              | Not Started |            |
| Analyse              | Not Started |            |
| Budget Calibration   | Not Started |            |
| Affordability Check  | Not Started |            |
| Plan                 | Not Started |            |
| Strategy             | Not Started |            |

---

## Account Balances (Statement Date: YYYY-MM-DD)

| Account         | Statement Balance | Payments Since | Outstanding | Confirmed Balance |
| --------------- | ----------------- | -------------- | ----------- | ----------------- |
| Current Account | £                 | £              | £           | £                 |
| Savings Account | £                 | £              | £           | £                 |
| Credit Card 1   | £                 | £              | £           | £                 |
| BT Card         | £                 | £              | £           | £                 |

---

## Reimbursements

| Description | Amount | Statement Period | Status   |
| ----------- | ------ | ---------------- | -------- |
|             | £      |                  | Pending  |

---

## Scheduled Payments Confirmed

| Payment         | Amount | Date       | Account  | Confirmed |
| --------------- | ------ | ---------- | -------- | --------- |
| Mortgage        | £      | YYYY-MM-DD |          | [ ]       |
| Council Tax     | £      | YYYY-MM-DD |          | [ ]       |

---

## Discrepancies

<!-- Note any amounts that don't reconcile, items to investigate, or unresolved items -->

---

## Phase Lock

Status: <!-- Not Started / In Progress / Complete / Blocked -->
Completed: <!-- YYYY-MM-DD -->

Financial facts locked. No further changes to balances without documented reason.
```

---

---

## assumptions.md Template

```markdown
# Assumptions — [Month] [Year]

> Requires: Reconcile complete

## Phase Status

| Phase                | Status      | Completed  |
| -------------------- | ----------- | ---------- |
| Collect              | Complete    | YYYY-MM-DD |
| Reconcile            | Complete    | YYYY-MM-DD |
| Assumptions          | In Progress |            |
| Position             | Not Started |            |
| Handoff              | Not Started |            |
| Analyse              | Not Started |            |
| Budget Calibration   | Not Started |            |
| Affordability Check  | Not Started |            |
| Plan                 | Not Started |            |
| Strategy             | Not Started |            |

---

## Planning Assumptions — This Month

Review each assumption against [finance-profile.md](/docs/finance-profile.md).
Confirm or override for this month.

| Assumption              | Profile Value | This Month Value | Override? | Reason      |
| ----------------------- | ------------- | ---------------- | --------- | ----------- |
| Minimum cash buffer     | £             | £                | No        |             |
| Preferred cash buffer   | £             | £                | No        |             |
| Mortgage split method   |               |                  | No        |             |
| Bill split method       |               |                  | No        |             |
| BT monthly target       | £             | £                | No        |             |
| Emergency fund contrib. | £             | £                | No        |             |

---

## One-Time Overrides

<!-- Document any assumptions changed for this month only -->

---

## Phase Lock

Status: <!-- Not Started / In Progress / Complete / Blocked -->
Completed: <!-- YYYY-MM-DD -->

Planning assumptions locked for this review.
```

---

---

## position.md Template

```markdown
# Position — [Month] [Year]

> Requires: Reconcile + Assumptions complete

## Phase Status

| Phase                | Status      | Completed  |
| -------------------- | ----------- | ---------- |
| Collect              | Complete    | YYYY-MM-DD |
| Reconcile            | Complete    | YYYY-MM-DD |
| Assumptions          | Complete    | YYYY-MM-DD |
| Position             | In Progress |            |
| Handoff              | Not Started |            |
| Analyse              | Not Started |            |
| Budget Calibration   | Not Started |            |
| Affordability Check  | Not Started |            |
| Plan                 | Not Started |            |
| Strategy             | Not Started |            |

---

## Current Financial Position (as of YYYY-MM-DD)

### Cash

| Account         | Balance |
| --------------- | ------- |
| Current Account | £       |
| Savings Account | £       |
| **Total Cash**  | **£**   |

### Credit

| Account       | Balance Owed | Limit | Available |
| ------------- | ------------ | ----- | --------- |
| Credit Card 1 | £            | £     | £         |
| BT Card       | £            | £     | £         |
| **Total Owed**| **£**        |       |           |

### Net Position

| Item                      | Amount |
| ------------------------- | ------ |
| Total cash                | £      |
| Less: minimum buffer      | £      |
| Less: known liabilities   | £      |
| **Available for planning**| **£**  |

---

## Known Upcoming Liabilities

| Item          | Amount | Due Date   | Account  |
| ------------- | ------ | ---------- | -------- |
|               | £      | YYYY-MM-DD |          |

---

## Phase Lock

Status: <!-- Not Started / In Progress / Complete / Blocked -->
Completed: <!-- YYYY-MM-DD -->

Financial position locked. Available for planning: £[amount]
```

---

---

## position-handoff.md Template

See `templates/position-handoff-template.md` for the full template.

When creating a new review, copy that template to `reviews/YYYY-MM/position-handoff.md` and populate during the handoff phase.

Artefacts required:
- `reviews/YYYY-MM/position-handoff.md` — from `templates/position-handoff-template.md`
- `reviews/YYYY-MM/transactions.csv` — from `templates/transactions-template.csv`

Both files must be committed before ChatGPT begins analyse.

---

---

## analyse.md Template

```markdown
# Analyse — [Month] [Year]

> Requires: Position complete

## Phase Status

| Phase                | Status      | Completed  |
| -------------------- | ----------- | ---------- |
| Collect              | Complete    | YYYY-MM-DD |
| Reconcile            | Complete    | YYYY-MM-DD |
| Assumptions          | Complete    | YYYY-MM-DD |
| Position             | Complete    | YYYY-MM-DD |
| Handoff              | Complete    | YYYY-MM-DD |
| Analyse              | In Progress |            |
| Budget Calibration   | Not Started |            |
| Affordability Check  | Not Started |            |
| Plan                 | Not Started |            |
| Strategy             | Not Started |            |

---

## Credit Card Spending — [Month] [Year]

### Romeo — Amex (statement period: DD MMM – DD MMM YYYY)

| Category | Amount |
| --- | --- |
| Groceries | £ |
| Dining & Restaurants | £ |
| Coffee & Cafes | £ |
| Takeaway & Fast Food | £ |
| Transport & Travel | £ |
| EV Charging | £ |
| Entertainment & Events | £ |
| Subscriptions & Streaming | £ |
| Health & Medical | £ |
| Sport & Fitness | £ |
| Clothing & Retail | £ |
| Household & Home | £ |
| Business & Professional | £ |
| Charity & Giving | £ |
| Other | £ |
| **Total** | **£** |

### Romeo — Barclaycard

<!-- same category table -->

### Romeo — Halifax CC

<!-- same category table -->

### Kelly — Amex

<!-- same category table -->

### Kelly — Halifax CC

<!-- same category table -->

---

## Household Combined

| Category | Romeo Total | Kelly Total | Household Total |
| --- | --- | --- | --- |
| Groceries | £ | £ | £ |
| Dining & Restaurants | £ | £ | £ |
| Coffee & Cafes | £ | £ | £ |
| Takeaway & Fast Food | £ | £ | £ |
| Transport & Travel | £ | £ | £ |
| EV Charging | £ | £ | £ |
| Entertainment & Events | £ | £ | £ |
| Subscriptions & Streaming | £ | £ | £ |
| Health & Medical | £ | £ | £ |
| Sport & Fitness | £ | £ | £ |
| Clothing & Retail | £ | £ | £ |
| Household & Home | £ | £ | £ |
| Business & Professional | £ | £ | £ |
| Charity & Giving | £ | £ | £ |
| Other | £ | £ | £ |
| **Total** | **£** | **£** | **£** |

---

## Subscriptions Identified

| Subscription | Card | Monthly Cost |
| --- | --- | --- |
| | | £ |

---

## Notable Observations

<!-- Highest spend categories, large single transactions, patterns worth noting.
     Facts and patterns only — no recommendations. -->

---

## Phase Lock

Status: <!-- Not Started / In Progress / Complete / Blocked -->
Completed: <!-- YYYY-MM-DD -->

Spending analysis locked.
```

---

---

## budget-calibration.md Template

```markdown
# Budget Calibration — [Month] [Year]

> Requires: Analyse complete

> **This file is ChatGPT-owned.** Do not populate manually. Import using: `import budget-calibration`

## Phase Status

| Phase                | Status      | Completed  |
| -------------------- | ----------- | ---------- |
| Collect              | Complete    | YYYY-MM-DD |
| Reconcile            | Complete    | YYYY-MM-DD |
| Assumptions          | Complete    | YYYY-MM-DD |
| Position             | Complete    | YYYY-MM-DD |
| Handoff              | Complete    | YYYY-MM-DD |
| Analyse              | Complete    | YYYY-MM-DD |
| Budget Calibration   | In Progress |            |
| Affordability Check  | Not Started |            |
| Plan                 | Not Started |            |
| Strategy             | Not Started |            |

---

_Content imported from ChatGPT._
```

---

---

## affordability-check.md Template

```markdown
# Affordability Check — [Month] [Year]

> Requires: Budget Calibration complete

> **This file is ChatGPT-owned.** Do not populate manually. Import using: `import affordability-check`

Budget Calibration answers: what are sensible behavioural spending caps?
Affordability Check answers: can those caps actually be funded from current cashflow?
Plan answers: what actions should be taken now given the affordable limits?

## Phase Status

| Phase                | Status      | Completed  |
| -------------------- | ----------- | ---------- |
| Collect              | Complete    | YYYY-MM-DD |
| Reconcile            | Complete    | YYYY-MM-DD |
| Assumptions          | Complete    | YYYY-MM-DD |
| Position             | Complete    | YYYY-MM-DD |
| Handoff              | Complete    | YYYY-MM-DD |
| Analyse              | Complete    | YYYY-MM-DD |
| Budget Calibration   | Complete    | YYYY-MM-DD |
| Affordability Check  | In Progress |            |
| Plan                 | Not Started |            |
| Strategy             | Not Started |            |

---

## Scope and Basis

<!-- Imported from ChatGPT -->

---

## Inputs Used

- `reviews/YYYY-MM/position-handoff.md` — verified facts and locked assumptions
- `reviews/YYYY-MM/budget-calibration.md` — calibrated bucket limits

---

## Fixed Obligations

<!-- Imported from ChatGPT -->

---

## Required Buffers

<!-- Imported from ChatGPT -->

---

## Available Cashflow

<!-- Imported from ChatGPT -->

---

## Calibrated Bucket Requirement

<!-- Imported from ChatGPT -->

---

## Affordability Result

<!-- Imported from ChatGPT -->

---

## Required Adjustments

<!-- Imported from ChatGPT — only present if calibrated limits are not fully fundable -->

---

## Final Affordable Bucket Limits

<!-- Imported from ChatGPT -->

---

## Implications for Plan

<!-- Imported from ChatGPT -->

---

## Phase Lock

Status: <!-- Not Started / In Progress / Complete / Blocked -->
Completed: <!-- YYYY-MM-DD -->

Affordability check complete. Proceed to Plan.
```

---

---

## plan.md Template

```markdown
# Plan — [Month] [Year]

> Requires: Affordability Check complete

## Phase Status

| Phase                | Status      | Completed  |
| -------------------- | ----------- | ---------- |
| Collect              | Complete    | YYYY-MM-DD |
| Reconcile            | Complete    | YYYY-MM-DD |
| Assumptions          | Complete    | YYYY-MM-DD |
| Position             | Complete    | YYYY-MM-DD |
| Handoff              | Complete    | YYYY-MM-DD |
| Analyse              | Complete    | YYYY-MM-DD |
| Budget Calibration   | Complete    | YYYY-MM-DD |
| Affordability Check  | Complete    | YYYY-MM-DD |
| Plan                 | In Progress |            |
| Strategy             | Not Started |            |

---

## Available Funds

Available for planning (from position.md): £

---

## Payment Allocations

| Allocation                  | Amount | Account From | Due Date   | Priority |
| --------------------------- | ------ | ------------ | ---------- | -------- |
| Mortgage                    | £      |              | YYYY-MM-DD | 1        |
| Bills (split per assumptions)| £     |              |            | 1        |
| Credit card minimum         | £      |              | YYYY-MM-DD | 1        |
| BT repayment                | £      |              | YYYY-MM-DD | 2        |
| Emergency fund contribution | £      |              |            | 3        |
| Credit card full balance    | £      |              |            | 4        |
| **Total Allocated**         | **£**  |              |            |          |

---

## Reconciliation

| Item                    | Amount |
| ----------------------- | ------ |
| Available for planning  | £      |
| Less: total allocated   | £      |
| **Remaining surplus**   | **£**  |

---

## Surplus Allocation

<!-- How is any surplus allocated? Savings? Additional BT payment? Reserve? -->

---

## Phase Lock

Status: <!-- Not Started / In Progress / Complete / Blocked -->
Completed: <!-- YYYY-MM-DD -->
Approved: <!-- Yes / No — confirm plan is approved before locking -->
```

---

---

## strategy.md Template

```markdown
# Strategy — [Month] [Year]

> Requires: Plan complete

## Phase Status

| Phase                | Status      | Completed  |
| -------------------- | ----------- | ---------- |
| Collect              | Complete    | YYYY-MM-DD |
| Reconcile            | Complete    | YYYY-MM-DD |
| Assumptions          | Complete    | YYYY-MM-DD |
| Position             | Complete    | YYYY-MM-DD |
| Handoff              | Complete    | YYYY-MM-DD |
| Analyse              | Complete    | YYYY-MM-DD |
| Budget Calibration   | Complete    | YYYY-MM-DD |
| Affordability Check  | Complete    | YYYY-MM-DD |
| Plan                 | Complete    | YYYY-MM-DD |
| Strategy             | In Progress |            |

---

## Open Strategic Items

<!-- List any ongoing strategic questions under review -->

### [Item Title]

Status: Open / Decided / Deferred  
Decision: <!-- if decided -->  
Reasoning: <!-- why this decision was made -->  
Next review: <!-- when to revisit -->

---

## Decisions Made This Month

| Decision    | Outcome     | Reasoning   | Effective Date |
| ----------- | ----------- | ----------- | -------------- |
|             |             |             |                |

---

## Items Deferred

| Item        | Reason Deferred | Next Review |
| ----------- | --------------- | ----------- |
|             |                 |             |

---

## Finance Profile Updates

<!-- Note any changes to finance-profile.md made as a result of this review -->

---

## Phase Lock

Status: <!-- Not Started / In Progress / Complete / Blocked -->
Completed: <!-- YYYY-MM-DD -->

Monthly review complete.
```
