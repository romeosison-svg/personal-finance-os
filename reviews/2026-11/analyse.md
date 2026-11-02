# Analyse — November 2026

> Requires: Handoff artefacts complete

## Phase Status

| Phase | Status | Completed |
| --- | --- | --- |
| Collect | Complete | 2026-11-02 |
| Reconcile | Complete | 2026-11-02 |
| Assumptions | Complete | 2026-11-02 |
| Position | Complete | 2026-11-02 |
| Handoff | Complete | 2026-11-02 |
| Analyse | Complete | 2026-11-02 |
| Budget Calibration | Not Started | |
| Affordability Check | Not Started | |
| Plan | Not Started | |
| Strategy | Not Started | |

## Spending Analysis

Observations only. No payment plan, bucket limit or recommendation is made in this phase.

## Scope and Limitations

- Source: the 55 raw rows in locked `reviews/2026-11/transactions.csv`.
- This is statement-period card analysis, not a clean November calendar-month view. Kelly Amex covers 25 Sep to 24 Oct; the Halifax, M&S and MBNA exports are statement-dated rows that include September and October activity.
- Kelly Amex, Kelly Halifax, Romeo Halifax, M&S and MBNA are represented. Romeo Amex, Amex Platinum and Barclaycard had no statement this cycle and were user-confirmed nil.
- M&S and MBNA contain repayment rows only and add no new observed spending.
- Current-account, Monzo, Starling and Santander transaction activity is outside this export. The analysis therefore excludes most recurring bills, cash-rail spending and joint-account spending.
- Santander's £391.10 of net intervening activity remains unitemised, limiting household-wide conclusions.
- Categories below are analysis labels based on raw merchant text. They do not alter the locked transaction export.
- `SP POTIEGA FOLKESTONE` at £32.00 is classified as Shopping / Personal because the user confirmed it was a birthday present for Kelly's sister.
- The Monzo balance-depletion view uses the original allocations locked in `reviews/2026-10/plan.md` and the live pot balances locked in the November Reconcile and Handoff. It is a balance-based proxy, not transaction-level spend.
- The Romeo Starling balance-depletion view uses the completed £675.00 funding recorded in the October Plan and the full £74.03 Spaces breakdown locked in the November Reconcile.
- Kelly's category-level Spaces screenshot was supplied during Analyse after Handoff was locked. It shows all five Spaces at £0.00 and is consistent with the locked £10.17 Starling account total because that £10.17 sits outside the Spaces. It is recorded as supplementary Analyse evidence and does not change the locked Handoff total.

## Flow Reconciliation

| Flow | Amount | Treatment |
| --- | ---: | --- |
| Gross debit rows | £848.48 | Starting transaction total |
| Merchant refunds | -£38.60 | Pickleball England £20.50 and Perplexity £18.10; netted against their categories |
| **Net observed spend** | **£809.88** | Categorised below |
| Card and BT repayments | £4,069.32 | Excluded because they repay existing balances rather than represent new spending |

The nine repayment rows are Kelly Amex £2,455.90, Kelly Halifax £318.15, Romeo Halifax £598.27 across three rows, M&S £200.00 across three rows, and MBNA £497.00.

## Observed Spend by Category

| Category | Total | Romeo | Kelly | Share |
| --- | ---: | ---: | ---: | ---: |
| Shopping / personal | £326.13 | £60.28 | £265.85 | 40.3% |
| Eating out / coffee / takeaway | £90.95 | £77.28 | £13.67 | 11.2% |
| Health / personal care | £89.99 | £0.00 | £89.99 | 11.1% |
| Transport / parking | £87.98 | £0.00 | £87.98 | 10.9% |
| Entertainment / events | £86.60 | £82.60 | £4.00 | 10.7% |
| Sport / fitness | £45.70 | £0.00 | £45.70 | 5.6% |
| Groceries / household | £41.91 | £0.00 | £41.91 | 5.2% |
| Fees / interest | £22.68 | £7.94 | £14.74 | 2.8% |
| Subscriptions / software | £17.94 | £17.94 | £0.00 | 2.2% |
| **Total** | **£809.88** | **£246.04** | **£563.84** | **100.0%** |

## Observed Spend by Card

| Card | Holder | Gross debits | Merchant refunds | Net observed spend |
| --- | --- | ---: | ---: | ---: |
| Amex credit | Kelly | £471.23 | -£20.50 | £450.73 |
| Halifax credit | Kelly | £113.11 | £0.00 | £113.11 |
| Halifax credit | Romeo | £264.14 | -£18.10 | £246.04 |
| M&S balance transfer | Romeo | £0.00 | £0.00 | £0.00 |
| MBNA balance transfer | Romeo | £0.00 | £0.00 | £0.00 |
| **Total** | | **£848.48** | **-£38.60** | **£809.88** |

## Monzo Joint Bucket Depletion

The October Plan funded £950.00 of shared spendable Monzo pots and a separate £383.93 Travel / Experiences sinking pot. The 2 November screenshot provides the remaining balances.

