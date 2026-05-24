# CLAUDE.md — Deep-Research for Technical Slide PDFs

Guide for Claude sessions working in this repo.

## What this project is

An agentic deep-research system. A user drops a **technical slide PDF** into
`input/`, runs `/deep-research` (a skill) or asks in natural language
("do a deep research on this document"), and the system produces a structured,
researched markdown deliverable in `output/`, written for a chosen **role**, in
a chosen **language**, at a chosen **depth**.

## Directory layout

```
input/                          # User drops slide PDFs here
output/<slug>/                  # Deliverable per PDF (slug = hyphenated-lowercase PDF name)
  README.md                     #   index / overview
  topics/<NN>-<slug>.md         #   one file per researched topic
  slides/slide-<NN>.md          #   one file per slide
  .research/                    #   intermediate artifacts (extraction, topic map, notes)
docs/
  README.md                     # User-facing usage guide
  adr/                          # Architecture Decision Records (0001..)
.claude/
  skills/deep-research/         # Orchestrator skill (entry point)
  agents/                       # The 5 specialized subagents
  research-config.yaml          # User-editable config (defaults, sources, sections)
CLAUDE.md                       # This file
```

## How a run flows (orchestrator + 5 subagents)

The `/deep-research` **orchestrator skill** resolves the 3 params (see below),
then delegates in order:

1. **slide-extractor** — reads the PDF (native Read tool `pages` for visuals +
   `pdftotext` for text) into per-slide structured notes.
2. **topic-mapper** — clusters slides into topics and identifies prerequisite
   concepts; produces the topic map.
3. **web-researcher** — one per topic. Searches the web **in English first**
   using the trusted-source list in the config, and **verifies every link** is
   live before citing it.
4. **md-author** — writes the final markdown in the chosen language/role/depth,
   following the fixed/optional section schema.
5. **research-reviewer** — verifies coverage, link liveness, and that sources
   actually support the claims. May request fixes (looped up to `max_iterations`).

## Param model + dual-input rule

Three params: `role` (free text), `language` (`es`|`en`), `depth`
(`quick`|`standard`|`deep`).

Resolution order: **explicit flags/args → config `defaults:` → interactive
AskUserQuestion** (only when the run is interactive AND a value is still
missing).

> **CRITICAL:** Non-interactive `claude -p` runs must **never block on input.**
> When invoking non-interactively, pass ALL params explicitly (or rely on
> config defaults). The AskUserQuestion fallback is interactive-only.

## Where outputs land

`output/<slug>/` where `<slug>` is the PDF filename lowercased and hyphenated.
Contains `README.md`, `topics/`, `slides/`, and intermediate artifacts under
`.research/`.

## Editing trusted sources & sections

All in `.claude/research-config.yaml`:

- `trusted_sources:` — add/remove domains the researcher prefers (name, url,
  tags, priority).
- `sections:` — the fixed/optional section lists and the depth→sections mapping.
- `defaults:`, `max_iterations:`, and the `research:` rules also live here.

## Good-enough checklist (the stop condition)

A run is done when ALL hold:

- [ ] Every slide is covered.
- [ ] Each topic has ≥1 general source **and** the required specific sources.
- [ ] 0 broken links.
- [ ] Cited sources actually support the claims made.
- [ ] The run completes end-to-end via CLI with no human input.

If the reviewer cannot satisfy these within `max_iterations`, the run stops and
documents the remaining gaps.
