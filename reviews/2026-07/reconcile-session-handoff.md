# Reconcile — Session Handoff Note
> July 2026 review | Created: 2026-07-01 | Status: In Progress (incomplete)

This file exists because the reconcile phase was interrupted mid-session. Use it to resume in a new Claude conversation without losing context.

---

## What Has Been Done

All 9 statement PDFs were read from `reviews/2026-07/statements/`. 8 of 9 succeeded. Figures have been written into `reviews/2026-07/reconcile.md`.

### Accounts reconciled (balances confirmed from statements):

| Account | Confirmed Balance | Statement Date |
|---|---|---|
| Romeo / Lloyds current | £4,980.04 | 30 Jun 2026 |
| Romeo / Starling current | -£622.18 (overdrawn) | 30 Jun 2026 |
| Kelly / Halifax current | £3,565.43 | 29 Jun 2026 |
| Kelly / Amex credit | £877.67 | 24 Jun 2026 |
| Kelly / Halifax credit | £0.00 (paid in full 29 Jun) | 07 Jun 2026 |
| Romeo / Amex credit | £933.57 + £443.32 Plan It = £1,376.89 total | 15 Jun 2026 |
| Romeo / Barclaycard | £284.67 | 15 Jun 2026 |
| Romeo / MBNA BT | £11,048.29 | 28 Jun 2026 |

### Income confirmed:
- Romeo net salary: £4,654.89 (TekSystems, 30 Jun, Lloyds)
- Kelly net salary: £4,252.89 (Morningstar, 24 Jun, Halifax) — inflated by May 18–31 arrears

---

## What Is Still Outstanding

Before reconcile can be locked, the following must be resolved:

### 1. Romeo / M&S BT — balance unknown
- `reviews/2026-07/statements/2026-06_Romeo_M&S_BT.pdf` is an **invalid/corrupt PDF** (missing %PDF- header)
- Action: user must provide the closing balance and statement date manually, OR re-upload the file

### 2. Kelly payslip — normal monthly salary not yet extracted
- File present: `2026-06_Kelly_payslip.pdf` — has not been read
- Need: normal monthly net salary (i.e. June gross minus May 18–31 arrears) for mortgage ratio calc
- Action: read the payslip OR ask user to confirm the figure

### 3. Court reimbursements total — not yet extracted
- File present: `2026-06_Romeo_courtreimbursements.pdf` — has not been read
- Need: total outstanding reimbursements owed to Romeo for June
- Action: read the file OR ask user to confirm the figure

### 4. New July direct debits — account not confirmed
- MG PCP lease: £310.84/month — which account?
- MG insurance: £40.00/month — which account?
- Zoe insurance: £61.29/month — which account?
- Action: ask user

### 5. Joint account estimated balance
- Statement arrives 3 July 2026
- Need: rough balance estimate from online banking, or defer to position phase
- Action: ask user

---

## How to Resume

In a new Claude session:

1. Say: `reconcile`
2. Claude will read `reconcile.md` (already populated) and `collect.md` (locked Complete)
3. The outstanding items above will guide what to ask next
4. Do NOT re-read all 9 statement PDFs — the facts are already in `reconcile.md`

Or paste this file directly into the new session as context.

---

## Key Flags Already Documented in reconcile.md

- Romeo Starling overdrawn -£622.18 at 35% APR (no income received in Jun)
- MBNA jumped to £11,048.29 due to £2,317 BT from Barclaycard (4 Jun) + £69.51 fee; both tranches 0% promo
- Romeo Amex has 5 active Plan It instalments, £443.32 remaining, £101/month
- Kelly → Romeo: £428.94 Zoe reimbursement still outstanding
