---
name: deep-research
description: Run a deep-research pass on a source document — extract sections, group them into topics, research the web (verifying every link), and write per-topic and per-section markdown in the chosen language, role, and depth. Trigger when the user gives a file path in input/ (or elsewhere) and asks to "deep research" / "research this document", or invokes /deep-research.
---

# Deep Research — the orchestrator

This skill is the **conductor**. It does not do the work itself: it hands the
work off to six specialised agents, in order, and waits for each one. Each
agent is an LLM with a written brief (in plain text, like a job description);
it reads the previous artifact, thinks, and writes the next one. The
structure of the workflow lives in the briefs and in the files agents leave
behind for each other, not in fixed code.

The six agents (in order):

1. `source-extractor` — reads the source file and describes every section.
2. `topic-mapper` — clusters the sections into topics.
3. `web-researcher` — researches ONE topic (one is launched per topic, in parallel).
4. `md-author` — writes the final markdown in the chosen language.
5. `research-reviewer` — audits the bundle for coverage and citation quality.
6. `pdf-exporter` — packages the finished bundle into a single local PDF.

## Parameters (always ask)

Never assume values. Confirm all three with **AskUserQuestion** before
starting. If the user already mentioned one in their prompt, offer it as the
recommended option so they can confirm in one click.

- `role` — free text (e.g. "Project Manager", "AI Engineer", "Student").
- `language` — `es` or `en`.
- `depth` — `quick`, `standard`, or `deep`.

## Source input

This version of the system takes **one input: a file path**. The file can be
any type the `source-extractor` knows how to read (PDF slides, PDF article,
markdown, plain text, …). The extractor decides what a "section" means for
that input.

If the user gave a path, use it. Otherwise look in `input/`. If `input/` has
zero or several files, ask which one.

> Extending the system to accept other input types (a URL, a free-text
> topic, a folder, …) is left as an exercise.

## Where outputs go

Compute `<slug>` = the file's base name lowercased with hyphens (e.g.
`My Deck.pdf` → `my-deck`). The whole run lives under `output/<slug>/`:

- `output/<slug>/README.md` — bundle index.
- `output/<slug>/topics/<NN>-<topic-slug>.md` — one file per topic.
- `output/<slug>/sections/section-<NN>.md` — one file per section
  (omit the whole folder when the source has only one section).
- `output/<slug>/.research/` — intermediate artifacts (extraction, topic
  map, findings, review, and `params.json` with the three params + date +
  `source_path`).

## The steps

1. **Ask for the parameters** and save `params.json` under `.research/`.
2. **Extract.** Launch `source-extractor` with the source path and the slug.
   Wait.
3. **Topic map.** Launch `topic-mapper` with the slug. Read the resulting
   map to learn the topic list.
4. **Research.** Launch one `web-researcher` per topic, in parallel
   (cap at ~4 concurrent).
5. **Author.** Launch `md-author` to write every topic, every section, and
   the README — also in parallel where possible.
6. **Review.** Launch `research-reviewer`. If it passes, you're done. If it
   fails, fire targeted fixes (re-research a topic that came up short,
   re-write a file with problems) and review again. **Cap: 3 iterations.**
   If problems remain after the third pass, list them in a "Known gaps"
   section of the README and stop.
7. **Export to PDF.** Once the review passes (or stops at the iteration
   cap with documented gaps), launch `pdf-exporter` with the slug. It
   produces `output/<slug>/research.pdf` — README as cover/index, topics
   in order, sections as an appendix.
8. **Open the PDF.** Run `open output/<slug>/research.pdf` (macOS) so the
   reader sees the deliverable the moment the run ends. If `open` fails or
   isn't available, fall back to printing the path — don't block the
   summary on it.
9. **Summarise.** Print: output folder, topic count, section count, review
   verdict (and iteration count), and the PDF path.

## Depth quick reference

Pass this to `web-researcher` and `md-author` — it defines how many sources
and which sections each topic gets.

| depth      | Sources per topic           | Topic sections                                          |
|------------|-----------------------------|---------------------------------------------------------|
| `quick`    | 1 general + 1 specific      | Fixed sections only, concise                            |
| `standard` | 1 general + 2-3 specific    | Fixed + "Why it matters for <role>" + "Common pitfalls" |
| `deep`     | 1 general + 3-5 specific    | Fixed + ALL optional sections, thorough                 |

Fixed topic sections: Summary / Prerequisite concepts / Deep dive / Sources
/ References. For section files: What this section says / Key concepts /
Linked topics (and "Notes for <role>" at `standard` and `deep`).
