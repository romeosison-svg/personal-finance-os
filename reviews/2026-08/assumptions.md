# Assumptions — August 2026

> Requires: Reconcile complete

## Phase Status

| Phase                | Status      | Completed  |
| -------------------- | ----------- | ---------- |
| Collect              | Complete    | 2026-08-03 |
| Reconcile            | Complete    | 2026-08-03 |
| Assumptions          | Complete    | 2026-08-03 |
| Position             | Not Started |            |
| Handoff              | Not Started |            |
| Analyse              | Not Started |            |
| Budget Calibration   | Not Started |            |
| Affordability Check  | Not Started |            |
| Plan                 | Not Started |            |
| Strategy             | Not Started |            |

---

## Planning Assumptions — August 2026

Review each assumption against [finance-profile.md](/docs/finance-profile.md).
Confirm or override for this month.

### Cash Buffers

| Assumption | Profile Value | This Month Value | Override? | Reason |
| --- | ---: | ---: | --- | --- |
| Minimum cash buffer | £500 | £500 | No | Absolute floor after planned allocations |
| Preferred cash buffer | £1,000 | £1,000 | No | Normal month-end planning target |
| Emergency fund minimum operating level | £5,000 | £5,000 | No | Profile minimum |
| Emergency fund target | £20,000 - £22,000 | £20,000 - £22,000 | No | Long-term target |

Emergency fund current balance is a locked reconcile fact: Trading 212 Cash ISA total value £15,131.43.

---

### Income

Use current confirmed monthly net income for household allocation calculations.

| Person | Net Monthly Income | Basis |
| --- | ---: | --- |
| Romeo | £4,654.90 | Confirmed salary receipt from TEKSYSTEMS GLOBAL on 2026-07-31 |
| Kelly | £4,234.02 | Confirmed Morningstar full-month payslip net pay on 2026-07-24 |
| **Total household** | **£8,888.92** | |
| Romeo % | **52.37%** | £4,654.90 / £8,888.92 |
| Kelly % | **47.63%** | £4,234.02 / £8,888.92 |

**Kelly income normalisation update**

Profile value: use ~£3,272 normalised monthly net until Kelly has a first full-month Morningstar payslip.

This month value: use actual confirmed full-month Morningstar net pay of £4,234.02.

Override? No. This follows the profile review rule because the full-month payslip is now available.

---

### Mortgage

Total mortgage: £3,069.53.

| Assumption | Profile Value | This Month Value | Override? | Reason |
| --- | --- | --- | --- | --- |
| Mortgage split methodology | Proportional to net household income | 52.37% Romeo / 47.63% Kelly | No | Based on locked August income |
| Romeo contribution | Calculated from income % | £1,607.43 | No | £3,069.53 x 52.3674% |
| Kelly contribution | Calculated from income % | £1,462.10 | No | £3,069.53 x 47.6326% |

No mortgage payment plan decision is made in this phase.

---

### Bills and Shared Obligations

Shared household bills use the same proportional-income methodology as the mortgage unless explicitly overridden.

| Assumption | Profile Value | This Month Value | Override? | Reason |
| --- | --- | --- | --- | --- |
| Bill split methodology | Proportional to net household income | 52.37% Romeo / 47.63% Kelly | No | Based on locked August income |
| Shared bills account | Santander joint account | Santander joint account | No | Persistent bills account |
| Shared household bills baseline | £767.80/month | £767.80/month | No | Profile recurring shared household bills baseline |
| Spotify Premium Family gross DD | £21.99/month | £21.99/month | No | Recurring DD from Santander joint account |
| Spotify reimbursement from Elaine | -£7.33/month | -£7.33/month | No | Reimbursement reduces household net cost |
| Shared household bills net cost | £782.46/month | £782.46/month | No | £767.80 + £21.99 - £7.33 |
| Romeo target share of £782.46 net cost | Calculated from income % | £409.75 | No | £782.46 x 52.3674% |
| Kelly target share of £782.46 net cost | Calculated from income % | £372.71 | No | £782.46 x 47.6326% |
| Santander current balance | N/A | £599.42 | No | User-confirmed reconcile fact |
| Kelly Santander top-up | N/A | £665.00 | No | User-confirmed reconcile fact |
| Santander top-up imbalance | N/A | Track in Position / Plan | No | Kelly likely paid above ratio share; exact balancing amount depends on August shared outflow facts |

No Santander reimbursement or top-up decision is made in this phase.

---

### Balance Transfers

Use confirmed August statement/direct debit figures from `reconcile.md` and profile operational targets.

