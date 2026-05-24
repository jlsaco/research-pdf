# 0005 — Output structure and section schema

- **Status:** Accepted
- **Date:** 2026-05-24

## Context

A researched deck can produce a lot of material across many slides and topics.
The output needs to be navigable, adaptable to the requested role and depth, and
consistent enough for the reviewer to check mechanically.

## Decision

- Write output to a folder **named after the PDF** (`output/<slug>/`, slug =
  lowercased + hyphenated PDF name), containing:
  - `README.md` — overview/index
  - `topics/<NN>-<slug>.md` — one file per researched topic
  - `slides/slide-<NN>.md` — one file per slide
  - `.research/` — intermediate artifacts
- Use a **fixed + optional section schema** driven by **depth** and **role**:
  - Topic fixed: Summary, Prerequisite concepts, Deep dive, Sources, References.
  - Slide fixed: What this slide says, Key concepts, Linked topics.
  - Optional sections (e.g. "Why it matters for &lt;role&gt;", Common pitfalls,
    Hands-on, Glossary, ...) are added per the depth mapping in the config.

## Alternatives considered

- **One big markdown file** — simple, but unwieldy to read and navigate.
- **Flat files** (no topics/slides folders) — fewer files, but poor structure
  and harder cross-linking.

## Consequences

- Navigable, cross-linkable output that adapts to role and depth.
- Slightly more files to manage.
- A predictable schema the reviewer can verify section-by-section.
