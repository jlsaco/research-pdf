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
.claude/                        # ◀ SOURCE OF TRUTH (edit here)
  skills/deep-research/         #   Orchestrator skill (entry point)
  agents/                       #   The 5 specialized subagents
.opencode/                      # ◀ GENERATED from .claude/ — do not edit by hand
  command/deep-research.md      #   Orchestrator as an OpenCode command (/deep-research)
  agent/                        #   The 5 subagents in OpenCode frontmatter
  agents -> agent, commands -> command  # compat symlinks (OpenCode dir-name ambiguity)
opencode.json                   # OpenCode project config (points instructions at AGENTS.md)
scripts/sync-opencode.py        # Transpiler: .claude/ -> .opencode/ (run / --check)
.githooks/pre-commit            # Auto-regenerates .opencode/ on commit
CLAUDE.md                       # This file
AGENTS.md                       # Symlink -> CLAUDE.md (so OpenCode reads the same guide)
```

> **Dual runtime:** this repo runs under both **Claude Code** and **OpenCode**
> from one source. You ONLY edit `.claude/` and `CLAUDE.md`; `.opencode/` is
> generated. See [ADR 0008](docs/adr/0008-dual-runtime-claude-and-opencode.md)
> and [ADR 0009](docs/adr/0009-always-interactive-no-config.md), and run
> `python3 scripts/sync-opencode.py` after editing any agent/skill.

## How a run flows (orchestrator + 5 subagents)

The `/deep-research` **orchestrator skill** resolves the 3 params (see below),
then delegates in order:

1. **slide-extractor** — reads the PDF (`pdftoppm` rasterizes each page to PNG
   for the visual pass + `pdftotext` for text; portable across both runtimes)
   into per-slide structured notes.
2. **topic-mapper** — clusters slides into topics and identifies prerequisite
   concepts; produces the topic map.
3. **web-researcher** — one per topic. Searches the web **in English first**
   using a curated trusted-source list (inline in the agent), and **verifies
   every link** is live before citing it.
4. **md-author** — writes the final markdown in the chosen language/role/depth,
   following the fixed/optional section schema.
5. **research-reviewer** — verifies coverage, link liveness, and that sources
   actually support the claims. May request fixes (looped up to `max_iterations`).

## Param model (always interactive)

Three params: `role` (free text), `language` (`es`|`en`), `depth`
(`quick`|`standard`|`deep`).

The orchestrator **always asks the human** to confirm these via
AskUserQuestion — there are no config defaults and no silent fallbacks. If the
user already named a value in their prompt, it is offered as the recommended
option to confirm. The run never proceeds on an unconfirmed parameter.

## Where outputs land

`output/<slug>/` where `<slug>` is the PDF filename lowercased and hyphenated.
Contains `README.md`, `topics/`, `slides/`, and intermediate artifacts under
`.research/`.

## Editing trusted sources & sections

There is no config file — settings live inline next to the code that uses them:

- **Trusted sources** — the curated domain table in
  `.claude/agents/web-researcher.md`.
- **Sections** — the fixed/optional section schema in
  `.claude/agents/md-author.md` and the Depth reference in
  `.claude/skills/deep-research/SKILL.md`.
- **Fix-loop cap** — `3 iterations`, set in the orchestrator's STEP 6.

## Good-enough checklist (the stop condition)

A run is done when ALL hold:

- [ ] Every slide is covered.
- [ ] Each topic has ≥1 general source **and** the required specific sources.
- [ ] 0 broken links.
- [ ] Cited sources actually support the claims made.

If the reviewer cannot satisfy these within the **3-iteration** fix-loop cap, the
run stops and documents the remaining gaps.
