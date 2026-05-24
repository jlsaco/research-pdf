# 0004 — Trusted sources + English-first research

- **Status:** Accepted
- **Date:** 2026-05-24

## Context

Open web research yields variable quality and can surface SEO spam, outdated
blogs, or unverifiable claims. The subject matter (AI, agents, automation, APIs)
has authoritative primary sources, most of which publish in English. The
deliverable, however, may be requested in Spanish or English.

## Decision

- Maintain an **editable YAML trusted-source list** (`trusted_sources:` in the
  config) that the web-researcher prefers, ranked by priority and matched by
  tags.
- **Always search in English** (`research.prefer_language: en`) for the best
  source quality, regardless of output language.
- **Emit output in the chosen `language`** (translating/localizing as needed).
- **Verify every link** is live before citing it (`research.verify_links`).

## Alternatives considered

- **Open web, no curation** — broader reach, but lower and inconsistent quality.
- **Search in the output language** — better-localized hits, but thinner and
  lower-authority coverage for technical topics.

## Consequences

- Higher source quality and consistency.
- An English bias in the search phase (acceptable; primary docs are English).
- Localized, role-appropriate deliverables decoupled from search language.
- The source list is user-maintained and must be kept current.
