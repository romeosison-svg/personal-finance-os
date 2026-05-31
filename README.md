# Personal Finance OS

A structured, auditable monthly finance review process.

---

## Purpose

Personal Finance OS is not a budgeting app.

It is a **process and memory system** — a Personal Finance Operating System that enforces a disciplined, phase-gated monthly review cycle. Every financial decision is traceable. Every recommendation is earned by completing the phases that precede it.

The system is designed to evolve. V1 is entirely file-based. Future versions will introduce databases, Open Banking feeds, and AI-assisted analysis. But the process — the Assembly Line — stays constant across every version.

---

## Philosophy

### No shortcuts

Phases are gates, not suggestions. A monthly review must complete Phase 1 before Phase 2 begins. No analysis is produced before the facts are established. No plan is produced before the position is known.

### Separation of fact and opinion

Facts (what the balances are, what payments cleared) are locked in the **Reconcile** phase before any planning begins. This prevents the common failure mode of planning from memory rather than from verified data.

### Assumptions are explicit

Planning rules — buffers, targets, split methodologies — are declared explicitly in **finance-profile.md** and confirmed each month in the **Assumptions** phase. There are no hidden rules.

### Auditability over convenience

Every monthly review is a folder. Every phase is a file. The git history is the audit trail. You can look back at any month and understand exactly what the financial position was, what assumptions were in play, and what decisions were made.

---

## Finance Assembly Line

The system operates as a Finance Assembly Line. Monthly reviews move through six gated phases in sequence.

```
collect → reconcile → assumptions → position → plan → strategy
```

| Phase       | Alias       | Purpose                                      | Output                    |
| ----------- | ----------- | -------------------------------------------- | ------------------------- |
| 1           | collect     | Gather all required inputs                   | Completed checklist       |
| 2           | reconcile   | Establish the truth                          | Locked financial facts    |
| 3           | assumptions | Set planning rules                           | Locked planning rules     |
| 4           | position    | Create current financial position snapshot   | Financial position report |
| 5           | plan        | Generate next month's payment plan           | Approved monthly plan     |
| 6           | strategy    | Long-term financial decisions                | Strategic recommendations |

See [Finance Assembly Line](/docs/finance-assembly-line.md) for full phase documentation.

---

## Repository Structure

```
personal-finance-os/
│
├── README.md
│
├── docs/
│   ├── finance-assembly-line.md     # Full phase documentation
│   ├── finance-profile.md           # Persistent planning assumptions
│   ├── monthly-review-template.md   # Reusable monthly review template
│   └── workflow.md                  # Process commands reference
│
└── reviews/
    └── 2026-06-example/             # Example monthly review folder
        ├── collect.md
        ├── reconcile.md
        ├── assumptions.md
        ├── position.md
        ├── plan.md
        └── strategy.md
```

Each monthly review lives in its own folder under `/reviews/`, named `YYYY-MM-description`.

---

## Monthly Review Process

### Starting a new month

1. Copy `/docs/monthly-review-template.md` structure into a new folder under `/reviews/`.
2. Name the folder `YYYY-MM` (e.g. `reviews/2026-07/`).
3. Create the six phase files: `collect.md`, `reconcile.md`, `assumptions.md`, `position.md`, `plan.md`, `strategy.md`.
4. Work through each phase in order, completing each before moving to the next.
5. Commit after each phase is completed and locked.

### Phase discipline

- A phase is **locked** when all required fields are populated and the phase status is marked `Complete`.
- Do not move to the next phase until the current phase is locked.
- Do not generate recommendations in phases 1–4.
- Plans belong in phase 5. Strategic decisions belong in phase 6.

See [Workflow](/docs/workflow.md) for full command reference.

---

## Future Roadmap

### V1 — Markdown Process System *(current)*

File-based. No automation. No dependencies.  
The process, the structure, and the discipline.

### V2 — Historical Trend Tracking

Month-over-month comparisons. Cash flow trending. Balance history.  
Still file-based, but with structured data files enabling analysis.

### V3 — Database Integration

SQLite or Postgres-backed storage.  
Monthly reviews stored as structured records.  
Query historical positions, track net worth over time.

### V4 — Open Banking Ingestion

Automated statement import via Open Banking APIs.  
The Collect and Reconcile phases become semi-automated.  
Human review remains required before locking facts.

### V5 — MCP Integration

Model Context Protocol integration.  
The system becomes queryable by AI assistants.  
Finance OS as a context provider, not just a document store.

### V6 — AI-Assisted Financial Operating System

Full AI co-pilot for monthly reviews.  
Phase completion assisted by LLM analysis.  
Strategic recommendations grounded in verified historical data.  
Human approval gates preserved at every phase boundary.

---

## Contributing

This is a personal system. It is not designed for generalisation or open contribution.  
It is published openly as a reference and to benefit from version control as an audit trail.
