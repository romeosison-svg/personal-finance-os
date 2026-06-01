# ChatGPT Phase Prompts

Standard prompts for handing off to ChatGPT after the handoff phase is complete.

Copy the relevant prompt, attach or paste the required artefacts, and send to ChatGPT.

---

## Phase 6 — Analyse

**Required inputs:**
- `reviews/YYYY-MM/position-handoff.md`
- `reviews/YYYY-MM/transactions.csv`

**Prompt:**

```
You are continuing a FinanceOS monthly review for YYYY-MM.

Phases 1–5 (collect, reconcile, assumptions, position, handoff) have been completed by Claude Code.
The verified facts and locked assumptions are in position-handoff.md.
The transaction data is in transactions.csv.

Your task is Phase 6: Analyse.

Do not reopen or contradict the completed phases unless you find a genuine inconsistency in the data.
If you find one, flag it explicitly before proceeding.

Using the transaction data in transactions.csv and the context in position-handoff.md:

1. Categorise all transactions from transactions.csv into spending categories.
2. Summarise total spend by category for YYYY-MM.
3. Identify the top 3–5 spending categories by household total.
4. Flag any unusual, large, or anomalous transactions.
5. Note any expected reimbursements or known one-offs that distort the picture.
6. Compare to any prior periods if data is available.
7. Note any subscriptions identified.

Output a clean spending analysis suitable for committing to reviews/YYYY-MM/analyse.md.

Do not produce a payment plan. Do not produce strategic recommendations. Analysis only.
```

---

## Phase 7 — Plan

**Required inputs:**
- `reviews/YYYY-MM/position-handoff.md`
- `reviews/YYYY-MM/analyse.md`

**Prompt:**

```
You are continuing a FinanceOS monthly review for YYYY-MM.

Phases 1–6 (collect, reconcile, assumptions, position, handoff, analyse) are complete.
The verified facts and locked assumptions are in position-handoff.md.
The spending analysis is in analyse.md.

Your task is Phase 7: Plan.

Using the locked assumptions in position-handoff.md and the spending picture from analyse.md:

1. Answer all open questions listed in section 8 of position-handoff.md.
2. Produce the complete payment plan for YYYY-MM with exact amounts.
3. List payments in priority order: mandatory obligations first, then buffer preservation, then discretionary.
4. For each balance transfer card, state the exact top-up amount required (if any).
5. For each credit card, state the exact payment amount and classification (mandatory / flexible / pay-in-full).
6. State the projected cash position after all payments, with a Lloyds balance trace if applicable.
7. Confirm the cash buffer is preserved at or above the minimum stated in position-handoff.md.

Use exact amounts. Not ranges. Not approximations.
Preserve the minimum cash buffer unless you flag an explicit exception with reasoning.
Explain all trade-offs where payments compete for limited funds.
Sequence payments around any cashflow timing constraints noted in position-handoff.md.

Output a clean payment plan suitable for committing to reviews/YYYY-MM/plan.md.
```

---

## Phase 8 — Strategy

**Required inputs:**
- `reviews/YYYY-MM/position-handoff.md`
- `reviews/YYYY-MM/analyse.md`
- `reviews/YYYY-MM/plan.md`

**Prompt:**

```
You are continuing a FinanceOS monthly review for YYYY-MM.

Phases 1–7 (collect, reconcile, assumptions, position, handoff, analyse, plan) are complete.
The verified facts are in position-handoff.md. The spending analysis is in analyse.md. The payment plan is in plan.md.

Your task is Phase 8: Strategy.

Using the full picture from position-handoff.md, analyse.md, and plan.md:

1. Identify any strategic risks that should be escalated for joint review.
2. Assess the current balance transfer strategy: is it on track? Should it be accelerated, maintained, or adjusted?
3. Assess the emergency fund position: adequate? Contributions paused, maintained, or increased?
4. Identify any longer-horizon decisions or changes to standing assumptions worth considering.
5. Flag any spending patterns from analyse.md that suggest a structural issue (not just a one-off).
6. Summarise the top 2–3 strategic priorities for the next 1–3 months.

Be specific. Explain trade-offs. Flag anything that requires a joint decision.

Output a clean strategy note suitable for committing to reviews/YYYY-MM/strategy.md.
```