| Pot | Original allocation | Balance 2 Nov | Implied depletion | Allocation used | Allocation remaining |
| --- | ---: | ---: | ---: | ---: | ---: |
| Groceries / household | £450.00 | £109.22 | £340.78 | 75.7% | 24.3% |
| Work commute | £400.00 | £26.10 | £373.90 | 93.5% | 6.5% |
| Discretionary transport | £50.00 | £4.71 | £45.29 | 90.6% | 9.4% |
| Entertainment / events | £50.00 | £25.00 | £25.00 | 50.0% | 50.0% |
| **Shared spendable subtotal** | **£950.00** | **£165.03** | **£784.97** | **82.6%** | **17.4%** |
| Travel / Experiences sinking pot | £383.93 | £16.60 | £367.33 | 95.7% | 4.3% |
| **All named Monzo pots** | **£1,333.93** | **£181.63** | **£1,152.30** | **86.4%** | **13.6%** |

The live Monzo main-account balance is £7.58 and is outside the original named-pot allocations above.

“Implied depletion” is original allocation minus live pot balance. It can reflect purchases, withdrawals, transfers between pots, or reallocations. Without the Monzo transaction export it cannot be treated as exact merchant-level spending. It is therefore kept separate from the £809.88 card-spend total and is not added to it.

## Romeo Starling Spaces Depletion

The October Plan records £475.00 of Romeo spendable funding plus a separate £200.00 Pickleball Events sinking allocation. The visible 2 November Spaces sum exactly to the locked £74.03 total; the omitted Takeaway Space therefore has a nil balance.

| Space | Original allocation | Balance 2 Nov | Implied depletion | Allocation used | Allocation remaining |
| --- | ---: | ---: | ---: | ---: | ---: |
| Pickleball monthly | £300.00 | £35.31 | £264.69 | 88.2% | 11.8% |
| Health / personal care | £25.00 | £0.00 | £25.00 | 100.0% | 0.0% |
| Takeaway | £75.00 | £0.00 | £75.00 | 100.0% | 0.0% |
| Shopping / personal | £75.00 | £18.35 | £56.65 | 75.5% | 24.5% |
| **Romeo spendable subtotal** | **£475.00** | **£53.66** | **£421.34** | **88.7%** | **11.3%** |
| Pickleball Events sinking space | £200.00 | £20.37 | £179.63 | 89.8% | 10.2% |
| **All Romeo Spaces** | **£675.00** | **£74.03** | **£600.97** | **89.0%** | **11.0%** |

The app screenshot shows a 17.7% target percentage beside the £35.31 Pickleball balance. The table above instead compares the balance with the £300.00 actual allocation locked in the October Plan; the Space target displayed in the app was not the same as that funded amount.

As with Monzo, implied depletion can include purchases, withdrawals and transfers between Spaces. It is not added to the £809.88 card-spend total.

## Kelly Starling Spaces Depletion

Kelly's 2 November screenshot shows every planned spending Space at £0.00. The table compares these balances with the October Plan allocations.

| Space | Planned allocation | Balance 2 Nov | Allocation no longer in Space | Planned capacity depleted | Planned capacity remaining |
| --- | ---: | ---: | ---: | ---: | ---: |
| Sport / Pickleball | £200.00 | £0.00 | £200.00 | 100.0% | 0.0% |
| Health / personal care | £25.00 | £0.00 | £25.00 | 100.0% | 0.0% |
| Takeaway | £75.00 | £0.00 | £75.00 | 100.0% | 0.0% |
| Shopping / personal | £75.00 | £0.00 | £75.00 | 100.0% | 0.0% |
| London work food | £100.00 | £0.00 | £100.00 | 100.0% | 0.0% |
| **Kelly planned Spaces total** | **£475.00** | **£0.00** | **£475.00** | **100.0%** | **0.0%** |

Kelly's Starling main-account balance is £10.17 and is outside these Spaces.

The October Plan checklist did not mark the full £475.00 transfer as completed. Therefore, “allocation no longer in Space” means the planned category capacity has been exhausted, not that £475.00 of merchant spending has been independently verified. The £10.17 main balance is not assigned back to a category.

## Largest Merchant Totals

| Owner | Merchant / payee | Category | Rows | Net amount |
| --- | --- | --- | ---: | ---: |
| Kelly | Amazon-labelled merchants | Shopping / personal | 7 | £128.44 |
| Kelly | Natural Cycles | Health / personal care | 1 | £89.99 |
| Romeo | gigantic.com | Entertainment / events | 1 | £82.60 |
| Romeo | Antalya retail merchants | Shopping / personal | 2 | £60.28 |
| Kelly | Antalya boutique merchants | Shopping / personal | 3 | £47.09 |
| Kelly | TFL Travel Charge | Transport / parking | 2 | £42.50 |
| Kelly | JJ's House via Klarna | Shopping / personal | 1 | £34.33 |
| Kelly | SNB Manchester | Transport / parking | 2 | £33.00 |
| Kelly | SP Potiega | Shopping / personal — sister's birthday present | 1 | £32.00 |
| Kelly | Costco Wholesale | Groceries / household | 1 | £26.47 |
| Kelly | Not On The High Street | Shopping / personal | 1 | £23.99 |
| Romeo | Perplexity | Subscriptions / software | 3 | £17.94 |

