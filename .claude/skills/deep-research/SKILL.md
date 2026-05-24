---
name: deep-research
description: Run a deep-research pass on a slide PDF — extract slides, map topics, research trusted English sources (verifying every link), and generate per-topic and per-slide markdown in the chosen language, role, and depth. Trigger when the user drops a PDF in input/ and asks to "deep research" / "research this document", or invokes /deep-research.
---

# Deep Research (orchestrator)

You orchestrate a multi-agent deep-research pass over a slide PDF and emit a structured markdown bundle. Run the steps below in order, delegating to subagents via the **Task** tool. Read defaults, trusted sources, the section schema, the depth mapping, and `max_iterations` from `.claude/research-config.yaml`.

## Contract / layout
- Per-run dir: `output/<slug>/` where `<slug>` = lowercased, hyphenated PDF basename
  (e.g. `NexusGuilds Week 4 Slides.pdf` → `nexusguilds-week-4-slides`).
- Intermediates: `output/<slug>/.research/` — `params.json`, `extraction.md`, `topic-map.md`, `findings/<topic-slug>.md`, `review.md`.
- Deliverables: `output/<slug>/README.md`, `output/<slug>/topics/<NN>-<topic-slug>.md`, `output/<slug>/slides/slide-<NN>.md`.
- Subagents: `slide-extractor`, `topic-mapper`, `web-researcher`, `md-author`, `research-reviewer`.

## Parameters
- `role`: free text (e.g. "Project Manager", "AI Engineer").
- `language`: `es` or `en`.
- `depth`: `quick` | `standard` | `deep`.

---

## STEP 1 — Param resolution (DUAL INPUT)

Resolve `pdf_path`, `role`, `language`, `depth` in this order:
1. **Explicit args** in the user's prompt — flags or natural language.
   - Flag form: `/deep-research input/NexusGuilds Week 4 Slides.pdf --role "Project Manager" --language en --depth standard`
   - Natural language: "do a deep research on input/foo.pdf for a project manager in spanish, standard depth".
2. **`defaults:`** in `.claude/research-config.yaml` for anything not given.
3. **AskUserQuestion** — ONLY if the session is interactive AND a value is still missing.

**PDF path:** if no path is given, default to the single PDF in `input/` when exactly one exists. (If `input/` has zero or multiple PDFs and none was specified, ask — interactive only — or fail with a clear message non-interactively.)

**CRITICAL — non-interactive runs must never block:** if all of `role`, `language`, `depth` are resolvable from args + config defaults, DO NOT ask any questions (required for `claude -p`). Only use `AskUserQuestion` when the session is interactive AND a parameter is genuinely still missing.

Compute `<slug>` from the PDF basename (drop extension, lowercase, replace non-alphanumerics with single hyphens, trim hyphens).

Create the working dir and write params:
```bash
mkdir -p "output/<slug>/.research/findings" "output/<slug>/topics" "output/<slug>/slides"
```
Write `output/<slug>/.research/params.json`:
```json
{ "role": "<role>", "language": "<language>", "depth": "<depth>", "pdf_path": "<pdf_path>", "slug": "<slug>", "date": "<YYYY-MM-DD>" }
```

---

## STEP 2 — Extract

Launch the **`slide-extractor`** subagent (Task tool), passing `pdf_path` and `slug`. It writes `output/<slug>/.research/extraction.md` and reports the slide count. Confirm the file exists before continuing.

## STEP 3 — Map topics

Launch **`topic-mapper`** with `slug`. It reads `extraction.md` and writes `output/<slug>/.research/topic-map.md` (topic clusters + slide→topic index). Read `topic-map.md` yourself to get the list of topics (slug, title, slides, prerequisites, queries).

## STEP 4 — Research (parallel)

For EACH topic cluster, launch one **`web-researcher`** subagent. Run them in **parallel batches, ~4 concurrent max** (issue up to 4 Task calls in a single message, wait, then the next batch). Pass each: `slug`, `topic_slug`, `topic_title`, `prerequisite_concepts`, `queries`, and the params (`role`, `language`, `depth`). Each writes `output/<slug>/.research/findings/<topic-slug>.md` with verified sources. Confirm one findings file per topic exists.

## STEP 5 — Author deliverables (parallel)

Launch **`md-author`** subagents:
- One per topic → `topics/<NN>-<topic-slug>.md` (uses the matching findings file).
- Cover EVERY slide → `slides/slide-<NN>.md` (one md-author can handle a batch of slides).
- One for the bundle `README.md` (index of topics + slides + global summary + params).

Parallelize sensibly (~4 concurrent). All output in the run's `language`, following the section schema and depth mapping from the config (see Depth reference below).

## STEP 6 — Review & iterate

Launch **`research-reviewer`** with `slug`. It writes `output/<slug>/.research/review.md` and returns a verdict + issue list.

- If verdict is **PASS** → go to Step 7.
- If **FAIL** and the iteration count is below `max_iterations` (config, default **3**): dispatch TARGETED fixes for the listed issues only — re-run `web-researcher` for topics with missing/broken sources, re-run `md-author` for files with bad content/links/coverage — then re-run `research-reviewer`. Increment the iteration counter.
- If the cap is reached and issues remain: record the remaining gaps in a "Known gaps" section of `output/<slug>/README.md` and stop.

## STEP 7 — Final summary

Print: the output folder path (`output/<slug>/`), number of topics, number of slides, and the review verdict (and iteration count).

---

## Depth reference (mirror of config)

Topic FIXED sections: `Summary`, `Prerequisite concepts`, `Deep dive`, `Sources`, `References`.
Topic OPTIONAL: `Why it matters for <role>`, `Hands-on`, `Common pitfalls`, `Going deeper`, `Glossary`, `Related slides & topics`.
Slide FIXED: `What this slide says`, `Key concepts`, `Linked topics`. Slide OPTIONAL: `Notes for <role>`.

- `quick`: fixed sections only; 1 general + 1 specific source per topic; concise.
- `standard`: fixed + "Why it matters for <role>" + "Common pitfalls"; 1 general + 2-3 specific sources.
- `deep`: all optional sections; 1 general + 3-5 specific sources; thorough.

## Research rules (enforced by web-researcher)
- Search the WEB IN ENGLISH even when output is Spanish.
- Prefer `trusted_sources` from `.claude/research-config.yaml`; need ≥1 general + depth-dependent specific sources per topic.
- VERIFY every link (WebFetch + optional `curl -sI`) before citing; never cite an unfetched or invented URL.
