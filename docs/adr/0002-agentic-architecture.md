# 0002 — Agentic architecture: orchestrator skill + 5 subagents

- **Status:** Accepted
- **Date:** 2026-05-24

## Context

The pipeline has distinct stages — read the PDF, map topics, research each
topic on the web, write the deliverable, and review it. Each stage has different
context needs and tool usage, and some (per-topic research) are naturally
parallel.

## Decision

Use an **orchestrator skill** (`/deep-research`) that resolves params and
delegates to **5 specialized subagents**:

1. **slide-extractor** — reads the PDF into per-slide notes.
2. **topic-mapper** — clusters slides into topics + prerequisite concepts.
3. **web-researcher** — one per topic; English-first, trusted-source web research
   with link verification.
4. **md-author** — writes the final markdown (language/role/depth aware).
5. **research-reviewer** — verifies coverage, links, and source support.

## Alternatives considered

- **Single monolithic prompt** — simpler, but loses context isolation, can't
  parallelize research, and degrades on long PDFs.
- **External pipeline script** — deterministic orchestration, but adds tooling/
  dependencies and reduces the system's ability to reason adaptively per stage.

## Consequences

- Clear separation of concerns; each agent has a focused role and toolset.
- Per-topic research is parallelizable.
- More orchestration overhead and inter-agent contract surface to maintain (the
  shared config and section schema keep this consistent).
