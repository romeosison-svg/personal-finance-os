# Workflow Reference

Process commands for the Personal Finance Assembly Line.

These are conceptual commands — process instructions, not executable scripts. They describe what to do at each stage of a monthly review.

---

## Command Reference

---

### `finance start`

**What it means:**  
Begin a new monthly review.

**Process:**
1. Create a new folder under `/reviews/` named `YYYY-MM` (e.g. `reviews/2026-07`)
2. Create the seven phase files: `collect.md`, `reconcile.md`, `assumptions.md`, `position.md`, `analyse.md`, `plan.md`, `strategy.md`
3. Create two handoff artefact placeholders: `position-handoff.md`, `transactions.csv`
4. Copy the templates from `/docs/monthly-review-template.md` and `templates/`
5. Set all phase statuses to `Not Started`
6. Record the review start date

**You are ready when:** The folder exists with phase files and handoff placeholders.

---

### `collect`

**What it means:**  
Begin Phase 1. Gather all financial inputs before any analysis.

**Process:**
1. Open `collect.md`
2. Work through the input checklist
3. Obtain or locate each item: bank statements, credit card statements, reimbursement records, current balances, known upcoming payments
4. Mark each checklist item as obtained or note why it is unavailable
5. Record any anomalies or items to chase
6. When all available inputs are confirmed, set phase status to `Complete` and record the date
7. Commit: `git commit -m "collect: phase 1 complete — YYYY-MM"`

**Gate:** Do not open `reconcile.md` until collect is marked `Complete`.

---

### `reconcile`

**What it means:**  
Begin Phase 2. Establish verified financial facts from the collected inputs.

**Requires:** `collect` complete.

**Process:**
1. Open `reconcile.md`
2. For each account: record the statement closing balance
3. Confirm any payments made since the statement date
4. Calculate the current outstanding balance for each account
5. Match reimbursements to their statement periods
6. Confirm all direct debits already scheduled
7. Document any discrepancies
8. When all accounts are reconciled, set phase status to `Complete` and record the date
9. Commit: `git commit -m "reconcile: phase 2 complete — YYYY-MM"`

**Gate:** Do not open `assumptions.md` until reconcile is marked `Complete`.

---

### `assumptions`

**What it means:**  
Begin Phase 3. Confirm the planning rules for this month.

**Requires:** `reconcile` complete.

**Process:**
1. Open `assumptions.md`
2. Open `/docs/finance-profile.md`
3. Review each persistent assumption
4. Confirm it still applies this month, or document an override with reason
5. Ensure all planning rules are explicitly stated for this review
6. When all assumptions are confirmed or overridden, set phase status to `Complete` and record the date
7. Commit: `git commit -m "assumptions: phase 3 complete — YYYY-MM"`

**Gate:** Do not open `position.md` until assumptions is marked `Complete`.

---

### `position`

**What it means:**  
Begin Phase 4. Calculate and record the current financial position.

**Requires:** `reconcile` and `assumptions` both complete.

**Process:**
1. Open `position.md`
2. Using locked facts from `reconcile.md`, calculate:
   - Total cash across all accounts
   - Total credit card balances owed
   - Total balance transfer balances owed
   - Known upcoming liabilities
   - Available funds (total cash minus required buffer minus known liabilities)
3. Record the current financial position clearly
4. When the position is fully calculated, set phase status to `Complete` and record the date
5. Commit: `git commit -m "position: phase 4 complete — YYYY-MM"`

**Gate:** Do not begin handoff until position is marked `Complete`.

---

### `handoff`

**What it means:**  
Begin Phase 5. Export verified facts and transaction data for ChatGPT.

This is the formal boundary between Claude's factual work and ChatGPT's judgement work. Handoff produces two artefacts. ChatGPT does not begin analyse until both are committed.

**Requires:** `position` complete.

**Process:**
1. Open `position-handoff.md` (or create from `templates/position-handoff-template.md`)
2. Populate all sections using verified data from `reconcile.md`, `assumptions.md`, and `position.md`
3. Include only facts — no categorisation, no recommendations, no analysis
4. Create `transactions.csv` (or use `templates/transactions-template.csv` as the header)
5. Populate transaction rows from raw credit card statement data — merchant, amount, type only
6. Do not categorise. Preserve raw merchant/description text.
7. Review both files for completeness and accuracy
8. Set phase status to `Complete` and record the date
9. Commit: `git commit -m "handoff: phase 5 complete — YYYY-MM"`
10. Provide to ChatGPT using the prompt in `templates/chatgpt-prompts.md`

**Gate:** Do not give ChatGPT the analyse prompt until both handoff artefacts are committed.

---

### `analyse`

**What it means:**  
Begin Phase 6. Review credit card spending patterns from the month's statements.

**Owner:** ChatGPT. Use the Phase 6 prompt from `templates/chatgpt-prompts.md`.

**Requires:** `handoff` complete.

