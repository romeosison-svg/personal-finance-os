# Analyse — September 2026

> Requires: Handoff artefacts complete

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

## Spending Analysis

Observations only. No payment plan or recommendations in this phase.

### Scope And Limitations

- Source: `reviews/2026-09/transactions.csv`, produced during handoff from 250 raw statement rows.
- This is statement-period analysis for the September 2026 review, not a clean calendar-month analysis. The exported rows include:
  - Current-account rows from 01 Aug 2026 to 27/28 Aug 2026.
  - Amex rows from 16 Jul to 15 Aug for Romeo and 25 Jul to 24 Aug for Kelly.
  - Halifax credit-card rows from July/August statement windows.
- Santander joint-account transaction detail is not included because the statement was unavailable.
- Post-statement Turkey items, including BA Holidays and Gatwick Plan It effects, are position/handoff facts but are not fully visible in the exported transaction rows.
- Categories are analysis labels only. They do not change the raw transaction export.

### Excluded From Spend Observations

| Excluded flow | Amount | Reason |
| --- | ---: | --- |
| Internal transfers / investment movements | £16,508.95 | Movement between accounts or investment platforms, not consumer spend |
| Card / debt payments | £2,065.84 | Repayments against existing card balances, not new spend |

### Observed Spend By Category

Observed spend after excluding internal transfers and card/debt payments: **£4,382.98**.

| Category | Total | Romeo | Kelly |
| --- | ---: | ---: | ---: |
| Eating out / coffee / takeaway | £1,040.88 | £800.95 | £239.93 |
| Transport / parking / charging | £640.08 | £135.90 | £504.18 |
| Sport / fitness / therapy | £652.00 | £259.45 | £392.55 |
| Fixed commitments / direct debits | £552.15 | £466.02 | £86.13 |
| Shopping / personal | £517.67 | £273.54 | £244.13 |
| Groceries / household shopping | £325.79 | £147.89 | £177.90 |
| Entertainment / events | £176.98 | £54.00 | £122.98 |
| Travel / holiday | £142.70 | £142.70 | £0.00 |
| Uncategorized observation | £136.28 | £62.80 | £73.48 |
| Giving / tithe | £100.00 | £0.00 | £100.00 |
| Fees / interest | £63.35 | £15.42 | £47.93 |
| Subscriptions / software | £35.10 | £35.10 | £0.00 |

### Observed Spend By Person

| Person | Observed spend | Notes |
| --- | ---: | --- |
| Romeo | £2,393.77 | Excludes internal transfers and card/debt payments |
| Kelly | £1,989.21 | Excludes internal transfers and card/debt payments |
| Combined | £4,382.98 | Statement-period observation total |

### Top Observed Merchants / Payees

| Owner | Merchant / Payee | Category | Rows | Amount |
| --- | --- | --- | ---: | ---: |
| Kelly | TFL Travel Charge | Transport / parking / charging | 11 | £197.25 |
| Romeo | Dojo Chez Rose | Eating out / coffee / takeaway | 1 | £181.25 |
| Kelly | Pure Sports Medicine | Sport / fitness / therapy | 2 | £175.00 |
| Romeo | HMRC NDDS | Fixed commitments / direct debits | 1 | £152.67 |
| Romeo | SumUp Popspecs Midlands | Shopping / personal | 1 | £140.00 |
| Romeo | Everyone Active | Sport / fitness / therapy | 6 | £123.00 |
| Kelly | Stev SDA Church | Giving / tithe | 1 | £100.00 |
| Romeo | Premier Inn Bolton | Travel / holiday | 1 | £91.00 |
| Kelly | TFL Enforcement Ops | Transport / parking / charging | 1 | £90.00 |
| Romeo | Costco Stevenage | Groceries / household shopping | 1 | £88.53 |
| Romeo | Vitality Health | Fixed commitments / direct debits | 1 | £82.40 |
| Romeo | L&G Insurance MI | Fixed commitments / direct debits | 2 | £82.33 |
| Kelly | TFL Travel Charge | Transport / parking / charging | 6 | £77.95 |
| Romeo | Cay Khe | Eating out / coffee / takeaway | 1 | £76.45 |
| Romeo | Burger King | Eating out / coffee / takeaway | 6 | £75.77 |

### Pattern Observations

- Eating out, coffee, and takeaway is the largest observed spend category at £1,040.88. Romeo accounts for £800.95 of this and Kelly £239.93.
- Transport, parking, and charging is the second-largest observed category at £640.08. Kelly accounts for £504.18, driven mainly by TFL, Trainline, SNB Manchester, and related London travel rows.
- Sport, fitness, and therapy totals £652.00. This includes pickleball / Everyone Active / Sharp Pickleb / Jolene Foster rows and therapy or sports medicine rows.
- Groceries and household shopping total £325.79 in the exported rows. This is incomplete as a whole-household grocery picture because Santander joint-account activity is absent.
- Fixed commitments / direct debits observed in the transaction export total £552.15. This includes current-account DDs already separated in Position as known September drawdowns.
- Fees and interest total £63.35, including Kelly Amex interest of £47.93, Starling overdraft charge of £10.42, and Lloyds fee activity.
- Travel / holiday rows visible in the statement export total £142.70, mainly Premier Inn Bolton and Gatwick/Nespresso travel-context spend. The Turkey BA Holidays £448 and Gatwick parking/Fast Track £102.20 are known position facts but not fully represented as raw statement rows in this export.
- The uncategorised bucket is £136.28. It consists mostly of low-value people transfers or merchant names that need later interpretation rather than a material category shift.
- User-confirmed category corrections on 2026-08-29: Drink Oshun is supplement / personal shopping, SNB Manchester is transport, Jolene Foster is pickleball / sport, and Thames River Services is an entertainment / family outing rather than transport.

### Items To Carry Forward

- Santander absence means household bills, joint-account groceries, and joint vehicle payments are not fully observable in this analysis.
- Post-lock Santander clarification on 2026-08-29: Spotify remains relevant and all listed Santander recurring items remain relevant for September. Later phases should use £1,261.91 gross Santander recurring outflow and £1,254.58 net household cost after Elaine's £7.33 Spotify reimbursement.
- Turkey trip costs should remain visible in later phases because some known costs sit outside the statement rows analysed here.
- London travel is a material Kelly-side observed pattern this statement period.
- Pickleball / sport spend remains visible across both people and should be handled carefully in budget calibration because some rows may be reimbursed or shared.
- Fees and interest are small in total but identifiable, with Kelly Amex interest and Starling overdraft cost both present in the export.

---

## Phase Lock

Status: Complete
Completed: 2026-08-29

Analysis complete.
