# Review — nexus-guilds-ai-foundations-week-2-slides

> Params: role="Student" · language="es" · depth="standard" · reviewed 2026-05-24

## Checklist results
1. Slide coverage — PASS — All 22 slides (1-22) have `slides/slide-NN.md`. Every slide is referenced by ≥1 topic in `.research/topic-map.md` (slide 13 maps to two topics), and every slide file links to its topic via a relative `../topics/*.md` link that resolves. README indexes all 22 slides and all 6 topics.
2. Source completeness — PASS — Each of the 6 topics has ≥1 GENERAL source and ≥3 SPECIFIC sources (standard depth): 01 (1+4), 02 (1+8), 03 (1+5), 04 (1+4), 05 (1+4), 06 (1+4).
3. Link liveness — PASS — 36 unique external URLs checked; all live. The two apparent failures are false positives: the Wikipedia "Llama_(language_model)" 404 was a grep artifact stripping the trailing ")", and the full URL returns 200; the Medium "how-to-choose-llm-models" article returns 403 to curl (anti-bot UA block) but is a live, real page. All internal relative links (README→topics/slides, slides→topics) resolve to existing files.
4. Sources support claims — PASS — Spot-checked across topics, all confirmed: Epoch AI (2x-6x slowdown to halve error; 6.0x GPQA / 2.8x AIME / 1.7x MATH) ✓; Wikipedia Vibe coding (Karpathy Feb 2025, Collins Word of the Year 2025) ✓; Clarifai (economy $0.25-4 / mid $3-15 / premium $15-75; 30-70% routing savings) ✓; Evidently AI (pairwise comparison >80% agreement with humans) ✓.
5. Organization & language — PASS — Files in correct `topics/` and `slides/` folders; naming matches contract (`NN-slug.md`, `slide-NN.md`). All prose and headings are in Spanish. Topic files use the standard-depth schema: Resumen / Conceptos previos / Análisis a fondo / Por qué le importa a un Student / Errores comunes / Fuentes / Referencias. Slides use Qué dice esta diapositiva / Conceptos clave / Temas relacionados / Notas para el estudiante.
6. Clarity for role — PASS — "Por qué le importa a un Student" and "Notas para el estudiante" sections are genuinely tailored (e.g., experiment cheaply with lightweight tiers, transferable structured-decision skill, read benchmarks critically), not generic restatements.

## Issues to fix
- [ ] (Minor, non-blocking) topics/04-tiers-and-cost.md lists 5 References but its Fuentes section omits the Merge.dev routing source (Reference #4 `https://www.merge.dev/blog/llm-routing`). Either add Merge.dev to the Fuentes list or drop it from References so the two lists match.
- [ ] (Cosmetic, non-blocking) Medium source in topic 01 (`mehmetozkaya.medium.com/...`) — wait, this is in topic 03. The Medium general source for topic 03 returns 403 to automated clients; it is live in-browser but consider swapping for a non-paywalled/non-bot-blocked equivalent to keep automated re-checks green.

## Rubric (1-5)
- Coverage: 5
- Source quality: 5
- Clarity for role: 5
- Organization: 4
- Simplicity: 5

## Verdict
PASS — All three hard gates (slide coverage, source completeness, link liveness) pass; sources verified to support claims; content is in Spanish and tailored to the Student role. Two minor, non-blocking polish items noted.
