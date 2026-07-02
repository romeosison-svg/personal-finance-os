# Assumptions — July 2026

> Requires: Reconcile complete

## Phase Status

| Phase                | Status      | Completed  |
| -------------------- | ----------- | ---------- |
| Collect              | Complete    | 2026-07-01 |
| Reconcile            | Complete    | 2026-07-01 |
| Assumptions          | Complete    | 2026-07-01 |
| Position             | Not Started |            |
| Handoff              | Not Started |            |
| Analyse              | Not Started |            |
| Budget Calibration   | Not Started |            |
| Affordability Check  | Not Started |            |
| Plan                 | Not Started |            |
| Strategy             | Not Started |            |

---

## Planning Assumptions — July 2026

Review each assumption against [finance-profile.md](/docs/finance-profile.md).
Confirm or override for this month.

### Cash Buffers

| Assumption | Profile Value | This Month Value | Override? | Reason |
| --- | ---: | ---: | --- | --- |
| Minimum cash buffer | £500 | £500 | No | Absolute floor after planned allocations |
| Preferred cash buffer | £1,000 | £1,000 | No | Normal month-end planning target |
| Emergency fund minimum operating level | £5,000 | £5,000 | No | Profile minimum; current balance to be confirmed in Position if needed |

---

### Income

Use normalised monthly net income for household allocation calculations.

| Person | Net Monthly Income | Basis |
| --- | ---: | --- |
| Romeo | £4,654.89 | Confirmed net salary received 30 Jun 2026 |
| Kelly | ~£3,272.00 | Normalised figure from finance profile: prior UHY baseline plus £1,000 annual salary uplift to £56k Morningstar salary |
| **Total household** | **~£7,926.89** | |
| Romeo % | **58.7%** | £4,654.89 / £7,926.89 |
| Kelly % | **41.3%** | £3,272.00 / £7,926.89 |

**Override carried for Kelly income normalisation**

Reason: Kelly's June Morningstar payslip includes £2,153.85 backpay, so actual net received (£4,252.89) is not a stable monthly run-rate.
Normal value: confirmed current monthly net from full-month payslip.
Override value: use ~£3,272 normalised monthly net.
Review: Replace with first full-month Morningstar payslip once available.

---

### Mortgage

Total mortgage: £3,069.53.

| Assumption | Profile Value | This Month Value | Override? | Reason |
| --- | --- | --- | --- | --- |
| Mortgage split methodology | Proportional to net household income | 58.7% Romeo / 41.3% Kelly | No | Based on locked normalised July income |
| Romeo contribution | Calculated from income % | **£1,802.51** | No | £3,069.53 x 58.7% |
| Kelly contribution | Calculated from income % | **£1,267.02** | No | £3,069.53 x 41.3% |

June's temporary override where Kelly used savings is not carried forward as an assumption. July uses the normal proportional-income methodology unless the Plan phase identifies a cashflow timing issue.

---

### Bills and Shared Obligations

Shared household bills use the same proportional-income methodology as the mortgage unless explicitly overridden.

| Assumption | Profile Value | This Month Value | Override? | Reason |
| --- | --- | --- | --- | --- |
| Bill split methodology | Proportional to net household income | 58.7% Romeo / 41.3% Kelly | No | Based on locked normalised July income |
| Shared bills account | Santander joint account | Santander joint account | No | Persistent bills account confirmed by user |
| Shared household bills baseline | £767.80/month | £767.80/month | No | Current known recurring shared household bills |
| Spotify Premium Family gross DD | £21.99/month | £21.99/month | No | New recurring DD from Santander joint account |
| Spotify reimbursement from Elaine | -£7.33/month | -£7.33/month | No | Reimbursement reduces household net cost |
| Shared household bills net cost | £782.46/month | £782.46/month | No | £767.80 + £21.99 - £7.33 |
| Santander shared bills gross outflow | N/A | £789.79/month | No | £767.80 + £21.99 before Elaine reimbursement |
| Romeo target share of £782.46 net cost | Calculated from income % | ~£459.48 | No | £782.46 x 58.7% |
| Kelly target share of £782.46 net cost | Calculated from income % | ~£322.98 | No | £782.46 x 41.3% |
| Kelly already paid into Santander joint | N/A | £358.00 | No | Pre-existing July contribution |
| Shared bills settlement adjustment | N/A | Romeo owes Kelly ~£35.02 | No | Kelly paid £358.00 against a target share of ~£322.98 |
| Santander joint account DDs | New July DDs confirmed | £412.13 | No | MG PCP £310.84 + MG insurance £40.00 + Zoe insurance £61.29 |
| Santander gross monthly outflow before reimbursement | N/A | £1,201.92 | No | £789.79 shared bills gross outflow + £412.13 vehicle DDs |
| Santander net household cost after reimbursement | N/A | £1,194.59 | No | £782.46 net shared bills + £412.13 vehicle DDs |
| Santander joint top-up need | N/A | At least £1,001.92 gross before reimbursement | No | Current estimated balance £200.00; top-up required before/around July DDs; Elaine reimbursement reduces net cost by £7.33 after receipt |

