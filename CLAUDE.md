# CLAUDE.md — Deep-Research for Technical Slide PDFs

This is a teaching repo for what an **agentic workflow** looks like in
practice. The job is small enough to fit in your head: a user drops a slide
PDF into `input/`, asks for "deep research", and gets back a structured
markdown bundle in `output/` — written for a chosen **role**, in a chosen
**language** (`es` / `en`), at a chosen **depth** (`quick` / `standard` /
`deep`).

## How it's wired

There is no fixed step-by-step diagram. There is an **orchestrator skill**
(`/deep-research`) that decides what to do next and delegates to **agents**
— each agent is an LLM with a written brief (in plain text, like a job
description). They read the previous artifact, think, and write the next
one. The structure of the workflow lives in the briefs and in the files
agents leave behind for each other, not in fixed code.

## How a run flows

The orchestrator asks the human for the three parameters, then calls these
agents in order:

1. **`slide-extractor`** — reads the PDF (visually + as text) and writes
   per-slide notes.
2. **`topic-mapper`** — groups the slides into topics and lists what a
   reader needs to know up front.
3. **`web-researcher`** — one per topic, in parallel. Searches the web in
   English, judges sources with a quality rubric (not a fixed allow-list),
   and verifies every link before citing it.
4. **`md-author`** — writes the final markdown in the chosen language,
   role, and depth.
5. **`research-reviewer`** — checks coverage, link liveness, and that the
   citations actually back up the claims. The orchestrator may loop with
   targeted fixes (cap: **3 iterations**).

Every brief lives as plain markdown in `.claude/`. If you want to change
behaviour — for example, make the reviewer stricter, or let
`web-researcher` use different heuristics — you edit the prose, not code.

## Layout

- `input/` — drop slide PDFs here.
- `output/<slug>/` — one folder per PDF, with `README.md`, `topics/`,
  `slides/`, and intermediate artifacts under `.research/`.
- `.claude/` — **source of truth**, edit here.
  - `skills/deep-research/SKILL.md` — the orchestrator.
  - `agents/*.md` — the five agents.
- `.opencode/` — generated from `.claude/` so the same project also runs
  under OpenCode. Don't edit by hand; run
  `python3 scripts/sync-opencode.py` after touching any brief
  (the pre-commit hook does it automatically).
- `docs/` — user guide and ADRs.
- `AGENTS.md` — a symlink to this file, so OpenCode reads the same guide.

> Dual-runtime detail: see [ADR 0008](docs/adr/0008-dual-runtime-claude-and-opencode.md)
> and [ADR 0009](docs/adr/0009-always-interactive-no-config.md).

## What to keep in mind when editing briefs

- **Plain prose, not scripts.** A brief is a job description. Snippets are
  fine when they save a paragraph, but if you find yourself writing a
  long bash recipe, ask whether you're telling the agent *what to do* or
  *how to do it* — the agent is smart enough to figure out the *how*.
- **No external config file.** Settings live next to the agent that uses
  them: the source-quality rubric is in `web-researcher.md`, the section
  schema is in `md-author.md`, the depth table is in the orchestrator
  `SKILL.md`, and the fix-loop cap (3) is in the orchestrator's step 6.
- **Always interactive.** The orchestrator asks the human to confirm the
  three parameters every run. No silent defaults.

## When is a run done?

All of these must hold:

- Every slide is covered.
- Each topic has at least one general source plus the required specific
  sources for the chosen depth.
- Zero broken links.
- Cited sources actually support the claims they're cited for.

If the reviewer can't get there in 3 fix-loop iterations, the run stops and
records the remaining gaps in the bundle's README.
