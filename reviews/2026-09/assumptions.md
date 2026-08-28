# Assumptions — September 2026

> Requires: Reconcile complete

## Phase Status

| Phase                | Status      | Completed  |
| -------------------- | ----------- | ---------- |
| Collect              | Complete    | 2026-08-28 |
| Reconcile            | Complete    | 2026-08-28 |
| Assumptions          | Complete    | 2026-08-28 |
| Position             | Complete    | 2026-08-28 |
| Handoff              | Complete    | 2026-08-28 |
| Analyse              | Not Started |            |
| Budget Calibration   | Not Started |            |
| Affordability Check  | Not Started |            |
| Plan                 | Not Started |            |
| Strategy             | Not Started |            |

---

## Planning Assumptions — This Month

Review each assumption against `docs/finance-profile.md`.
Confirm or override for this month.

| Assumption | Profile Value | This Month Value | Override? | Reason |
| --- | --- | --- | --- | --- |
| Household-income split methodology | Recalculate from current net income each review | Romeo £4,654.89 / Kelly £3,169.69; total £7,824.58; Romeo 59.5%, Kelly 40.5% | No | September income verified in reconcile |
| Minimum cash buffer | £500 household floor | £500 household floor | No | Preserve as absolute floor before optional allocations |
| Preferred cash buffer | £1,000 target | £1,000 target | No | Preserve as normal month-end planning target |
| Emergency fund account | Chip Cash ISA | Chip Cash ISA, £20,032.43 verified from screenshot | No | Reconcile confirmed Chip replaces Trading 212 as current emergency-fund source |
| Emergency fund target | £20,000 - £22,000 | £20,000 - £22,000 | No | Current balance is inside target range lower bound |
| Santander joint account | Shared bills account | Current balance user-confirmed at £58.77; statement unavailable until 3rd | Temporary source limitation | Use user-confirmed balance for September planning, but mark activity unverified |
| Mortgage split | Proportional to net household income | Use September split: Romeo 59.5%, Kelly 40.5% | No | Based on verified September net income |
| Bill split | Proportional to net household income | Use September split: Romeo 59.5%, Kelly 40.5% | No | Same methodology as mortgage |
| Shared bills baseline | £767.80/month before reimbursable Spotify | Use profile baseline until Santander statement is available | Temporary source limitation | Santander activity cannot be verified yet |
| Vehicle commitments | £472.12/month shared from Santander joint | Use profile baseline and September split; do not double count inside joint-account outflows | No | Vehicle costs remain shared household commitments |
| Kelly current-account DD baseline | £88.14/month | £88.14/month | No | August Halifax current statement supports the expected £11.69, £65.00, and £11.45 DDs |
| Romeo Lloyds fixed DD baseline | £454.02/month | £454.02/month | No | August Lloyds statement supports the recurring baseline including Vitality Health at £82.40 |
| Romeo M&S BT commitment | £195 operational target; £190 DD | Use statement DD £190 due 10 Sep; top-up need to be assessed in Plan | No | Statement verified £3,903.75 balance and £190 DD |
| Romeo MBNA BT commitment | Operational target to be recalculated monthly | Use statement DD £254.56 due 21 Sep; tranches £8,661.78 to 30 May 2028 and £1,520.51 to 3 Jun 2027 | No | Statement verified balance and tranche expiries |
| MBNA Barclaycard-transfer ownership | Romeo-specific unless explicitly overridden | Keep Romeo-specific for September | No | Durable profile states this tranche must not be included in Kelly's shared BT reimbursement unless overridden |
| Amex repayment policy | Pay in full where cashflow permits | Apply default policy; Romeo app-adjusted balance £1,224.84 and Kelly statement balance £1,767.32 are planning inputs | No | Reconcile verified balances; exact payment decision belongs in Plan |
| Romeo Amex BA Holidays Plan It | Not a durable standing assumption | Treat £448 BA Holidays payment as household Turkey trip cost, expected on 12-month Plan It unless current Amex app confirms different terms | One-time assumption | User selected/preferred 12 months for larger annual-trip purchase |
| Romeo Amex Gatwick Plan It | Not a durable standing assumption | Treat Gatwick parking/Fast Track £102.20 as paid and approved for Plan It after the 15 Aug statement | One-time assumption | LifeCoach confirms £88.20 parking + £14 Fast Track; user confirmed Plan It approval affects Amex app balance |
| Turkey euro cash | At least EUR 300; profile estimate ~£260 | Keep EUR 300 cash assumption; reference-rate equivalent £257.16 on 28 Aug 2026 before cash/provider spread | No | ECB 28 Aug 2026 reference rate EUR/GBP 0.85720 keeps the £260 estimate reasonable |
| Turkey Monzo TRY withdrawal float | £75 | £75 | No | User-confirmed September travel cash need |
| Turkey travel cash treatment | Shared household travel cost | Shared using September income split: Romeo 59.5%, Kelly 40.5% | No | Durable profile says to allocate using normal household-income split |
| Turkey low-spend funding stack | ~£270 one-week funding stack | Keep as planning assumption to test later: pickleball pause, avoided Kelly London travel, food-out reduction, tighter groceries, discretionary freeze | No | User requested this be logged for September review |
| LifeCoach travel context | Use as read-only context | Side, Antalya trip confirmed 19-25 Sep 2026; additional planned cash items are covered by EUR 300 assumption | No | `npm run travel:summary` checked during assumptions |
| PPL Challenger League September fixture | Tunbridge Wells 5-6 Sep; travel only | Keep as September travel-only sport cost assumption; exact travel cost not yet verified | No | Profile flags September fixture as day trip |
| Kelly tithe | 10% of Kelly net income | £316.97 planning amount | No | Based on Kelly verified net pay £3,169.69 |