---

### Balance Transfers

Use confirmed July statement/direct debit figures from `reconcile.md`.

| Assumption | Profile Value | Confirmed Actual | This Month Value | Override? | Reason |
| --- | ---: | ---: | ---: | --- | --- |
| MBNA operational target | £376/month | DD £276.21 | £376.00 | No | Profile target maintained |
| MBNA manual top-up | ~£151/month | £376 - £276.21 | **£99.79** | No | Direct debit counts toward target |
| M&S operational target | £195/month | DD £190.00 | £195.00 | No | Profile target maintained |
| M&S manual top-up | ~£5/month | £195 - £190.00 | **£5.00** | No | Direct debit counts toward target |

Note: M&S statement minimum is £107.09 due 10 Jul 2026, but the expected DD remains £190.00 from Lloyds and therefore exceeds the minimum.

---

### Credit Card Policy

| Card | Profile Policy | This Month Assumption | Override? | Reason |
| --- | --- | --- | --- | --- |
| Romeo Amex | Pay in full | Pay in full where cashflow permits; minimum £142.15 is mandatory | No | Confirmed statement balance £933.57; Plan It balance noted separately in reconcile |
| Romeo Barclaycard | Clear and downgrade | No new spend; prioritise clearing if cashflow permits after essentials and BT targets | No | Highest-cost card risk remains, but payment amount belongs in Plan |
| Kelly Amex | Pay in full where possible | Kelly self-funded unless Plan explicitly treats otherwise | No | Confirmed balance £877.67 |
| Kelly Halifax CC | Flexible | Already paid to £0.00 | No | Confirmed in reconcile |

---

### Tithe

| Assumption | Profile Value | This Month Value | Override? | Reason |
| --- | --- | ---: | --- | --- |
| Kelly tithe | 10% of Kelly net income | **~£327.20** | No | Based on normalised Kelly monthly net of ~£3,272 |

Note: Kelly's actual June net received is inflated by backpay. Use the normalised income figure for July planning unless the user chooses to tithe on actual received cash in Plan.

---

### Emergency Fund

| Assumption | Profile Value | This Month Value | Override? | Reason |
| --- | --- | --- | --- | --- |
| Emergency fund contribution | Variable | Determine in Plan | No | Profile says contribution depends on available cashflow |
| Emergency fund minimum operating level | £5,000 | £5,000 | No | Preserve minimum operating level |
| Kelly emergency fund replenishment priority | Replenish once salary in place | Carry into Plan/Strategy | No | Profile priority sits below committed obligations and above discretionary spending |
| Kelly personal savings replenishment goal | Replenish savings used during job transition | £1,316.83 target, funded only from surplus | No | Kelly used personal savings to fund her previous mortgage share; this is not a one-hit reimbursement and should only receive surplus after established goals |

No July emergency-fund contribution is assumed at this phase. Affordability belongs in the Plan phase after Position is calculated.

Clarification added 2026-07-01: Kelly's personal savings replenishment is a goal, not a fixed July liability. The Plan phase should prioritise established obligations and goals first, then allocate any remaining surplus to this replenishment target.

---

### Vehicle and Known July Costs

| Item | Assumption | This Month Value | Notes |
| --- | --- | ---: | --- |
| MG PCP | Kelly vehicle commitment | £310.84 | Paid from Santander joint account per reconcile |
| MG insurance | Kelly vehicle commitment | £40.00 | Paid from Santander joint account per reconcile |
| Zoe insurance | Vehicle commitment | £61.29 | Paid from Santander joint account per reconcile |
| Zoe vehicle cost settlement | Shared household vehicle reconciliation | £428.94 outstanding | Treat as a shared household vehicle cost recovery; may be funded from household cash rather than Kelly's personal spend bucket |
| PPL Challenger League - Bolton Arena | Known seasonal cost | First night already paid; extra night £91 payable at hotel; travel TBC | Fixture 18-19 Jul 2026; extended by one night |
| PPL Challenger training - Farnborough | Planned seasonal cost | £123 semi-flex Premier Inn for one night on 11 Jul 2026 | Aldershot was full; booking under consideration |
| Plumbing work | Optional household maintenance under consideration | ~£300 estimate | Do not treat as committed until affordability and Plan phases decide |

---

## One-Time Overrides

| Override | Normal Value | This Month Value | Reason | Review Date |
| --- | --- | --- | --- | --- |
| Kelly income normalisation | Use confirmed full-month payslip | Use ~£3,272 normalised net | June payslip includes £2,153.85 backpay and is not a stable monthly run-rate | Next full-month Morningstar payslip |

No other June overrides are carried forward as assumptions. July reverts to normal proportional-income methodology for mortgage, bills, and BT funding unless Position/Plan identifies a new cashflow constraint.

---

## Phase Lock

Status: Complete
Completed: 2026-07-01

Planning assumptions locked for this review.
