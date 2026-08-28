# Affordability Check — September 2026

> Requires: Budget Calibration complete

## Phase Status

| Phase                | Status      | Completed  |
| -------------------- | ----------- | ---------- |
| Collect              | Complete    | 2026-08-28 |
| Reconcile            | Complete    | 2026-08-28 |
| Assumptions          | Complete    | 2026-08-28 |
| Position             | Complete    | 2026-08-28 |
| Handoff              | Complete    | 2026-08-28 |
| Analyse              | Complete    | 2026-08-29 |
| Budget Calibration   | Complete    | 2026-08-29 |
| Affordability Check  | Complete    | 2026-08-29 |
| Plan                 | Not Started |            |
| Strategy             | Not Started |            |

---

## Affordability Test

Test whether calibrated bucket limits can be funded from cashflow. No payment plan in this phase.

## Scope

This phase tests whether the locked fixed commitments and calibrated bucket limits are fundable from the current September operating cash position.

It does not choose payment allocations, decide card repayment amounts, or create a cash trace.

## Inputs

| Input | Amount | Source |
| --- | ---: | --- |
| Operating cash excluding Chip | £7,135.17 | Position |
| Restricted emergency fund / Chip Cash ISA | £20,032.43 | Position |
| Minimum cash buffer | £500.00 | Assumptions |
| Preferred cash buffer | £1,000.00 | Assumptions |
| Calibrated controllable-spend requirement | £2,910.00 | Budget Calibration |
| Santander recurring gross outflow | £1,261.91 | Post-lock Santander clarification |
| Santander recurring net household cost | £1,254.58 | Gross outflow less £7.33 Elaine Spotify reimbursement |
| Starling overdraft balance | -£549.87 | Position |
| Kelly work reimbursement receivable | £400.00 | User-confirmed 2026-08-29; missed payroll cut-off and is not available this pay cycle |

Chip is not treated as ordinary operating cash in this test.

The £400 Kelly work reimbursement is not treated as available operating cash in this test. It is treated as a specific receivable that can explain carrying £400 of Kelly's Amex balance until the reimbursement is received.

## Fixed Commitment Stack Before Controllable Buckets

| Commitment | Amount | Notes |
| --- | ---: | --- |
| Mortgage | £3,069.53 | Fixed household commitment |
| Santander net household cost | £1,254.58 | £1,261.91 gross less £7.33 Spotify reimbursement |
| Romeo Lloyds fixed DD baseline | £454.02 | Current-account DDs excluding card / BT payments |
| Kelly Halifax current DD baseline | £88.14 | Current-account DDs excluding card payments |
| Kelly tithe | £316.97 | 10% of verified Kelly net pay |
| Card / BT minimum-DD stack | £669.87 | Romeo Amex minimum + Kelly Amex minimum + M&S DD + MBNA DD |
| **Total fixed / mandatory stack before buckets** | **£5,853.11** | |

## Minimum-Obligation Affordability Test

This test uses the minimum card obligations and BT direct debits only. It does not attempt to pay Amex statement balances in full.

| Measure | Amount |
| --- | ---: |
| Operating cash excluding Chip | £7,135.17 |
| Less fixed / mandatory stack before buckets | -£5,853.11 |
| Cash remaining before controllable buckets | £1,282.06 |
| Available for buckets after minimum buffer | £782.06 |
| Available for buckets after preferred buffer | £282.06 |
| Calibrated controllable buckets | £2,910.00 |
| Bucket shortfall after minimum buffer | £2,127.94 |
| Bucket shortfall after preferred buffer | £2,627.94 |

Result: the calibrated £2,910 bucket set is **not affordable** from operating cash after fixed commitments, minimum card/BT obligations, and the minimum buffer are preserved.

## Amex Pay-In-Full Stress Test

The finance profile default is to pay Amex in full where cashflow permits. This stress test shows the pressure if both Amex balances were paid in full rather than minimums only.

| Measure | Amount |
| --- | ---: |
| Romeo Amex app-adjusted balance | £1,224.84 |
| Kelly Amex statement balance | £1,767.32 |
| Total Amex balances | £2,992.16 |
| Amex minimums already included in base test | -£225.31 |
| Additional cash needed for Amex pay-in-full stress | £2,766.85 |
| Kelly work reimbursement available for this Amex cycle | £0.00 |
| Full-stress requirement including calibrated buckets | £11,529.96 |
| Shortfall before buffer | £4,394.79 |
| Shortfall after minimum buffer | £4,894.79 |
| Shortfall after preferred buffer | £5,394.79 |

