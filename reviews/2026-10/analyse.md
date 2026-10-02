# Analyse — October 2026

> Requires: Handoff artefacts complete

## Phase Status

| Phase | Status | Completed |
| --- | --- | --- |
| Collect | Complete | 2026-10-02 |
| Reconcile | Complete | 2026-10-02 |
| Assumptions | Complete | 2026-10-02 |
| Position | Complete | 2026-10-02 |
| Handoff | Complete | 2026-10-02 |
| Analyse | Complete | 2026-10-02 |
| Budget Calibration | Not Started | |
| Affordability Check | Not Started | |
| Plan | Not Started | |
| Strategy | Not Started | |

## Spending Analysis

Observations only. No payment plan or recommendations.

### Scope and Limitations

- Source: the 145 raw rows in locked `reviews/2026-10/transactions.csv`.
- This is statement-period credit-card analysis, not a clean October calendar-month view.
- Romeo Amex covers 16 Aug to 15 Sep; Kelly Amex covers 25 Aug to 24 Sep. Halifax rows use their respective statement windows, and Romeo Amex Platinum contains one posted transaction.
- M&S and MBNA contain repayment rows only; they add no observed new spending.
- Current-account and Santander joint-account transactions are outside this export. The analysis therefore does not represent all household spending or recurring bills.
- Categories are analysis labels based on raw merchant text. They do not alter the locked transaction export.

### Flow Reconciliation

| Flow | Amount | Treatment |
| --- | ---: | --- |
| Gross debit rows | £3,442.41 | Starting transaction total |
| Merchant refunds | -£35.28 | Netted against shopping / personal |
| **Net observed spend** | **£3,407.13** | Categorised below |
| Card and BT repayments | £903.10 | Excluded because they repay existing balances rather than represent new spend |

The refunds are Hobbycraft £4.50 and two Fabletics credits totalling £30.78. Six repayment rows make up the excluded £903.10.

### Observed Spend by Category

| Category | Total | Romeo | Kelly | Share |
| --- | ---: | ---: | ---: | ---: |
| Travel / holiday | £825.92 | £820.93 | £4.99 | 24.2% |
| Sport / fitness | £580.55 | £405.45 | £175.10 | 17.0% |
| Eating out / coffee / takeaway | £557.45 | £333.88 | £223.57 | 16.4% |
| Transport / parking | £388.62 | £20.60 | £368.02 | 11.4% |
| Groceries / household | £386.85 | £358.76 | £28.09 | 11.4% |
| Shopping / personal | £338.69 | £174.89 | £163.80 | 9.9% |
| Health / personal care | £163.90 | £101.00 | £62.90 | 4.8% |
| Fees / interest | £99.19 | £51.59 | £47.60 | 2.9% |
| Subscriptions / software | £38.98 | £38.98 | £0.00 | 1.1% |
| Entertainment / events | £14.98 | £0.00 | £14.98 | 0.4% |
| Uncategorised observation | £12.00 | £12.00 | £0.00 | 0.4% |
| **Total** | **£3,407.13** | **£2,318.08** | **£1,089.05** | **100.0%** |

### Observed Spend by Card

| Card | Holder | Gross debits | Merchant refunds | Net observed spend |
| --- | --- | ---: | ---: | ---: |
| Amex credit | Romeo | £1,928.75 | £0.00 | £1,928.75 |
| Amex Platinum | Romeo | £11.25 | £0.00 | £11.25 |
| Halifax Clarity | Romeo | £378.08 | £0.00 | £378.08 |
| Amex credit | Kelly | £775.40 | -£4.50 | £770.90 |
| Halifax Clarity | Kelly | £348.93 | -£30.78 | £318.15 |
| **Total** | | **£3,442.41** | **-£35.28** | **£3,407.13** |

### Largest Merchant Totals

| Owner | Merchant / payee | Category | Rows | Net amount |
| --- | --- | --- | ---: | ---: |
| Romeo | British Airways | Travel / holiday | 1 | £448.00 |
| Romeo | Premier Inn Bolton | Travel / holiday | 1 | £202.00 |
| Kelly | TFL Travel Charge | Transport / parking | 11 | £168.30 |
| Romeo | Pickleball England | Sport / fitness | 2 | £135.00 |
| Kelly | Pickleball England | Sport / fitness | 3 | £127.00 |
| Romeo | Everyone Active | Sport / fitness | 7 | £123.00 |
| Romeo | Centerline Athletic | Sport / fitness | 1 | £120.00 |
| Romeo | Gatwick Airport | Travel / holiday | 1 | £102.20 |
| Kelly | Beijing Dumpling | Eating out / coffee / takeaway | 1 | £89.50 |
| Romeo | Dental Health Care | Health / personal care | 1 | £75.00 |
| Romeo | Tesco Hatfield | Groceries / household | 1 | £73.55 |
| Romeo | Vietnamese Street Kitchen | Eating out / coffee / takeaway | 1 | £69.08 |

### Pattern Observations

- Travel / holiday is the largest category at £825.92. It is concentrated in Romeo's rows and includes British Airways £448.00, Premier Inn £245.00 across two rows, Gatwick Airport £102.20, Seven Tour £25.73, and Kelly's eSIM £4.99.
- Sport / fitness totals £580.55. The largest components are Pickleball England £262.00 across both people, Everyone Active £123.00, and Centerline Athletic £120.00.
- Eating out, coffee, and takeaway totals £557.45 across both people. The largest single dining row is Beijing Dumpling at £89.50.
- Kelly accounts for £368.02 of the £388.62 transport / parking total. Her largest transport groups are TFL £168.30, SNB Manchester £49.50, NEC Birmingham £49.50, and Trainline £63.60 across two merchant descriptions.
- Romeo accounts for £358.76 of the £386.85 groceries / household total. Santander joint-account activity is absent, so this is not a full household grocery measure.
- Shopping / personal is £338.69 after £35.28 of merchant refunds. Amazon-labelled rows form a material portion of this category across both people.
- Fees / interest totals £99.19: Romeo Amex £51.59 and Kelly Amex £47.60.
- Subscriptions / software totals £38.98 and comprises Perplexity £17.91, Neon £9.09, Amazon Prime £8.99, and Prime Video ad-free £2.99.
- One £12.00 Romeo row labelled `ZETTLE *LORDSHIP GARDEN` remains uncategorised because the merchant text does not establish the nature of the spend.

### Prior-Period Comparison

| Measure | Prior export | Current export | Change |
| --- | ---: | ---: | ---: |
| Net observed credit-card spend | £3,067.95 | £3,407.13 | +£339.18 (+11.1%) |
| Romeo | £1,485.31 | £2,318.08 | +£832.77 |
| Kelly | £1,582.64 | £1,089.05 | -£493.59 |

This comparison uses credit-card rows only from each handoff and excludes repayment credits. It is directional rather than a calendar-month comparison because statement windows and card coverage differ. The current-period increase is smaller than the £825.92 travel / holiday category, while the owner mix has shifted toward Romeo.

### Items to Carry Forward

- Travel / holiday spend is separately identifiable from recurring statement activity.
- Sport / fitness and dining are the largest non-travel observed categories.
- Kelly-side transport / parking is concentrated and material in this statement window.
- Santander's missing transaction detail limits conclusions about shared groceries, bills, and vehicle costs.
- £99.19 of card interest is visible as a distinct cost rather than consumer purchasing.
- The £12.00 Lordship Garden row remains explicitly uncertain.

## Phase Lock

Status: Complete
Completed: 2026-10-02
Locked by: Codex with user approval