| Assumption | Profile Value | Confirmed Actual | This Month Value | Override? | Reason |
| --- | ---: | ---: | ---: | --- | --- |
| MBNA operational target | £376/month | DD £269.30 | £376.00 | No | Profile target maintained |
| MBNA manual top-up | Difference between target and DD | £376.00 - £269.30 | £106.70 | No | Direct debit counts toward target |
| M&S operational target | £195/month | DD £190.00 | £195.00 | No | Profile target maintained |
| M&S manual top-up | Difference between target and DD | £195.00 - £190.00 | £5.00 | No | Direct debit counts toward target |

Promotional dates are now stored in `docs/finance-profile.md`:

| Account | Promotional End |
| --- | --- |
| MBNA tranche 1 | 2027-06-03 |
| MBNA tranche 2 | 2028-05-30 |
| M&S | 2028-03 |

---

### Credit Card Policy

| Card | Profile Policy | This Month Assumption | Override? | Reason |
| --- | --- | --- | --- | --- |
| Romeo Amex | Pay in full | Pay in full where cashflow permits; minimum £126.00 is mandatory | No | Confirmed statement balance £1,139.80; Plan It total balance also noted in reconcile |
| Romeo Barclaycard | Clear and downgrade | No new spend; clear if cashflow permits after essentials and BT targets | No | Confirmed balance £214.00 with £16.10 minimum |
| Romeo Halifax CC | Flexible | Accepted as cleared for reconcile | No | Statement balance cleared by £186.98 payment |
| Kelly Amex | Pay in full where possible | Kelly self-funded; £400.00 work reimbursement is pending and relevant to repayment planning | No | Confirmed balance £1,376.13 |
| Kelly Halifax CC | Flexible | Already paid to £0.00 | No | Statement balance cleared by £451.58 payment |

Payment amounts beyond mandatory minimums belong in Plan, not Assumptions.

---

### Tithe

| Assumption | Profile Value | This Month Value | Override? | Reason |
| --- | --- | ---: | --- | --- |
| Kelly tithe | 10% of Kelly net income | £423.40 | No | Based on confirmed Kelly net pay of £4,234.02 |

---

### Emergency Fund

| Assumption | Profile Value | This Month Value | Override? | Reason |
| --- | --- | --- | --- | --- |
| Emergency fund contribution | Variable | Determine in Plan | No | Profile says contribution depends on available cashflow |
| Emergency fund account | Trading 212 emergency fund | Trading 212 Cash ISA | No | Confirmed by reconcile screenshot |
| Emergency fund current | £15,091 profile value | £15,131.43 | No | Locked reconcile fact for this review |
| Emergency fund minimum operating level | £5,000 | £5,000 | No | Preserve minimum operating level |
| Kelly personal savings replenishment goal | Replenish savings used during job transition | Carry into Plan/Strategy | No | Goal remains below committed obligations and above discretionary spending |

No August emergency-fund contribution is assumed at this phase.

---

### Vehicle and Known August Costs

| Item | Assumption | This Month Value | Notes |
| --- | --- | ---: | --- |
| MG PCP | Kelly vehicle commitment | £310.84 | Known from prior review / Santander shared account tracking |
| MG insurance | Kelly vehicle commitment | £40.00 | Known from prior review / Santander shared account tracking |
| Zoe insurance | Vehicle commitment | £61.29 | Known from prior review / Santander shared account tracking |
| Santander joint-account funding | Shared account liquidity item | Kelly paid £665.00; balance £599.42 | Exact ratio settlement to be calculated later from locked facts |
| IOND share sale proceeds | One-off pending cash inflow | £9,327.50 | User-confirmed pending transfer to Romeo bank account; allocation to be checked with portfolio-os |
| IOND proceeds intended Cash ISA allocation | Pending portfolio-os consultation | At least £5,000.00 | User-stated intention; not a final investment decision in this phase |
| IOND proceeds intended Stocks & Shares ISA allocation | Pending portfolio-os consultation | Remainder after Cash ISA allocation | User-stated intention: global ex-USA ETF; not a final investment decision in this phase |
| Kelly work reimbursement | Pending reimbursement | £400.00 | Relevant to Kelly Amex repayment planning |

---

## One-Time Overrides

| Override | Normal Value | This Month Value | Reason | Review Date |
| --- | --- | --- | --- | --- |
| Kelly income normalisation | Use ~£3,272 until first full-month Morningstar payslip | Use actual confirmed net pay £4,234.02 | Full-month Morningstar payslip is now available | August 2026 |
| IOND proceeds availability | Treat one-off proceeds as general available cash | Hold for portfolio allocation check before treating as available for plan decisions | User intends at least £5,000 to Cash ISA and the remainder to Stocks & Shares ISA / global ex-USA ETF, subject to portfolio-os consultation | August 2026 |

No other July overrides are carried forward as assumptions. August uses the normal proportional-income methodology for mortgage, bills, and BT funding unless Position/Plan identifies a new cashflow constraint.

---

## Phase Lock

Status: Complete
Completed: 2026-08-03

Planning assumptions locked for this review.