Result: paying both Amex balances in full is not affordable within the current operating-cash envelope alongside the calibrated buckets and fixed commitments.

Kelly's £400 work reimbursement is a receivable, but it missed this pay cycle and should not be treated as cash available to fund Kelly's Amex payment in September.

## Amex Reimbursement-Adjusted Stress Test

This stress test treats £400 of Kelly's Amex as reimbursable work spend to be repaid when Kelly receives the reimbursement, rather than as September cash-funded Amex pressure.

| Measure | Amount |
| --- | ---: |
| Total Amex balances | £2,992.16 |
| Less Kelly work reimbursement receivable | -£400.00 |
| Current-cycle Amex cash funding pressure | £2,592.16 |
| Amex minimums already included in base test | -£225.31 |
| Additional current-cycle Amex cash needed above minimums | £2,366.85 |
| Reimbursement-adjusted requirement including calibrated buckets | £11,129.96 |
| Shortfall before buffer | £3,994.79 |
| Shortfall after minimum buffer | £4,494.79 |
| Shortfall after preferred buffer | £4,994.79 |

Result: carrying the £400 reimbursable portion reduces the September Amex pressure by £400, but the overall plan still needs a cashflow exception or bucket adjustment.

## Shared Household Load

| Shared input | Amount | Romeo 59.5% | Kelly 40.5% |
| --- | ---: | ---: | ---: |
| Mortgage | £3,069.53 | £1,826.37 | £1,243.16 |
| Santander net household cost | £1,254.58 | £746.48 | £508.10 |
| Shared controllable buckets | £1,910.00 | £1,136.45 | £773.55 |
| **Shared fixed + controllable load** | **£6,234.11** | **£3,709.30** | **£2,524.81** |

The shared household load is high relative to available operating cash because Santander starts at £58.77 and September includes Turkey cash.

## Santander Affordability Pressure

| Measure | Amount |
| --- | ---: |
| Santander current balance | £58.77 |
| Santander recurring gross outflow | £1,261.91 |
| Santander gross top-up gap | £1,203.14 |
| Gross gap split indicator - Romeo | £715.87 |
| Gross gap split indicator - Kelly | £487.27 |
| Santander net top-up gap after Elaine reimbursement | £1,195.81 |

This confirms Santander is an immediate liquidity pressure. Exact top-up timing and account movements belong in the Plan phase.

## Affordability Findings

1. The calibrated controllable bucket total of £2,910 is too high to fund from current operating cash after fixed obligations, card/BT minimums, and the minimum buffer.
2. Only £782.06 is available for controllable buckets after the minimum £500 buffer is preserved.
3. Only £282.06 is available for controllable buckets after the preferred £1,000 buffer is preserved.
4. The main pressures are Santander funding, Amex balances, Turkey cash, and the Starling overdraft remaining open.
5. The emergency fund is inside target range, but it remains restricted and is not used as normal affordability capacity in this check.
6. Kelly's £400 work reimbursement is not cash available in this pay cycle, but it can reduce the amount of Kelly's Amex that needs to be cash-funded now if the Plan explicitly carries that reimbursable portion until repayment is received.
7. A Plan-phase adjustment is required before any final payment allocation can be considered.

## Carry Forward To Plan

- The Plan phase must reduce, defer, or explicitly override some combination of controllable buckets, Amex full-payment policy, overdraft repayment timing, or buffer preference.
- Santander requires an explicit top-up trace because the current balance is £58.77 against recurring September outflows.
- Turkey cash remains a real September requirement and should not disappear from the plan.
- Any decision to pay less than the Amex statement balances in full must be documented as a cashflow exception in Plan.
- Kelly's £400 work reimbursement should be tracked as a future receivable. Plan can carry £400 of Kelly's Amex against that receivable and repay it when received.
- Starling overdraft must remain visible while open.

---

## Phase Lock

Status: Complete
Completed: 2026-08-29

Affordability check complete.
