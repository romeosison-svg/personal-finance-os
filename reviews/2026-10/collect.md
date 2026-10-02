# Collect — October 2026

Review started: 2026-09-30

## Phase Status

| Phase | Status | Completed |
| --- | --- | --- |
| Collect | Complete | 2026-10-02 |
| Reconcile | Complete | 2026-10-02 |
| Assumptions | Complete | 2026-10-02 |
| Position | Complete | 2026-10-02 |
| Handoff | Not Started | |
| Analyse | Not Started | |
| Budget Calibration | Not Started | |
| Affordability Check | Not Started | |
| Plan | Not Started | |
| Strategy | Not Started | |

---

## Input Checklist

### Bank Accounts

- [x] Current account statement — Kelly Halifax
- [x] Current account statement — Romeo Lloyds
- [x] Current account statement — Romeo Starling not required; user confirms balance is unchanged
- [x] Savings balance confirmation — Romeo Chip Cash ISA
- [x] Joint account statement — Santander
- [x] Any other accounts — Romeo Amex Platinum statement present and confirmed in scope

### Credit Cards

- [x] Credit card statement — Kelly Amex
- [x] Credit card statement — Kelly Halifax
- [x] Credit card statement — Romeo Amex
- [x] Credit card statement — Romeo Amex Platinum
- [x] Credit card statement — Romeo Barclaycard not required; user confirms nil balance
- [x] Credit card statement — Romeo Halifax
- [x] Balance transfer card statement — Romeo M&S
- [x] Balance transfer card statement — Romeo MBNA

### Other Inputs

- [x] Income confirmation / payslips — Kelly payslip present; user confirms Romeo's Lloyds salary receipt is sufficient
- [x] Reimbursement records — user confirms every Lloyds incoming transaction for exactly £5.15, £20.50, or £10.25 was a reimbursement
- [x] Upcoming direct debits confirmed — unchanged from the established baselines
- [x] Known one-off payments — none
- [x] Expected income beyond regular salary — £250 birthday gift from Romeo's mum received

## Notes

- `statements.md` was built from the 12 usable local filenames only. Statement contents were not read during Collect.
- Five missing Drive files were copied locally on 2026-10-01. Statement files remain local and are excluded from Git by `.gitignore`.
- Metadata files ending in `Zone.Identifier` were ignored.
- Romeo Starling and Barclaycard statements are not required: the user confirms the Starling balance is unchanged and Barclaycard has a nil balance.
- The user confirms `2026-09_Halifax_credit.pdf` is Romeo's Halifax card statement.
- The user confirms `2026-09_Romeo_AmexP_credit.pdf` is the in-scope Romeo Amex Platinum statement and that it has a small balance.
- Kelly's payslip is present. The user confirms Romeo's Lloyds salary receipt is sufficient income confirmation; verify it during Reconcile.
- Romeo received a £250 birthday gift from his mum. This is recorded as additional income only; do not apply it until the appropriate later phase.
- User confirms that every Lloyds incoming transaction for exactly £5.15, £20.50, or £10.25 was a reimbursement. During Reconcile, find every occurrence and calculate the total; do not assume there was only one of each.
- User confirms upcoming direct debits are unchanged from the established baselines and there are no known one-off payments.
- Statement files may be added while Collect remains open.
- Build `statements.md` from filenames only during Collect; do not read statement contents.
- A dated Chip Cash ISA balance confirmation is sufficient unless full evidence is needed because of a material change or discrepancy.

## Phase Lock

Status: Complete
Completed: 2026-10-02
Locked by: Codex

All available required inputs are present or explicitly confirmed. Proceed to Reconcile.
