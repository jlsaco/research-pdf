# 0003 — Dual-input parameter resolution

- **Status:** Accepted
- **Date:** 2026-05-24

## Context

The system must serve two modes: real users running it interactively (who may
not specify every param), and automated `claude -p` invocations (e.g. smoke
tests, CI) that must run unattended. The three params are `role`, `language`,
and `depth`.

## Decision

Resolve params in this order:

1. Explicit prompt **args / flags** (`--role`, `--language`, `--depth`).
2. Config **`defaults:`** in `research-config.yaml`.
3. Interactive **AskUserQuestion** — only when the run is interactive AND a
   value is still missing.

Non-interactive CLI runs must **never block** on input: if no flag and no
applicable default existed, defaults always backstop them, so the interactive
fallback is reached only in interactive sessions.

## Alternatives considered

- **Interactive-only** — would block/hang automated `claude -p` runs.
- **Config-only** — no way to override per-run; clumsy for ad-hoc requests.

## Consequences

- Works for real users (gets asked for missing values) and for automated runs
  (`claude -p` never hangs).
- Requires every entry point to honor the same resolution order; the config
  defaults guarantee a non-blocking path.
