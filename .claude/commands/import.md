# import

Import a ChatGPT-generated artefact into the active monthly review.

## Usage

Minimal (recommended):

```
import analyse
[paste content]
```

With optional overrides:

```
import analyse
Review Month: 2026-06

[paste content]
```

```
import analyse
Review Month: 2026-06
Source: ChatGPT

[paste content]
```

Where `<phase>` is one of: `analyse`, `plan`, `strategy`

---

## Defaults

| Parameter    | Default                                                                 |
| ------------ | ----------------------------------------------------------------------- |
| Review month | Active review (most recent folder under `reviews/`, excluding `2026-06-example`) |
| Source       | ChatGPT                                                                 |

Do not ask for review month or source. Infer them silently. Only request clarification if genuine ambiguity exists (e.g. two review folders with the same date, which cannot happen in practice).

---

## Supported Artefacts

| Artefact   | Phase   | Gate Requires      |
| ---------- | ------- | ------------------ |
| `analyse`  | Phase 6 | `handoff` complete |
| `plan`     | Phase 7 | `analyse` complete |
| `strategy` | Phase 8 | `plan` complete    |

Native Claude phases (`collect`, `reconcile`, `assumptions`, `position`, `handoff`) are executed locally and are not imported.

---

## Process

### Step 1 — Parse the input

Read the user's message. Extract:

- **Phase** — from `import <phase>`
- **Review month** — from `Review Month: YYYY-MM` if present; otherwise use the active review
- **Source** — from `Source: X` if present; otherwise `ChatGPT`
- **Content** — everything in the message after the command line and any override fields

If content is present in the same message, proceed immediately.

If content is absent, ask once — nothing else:

> Paste the content for `{phase}.md`.

Do not ask for review month, source, or confirmation of defaults.

### Step 2 — Validate artefact type

If the phase is not `analyse`, `plan`, or `strategy`:

> `import` supports: `analyse`, `plan`, `strategy`. Native Claude phases are not imported.

Stop.

### Step 3 — Check the phase gate

Read the preceding phase file and confirm its status is `Complete`:

- `import analyse` → `reviews/YYYY-MM/handoff.md` must be `Complete`
- `import plan` → `reviews/YYYY-MM/analyse.md` must be `Complete`
- `import strategy` → `reviews/YYYY-MM/plan.md` must be `Complete`

If the gate is not met:

> `{preceding-phase}` is not yet `Complete`. Complete or import it first.
> Run: `{preceding-phase}` or `import {preceding-phase}`

Stop.

### Step 4 — Check for existing content

Read `reviews/YYYY-MM/{phase}.md`.

If the phase status is already `Complete`, warn once:

> `{phase}.md` is already `Complete`. Overwrite? (yes / no)

If no, stop.

### Step 5 — Write the file

Compose file content in this order:

**1. Phase status dashboard**

Preserve from the existing file. Update the row for the imported phase:
- Status → `Complete`
- Completed → today's date (`YYYY-MM-DD`)

**2. ChatGPT content**

Append the pasted content verbatim. Do not reformat, summarise, or annotate.

**3. Import line**

Append a single line at the end of the file:

```
_Imported from {source} on YYYY-MM-DD._
```

Write to `reviews/YYYY-MM/{phase}.md`.

### Step 6 — Stage and commit

```
git add reviews/YYYY-MM/{phase}.md
git commit -m "{phase}: imported ChatGPT {label} — YYYY-MM"
```

| Phase      | Commit message                                     |
| ---------- | -------------------------------------------------- |
| `analyse`  | `analyse: imported ChatGPT analysis — YYYY-MM`     |
| `plan`     | `plan: imported ChatGPT plan — YYYY-MM`            |
| `strategy` | `strategy: imported ChatGPT strategy — YYYY-MM`    |

If a `strategy` import also updates `docs/finance-profile.md`, commit that separately:

```
git add docs/finance-profile.md
git commit -m "finance-profile: update [what changed] — YYYY-MM"
```

### Step 7 — Confirm

One line:

> `{phase}.md` imported for `YYYY-MM`. Phase {N} `Complete`. Next: `{next_command}`

Where `{next_command}`:
- After `analyse` → `import plan`
- After `plan` → `import strategy`
- After `strategy` → Monthly review complete.

---

## Commit Convention

```
analyse: imported ChatGPT analysis — YYYY-MM
plan: imported ChatGPT plan — YYYY-MM
strategy: imported ChatGPT strategy — YYYY-MM
```

---

## Edge Cases

| Situation | Behaviour |
| --- | --- |
| Content pasted in same message as `import` | Use it immediately. No prompt. |
| Phase already `Complete` | Warn once. Confirm overwrite. |
| Gate not met | Stop. Name the blocking phase. Suggest next step. |
| Unsupported phase name | Stop immediately. Do not guess. |
| `Review Month` override supplied | Use it. Validate the folder exists first. |
| `Source` override supplied | Use it in the import line. Commit message is always `ChatGPT`. |
| No `reviews/` folder exists | Tell user to run `finance start` first. |
