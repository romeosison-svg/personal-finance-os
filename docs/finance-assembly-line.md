# Finance Assembly Line

The Finance Assembly Line is the core operating model of Personal Finance OS.

Monthly reviews move through six sequential, gated phases. No phase may be skipped. Each phase produces a locked output that the next phase depends on.

```
collect → reconcile → assumptions → position → plan → strategy
```

---

## Why an Assembly Line?

Financial decisions made without verified facts are plans made from memory. Memory is unreliable. Assumptions made without explicit rules create invisible drift. Recommendations made before the position is known are guesses dressed as plans.

The Assembly Line enforces a discipline:

- **Facts before analysis**
- **Position before planning**
- **Planning before strategy**

Each phase gate is a quality checkpoint.

---

## Phase Reference

---

### Phase 1 — Collect

**Alias:** `collect`

**Purpose:**  
Gather all required inputs before any analysis begins.

**Inputs:**
- Bank statements (all accounts)
- Credit card statements (all cards)
- Reimbursement spreadsheets
- Current balances (as of review date)
- Known upcoming obligations (direct debits, scheduled payments)
- Outstanding invoices or expected income

**Process:**
Work through the collect checklist. Mark each item as obtained or confirmed not applicable.  
Do not begin analysis. Do not calculate anything.  
The only goal of this phase is to confirm that all inputs are present.

**Output:**  
A completed input checklist. All items either obtained or explicitly noted as unavailable and why.

**Gate condition:**  
All available inputs confirmed present. Phase status set to `Complete`.

**What does NOT belong here:**  
No balances calculated. No totals. No commentary on what the numbers mean.

---

### Phase 2 — Reconcile

**Alias:** `reconcile`

**Purpose:**  
Establish the financial truth from the gathered inputs.

**Inputs:**
- Outputs from Phase 1 (collect)

**Process:**
- Record statement closing balances for each account
- Confirm payments already made since statement date
- Confirm outstanding balances (what is still owed, not yet paid)
- Match reimbursements to the statement periods they belong to
- Confirm direct debits already scheduled
- Note any discrepancies or items requiring resolution

**Output:**  
Locked financial facts. A verified snapshot of balances, payments, and outstanding amounts as of the review date.

**Gate condition:**  
All accounts reconciled. Discrepancies resolved or explicitly noted. Phase status set to `Complete`.

**What does NOT belong here:**  
No planning. No recommendations. No "we should pay X this month."  
This phase only establishes what is true, not what should happen.

---

### Phase 3 — Assumptions

**Alias:** `assumptions`

**Purpose:**  
Confirm the planning rules that will govern the monthly plan.

**Inputs:**
- Persistent assumptions from [finance-profile.md](/docs/finance-profile.md)
- Any one-time overrides for this month

**Process:**
- Review the planning assumptions in finance-profile.md
- Confirm each assumption is still valid for this month
- Note any temporary overrides (e.g. lower buffer this month due to known expense)
- Lock the assumptions that the plan will be built from

**Output:**  
Locked planning assumptions for this month.

**Gate condition:**  
All assumptions reviewed and confirmed or overridden with reason. Phase status set to `Complete`.

**What does NOT belong here:**  
No plan generation. No calculations using the assumptions yet.  
This phase only confirms the rules — it does not apply them.

---

### Phase 4 — Position

**Alias:** `position`

**Purpose:**  
Create a current financial position snapshot using locked facts and confirmed assumptions.

**Inputs:**
- Locked facts from Phase 2 (reconcile)
- Locked assumptions from Phase 3 (assumptions)

**Process:**
- Summarise current cash balances across all accounts
- Summarise current credit card balances
- Summarise current balance transfer balances
- List known liabilities (scheduled payments, outstanding bills)
- Calculate available funds (cash minus required buffer)
- Note the financial position clearly and plainly

**Output:**  
Current Financial Position. A single document summarising where things stand financially as of the review date.

**Gate condition:**  
All positions calculated from locked facts. Available funds clearly stated. Phase status set to `Complete`.

**What does NOT belong here:**  
No payment plan. No recommendations.  
The position describes the current state — it does not prescribe actions.

---

### Phase 5 — Plan

**Alias:** `plan`

**Purpose:**  
Generate the next month's payment plan from the locked position and confirmed assumptions.

**Inputs:**
- Current Financial Position from Phase 4 (position)
- Locked assumptions from Phase 3 (assumptions)

**Process:**
- Allocate mortgage payments
- Allocate bill payments (with split methodology applied)
- Allocate credit card payments (minimum and over-minimum)
- Allocate balance transfer top-ups if applicable
- Allocate emergency fund contribution if applicable
- Confirm total allocations against available funds
- Note surplus or shortfall

**Output:**  
Approved Monthly Plan. A complete schedule of payments and allocations for the month.

**Gate condition:**  
All allocations made. Total reconciled against available funds. Plan approved. Phase status set to `Complete`.

**What does NOT belong here:**  
No vehicle finance decisions. No investment decisions.  
Tactical month-to-month payments only. Strategic decisions belong in Phase 6.

---

### Phase 6 — Strategy

**Alias:** `strategy`

**Purpose:**  
Review and record long-term financial decisions.

**Inputs:**
- Current Financial Position from Phase 4 (position)
- Approved Monthly Plan from Phase 5 (plan)
- Historical reviews (for trend context)

**Process:**
- Review any open strategic questions (vehicles, pensions, investments, business)
- Assess whether current direction is aligned with long-term goals
- Record decisions made and reasoning
- Note items deferred and why
- Update finance-profile.md if any persistent assumptions change

**Output:**  
Strategic recommendations and decisions for this review period.

**Gate condition:**  
All open strategic items reviewed. Decisions recorded with reasoning. Phase status set to `Complete`.

**What does NOT belong here:**  
This phase does not override the plan. Strategic decisions affect future months, not the current plan.

---

## Phase Status Values

| Status      | Meaning                                          |
| ----------- | ------------------------------------------------ |
| Not Started | Phase not yet begun                              |
| In Progress | Phase started, not yet locked                    |
| Complete    | Phase locked, output available to next phase     |
| Blocked     | Phase cannot proceed — reason documented         |

---

## Phase Dependencies

```
Phase 1 (collect)
    ↓
Phase 2 (reconcile)     ← requires: Phase 1 complete
    ↓
Phase 3 (assumptions)   ← requires: Phase 2 complete
    ↓
Phase 4 (position)      ← requires: Phases 2 + 3 complete
    ↓
Phase 5 (plan)          ← requires: Phases 3 + 4 complete
    ↓
Phase 6 (strategy)      ← requires: Phases 4 + 5 complete
```
