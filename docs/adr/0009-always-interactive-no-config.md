# 0008 — Always-interactive params; no config file

- **Status:** Accepted
- **Date:** 2026-05-25

## Context

The original design ([ADR 0003](0003-dual-input-params.md)) resolved the three
params (`role`, `language`, `depth`) from flags → `defaults:` in
`research-config.yaml` → an interactive fallback, specifically so unattended
`claude -p` runs ([ADR 0007](0007-smoke-test-execution-method.md)) never blocked
on input. In practice this added moving parts the project did not want: a config
file to keep in sync, silent defaults that could ship a deliverable written for
the wrong audience, and a "never block" rule that complicated every entry point.

The owner's intent is the opposite: **a human should always confirm what is
being produced, and the workflow should stay simple.**

## Decision

1. **Always ask the human.** The orchestrator resolves `role`, `language`, and
   `depth` by asking via `AskUserQuestion` every run. Values named in the user's
   prompt are offered as the recommended option (one-click confirm); nothing
   proceeds on an unconfirmed parameter. There are no silent defaults.
2. **Remove the config file.** `research-config.yaml` is deleted. Its content
   moves inline next to the code that uses it:
   - the curated **trusted-source** table → `.claude/agents/web-researcher.md`;
   - the **section schema** → `.claude/agents/md-author.md`;
   - the **depth → sections / source-count** mapping → the orchestrator's Depth
     reference in `.claude/skills/deep-research/SKILL.md`;
   - the **fix-loop cap** (3 iterations) → the orchestrator's STEP 6.
3. **Drop the headless rules.** All `claude -p` / "non-interactive must never
   block" language is removed, including the "completes via CLI with no human
   input" item of the good-enough checklist ([ADR 0006](0006-good-enough-criterion.md)).

This supersedes ADR 0003 and ADR 0007 and amends ADR 0006.

## Alternatives considered

- **Keep config for sources/sections, drop only defaults** — rejected; the owner
  wanted the config gone entirely for simplicity, and the data is small enough to
  live inline beside its single consumer.
- **Honor explicit flags without re-confirming** — rejected; "always consult the
  human" is the point. Flags are still honored, but as a pre-filled choice to
  confirm, not a way to skip the human.

## Consequences

- Simpler mental model: one source of truth per setting, no YAML to maintain, and
  a guaranteed human checkpoint on audience/language/depth before any work runs.
- The system can no longer run fully unattended (e.g. CI `claude -p`). That is an
  accepted trade-off — interactive confirmation is now a feature, not a bug.
- Editing trusted sources or sections means editing the relevant agent file.
