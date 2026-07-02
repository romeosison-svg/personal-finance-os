# Affordability Check - July 2026

> Requires: Budget Calibration complete

Budget Calibration answers: what are sensible behavioural spending caps?
Affordability Check answers: can those caps actually be funded from current cashflow?
Plan answers: what actions should be taken now given the affordable limits?

## Phase Status

| Phase                | Status      | Completed  |
| -------------------- | ----------- | ---------- |
| Collect              | Complete    | 2026-07-01 |
| Reconcile            | Complete    | 2026-07-01 |
| Assumptions          | Complete    | 2026-07-01 |
| Position             | Complete    | 2026-07-01 |
| Handoff              | Complete    | 2026-07-01 |
| Analyse              | Complete    | 2026-07-01 |
| Budget Calibration   | Complete    | 2026-07-01 |
| Affordability Check  | Complete    | 2026-07-02 |
| Plan                 | Not Started |            |
| Strategy             | Not Started |            |

---

## Scope and Basis

This phase tests whether the July budget calibration can be funded from the locked July position.

It does not:

- decide final payment amounts;
- approve optional spending;
- create the payment plan;
- reopen locked assumptions;
- change the cash buffer policy.

The Plan phase should use this affordability result to decide what gets funded, reduced, deferred, or paid down.

---

## Inputs Used

- `reviews/2026-07/position.md` - locked July position
- `reviews/2026-07/position-handoff.md` - verified position handoff
- `reviews/2026-07/assumptions.md` - locked assumptions plus approved Zoe classification correction
- `reviews/2026-07/budget-calibration.md` - calibrated July bucket limits

---

## Fixed Obligations Already Included in Position

The locked Position already deducts the following listed July liabilities before calculating available cash for planning:

| Item | Amount |
| --- | ---: |
| Mortgage | £3,069.53 |
| Santander joint account gross top-up need | £1,001.92 |
| M&S credit card DD | £190.00 |
| Romeo Amex minimum | £142.15 |
| Romeo Barclaycard payment already made | £123.20 |
| MBNA DD | £276.21 |
| MBNA manual top-up to operational target | £99.79 |
| M&S manual top-up to operational target | £5.00 |
| Kelly Amex minimum | £25.00 |
| Kelly tithe | ~£327.20 |
| Shared bills settlement adjustment | £35.02 |
| PPL Bolton extra hotel night | £91.00 |
| PPL Farnborough accommodation | £123.00 |
| **Total listed known liabilities** | **£5,509.02** |

These are treated as already funded before the affordability test begins.

---

## Required Buffer

| Buffer | Amount | Treatment |
| --- | ---: | --- |
| Minimum cash buffer | £500.00 | Absolute floor |
| Preferred cash buffer | £1,000.00 | Used by locked Position |

This affordability check preserves the preferred £1,000 buffer unless the Plan explicitly chooses otherwise.

---

## Available Cashflow

| Item | Amount |
| --- | ---: |
| Total household-visible cash | £8,123.29 |
| Less: preferred cash buffer | -£1,000.00 |
| Less: listed known liabilities | -£5,509.02 |
| **Available for affordability decisions** | **£1,614.27** |

This £1,614.27 is the maximum available for discretionary buckets, optional costs, extra card payments, emergency-fund contribution, and surplus-only goals while preserving the preferred buffer.

---

## Calibrated Bucket Requirement

Budget Calibration set the following July controllable spending buckets:

| Bucket group | Amount |
| --- | ---: |
| Shared household buckets | £1,300.00 |
| Romeo individual buckets | £380.00 |
| Kelly individual buckets | £400.00 |
| **Total calibrated bucket requirement** | **£2,080.00** |

Shared household bucket funding split:

| Person | Shared bucket share | Individual buckets | Total |
| --- | ---: | ---: | ---: |
| Romeo | £763.10 | £380.00 | £1,143.10 |
| Kelly | £536.90 | £400.00 | £936.90 |

---

## Affordability Result

The calibrated July buckets are **not fully affordable** while preserving the preferred £1,000 buffer.

| Test | Amount |
| --- | ---: |
| Available for affordability decisions | £1,614.27 |
| Less: calibrated bucket requirement | -£2,080.00 |
| **Shortfall vs calibrated buckets** | **-£465.73** |

To fund all calibrated buckets without changing anything else, the household would need to operate at an implied buffer of approximately **£534.27** instead of £1,000.

That is above the absolute £500 minimum buffer, but below the preferred buffer.

---

## Optional / Internal Items

