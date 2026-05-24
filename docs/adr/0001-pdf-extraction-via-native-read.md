# 0001 — PDF extraction via native Read + pdftotext

- **Status:** Accepted
- **Date:** 2026-05-24

## Context

We need to extract content from slide PDFs, including both text and visual
elements (diagrams, charts, layout-dependent meaning). No Python PDF libraries
are installed in this environment, but poppler's `pdftotext` and `pdfinfo` are
available on PATH. Claude's native Read tool can render PDF pages visually via
its `pages` parameter.

## Decision

Extract slides using **Claude's native Read tool** (visual PDF reading via the
`pages` parameter) for visual/layout understanding, combined with **`pdftotext`**
for clean, reliable text extraction (and `pdfinfo` for page counts/metadata). No
Python PDF libraries are installed.

## Alternatives considered

- **pypdf** — text-only, weak on layout, requires install.
- **pdfplumber** — good tables/layout, requires install.
- **pymupdf (fitz)** — fast and capable, requires install and has licensing
  considerations.

## Consequences

- Zero extra dependencies; works out of the box with what is installed.
- Captures visuals and slide layout, not just raw text.
- Relies on model vision for visual interpretation, which can vary; `pdftotext`
  provides a deterministic text backstop.
