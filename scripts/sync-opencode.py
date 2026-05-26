#!/usr/bin/env python3
"""
sync-opencode.py — Transpile the Claude Code source-of-truth into OpenCode.

Single source of truth lives under `.claude/`. This script regenerates the
OpenCode equivalents under `.opencode/` so the two agent runtimes never drift:

  .claude/agents/<name>.md            ->  .opencode/agent/<name>.md
  .claude/skills/deep-research/SKILL.md -> .opencode/command/deep-research.md

Only the frontmatter and tool casing differ between the two systems; the prompt
BODY is copied verbatim. Edit the `.claude/` files; run this; commit both.

Usage:  python3 scripts/sync-opencode.py [--check]
  --check  exit non-zero if generated files are stale (for CI / hooks).
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Claude tool name  ->  OpenCode tool name
TOOL_MAP = {
    "Read": "read",
    "Write": "write",
    "Edit": "edit",
    "Bash": "bash",
    "Grep": "grep",
    "Glob": "glob",
    "WebSearch": "websearch",
    "WebFetch": "webfetch",
    "Task": "task",
    "AskUserQuestion": "question",
}

# Powerful tools we explicitly DISABLE when an agent's whitelist omits them, so
# OpenCode faithfully reproduces the Claude `tools:` whitelist (read-only stays
# read-only). Harmless read/search tools are left at their OpenCode defaults.
RESTRICTED = ["write", "edit", "bash", "webfetch", "websearch", "task", "patch"]

GEN_HEADER = (
    "<!-- GENERATED FILE — DO NOT EDIT.\n"
    "     Source of truth: {src}\n"
    "     Regenerate with: python3 scripts/sync-opencode.py -->\n"
)


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Return (frontmatter dict of raw string values, body). Naive but enough
    for our flat frontmatter (no nested structures on the Claude side)."""
    if not text.startswith("---"):
        raise ValueError("file has no frontmatter")
    _, fm, body = text.split("---", 2)
    meta: dict[str, str] = {}
    for line in fm.strip().splitlines():
        if ":" in line:
            key, val = line.split(":", 1)
            meta[key.strip()] = val.strip()
    return meta, body.lstrip("\n")


def map_tools(tools_csv: str) -> list[str]:
    out = []
    for raw in tools_csv.split(","):
        name = raw.strip()
        if not name:
            continue
        if name not in TOOL_MAP:
            raise ValueError(f"unknown tool in whitelist: {name!r}")
        out.append(TOOL_MAP[name])
    return out


def render_tools_block(allowed: list[str]) -> str:
    # OpenCode's permission model: `edit` gates write, edit, and patch.
    # If write or patch are whitelisted, edit must also be allowed, and vice
    # versa — they share the same underlying permission bit.
    expanded = set(allowed)
    if "write" in expanded or "patch" in expanded:
        expanded.add("edit")
    if "edit" in expanded:
        expanded.add("write")
        expanded.add("patch")
    lines = ["tools:"]
    for t in sorted(expanded):
        lines.append(f"  {t}: true")
    for t in RESTRICTED:
        if t not in expanded:
            lines.append(f"  {t}: false")
    return "\n".join(lines)


def build_agent(src: Path) -> str:
    meta, body = split_frontmatter(src.read_text())
    desc = meta.get("description", "")
    allowed = map_tools(meta.get("tools", ""))
    fm = "\n".join([
        "---",
        f"description: {desc}",
        "mode: subagent",
        render_tools_block(allowed),
        "---",
    ])
    rel = src.relative_to(ROOT)
    return f"{fm}\n{GEN_HEADER.format(src=rel)}\n{body}"


def build_command(src: Path) -> str:
    meta, body = split_frontmatter(src.read_text())
    desc = meta.get("description", "")
    fm = "\n".join([
        "---",
        f"description: {desc}",
        "agent: build",
        "---",
    ])
    rel = src.relative_to(ROOT)
    # Surface the user's invocation args to the orchestrator body.
    args = (
        "> **User request / arguments:** $ARGUMENTS\n"
        "> (Parse role/language/depth/pdf path from the line above per STEP 1.)\n"
    )
    return f"{fm}\n{GEN_HEADER.format(src=rel)}\n{args}\n{body}"


# (source path, builder, output path)
def targets() -> list[tuple[Path, callable, Path]]:
    items: list[tuple[Path, callable, Path]] = []
    for agent in sorted((ROOT / ".claude/agents").glob("*.md")):
        items.append((agent, build_agent, ROOT / ".opencode/agent" / agent.name))
    skill = ROOT / ".claude/skills/deep-research/SKILL.md"
    items.append((skill, build_command, ROOT / ".opencode/command/deep-research.md"))
    return items


def main() -> int:
    check = "--check" in sys.argv
    stale: list[str] = []
    for src, builder, out in targets():
        content = builder(src)
        current = out.read_text() if out.exists() else None
        if current == content:
            continue
        if check:
            stale.append(str(out.relative_to(ROOT)))
            continue
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(content)
        print(f"wrote {out.relative_to(ROOT)}")
    if check and stale:
        print("STALE OpenCode files (run scripts/sync-opencode.py):", file=sys.stderr)
        for s in stale:
            print(f"  - {s}", file=sys.stderr)
        return 1
    if not check:
        print("OpenCode mirror in sync.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