| Item | Amount | Affordability treatment |
| --- | ---: | --- |
| Plumbing work | ~£300.00 | Optional cost; not affordable on top of full calibrated buckets while preserving the £1,000 buffer |
| Zoe vehicle cost settlement | £428.94 | Internal household settlement; does not reduce aggregate household-visible cash if moved within included accounts |
| Kelly personal savings replenishment | £1,316.83 target | Surplus-only goal; not affordable before reducing buckets or extra debt payments |
| Emergency fund contribution | TBC | Not affordable unless Plan reduces buckets, lowers buffer, or defers other goals |
| Romeo Amex above minimum | Up to £791.42 extra to pay statement balance in full | Competes directly with buckets and optional costs |
| Barclaycard clearance | £202.97 remaining balance | July minimum has already been satisfied by the 1 Jul payment; clearing the remaining balance competes directly with buckets and optional costs |

The Zoe settlement affects ownership and fairness between accounts, not aggregate household affordability. The Plan phase should decide the mechanics of settlement.

---

## Required Adjustments

If the preferred £1,000 buffer is preserved, July must reduce the calibrated bucket plan by at least **£465.73** before approving any optional spending or extra debt repayment.

User direction added 2026-07-02: use the minimum-buffer approach and trim buckets enough to prioritise clearing Barclaycard.

Possible adjustment routes for Plan:

1. Reduce controllable buckets to **£1,614.27** and approve no optional plumbing, no emergency-fund contribution, and no extra card repayment above already-listed liabilities.
2. Preserve more of the calibrated buckets by temporarily operating closer to the £500 minimum buffer.
3. Fund plumbing only by either reducing buckets further or accepting a lower buffer.
4. Treat any Amex pay-in-full amount above the minimum as a Plan trade-off against buckets, not as automatically affordable.
5. Treat clearing the remaining Barclaycard balance as a Plan trade-off against buckets, not as automatically affordable.
6. Keep Kelly savings replenishment as surplus-only after established goals.

---

## Final Affordable Bucket Limits

This phase does not choose the final cuts. For Plan, the affordability ceiling is:

| Scenario | Bucket funding | Optional plumbing | Extra card repayment above listed liabilities | Result |
| --- | ---: | ---: | ---: | --- |
| Preserve preferred buffer | £1,614.27 | £0.00 | £0.00 | Affordable |
| Full calibrated buckets | £2,080.00 | £0.00 | £0.00 | Short by £465.73 |
| Full calibrated buckets + plumbing | £2,080.00 | £300.00 | £0.00 | Short by £765.73 |
| Preserve preferred buffer + plumbing | £1,314.27 | £300.00 | £0.00 | Affordable only if buckets are cut to £1,314.27 |
| Minimum-buffer approach | Up to £2,114.27 | £0.00 | £0.00 | Uses cash down to £500 buffer |
| Minimum buffer + clear Barclaycard | £1,911.30 | £0.00 | £202.97 | Affordable; trims calibrated buckets by £168.70 |

The minimum-buffer approach creates only **£34.27** of headroom above full calibrated buckets, so it still does not fund plumbing or meaningful extra card repayment without further cuts.

With the user-directed bucket trim, Plan should test a working bucket ceiling of **£1,911.30** and allocate **£202.97** to clear the remaining Barclaycard balance.

Suggested bucket trim for Plan to confirm:

| Bucket | Original limit | Trim | Revised limit |
| --- | ---: | ---: | ---: |
| Dining / restaurants | £200.00 | -£70.00 | £130.00 |
| Fast food | £50.00 | -£25.00 | £25.00 |
| Coffee / bakery | £50.00 | -£18.70 | £31.30 |
| Discretionary transport | £100.00 | -£30.00 | £70.00 |
| Entertainment | £100.00 | -£25.00 | £75.00 |
| **Total trim** | | **-£168.70** | |

---

## Implications for Plan

Plan should start from a constrained position:

1. The £2,080 calibrated bucket plan is a useful behavioural target, but it is not fully fundable with the preferred buffer.
2. User direction is to trim buckets, use the £500 minimum buffer, and prioritise clearing Barclaycard.
3. The working Plan scenario is £1,911.30 of controllable buckets plus £202.97 to clear the remaining Barclaycard balance.
4. Plumbing at ~£300 can fit only if controllable buckets are reduced further, the buffer is pushed below £500, or another goal is deferred.
5. The Zoe settlement can be processed as an internal household allocation without reducing aggregate household cash.
6. Amex pay-in-full is not automatically affordable; only the £142.15 minimum is already included in locked liabilities.
7. Barclaycard should still receive no new lifestyle spend. Its corrected current balance is £202.97, and the July minimum has already been satisfied by the 1 Jul payment.
8. Kelly personal savings replenishment remains a surplus-only goal and should not be funded ahead of established July priorities.

---

## Phase Lock

Status: Complete
Completed: 2026-07-02

Affordability check complete. Proceed to Plan.
