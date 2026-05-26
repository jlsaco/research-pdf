# 0008 — Dual runtime: Claude Code and OpenCode from one source

- **Status:** Accepted (config-sharing portion superseded by [ADR 0009](0009-always-interactive-no-config.md))
- **Date:** 2026-05-24

> **Partial supersede (2026-05-25):** the dual-runtime mechanism (transpiler,
> `.opencode/` mirror, `AGENTS.md` symlink, git hook) is unchanged. What ADR 0009
> removed is the `research-config.yaml` itself — so references in this ADR to
> sharing the YAML at repo root no longer apply. Settings are now inline in the
> skill and agents and propagate to OpenCode via the same transpiler.

## Context

The system was built Claude-Code-native: an orchestrator **skill** plus five
**subagents** under `.claude/`, a `CLAUDE.md` guide, and a YAML config. We want
the same system to run under **OpenCode** as well, without maintaining two
hand-edited copies that inevitably drift.

OpenCode has near-parity primitives — `task` (subagents), `websearch`,
`webfetch`, `question`, `skill` — so this is a *translation* problem, not a
redesign. The only real divergences between the two runtimes are mechanical:

- **File location:** `.claude/agents/` vs `.opencode/agent/`; the skill becomes
  an OpenCode **command** (`/deep-research`).
- **Frontmatter schema:** Claude uses `name:` + `tools: A, B, C`; OpenCode uses
  `mode:` + a `tools:` object map.
- **Tool name casing:** `Read`/`Bash`/`WebSearch` vs `read`/`bash`/`websearch`.
- **Instructions file:** `CLAUDE.md` vs `AGENTS.md`.

The prompt **bodies** are otherwise identical — and they are where all the value
lives.

The one body-level divergence was `slide-extractor`, which relied on Claude
Code's native `Read` tool `pages` param for the visual pass (OpenCode's `read`
does not rasterize PDFs).

## Decision

Keep **`.claude/` as the single source of truth** and **generate `.opencode/`**.

1. **Make bodies portable.** Rewrite `slide-extractor`'s visual pass to
   `pdftoppm -png` → `Read` the PNGs. This works in both runtimes (Claude Code
   also reads images), eliminating the last body-level divergence so a purely
   mechanical transform suffices.
2. **Share what is identical, with no transform:**
   - `research-config.yaml` moved to the repo root; referenced by the same path
     from both runtimes.
   - `AGENTS.md` is a **symlink to `CLAUDE.md`**; `opencode.json` points
     `instructions` at `AGENTS.md`.
3. **Generate the schema-divergent wrappers.** `scripts/sync-opencode.py`
   transpiles each `.claude/agents/*.md` → `.opencode/agent/*.md` and the
   orchestrator `SKILL.md` → `.opencode/command/deep-research.md`: it remaps the
   frontmatter, lowercases tool names, faithfully reproduces the per-agent tool
   whitelist (powerful tools explicitly set `false` when omitted), and copies the
   body verbatim with a `DO NOT EDIT` header.
4. **Keep them in sync automatically.** `.githooks/pre-commit` runs the
   transpiler and stages `.opencode/` whenever `.claude/` (or the transpiler)
   changes. `scripts/sync-opencode.py --check` fails if the mirror is stale (for
   CI). Enable per clone with `git config core.hooksPath .githooks`.

## Alternatives considered

- **Maintain two hand-edited copies** — rejected; guaranteed drift the moment a
  prompt is edited and the mirror is forgotten.
- **Symlink the agent files directly** — rejected; the frontmatter schemas differ,
  so the same file cannot be valid in both runtimes.
- **Generate Claude *from* OpenCode** — symmetric, but Claude Code is the existing
  native, documented (ADRs) side, so it stays canonical.
- **Factor bodies into neutral includes** — rejected; Claude Code agents read a
  whole `.md` and do not support includes, so the approach is not symmetric.

## Consequences

- One place to edit (`.claude/`, `research-config.yaml`, `CLAUDE.md`); the
  OpenCode mirror adapts automatically.
- A small build step and a tool-name mapping table in the transpiler must be
  maintained if either runtime renames tools.
- `.opencode/` is committed (so OpenCode users need not run the build) but is
  generated — never hand-edit it.
- The PDF visual pass is now `pdftoppm`-based in both runtimes (poppler is already
  a dependency via `pdfinfo`/`pdftotext`).