The Antalya merchant groupings above combine separate raw rows only for display. Kelly's group is Side Antik Butik, Side Cotton and OST Butik; Romeo's group is Neva Doga and Sonya Butik.

## Pattern Observations

- Shopping / personal is the largest category at £326.13, representing 40.3% of net observed spend. Kelly accounts for £265.85 and Romeo £60.28.
- Amazon-labelled Kelly rows total £128.44 across seven transactions, equal to 39.4% of the shopping / personal category.
- Natural Cycles is the only health / personal-care row and accounts for the full £89.99 category total.
- Eating out, coffee and takeaway totals £90.95. Romeo accounts for £77.28, including Burger King, Doumo, Carpe Diem Restaurant and Simus Restorant.
- Kelly accounts for all £87.98 of observed transport / parking. The components are TFL £42.50, SNB Manchester £33.00, Dartford crossing £7.00 and RingGo £5.48.
- Entertainment / events totals £86.60 and is concentrated in Romeo's £82.60 gigantic.com transaction; Kelly's Odeon row is £4.00.
- Sport / fitness is £45.70 net after the £20.50 Pickleball England refund. It consists of Spond, Pickleball England, Lemon Pickleball and Sharp Pickleball rows, all on Kelly's Amex.
- Groceries / household totals £41.91 across Costco, OBA Market and Sainsbury's. Monzo and Santander activity is absent, so this is not a complete household grocery measure.
- Fees / interest total £22.68: Kelly Amex £14.74 and Romeo Halifax £7.94.
- Perplexity subscription activity is £17.94 net after an £18.10 credit, comprising two debits of £17.82 and £18.22.
- The £32.00 SP Potiega row is Kelly's sister's birthday present and is included in Shopping / Personal.
- Kelly accounts for £563.84, or 69.6%, of net observed spend; Romeo accounts for £246.04, or 30.4%. This owner mix reflects the cards and statement windows present in this export.
- The four £950 shared spendable Monzo pots have £165.03 remaining, implying £784.97 or 82.6% depletion from their original allocations.
- Work Commute has the highest absolute implied depletion among the spendable Monzo pots at £373.90 and 93.5%; Entertainment / Events has the largest remaining share at 50.0%.
- The separate Travel / Experiences sinking pot has £16.60 remaining from £383.93, implying £367.33 or 95.7% depletion.
- Romeo's £475.00 spendable Starling allocation has £53.66 remaining, implying £421.34 or 88.7% depletion.
- Romeo's separate £200.00 Pickleball Events sinking allocation has £20.37 remaining, implying £179.63 or 89.8% depletion.
- Romeo's Takeaway and Health / Personal Care Spaces are at £0.00; Shopping / Personal has the largest remaining share of his spendable Spaces at 24.5%.
- Kelly's five planned spending Spaces are all at £0.00. Her £10.17 Starling balance remains in the main account rather than a Space.

## Prior-Export Comparison

| Measure | Prior export | Current export | Change |
| --- | ---: | ---: | ---: |
| Net observed card spend | £3,407.13 | £809.88 | -£2,597.25 (-76.2%) |
| Romeo | £2,318.08 | £246.04 | -£2,072.04 (-89.4%) |
| Kelly | £1,089.05 | £563.84 | -£525.21 (-48.2%) |

This is a directional statement-export comparison, not a calendar-month trend. The current export has materially narrower active-card coverage: Romeo's Amex and Amex Platinum had nil balances and no statements, while M&S and MBNA contain repayments only.

## Items to Carry Forward

- The statement export contains £809.88 of net observed spend, but it does not capture the household's full cash-rail or joint-account outturn.
- Shopping / personal is the largest observed card category, with Amazon-labelled rows its largest merchant grouping.
- Transport / parking is entirely Kelly-side in the represented rows and remains concentrated in TFL and SNB Manchester.
- The observed sport / fitness amount is net of a £20.50 refund.
- £22.68 of card interest is visible as a distinct cost rather than consumer purchasing.
- The £32.00 SP Potiega transaction is classified as Kelly Shopping / Personal based on the user's confirmation.
- The PPL Stourbridge costs are future November activity and do not appear in these statement-period rows; the already-paid £43 hotel is present in the prior export, not this one.
- Monzo pot balances provide a depletion view of £784.97 across the £950 shared spendable allocation, but exact Monzo merchant spending remains unavailable.
- Romeo Starling Spaces provide a depletion view of £421.34 across his £475 spendable allocation and £179.63 across the separate £200 Pickleball Events sinking allocation.
- Kelly's screenshot shows that none of the planned £475 category capacity remains in her Spaces, but the full £475 top-up is not verified as executed; the Space comparison is therefore not treated as exact spending.
- Missing Santander detail and the absence of transaction-level Monzo and Romeo Starling data still prevent a complete merchant-level assessment of the full £1,900 pilot allowance.

## Phase Lock

Status: Complete
Completed: 2026-11-02
Locked by: Codex with user approval
