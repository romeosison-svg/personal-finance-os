# import

Import an externally generated artefact into the active monthly review.

## Usage

```
import <phase>
```

Where `<phase>` is one of: `analyse`, `plan`, `strategy`

## Purpose

Accepts a ChatGPT-generated phase output and saves it as a first-class FinanceOS artefact. Once imported and committed, the phase is marked `Complete` and the review proceeds normally.

Claude owns repository persistence. ChatGPT owns reasoning. Import is the bridge.

---

## Supported Artefacts

| Artefact   | Phase   | Gate Requires      |
| ---------- | ------- | ------------------ |
| `analyse`  | Phase 6 | `handoff` complete |
| `plan`     | Phase 7 | `analyse` complete |
| `strategy` | Phase 8 | `plan` complete    |

---

## Process

### Step 1 — Identify active review

Find the most recent folder under `reviews/` (alphabetically last), excluding `2026-06-example`. This is the active review month (`YYYY-MM`).

### Step 2 — Validate artefact type

If the artefact name is not one of `analyse`, `plan`, `strategy`, tell the user:

> `import` only supports: `analyse`, `plan`, `strategy`.
> Native Claude phases (collect, reconcile, assumptions, position, handoff) are executed locally — they are not imported.

Stop.

### Step 3 — Check the phase gate

Confirm the preceding phase is `Complete` in the active review's phase file:

- `import analyse` → requires `handoff` complete
- `import plan` → requires `analyse` complete
- `import strategy` → requires `plan` complete

If the gate is not met, tell the user which phase must be completed first and suggest the appropriate alias. Stop.

### Step 4 — Check for existing content

Read the target file: `reviews/YYYY-MM/{phase}.md`.

If the phase status is already `Complete`, warn:

> `{phase}.md` is already marked `Complete`. Importing will overwrite the existing content.
> Proceed? (yes / no)

If no, stop.

### Step 5 — Receive content from user

Tell the user:

> Ready to import `{phase}.md` for `YYYY-MM`.
>
> Paste the ChatGPT-generated content now. When you're done, tell me to save it.

Wait for the user to provide the full content. Do not proceed until content is received.

### Step 6 — Compose the file

Build the file content in this order:

**1. Phase status dashboard** (preserve from existing file, or create if absent)

Update the row for the imported phase:
- Status → `Complete`
- Completed → today's date (`YYYY-MM-DD`)

**2. Import metadata block** (insert immediately after dashboard)

```markdown
## Import Metadata

- **Source:** ChatGPT / External analysis
- **Imported:** YYYY-MM-DD
- **Phase:** {phase} (Phase N — e.g. Phase 6)
- **Review:** YYYY-MM
```

**3. ChatGPT content** (append verbatim below the metadata block)

Preserve the content exactly as provided. Do not reformat, summarise, or annotate.

### Step 7 — Write the file

Write the composed content to `reviews/YYYY-MM/{phase}.md`.

### Step 8 — Stage and commit

Stage only the imported phase file:

```
git add reviews/YYYY-MM/{phase}.md
```

Commit with the appropriate message:

| Phase      | Commit message                                       |
| ---------- | ---------------------------------------------------- |
| `analyse`  | `analyse: imported external analysis — YYYY-MM`      |
| `plan`     | `plan: imported external plan — YYYY-MM`             |
| `strategy` | `strategy: imported external strategy — YYYY-MM`     |

If `strategy` import also includes updates to `docs/finance-profile.md`, stage and commit that file separately after the strategy import commit:

```
git add docs/finance-profile.md
git commit -m "finance-profile: update [what changed] — YYYY-MM"
```

### Step 9 — Confirm to user

Tell the user:

> `{phase}.md` imported and committed for `YYYY-MM`.
> Source: ChatGPT / External analysis
> Phase N is now `Complete`.
>
> Next: `{next_command}`

Where `{next_command}` is:

- After `analyse` → `import plan` or `plan`
- After `plan` → `import strategy` or `strategy`
- After `strategy` → The monthly review is complete.

---

## Commit Convention

```
analyse: imported external analysis — YYYY-MM
plan: imported external plan — YYYY-MM
strategy: imported external strategy — YYYY-MM
```

---

## Notes

- Import does not validate the content — it trusts the user has reviewed it before importing.
- The ChatGPT content is preserved verbatim. Claude does not edit or reformat it.
- Once committed, an imported artefact is a first-class FinanceOS output and is treated identically to a Claude-generated phase output.
- The phase gate is enforced the same way as native phases — import does not bypass sequencing.
