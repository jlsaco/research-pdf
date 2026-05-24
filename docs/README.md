# Deep-Research for Technical Slide PDFs — Usage Guide

Turn a technical slide deck (PDF) into a structured, web-researched markdown
deliverable, tailored to a **role**, a **language**, and a **depth**.

## Quick start

1. Drop your PDF into `input/`:

   ```
   input/my-deck.pdf
   ```

2. Run it. Two ways:

   **Interactive** (Claude will ask for any missing params):

   ```
   /deep-research
   ```

   or just ask in natural language:

   ```
   do a deep research on input/my-deck.pdf for a Project Manager, in English, standard depth
   ```

   **Non-interactive** (CLI — pass every param so nothing blocks):

   ```bash
   claude -p "/deep-research input/my-deck.pdf --role \"Project Manager\" --language en --depth standard"
   ```

## Parameters

| Param      | Allowed values                  | Default            | How to pass it |
| ---------- | ------------------------------- | ------------------ | -------------- |
| `role`     | free text (any audience)        | `Project Manager`  | `--role "AI Engineer"`, natural language, or config default |
| `language` | `es` \| `en`                    | `en`               | `--language es`, natural language, or config default |
| `depth`    | `quick` \| `standard` \| `deep` | `standard`         | `--depth deep`, natural language, or config default |

**Resolution order:** explicit flag/arg → config `defaults:` → interactive
question (interactive runs only).

> Non-interactive `claude -p` runs never prompt. Pass all params explicitly, or
> ensure `.claude/research-config.yaml` defaults are set how you want.

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

Edit `.claude/research-config.yaml`:

- **Trusted sources** — under `trusted_sources:`. Add or remove domains the
  researcher prefers. Each entry has `name`, `url`, `tags`, and `priority`
  (`high`|`medium`):

  ```yaml
  trusted_sources:
    - name: "My Internal Wiki"
      url: "https://wiki.example.com"
      tags: ["internal", "api"]
      priority: high
  ```

- **Sections** — under `sections:`. Change the fixed/optional lists or the
  `depth_mapping:` that controls which optional sections appear per depth.

- **Defaults** — under `defaults:` (role/language/depth) and `max_iterations:`
  (reviewer fix-loop cap).

## Good-enough criterion

A run is considered complete when:

- every slide is covered;
- each topic has ≥1 general source plus the required specific sources for the
  depth;
- there are 0 broken links;
- the cited sources actually support the claims; and
- the whole run completes via CLI with no human input.

If these can't all be met within `max_iterations`, the run stops and documents
the remaining gaps.
