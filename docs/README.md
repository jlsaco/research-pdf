# Deep-Research for Technical Slide PDFs — Usage Guide

Turn a technical slide deck (PDF) into a structured, web-researched markdown
deliverable, tailored to a **role**, a **language**, and a **depth**.

## Quick start

1. Drop your PDF into `input/`:

   ```
   input/my-deck.pdf
   ```

2. Run it — the run is **always interactive**, so just start it:

   ```
   /deep-research
   ```

   or ask in natural language:

   ```
   do a deep research on input/my-deck.pdf for a Project Manager, in English, standard depth
   ```

### Running under OpenCode

This repo also runs under [OpenCode](https://opencode.ai) from the same source.
The orchestrator is exposed as the `/deep-research` command and the five
subagents live under `.opencode/`. Run it interactively the same way:

```bash
opencode
# then: /deep-research
```

Because every run is interactive (the orchestrator must ask the human to
confirm params), use the interactive mode — `opencode run "…"` would skip the
confirmation prompts.

> `.opencode/` is **generated** from `.claude/` — never edit it by hand. After a
> fresh clone, enable the auto-sync hook once: `git config core.hooksPath .githooks`.
> See [ADR 0008](adr/0008-dual-runtime-claude-and-opencode.md) for the
> dual-runtime design and [ADR 0009](adr/0009-always-interactive-no-config.md)
> for the always-interactive decision.


## Parameters

| Param      | Allowed values                  | How it's set |
| ---------- | ------------------------------- | ------------ |
| `role`     | free text (any audience)        | asked interactively |
| `language` | `es` \| `en`                    | asked interactively |
| `depth`    | `quick` \| `standard` \| `deep` | asked interactively |

**The orchestrator always asks you to confirm all three** before it starts —
there are no config defaults. If you already named a value in your prompt (e.g.
"…for a Project Manager in English"), it's offered as the recommended option so
confirming is one click.

### What each depth produces

- **quick** — fixed sections only; 1 general + 1 specific source per topic.
- **standard** — fixed + "Why it matters for &lt;role&gt;" + "Common pitfalls";
  1 general + 2–3 specific sources.
- **deep** — all optional sections; 1 general + 3–5 specific sources.

## Where output appears

```
output/<slug>/                  # slug = your PDF name, lowercased + hyphenated
  README.md                     # overview & index of topics/slides
  topics/<NN>-<slug>.md         # one researched topic per file
  slides/slide-<NN>.md          # one file per slide
  .research/                    # intermediate artifacts (extraction, topic map, notes)
```

Example: `input/My Deck.pdf` → `output/my-deck/`.

**Topic file sections:** Summary, Prerequisite concepts, Deep dive, Sources,
References (fixed) — plus optional sections per depth (Why it matters for
&lt;role&gt;, Hands-on, Common pitfalls, Going deeper, Glossary, Related slides &
topics).

**Slide file sections:** What this slide says, Key concepts, Linked topics
(fixed) — plus optional "Notes for &lt;role&gt;".

## Customizing: trusted sources & sections

There is no config file — settings live inline next to the agent that uses them:

- **Trusted sources** — the domain table in `.claude/agents/web-researcher.md`
  (columns: source, URL, good-for tags, priority). Add or remove rows there.
- **Sections** — the fixed/optional section schema in
  `.claude/agents/md-author.md`, and the Depth reference in
  `.claude/skills/deep-research/SKILL.md` (which optional sections each depth
  includes).
- **Fix-loop cap** — `3 iterations`, in the orchestrator's STEP 6.

## Good-enough criterion

A run is considered complete when:

- every slide is covered;
- each topic has ≥1 general source plus the required specific sources for the
  depth;
- there are 0 broken links; and
- the cited sources actually support the claims.

If these can't all be met within the **3-iteration** fix-loop cap, the run stops
and documents the remaining gaps.
