# Operating Allowance Tracker Handoff - July 2026

Use this handoff to start a new chat focused only on tracking July operating spend, especially Amex spend.

## Purpose

Track July day-to-day spending against the transition/control plan without trying to run a full bucket system yet.

The user should be able to enter a simple spend message such as:

`Romeo Amex £18.40 Tesco groceries`

The tracker should:

1. classify the spend;
2. subtract it from the July operating allowance;
3. show remaining operating allowance;
4. show how much Amex-backed cash should be preserved for future Amex payment;
5. warn if spend is outside the July guardrails.

---

## Source Plan

Source file: `reviews/2026-07/plan.md`

July is a transition/control month, not a full bucket rollout.

Key plan numbers:

| Item | Amount |
| --- | ---: |
| July operating allowance | £1,256.38 |
| Amex payoff reserve | £1,015.91 |
| Clear remaining Barclaycard | £0.00 deferred / conditional |
| Minimum cash buffer | £500.00 |

The operating allowance is the ceiling for normal July living costs.

---

## Starting Tracker State

| Tracker item | Amount |
| --- | ---: |
| Starting July operating allowance | £1,256.38 |
| Tracked operating spend so far | £0.00 |
| Remaining operating allowance | £1,256.38 |
| Amex-backed cash to preserve | £0.00 |
| Remaining Amex payoff reserve | £1,015.91 |

Update these numbers after each user entry.

---

## Spend Entry Format

Accept loose natural language. Expected examples:

- `Romeo Amex £18.40 Tesco groceries`
- `Kelly Amex £12.50 train`
- `Lloyds debit £7.80 coffee`
- `Cash £20 pickleball`
- `Refund £15 Tesco`

For each entry, extract:

| Field | Examples |
| --- | --- |
| Date | default to current date if not provided |
| Person | Romeo, Kelly, Shared, Unknown |
| Payment method | Romeo Amex, Kelly Amex, Lloyds, Halifax, Santander, cash, other |
| Amount | positive for spend, negative for refund |
| Merchant / description | Tesco, train, coffee, pickleball |
| Category | see categories below |
| Amex-backed? | Yes if paid on Romeo Amex or Kelly Amex |

Important categorisation rule: `SNB` / `SNB S200217` on Kelly Amex means train fare / essential transport, not pickleball.

Shared grocery rule: grocery / household food card transactions of **£20 or more** should be treated as shared household costs unless clearly personal. The earlier £40 working threshold is superseded.

---

## Categories

Use these broad categories, not detailed buckets:

| Category | Treatment |
| --- | --- |
| Groceries / household basics | Allowed, but essential spend only |
| Dining / takeaway / coffee | Allowed only if tightly controlled |
| Pickleball / sport | Allowed if conscious and not drifting |
| Essential transport | Kelly London train/TFL/SNB, necessary travel |
| Discretionary transport | Uber, optional parking, avoid where possible |
| Personal discretionary | Keep light |
| PPL / event cost | Not approved unless explicitly agreed |
| Plumbing / household repair | Deferred unless explicitly approved |
| Refund / reimbursement | Add back to allowance if it relates to tracked spend |
| Unknown | Ask user to classify |

---

## Update Rules

For normal spend:

`remaining operating allowance = previous remaining - spend amount`

For refunds:

`remaining operating allowance = previous remaining + refund amount`

For Amex spend:

Also update:

`Amex-backed cash to preserve = previous Amex-backed cash + spend amount`

For Amex refunds:

`Amex-backed cash to preserve = previous Amex-backed cash - refund amount`

Do not reduce the Amex payoff reserve for normal tracked operating spend unless the user explicitly overspends the operating allowance and chooses to cover the overspend from the reserve.

If operating allowance goes below £0:

1. show the overspend;
2. ask whether to reduce Amex payoff reserve, cut future spend, or use another source;
3. do not silently absorb it.

---

## Guardrails

Warn the user when:

| Situation | Warning |
| --- | --- |
| Barclaycard spend appears | Barclaycard should have no new spend in July |
| Uber / discretionary transport appears | Uber should be near-zero now Romeo has a driving licence |
| PPL accommodation appears | Not approved unless cheaper option is explicitly confirmed |
| Plumbing appears | Deferred unless explicitly approved |
| Amex spend is entered | Remind that matching cash should be preserved |
| Spend is unclear | Ask for category before updating |

---

## Response Format For Tracker Chat

After each spend entry, respond with:

```text
Recorded:
- Date:
- Person:
- Method:
- Category:
- Amount:
- Amex-backed cash to preserve:

Updated totals:
- Operating spend so far:
- Remaining operating allowance:
- Amex-backed cash to preserve:
- Remaining Amex payoff reserve:

Notes:
- ...
```

Keep responses short.

---

## Ledger Template

Maintain an in-chat ledger like this:

| Date | Person | Method | Merchant / description | Category | Amount | Amex-backed? |
| --- | --- | --- | --- | --- | ---: | --- |

If the user later asks to persist the tracker, update this file or create a CSV in `reviews/2026-07/`.

Suggested CSV path if needed:

`reviews/2026-07/operating-allowance-ledger.csv`

Suggested CSV columns:

```csv
date,person,method,merchant,category,amount,amex_backed,notes
```

---

## Current Open Decisions

Do not decide these silently:

1. Whether the £1,015.91 Amex payoff reserve goes to Romeo Amex, Kelly Amex, or split.
2. Whether PPL training accommodation is approved once a cheaper option is found.
3. Whether plumbing is approved.
4. Whether Kelly replenishes emergency savings from personal cash or from the Amex reserve.

---

## Starter Prompt For New Chat

Paste this into a new chat:

```text
Use `reviews/2026-07/operating-allowance-tracker-handoff.md` as the source of truth.

Your job is to track my July operating allowance.

Starting operating allowance: £1,256.38.
Starting tracked spend: £0.00.
Starting Amex-backed cash to preserve: £0.00.
Amex payoff reserve: £1,015.91.

When I enter spend, classify it, update the remaining allowance, and show the updated totals. If I paid on Amex, also track the cash that must be preserved for the future Amex payment.

Do not run the full monthly finance review. Only track the operating allowance and flag guardrail breaches.
```
