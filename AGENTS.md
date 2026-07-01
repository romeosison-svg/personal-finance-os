# Personal Finance OS — Codex Instructions

These instructions are authoritative for Codex work in this repository.

## Operating Rule

Personal Finance OS is a gated monthly finance review process. Codex must preserve phase discipline, auditability, and the separation between facts, assumptions, analysis, plans, and strategy.

Do not skip phases. Do not produce recommendations before the phase permits them. Do not lock a phase without explicit user approval.

## Active Review

The active review is the most recent folder under `reviews/` by name, excluding `2026-06-example`.

If no review folder exists, tell the user to start a review before running a phase.

## Canonical Phase Flow

The canonical flow is:

```text
collect -> reconcile -> assumptions -> position -> handoff -> analyse -> budget-calibration -> affordability-check -> plan -> strategy
```

| Phase | Alias | Gate |
| --- | --- | --- |
| 1 | `collect` | none |
| 2 | `reconcile` | `collect` complete |
| 3 | `assumptions` | `reconcile` complete |
| 4 | `position` | `reconcile` and `assumptions` complete |
| 5 | `handoff` | `position` complete |
| 6 | `analyse` | handoff artefacts complete |
| 7 | `budget-calibration` | `analyse` complete |
| 8 | `affordability-check` | `budget-calibration` complete |
| 9 | `plan` | `affordability-check` complete |
| 10 | `strategy` | `plan` complete |

## Phase Gate Checks

Before working on any phase, read the active review's relevant phase files and confirm the preceding gate is `Complete`.

If a gate is not met, stop and tell the user:

- which phase is blocking progress
- what needs to happen next
- the command or phase name to run next

Do not write future phase files while an earlier phase is incomplete, except for initial placeholders created during review setup.

## Handoff Phase

There is no separate financial decision in handoff. Handoff is a lock boundary.

The handoff phase is complete only when these artefacts exist, have been reviewed, and are committed:

- `reviews/YYYY-MM/handoff.md`
- `reviews/YYYY-MM/position-handoff.md`
- `reviews/YYYY-MM/transactions.csv`

`position-handoff.md` contains verified facts and locked assumptions only.
`transactions.csv` contains raw transaction rows only.

Do not include categorisation, analysis, recommendations, or strategy in handoff artefacts.

## Ownership

Codex owns repository persistence and may execute every phase in this repo.

External tools or models may still produce artefacts for `analyse`, `budget-calibration`, `affordability-check`, `plan`, or `strategy`, but Codex must import, review gates, write, and commit those artefacts.

## Statements

During `collect`, build `reviews/YYYY-MM/statements.md` from filenames only. Do not read statement contents in collect.

Statement lookup priority:

1. Local: `reviews/YYYY-MM/statements/`
2. Google Drive folder ID `1D_U5sNk52firQcWsD6K1QBfmcsTCJxP0`
3. Manual figures from the user

Ignore `.gitkeep`, `.Zone.Identifier`, and other metadata files.

Statement filenames are expected to use:

```text
YYYY-MM_<person>_<institution>_<account-type>
```

Do not rename or move statement files unless the user explicitly asks.

## Phase Boundaries

Collect:
Only confirm inputs. No balance extraction, analysis, or commentary.

Reconcile:
Establish verified facts from statements and user-confirmed figures. No recommendations.

Assumptions:
Confirm planning rules from `docs/finance-profile.md`. Do not apply them yet.

Position:
Calculate the current financial position from locked facts and assumptions. No payment plan.

Handoff:
Export verified facts and raw transactions. No analysis.

Analyse:
Categorise and summarise spending. Observations only, no payment plan.

Budget Calibration:
Translate spending patterns into explicit next-month bucket limits. No debt repayment or payment plan decisions.

Affordability Check:
Test whether calibrated bucket limits are fundable from cashflow. No payment plan.

Plan:
Produce exact monthly payment allocations and cash trace.

Strategy:
Review longer-term risks, trade-offs, and standing assumptions. Update `docs/finance-profile.md` only with user approval and commit separately.

## User Approval

Before locking any phase, ask the user whether they are ready to lock it.

Only after approval:

- set the phase status to `Complete`
- record the completion date
- update phase status tables as needed
- stage and commit the phase output

## Commit Convention

Use these commit messages for native Codex phase completion:

```text
collect: phase 1 complete - YYYY-MM
reconcile: phase 2 complete - YYYY-MM
assumptions: phase 3 complete - YYYY-MM
position: phase 4 complete - YYYY-MM
handoff: phase 5 complete - YYYY-MM
analyse: phase 6 complete - YYYY-MM
budget-calibration: phase 7 complete - YYYY-MM
affordability-check: phase 8 complete - YYYY-MM
plan: phase 9 complete - YYYY-MM
strategy: phase 10 complete - YYYY-MM
```

If preserving existing history style, an en dash in commit messages is acceptable.

For imported external artefacts:

```text
analyse: imported external analysis - YYYY-MM
budget-calibration: imported external budget calibration - YYYY-MM
affordability-check: imported external affordability check - YYYY-MM
plan: imported external plan - YYYY-MM
strategy: imported external strategy - YYYY-MM
```

## Current Migration Note

Claude-specific instructions under `CLAUDE.md` and `.claude/commands/` are legacy references. Use this file, `docs/finance-assembly-line.md`, and `docs/workflow.md` as the current authority.
