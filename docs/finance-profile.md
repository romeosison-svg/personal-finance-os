# Finance Profile

Persistent planning assumptions for the Personal Finance Assembly Line.

These assumptions are reviewed and confirmed (or overridden) during Phase 3 of every monthly review.

> **Note:** All values below are examples. Replace with your actual figures before using this system.

---

## Cash Buffers

| Assumption              | Example Value | Notes                                              |
| ----------------------- | ------------- | -------------------------------------------------- |
| Minimum cash buffer     | £1,500        | Below this level, no discretionary spending        |
| Preferred cash buffer   | £3,000        | Target end-of-month balance before allocations     |
| Emergency fund target   | £10,000       | 3–6 months essential expenses                      |
| Emergency fund current  | (update monthly) | Track in reconcile phase                        |

**Minimum buffer:** The floor. If available funds after all allocations would drop below this amount, the plan must be revised.

**Preferred buffer:** The target. The plan is built to maintain this balance, not the minimum.

---

## Mortgage

| Assumption              | Example Value | Notes                                              |
| ----------------------- | ------------- | -------------------------------------------------- |
| Monthly mortgage amount | £1,200        | Full mortgage payment                              |
| Split methodology       | 60/40         | Example: 60% from Account A, 40% from Account B   |
| Overpayment target      | £0            | Set if making regular overpayments                 |

**Split methodology:** Defines how the mortgage payment is divided between accounts or income sources. Must be applied consistently each month.

---

## Bills

| Assumption              | Example Value | Notes                                              |
| ----------------------- | ------------- | -------------------------------------------------- |
| Monthly bills total     | £800          | All regular household bills combined               |
| Bill split methodology  | 50/50         | Example: split equally between two accounts        |
| Shared bills accounts   | Account A, B  | Which accounts bills are split across              |

**Bill split methodology:** Defines how shared household bills are divided. Update if income or living arrangements change.

---

## Balance Transfers

| Assumption                    | Example Value | Notes                                          |
| ----------------------------- | ------------- | ---------------------------------------------- |
| BT card 1 balance             | (update monthly) | Current balance on BT card                 |
| BT card 1 promotional end     | 2026-12-01    | Date promotional 0% rate expires              |
| BT card 1 monthly target      | £300          | Monthly payment to clear before promo ends    |
| BT card 2 balance             | (update monthly) |                                             |
| BT card 2 promotional end     | (update monthly) |                                             |
| BT card 2 monthly target      | (update monthly) |                                             |

**BT repayment target methodology:** Calculate required monthly payment by dividing remaining balance by remaining months before promotional rate expires. Review each month.

---

## Credit Cards

| Assumption                    | Example Value | Notes                                          |
| ----------------------------- | ------------- | ---------------------------------------------- |
| Primary card minimum payment  | £25           | Minimum payment only (example)                 |
| Primary card preferred payment| Full balance  | Default: pay in full each month                |
| Secondary card methodology    | Minimum + £X  | If carrying a balance                          |

**Default policy:** Pay credit cards in full each month where possible. If carrying a balance, the plan phase must explicitly justify why and define the repayment schedule.

---

## Emergency Fund

| Assumption                      | Example Value | Notes                                        |
| ------------------------------- | ------------- | -------------------------------------------- |
| Emergency fund target           | £10,000       | Target total                                 |
| Emergency fund monthly contribution | £200      | Regular monthly contribution                 |
| Emergency fund account          | Easy-access savings | Instant access, not fixed-term         |
| Emergency fund current          | (update monthly) | Update in reconcile phase                |
| Months to target (calculated)   | (calculate)   | (target − current) ÷ monthly contribution    |

---

## Planning Rule Hierarchy

When there is a conflict between allocations, apply this priority order:

1. Minimum cash buffer must be maintained (non-negotiable)
2. Mortgage payment (scheduled, non-negotiable)
3. Minimum credit card payments (non-negotiable)
4. Bills (scheduled, non-negotiable)
5. BT repayment targets (to avoid promotional rate expiry)
6. Emergency fund contribution (reduce before discretionary spending)
7. Preferred buffer maintenance
8. Credit card full balance payment
9. Overpayments and accelerated repayments

---

## One-Time Override Policy

If a monthly review requires a temporary departure from these assumptions, document it in the **Assumptions** phase file for that month.

Format:

```
Override: [assumption name]
Reason:   [why the override is needed]
This month value: [value used]
Normal value: [value from finance-profile.md]
Review: [when this override should be reviewed or reversed]
```

Persistent changes (not one-time overrides) should update this file directly. Commit the change with a descriptive message.

---

## Last Updated

Date: <!-- update when this file changes -->  
Reason: <!-- brief note on what changed and why -->
