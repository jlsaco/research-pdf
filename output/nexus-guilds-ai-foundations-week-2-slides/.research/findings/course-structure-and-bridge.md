# Findings — Course Structure, Deliverable & Week 3 Bridge (course-structure-and-bridge)

## General source(s)
- [Vibe coding — Wikipedia](https://en.wikipedia.org/wiki/Vibe_coding) — High-level, definitional introduction to AI-assisted development: describing software in plain language to an LLM that generates the code. Names the tool families bridged to in Week 3 (Replit, Cursor, Lovable, GitHub Copilot), so it frames why the course moves from foundations into AI-assisted development.

## Specific sources
- [Best AI App Builders in 2026 (Lovable guide)](https://lovable.dev/guides/best-ai-app-builders) — Covers the **no-code app builders** prerequisite: positions Bolt.new (rapid prototyping, Bolt Cloud with DB/auth) and Replit Agent 3 (full-stack generation, sees the code, 50+ languages) in the 2026 landscape; explains the no-code/"vibe coding" build model.
- [Replit Agent (official docs)](https://docs.replit.com/replitai/agent) — Covers the **Replit Agent** prerequisite specifically: an AI tool that turns plain-English descriptions into functional apps (writes code, sets up infrastructure, tests, deploys) with no coding required; Plan mode and Lite/Economy/Power modes.
- [Claude Code: Overview (official Claude Docs)](https://code.claude.com/docs/en/overview) — Covers the **agentic coding environments / Claude Code** prerequisite and the **GitHub tooling** prerequisite: defines Claude Code as an agentic coding tool that reads a codebase, edits files, runs commands, and works with git (stages changes, creates branches, opens pull requests) and GitHub Actions. High-priority trusted source.
- [Claude Code vs Cursor: 2026 comparison (Builder.io)](https://www.builder.io/blog/cursor-vs-claude-code) — Covers the **agentic coding environments (Cursor vs Claude Code)** prerequisite: contrasts Cursor (IDE-first VS Code fork, tab completion, inline diffs, multi-model) with Claude Code (agent-first, autonomous multi-file work, terminal/CLI), and the pair-programming "use both" pattern.

## Key facts
- Vibe coding = describing a project in natural language to an LLM that generates the source code automatically; practitioners often accept AI output and iterate via follow-up prompts. — source: https://en.wikipedia.org/wiki/Vibe_coding
- The term "vibe coding" was coined by Andrej Karpathy in February 2025; it was Collins English Dictionary Word of the Year 2025. — source: https://en.wikipedia.org/wiki/Vibe_coding
- No-code app builders let non-developers ship full-stack apps from a prompt; Gartner projects low-code tools will account for 75% of new application development by 2026. — source: https://lovable.dev/guides/best-ai-app-builders
- Bolt.new is optimized for fast shareable prototypes; Bolt Cloud (mid-2025) added hosting, databases, and authentication. — source: https://lovable.dev/guides/best-ai-app-builders
- Replit Agent turns plain-English descriptions into working apps — it writes the code, sets up infrastructure, tests, and deploys, with no coding knowledge required; offers Plan mode plus Lite/Economy/Power build modes. — source: https://docs.replit.com/replitai/agent
- Claude Code is an agentic coding tool that reads your codebase, edits files, runs commands, and integrates with dev tools across terminal, IDE, desktop, and web. — source: https://code.claude.com/docs/en/overview
- Claude Code works directly with git: it stages changes, writes commit messages, creates branches, and opens pull requests, and can automate review via GitHub Actions — relevant to the GitHub prerequisite tooling setup. — source: https://code.claude.com/docs/en/overview
- Cursor is an IDE-first VS Code fork (tab completion, inline diffs, multi-model chat, agent mode) while Claude Code is agent-first (autonomous multi-file refactoring, terminal/CLI); power users commonly use both together (pair programming). — source: https://www.builder.io/blog/cursor-vs-claude-code

## Verification checklist
| URL | HTTP | Supports |
|-----|------|----------|
| https://en.wikipedia.org/wiki/Vibe_coding | 200 | General definition of AI-assisted development / vibe coding; lists Replit, Cursor, Lovable, Copilot. |
| https://lovable.dev/guides/best-ai-app-builders | 200 | No-code app builders 2026 landscape; Bolt.new and Replit Agent positioning. |
| https://docs.replit.com/replitai/agent | 200 | Replit Agent builds apps from plain-English descriptions; build modes. |
| https://code.claude.com/docs/en/overview | 200 | Claude Code = agentic coding tool; git/GitHub integration; agentic environments. |
| https://www.builder.io/blog/cursor-vs-claude-code | 200 | Cursor vs Claude Code agentic coding tools; pair-programming "use both" pattern. |
