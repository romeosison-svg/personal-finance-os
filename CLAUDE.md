# Personal Finance OS — Claude Instructions

## Command Aliases

The following words are command aliases. When the user types one of these words (with or without a slash), execute the corresponding behaviour exactly as defined in `.claude/commands/`.

| Alias | Maps to |
| --- | --- |
| `finance start` | `.claude/commands/finance-start.md` |
| `collect` | `.claude/commands/collect.md` |
| `reconcile` | `.claude/commands/reconcile.md` |
| `assumptions` | `.claude/commands/assumptions.md` |
| `position` | `.claude/commands/position.md` |
| `handoff` | `.claude/commands/handoff.md` |
| `analyse` | `.claude/commands/analyse.md` |
| `plan` | `.claude/commands/plan.md` |
| `strategy` | `.claude/commands/strategy.md` |
| `status` | `.claude/commands/status.md` |

## Phase Gate Rule

Never skip a phase. Before executing any phase command, confirm the preceding phase is locked (`Complete`) in the active review folder. If it is not, tell the user which phase must be completed first and suggest the appropriate alias.

## Active Review

The active review is always the most recent folder under `reviews/` by name (alphabetically last), excluding `2026-06-example`.

## Finance Profile

Persistent planning assumptions live in `docs/finance-profile.md`. All values in that file are marked as examples until the user replaces them with real figures.

## Google Drive — Statements

Statement files can be uploaded from any device (including mobile) to Google Drive instead of the local `statements/` folder.

| Location | Drive Folder ID |
| --- | --- |
| Finance OS | `1ZjWe-hCug3VAESqRHTBsRl2GZvppuRxc` |
| Finance OS / Statements | `1D_U5sNk52firQcWsD6K1QBfmcsTCJxP0` |

During `collect` and `reconcile`, check the Drive Statements folder for files if the local `statements/` folder is empty or absent. Use the Google Drive MCP tools to list and read files from folder ID `1D_U5sNk52firQcWsD6K1QBfmcsTCJxP0`.
