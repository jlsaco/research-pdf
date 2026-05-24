# Review — nexusguilds-week-4-slides

## Checklist results

1. Slide coverage — PASS — All 16 slides (per `.research/extraction.md` and the SLIDE → TOPIC INDEX in `.research/topic-map.md`) have a corresponding `slides/slide-NN.md` file (slide-01 … slide-16, verified present). Every slide is referenced by at least one topic via the topic-map's slide assignments (topics 01–07 collectively cover slides 1–16, with several slides mapped to two topics). Each slide file also contains a "Linked topics" section pointing back to its topic(s). No missing slide files, no unreferenced slides.

2. Source completeness — PASS — All 7 topic files carry ≥1 GENERAL and ≥1 SPECIFIC source:
   - 01-apis-fundamentals: 2 General (MDN, Wikipedia) + 2 Specific (Claude API overview, rate-limits).
   - 02-integration-patterns: 1 General (freeCodeCamp) + 5 Specific (Red Hat webhook, Nordic APIs, OpenAI batch, LangChain streaming, OpenAI function calling).
   - 03-tool-spectrum: 1 General (Nintex) + 5 Specific (Retool, Zapier vs Make, n8n vs Retool, Replit vs Cursor, TechConcepts).
   - 04-automation-anatomy: 1 General (Zapier AI workflows) + 3 Specific (Zapier workflow automation, n8n template, Claude prompting).
   - 05-build-automation-hands-on: 1 General (Zapier AI workflows) + 4 source-specific links (Zapier categorize emails, Make HTTP module, Claude get-started, PandaDoc). Note: only the first is explicitly tagged "General:"; the remaining four are specific in nature but lack an explicit "Specific:" prefix (cosmetic labeling, not a content gap).
   - 06-process-mapping: 2 General (Wikipedia, Asana) + 4 specific (Zapier choose software, Zapier low-code vs no-code, ProcessMaker, Qntrl). Latter four not prefixed "Specific:" but are specific in nature.
   - 07-course-framing-and-orchestration-preview: 1 General (Anthropic Building Effective Agents) + 3 specific (Purple Frog, Zapier orchestration, LangChain agent). Latter three not prefixed "Specific:".

3. Link liveness — PASS (0 broken cited links) — Extracted 40 unique URLs from the bundle and curled each. Every URL cited as a reference/source in the published files (`README.md`, `topics/`, `slides/`) returned 2xx/3xx. Intra-bundle relative links: all 60 relative `.md` links (README → topics/slides, slides/ → ../topics, topics → topics) resolve to existing files — 0 missing targets.
   Non-2xx results, all NON-citation occurrences:
   - `https://api.anthropic.com/v1/messages` → 405 — illustrative cURL command inside a fenced code block in `topics/05-build-automation-hands-on.md` (POST endpoint; GET returns 405; server is live). Not a citation.
   - `https://api.anthropic.com` (backtick-quoted) → 404 — illustrative base URL inside inline code in `topics/01-apis-fundamentals.md` and findings. Not a citation.
   - `https://www.datacamp.com/tutorial/building-langchain-agents-to-automate-tasks-in-python` → 403 — appears only in `.research/findings/course-framing-and-orchestration-preview.md`, explicitly marked "DISCARDED — bot-blocked (403), not cited." Not in the published bundle.
   - `docs.anthropic.com` / `docs.claude.com` URLs → 200 (and only appear in `.research/findings/` working notes; published topics use canonical `platform.claude.com` equivalents which return 200).

4. Sources support claims — PASS — WebFetch spot-checks across 5 topics all confirmed the cited page supports the cited fact:
   - Claude rate-limits page (topic 01): confirms RPM/ITPM/OTPM, token bucket algorithm, and 429 + `retry-after` header.
   - Red Hat webhook (topic 02): confirms webhook as event-driven HTTP push vs. polling ("reverse APIs", server pushes payload to registered URL).
   - Zapier vs Make (topic 03): confirms "9,000+ apps" vs Make "~3,000 integrations", Zapier easiest for non-technical users, Make steeper learning curve / more control.
   - Anthropic Building Effective Agents (topic 07): confirms workflow vs agent definitions verbatim, the five patterns (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer), and the "simplest solution possible" guidance.
   - Purple Frog (topic 07): confirms "a well written prompt does not change how a business operates" and integration-changes-operations distinction.

5. Organization & language — PASS — Files are correctly placed: topics in `topics/` (01–07, kebab-case matching topic-map slugs), slides in `slides/` (slide-01 … slide-16, zero-padded), README.md at bundle root, working notes under `.research/`. All prose and headings are in English (params.json language = "en"). Naming matches the contract.

6. Clarity for role (Project Manager) — PASS — Role tailoring is genuine and consistent, not boilerplate. Topic files use a "Why it matters for a Project Manager" section framing each concept in PM terms (scoping, staffing model, run-cost vs build-cost, maintenance as a hidden line item, the 80/20 rule as anti-over-engineering, batch as a budget lever, tool use as a governance/oversight tier). Slide files use "Notes for a Project Manager" with concrete, slide-specific PM takeaways (e.g., slide-10 treats the agenda as a reusable run-of-show and flags 4.C as the squeeze risk; slide-12 ties the Planner option to backlog grooming; slide-16 frames the date inconsistency as a definition-of-done/QC lesson). Explanations are clear for a non-engineer PM audience.

## Issues to fix
- [ ] `topics/03-tool-spectrum.md` (Summary, line ~5): the link text "[process-mapping](04-automation-anatomy.md)" points to the wrong file — the anchor says "process-mapping" but targets `04-automation-anatomy.md`. It should point to `06-process-mapping.md` (the file exists, so the link is not broken, but the destination is incorrect for the phrase).
- [ ] `topics/04-automation-anatomy.md` ("Why it matters" section, line ~36): the link text "[process-mapping](03-tool-spectrum.md)" points to the wrong file — should point to `06-process-mapping.md`, not `03-tool-spectrum.md`.
- [ ] (Cosmetic, low priority) In `topics/05-build-automation-hands-on.md`, `06-process-mapping.md`, and `07-course-framing-and-orchestration-preview.md`, only the first source line carries an explicit "General:" prefix; the remaining specific sources are not tagged "Specific:". They are specific in nature, so source completeness still passes, but adding the "Specific:" prefix would make the contract labeling consistent with topics 01–04.

## Rubric (1-5)
- Coverage: 5
- Source quality: 5
- Clarity for role: 5
- Organization: 4
- Simplicity: 5

## Verdict
PASS — All three hard gates (slide coverage, source completeness, link liveness with 0 broken cited links) pass; the only substantive issues are two mislabeled intra-bundle link destinations and one cosmetic source-labeling inconsistency.
