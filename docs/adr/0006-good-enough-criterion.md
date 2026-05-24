# 0006 — Good-enough criterion

- **Status:** Accepted
- **Date:** 2026-05-24

## Context

The system runs unattended (including via `claude -p`), so it needs an objective
stop condition: when is a deliverable "done enough" to ship, and when should the
reviewer keep iterating? Without a cap, a fix loop could run indefinitely.

## Decision

Combine three things:

1. **A mandatory checklist** (all must pass):
   - every slide covered;
   - each topic has ≥1 general source + the required specific sources for the
     depth;
   - 0 broken links;
   - cited sources actually support the claims;
   - the run completes end-to-end via CLI with no human input.
2. **A 1–5 quality rubric** the reviewer scores the deliverable against (clarity,
   accuracy, role-fit, completeness, source quality).
3. **A `max_iterations` cap** (default 3) on the reviewer→md-author fix loop.

If the checklist passes and the rubric clears the bar, the run ships. If not, the
reviewer requests fixes — up to the cap.

## Alternatives considered

- **Fixed iteration count** — wastes effort when done early; insufficient when
  hard.
- **No cap** — risk of infinite loops in unattended runs.

## Consequences

- An objective, automatable stop condition suitable for unattended runs.
- At the cap, the run may stop with **documented gaps** rather than perfect
  output — which is acceptable and explicit.
