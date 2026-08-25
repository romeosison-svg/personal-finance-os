# Affordability Check — August 2026

> Requires: Budget Calibration complete

Budget Calibration answers: what are sensible behavioural spending caps?
Affordability Check answers: can those caps actually be funded from current cashflow?
Plan answers: what actions should be taken now given the affordable limits?

## Phase Status

| Phase                | Status      | Completed  |
| -------------------- | ----------- | ---------- |
| Collect              | Complete    | 2026-08-03 |
| Reconcile            | Complete    | 2026-08-03 |
| Assumptions          | Complete    | 2026-08-03 |
| Position             | Complete    | 2026-08-03 |
| Handoff              | Complete    | 2026-08-03 |
| Analyse              | Complete    | 2026-08-03 |
| Budget Calibration   | Complete    | 2026-08-03 |
| Affordability Check  | Complete    | 2026-08-03 |
| Plan                 | Not Started |            |
| Strategy             | Not Started |            |

---

## Scope and Basis

This phase tests whether the locked August budget calibration can be funded from the locked August position.

It does not:

- decide final payment amounts;
- create the payment plan;
- allocate remaining surplus;
- reopen locked assumptions;
- change the cash buffer policy;
- treat pending IOND proceeds as general plan cash.

The Plan phase should use this affordability result to decide exact account movements and payment timing.

---

## Inputs Used

- `reviews/2026-08/position-handoff.md` — verified facts and locked assumptions
- `reviews/2026-08/position.md` — locked position
- `reviews/2026-08/budget-calibration.md` — calibrated August bucket limits

---

## Fixed Obligations Already Included in Position

The locked Position already deducts the following listed August liabilities before calculating available cash for planning:

| Item | Amount |
| --- | ---: |
| Mortgage | £3,069.53 |
| Santander joint account gross top-up need | £662.49 |
| M&S BT DD | £190.00 |
| Romeo Amex minimum | £126.00 |
| Romeo Barclaycard minimum | £16.10 |
| MBNA DD | £269.30 |
| MBNA manual top-up to target | £106.70 |
| M&S manual top-up to target | £5.00 |
| Kelly Amex minimum | £27.52 |
| Kelly tithe | £423.40 |
| **Total listed known liabilities** | **£4,896.04** |

These are treated as already funded before the affordability test begins.

---

## Required Buffers

| Buffer | Amount | Treatment |
| --- | ---: | --- |
| Minimum cash buffer | £500.00 | Absolute floor |
| Preferred cash buffer | £1,000.00 | Used by locked Position and preserved in this check |

This affordability check preserves the preferred £1,000 buffer.

---

## Available Cashflow

| Item | Amount |
| --- | ---: |
| Total operating household-visible cash | £8,751.04 |
| Less: preferred cash buffer | -£1,000.00 |
| Less: listed known liabilities | -£4,896.04 |
| **Available for affordability decisions** | **£2,855.00** |

Scope notes:

- Trading 212 Cash ISA is treated as emergency fund / restricted cash and is not included in the cashflow test.
- The pending £9,327.50 IOND proceeds are excluded under the locked portfolio allocation assumption.
- Kelly's pending £400.00 work reimbursement is not included in the base affordability test because it has not yet been received.
- The Santander top-up imbalance is not included as a fixed cash outflow because the exact settlement amount has not been calculated and an internal settlement may not reduce aggregate household-visible cash.

---

## Calibrated Bucket Requirement

Budget Calibration set the following August controllable spending buckets:

| Bucket group | Amount |
| --- | ---: |
| Shared household buckets | £1,575.00 |
| Romeo personal buckets | £523.70 |
| Kelly personal buckets | £476.30 |
| **Total calibrated bucket requirement** | **£2,575.00** |

Shared and personal bucket funding split:

| Person | Shared bucket share | Personal buckets | Total controllable bucket funding |
| --- | ---: | ---: | ---: |
| Romeo | £824.83 | £523.70 | £1,348.53 |
| Kelly | £750.17 | £476.30 | £1,226.47 |
| **Total** | **£1,575.00** | **£1,000.00** | **£2,575.00** |

---

## Affordability Result

The calibrated August buckets are fully affordable while preserving the preferred £1,000 buffer.

| Test | Amount |
| --- | ---: |
| Available for affordability decisions | £2,855.00 |
| Less: calibrated bucket requirement | -£2,575.00 |
| **Headroom after calibrated buckets** | **£280.00** |

The household can fund the full calibrated bucket requirement without reducing the preferred buffer and without using the pending IOND proceeds.

---

## Sensitivity Checks

| Scenario | Result |
| --- | --- |
| Preserve preferred £1,000 buffer and fund full calibrated buckets | Affordable; £280.00 headroom remains |
| Preserve minimum £500 buffer and fund full calibrated buckets | Affordable; £839.99 headroom above minimum buffer |
| Include pending Kelly £400 reimbursement after receipt | Would increase available headroom to £739.99 if treated as available household cash |
| Include pending IOND proceeds as general cash | Not tested; locked assumptions exclude it pending portfolio-os allocation |

---

## Required Adjustments

No reductions to the calibrated August bucket limits are required for affordability.

No optional surplus use is approved in this phase. The £280.00 headroom belongs to Plan.

---

## Final Affordable Bucket Limits

| Bucket group | Affordable limit |
| --- | ---: |
| Shared household buckets | £1,575.00 |
| Romeo personal buckets | £523.70 |
| Kelly personal buckets | £476.30 |
| **Total affordable bucket limit** | **£2,575.00** |

Detailed bucket limits remain as set in `budget-calibration.md`.

---

## Implications for Plan

1. Plan can start from the full calibrated bucket requirement of £2,575.00.
2. The preferred £1,000 buffer can be preserved with £280.00 headroom remaining.
3. The £280.00 headroom is not allocated by this phase.
4. IOND proceeds remain excluded from ordinary plan cash unless the portfolio allocation assumption changes.
5. Kelly's pending £400.00 reimbursement should be handled by Plan only if timing and treatment are confirmed there.
6. Santander internal settlement remains a Plan trace item because the exact amount is still pending.
7. Payments above listed minimums and BT operational targets remain Plan decisions.

---

## Phase Lock

Status: Complete
Completed: 2026-08-03

Affordability check complete. Proceed to Plan.
