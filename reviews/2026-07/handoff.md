# Handoff — July 2026

> Requires: Position complete

## Phase Status

| Phase                | Status      | Completed  |
| -------------------- | ----------- | ---------- |
| Collect              | Complete    | 2026-07-01 |
| Reconcile            | Complete    | 2026-07-01 |
| Assumptions          | Complete    | 2026-07-01 |
| Position             | Complete    | 2026-07-01 |
| Handoff              | Complete    | 2026-07-01 |
| Analyse              | Not Started |            |
| Budget Calibration   | Not Started |            |
| Affordability Check  | Not Started |            |
| Plan                 | Not Started |            |
| Strategy             | Not Started |            |

---

## Handoff Artefacts

| Artefact | Status | Notes |
| --- | --- | --- |
| `reviews/2026-07/position-handoff.md` | Complete | Contains verified facts and locked assumptions only |
| `reviews/2026-07/transactions.csv` | Complete | Raw transaction export populated from local statement PDFs |

---

## Source Artefacts

| File | Status |
| --- | --- |
| `reviews/2026-07/collect.md` | Complete |
| `reviews/2026-07/reconcile.md` | Complete |
| `reviews/2026-07/assumptions.md` | Complete |
| `reviews/2026-07/position.md` | Complete |
| `docs/finance-profile.md` | Reference |

---

## Transaction Export

Raw transaction rows were exported from the local statement PDFs under `reviews/2026-07/statements/` using `pdftotext`.

Checked tools:

| Tool | Available? |
| --- | --- |
| `pdftotext` | Yes |
| `mutool` | No |
| `qpdf` | No |
| `tesseract` | No |
| `ocrmypdf` | No |
| Python PDF libraries (`pypdf`, `PyPDF2`, `pdfplumber`, `fitz`) | No |

`transactions.csv` contains 292 raw rows.

Extraction reconciliation:

| Account / Source | Rows | Check |
| --- | ---: | --- |
| Romeo Lloyds current | 58 | Money in £4,963.20; money out £5,048.05 |
| Kelly Halifax current | 39 | Money in £7,413.87; money out £3,872.92 |
| Romeo Starling current | 8 | Payments out £332.92 |
| Romeo Amex credit | 42 | Credits £810.78; extracted statement spend/fees £919.87 |
| Kelly Amex credit | 71 | Credits £774.12; new debits £877.67 |
| Romeo Barclaycard credit | 56 | Payments £3,477.40; transactions/charges £1,547.03 |
| Kelly Halifax credit | 11 | Payment £27.12; new transactions £218.60 |
| Romeo MBNA BT | 4 | Payments £349.00; new transactions/fees £2,386.51 |
| Romeo M&S BT | 2 | Payments £195.00 |
| Court reimbursements | 1 | User-confirmed £107.80 paid/received |

Notes:

- Credit-card purchase/fee rows are signed as positive balance increases.
- Credit-card payments and credits are signed as negative balance reductions.
- Current-account money in is signed positive and money out is signed negative.
- Romeo Amex Plan It principal due is tracked in `position-handoff.md`; only statement transaction/fee rows are exported in `transactions.csv`.

---

## Phase Lock

Status: Complete
Completed: 2026-07-01

Handoff locked. Artefacts committed for use by later phases.