**Process:**
1. Open `analyse.md`
2. Read all credit card statements (Romeo and Kelly's cards) from the statements folder or Google Drive
3. Categorise every transaction by type (groceries, dining, transport, subscriptions, health, entertainment, retail, etc.)
4. Total spend per card and across the household combined
5. Flag notable items: highest categories, recurring subscriptions, large one-off transactions
6. Record observations only — no recommendations, no judgements
7. Set phase status to `Complete` and record the date
8. Commit: `git commit -m "analyse: phase 5 complete — YYYY-MM"`

**Gate:** Do not open `plan.md` until analyse is marked `Complete`.

---

### `plan`

**What it means:**  
Begin Phase 7. Generate the monthly payment plan.

**Owner:** ChatGPT. Use the Phase 7 prompt from `templates/chatgpt-prompts.md`.

**Requires:** `analyse` complete.

**Process:**
1. Open `plan.md`
2. Using the available funds figure from `position.md` and the locked assumptions from `assumptions.md`:
   - Allocate mortgage payment (with split as defined in assumptions)
   - Allocate bill payments (with split as defined in assumptions)
   - Allocate minimum credit card payments
   - Allocate BT repayments to hit monthly targets
   - Allocate emergency fund contribution
   - Allocate remaining credit card balance if funds allow
3. Total all allocations
4. Compare total allocations against available funds
5. Confirm surplus or note shortfall and resolution
6. Review and approve the plan
7. Set phase status to `Complete` and record the date
8. Commit: `git commit -m "plan: phase 6 complete — YYYY-MM"`

**Gate:** Do not open `strategy.md` until plan is marked `Complete`.

---

### `strategy`

**What it means:**  
Begin Phase 8. Review long-term financial decisions.

**Owner:** ChatGPT. Use the Phase 8 prompt from `templates/chatgpt-prompts.md`.

**Requires:** `plan` complete.

**Process:**
1. Open `strategy.md`
2. Review any open strategic questions (vehicles, pensions, investments, business decisions)
3. Assess alignment with long-term financial goals
4. Record decisions made and reasoning
5. Note items deferred and when to revisit them
6. If any persistent assumptions should change, update `finance-profile.md` and commit the change separately
7. Set phase status to `Complete` and record the date
8. Commit: `git commit -m "strategy: phase 7 complete — YYYY-MM"`

**The monthly review is now complete.**

---

### `import`

**What it means:**  
Import a ChatGPT-generated artefact into the active review and commit it as a first-class FinanceOS output.

**Usage:** `import <phase>` where `<phase>` is `analyse`, `plan`, or `strategy`

**Requires:** The preceding phase must be `Complete` (same gate rules as native phases).

**Process:**
1. Identify the active review month
2. Validate the artefact type and phase gate
3. Ask the user to paste the ChatGPT-generated content
4. Write the content to `reviews/YYYY-MM/{phase}.md`, preserving the phase status dashboard
5. Add an import metadata block (source, date, phase, review)
6. Update the phase status to `Complete`
7. Stage and commit

**Commit messages:**
```
analyse: imported external analysis — YYYY-MM
plan: imported external plan — YYYY-MM
strategy: imported external strategy — YYYY-MM
```

**Repository persistence:** Claude Code always owns the commit. ChatGPT may produce the content; Claude saves and versions it. Once committed, an imported artefact is treated identically to a native phase output.

**Gate:** Same as native phases — import does not bypass sequencing.

---

### `status`

**What it means:**  
Check the current state of the active monthly review.

**Process:**
1. Open the current month's folder under `/reviews/`
2. Check the phase status table in each phase file
3. Identify the last completed phase
4. Identify the current active phase
5. Note any blocked phases and their blocking reasons

**Quick check:** The phase status dashboard at the top of each phase file shows the current state of the entire review.

---

## Review Commit Convention

Each phase completion should be committed with a consistent message format:

```
collect: phase 1 complete — 2026-07
reconcile: phase 2 complete — 2026-07
assumptions: phase 3 complete — 2026-07
position: phase 4 complete — 2026-07
handoff: phase 5 complete — 2026-07
analyse: phase 6 complete — 2026-07
plan: phase 7 complete — 2026-07
strategy: phase 8 complete — 2026-07
```

When a phase is fulfilled by an imported artefact rather than a native Claude execution, use the import convention instead:

```
analyse: imported external analysis — 2026-07
plan: imported external plan — 2026-07
strategy: imported external strategy — 2026-07
```

Both conventions create a clean, readable git history. The commit message distinguishes native from imported artefacts while preserving the same audit trail for every monthly review.

---

## Blocking and Resuming

If a phase is blocked (e.g., a bank statement has not arrived), set the phase status to `Blocked` and document the reason.

Do not advance to the next phase while a phase is blocked.

When the blocker is resolved, update the phase status and continue.

---

## Phase File Discipline

- Open only the phase file for the active phase.
- Do not write in future phase files until the preceding phase is locked.
- The phase lock section at the bottom of each file must be completed before moving on.
- Once a phase is locked, its facts and decisions are not revised without a documented reason.
