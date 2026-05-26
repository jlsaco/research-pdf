---
name: deep-research
description: Run a deep-research pass on a slide PDF — extract slides, group them into topics, research the web (verifying every link), and write per-topic and per-slide markdown in the chosen language, role, and depth. Trigger when the user drops a PDF in input/ and asks to "deep research" / "research this document", or invokes /deep-research.
---

# Deep Research — the orchestrator

This skill is the **conductor**. It does not do the work itself: it hands the
work off to five specialised agents, in order, and waits for each one. Each
agent is an LLM with a written brief (in plain text, like a job description);
it reads the previous artifact, thinks, and writes the next one. The
structure of the workflow lives in the briefs and in the files agents leave
behind for each other, not in fixed code.

The five agents (in order):

1. `slide-extractor` — reads the PDF and describes every slide.
2. `topic-mapper` — clusters the slides into topics.
3. `web-researcher` — researches ONE topic (one is launched per topic, in parallel).
4. `md-author` — writes the final markdown in the chosen language.
5. `research-reviewer` — audits the bundle for coverage and citation quality.

## Parameters (always ask)

Never assume values. Confirm all three with **AskUserQuestion** before
starting. If the user already mentioned one in their prompt, offer it as the
recommended option so they can confirm in one click.

- `role` — free text (e.g. "Project Manager", "AI Engineer", "Student").
- `language` — `es` or `en`.
- `depth` — `quick`, `standard`, or `deep`.

About the PDF: if the user gave a path, use it. Otherwise look in `input/`.
If there are zero or several PDFs, ask which one.

## Where outputs go

Compute `<slug>` = the PDF name lowercased with hyphens (e.g.
`My Deck.pdf` → `my-deck`). The whole run lives under `output/<slug>/`:

- `output/<slug>/README.md` — bundle index.
- `output/<slug>/topics/<NN>-<topic-slug>.md` — one file per topic.
- `output/<slug>/slides/slide-<NN>.md` — one file per slide.
- `output/<slug>/.research/` — intermediate artifacts (extraction, topic map,
  findings, review, and `params.json` with the three params + date + pdf_path).

## The steps

1. **Ask for the parameters** and save `params.json` under `.research/`.
2. **Extract.** Launch `slide-extractor` with the PDF path and the slug. Wait.
3. **Topic map.** Launch `topic-mapper` with the slug. Read the resulting
   map to learn the topic list.
4. **Research.** Launch one `web-researcher` per topic, in parallel
   (cap at ~4 concurrent).
5. **Author.** Launch `md-author` to write every topic, every slide, and the
   README — also in parallel where possible.
6. **Review.** Launch `research-reviewer`. If it passes, you're done. If it
   fails, fire targeted fixes (re-research a topic that came up short,
   re-write a file with problems) and review again. **Cap: 3 iterations.**
   If problems remain after the third pass, list them in a "Known gaps"
   section of the README and stop.
7. **Summarise.** Print: output folder, topic count, slide count, review
   verdict (and iteration count).

## Depth quick reference

Pass this to `web-researcher` and `md-author` — it defines how many sources
and which sections each topic gets.

| depth      | Sources per topic           | Topic sections                                        |
|------------|-----------------------------|-------------------------------------------------------|
| `quick`    | 1 general + 1 specific      | Fixed sections only, concise                          |
| `standard` | 1 general + 2-3 specific    | Fixed + "Why it matters for <role>" + "Common pitfalls" |
| `deep`     | 1 general + 3-5 specific    | Fixed + ALL optional sections, thorough               |

Fixed topic sections: Summary / Prerequisite concepts / Deep dive / Sources /
References. For slides: What this slide says / Key concepts / Linked topics
(and "Notes for <role>" at `standard` and `deep`).