---

## September Prompts From Durable Profile

- Confirm current household-income split.
- Confirm current-account DD baselines against statements where available.
- Confirm Turkey travel cash requirement and exchange-rate assumption.
- Treat Turkey travel cash as a shared household travel cost unless explicitly overridden.
- Check LifeCoach OS travel context before asking the user to restate Turkey trip details.

---

## One-Time Overrides

| Override | Normal Value | September Value | Review Date | Reason |
| --- | --- | --- | --- | --- |
| Santander source limitation | Use Santander statement for joint-account balance and activity | Use user-confirmed £58.77 current balance until statement is available | September position / plan | Statement is issued after the review start date |
| Turkey travel Plan It treatment | Amex pay-in-full default where cashflow permits | BA Holidays £448 expected as 12-month Plan It; Gatwick parking/Fast Track £102.20 treated as post-statement approved Plan It | September position / plan | User preference is to spread larger annual-trip purchases and confirmed Gatwick Plan It changed the Amex app balance |
| Turkey cash set-aside | No standing monthly travel-cash set-aside | EUR 300 cash plus £75 Monzo TRY withdrawal float | September plan | Known September trip cash requirement |

---

## External Context Checked

- LifeCoach OS travel summary checked on 2026-08-28.
- Side, Antalya trip is confirmed for 19 Sep 2026 to 25 Sep 2026.
- Finance-relevant LifeCoach costs for assumptions:
  - BA Holidays package cash payment: £448.00 paid.
  - Gatwick Long Stay South parking: £88.20 paid.
  - Gatwick South Terminal Fast Track for two: £14.00 paid.
  - Planned cash euro items: AVO transfer EUR 120, hammam EUR 40, massages EUR 100, Side admission EUR 14.
  - The planned euro cash items total EUR 274, so the FinanceOS EUR 300 cash assumption remains sufficient before discretionary extras or exchange/provider spread.
- ECB euro reference rate checked on 2026-08-28: EUR/GBP 0.85720. EUR 300 equals £257.16 at that reference rate before provider spread.

---

## Phase Lock

Status: Complete
Completed: 2026-08-28

Planning assumptions locked for this review.
