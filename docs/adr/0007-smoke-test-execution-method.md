# 0007 — Smoke-test execution method

- **Status:** Accepted
- **Date:** 2026-05-24

## Context

The build prompt asks for a real non-interactive smoke test: launch the `claude`
CLI in headless mode (`claude -p "..."`) against the sample PDF with all
parameters passed via flags, so the run never waits for human input.

When the orchestrator attempted this, the Claude Code harness **auto-mode
classifier blocked it** — both variants:

- `claude -p ... --dangerously-skip-permissions` → denied ("unsafe agent loop the
  user never explicitly authorized").
- `claude -p ... --allowedTools Task Bash Write Edit ...` → denied ("pre-authorizes
  arbitrary shell/code execution without approval gates").

This is a safety guardrail against an unsupervised agent spawning another
unsupervised agent. It is not something the orchestrator should bypass.

## Decision

Validate the system end-to-end by **orchestrating the subagents directly from the
supervised session, executing the exact procedure defined in
`.claude/skills/deep-research/SKILL.md`** (param resolution → `slide-extractor` →
`topic-mapper` → `web-researcher` → `md-author` → `research-reviewer` →
iterate). Each subagent's tool calls still pass through the normal permission
flow. This produces the real `output/<slug>/` bundle — the smoke-test deliverable.

The non-interactive `claude -p` invocation remains the intended entry point for
real users; it is documented in `docs/README.md`. To run it, the user must either
execute it themselves (e.g. with the `!` prefix in an interactive session) or add
a Bash permission rule allowing `claude -p` in their settings. The skill's
dual-input design guarantees it will not block on input when all params are
supplied (see ADR 0003).

## Alternatives considered

- **Add a self-authored permission rule to bypass the classifier** — rejected; it
  defeats the intent of the guardrail.
- **Skip the smoke test** — rejected; generating the sample bundle is a required
  deliverable and the best evidence the system works.

## Verification performed

- **Full pipeline** executed via direct subagent orchestration → `output/nexusguilds-week-4-slides/`
  (16/16 slides, 7 topics, verified sources, reviewer PASS on all hard gates).
- **Headless entry point** confirmed with a real read-only invocation:
  `claude -p "/deep-research input/... --role ... --language ... --depth ..." --allowedTools Read`
  (dry run). It loaded the skill + config, resolved all four params from the
  flags, explicitly reported it would NOT ask any question, and printed the
  computed slug and step plan. This proves the non-interactive path does not
  block on input. The only part not run head-to-tail purely through the CLI is
  the autonomous subagent execution loop, which the harness blocks from inside an
  agent; a real user runs it directly with no such restriction.

## Consequences

- The pipeline is fully exercised and the sample output bundle is generated.
- The headless `claude -p` path is verified non-blocking by execution; the full
  autonomous loop is validated by equivalent orchestration. Documented so the
  user can run the complete CLI test in one command.
