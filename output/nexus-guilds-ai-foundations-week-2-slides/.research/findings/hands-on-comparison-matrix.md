# Findings — Hands-On: Model Comparison & Selection Matrix (hands-on-comparison-matrix)

## General source(s)
- [LLM-as-a-judge: a complete guide to using LLMs for evaluations (Evidently AI)](https://www.evidentlyai.com/llm-guide/llm-as-a-judge) — High-level guide to comparing model outputs: pairwise/side-by-side comparison, criteria-based scoring, rubric design, and how to validate the comparison process. Good overview for the whole "compare and select" workflow.

## Specific sources
- [How to Write an LLM Evaluation Rubric (Twine)](https://www.twine.net/blog/how-to-write-an-llm-evaluation-rubric/) — Covers **rubric-based output evaluation** and **mapping task categories to ranked dimensions**: rubric components (dimension, success definition, scoring scale, observable evidence), separating independent quality dimensions, and choosing scoring scales per decision type.
- [LLM Rubric (Promptfoo docs)](https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/llm-rubric/) — Concrete, tool-level example of **rubric-based output evaluation**: defining natural-language criteria, returning a numeric score (0.0–1.0) with reason/pass, thresholds, and using different judge models. Useful for the hands-on scoring mechanics.
- [Model fallbacks: Your safety net for production AI (Mastra)](https://mastra.ai/blog/model-fallback) — Covers **primary vs. fallback model selection**: try the primary first, auto-switch to a secondary model on error/timeout/rate-limit, per-model retry configs, and transparent failover for users.
- [Decision Matrix Examples: 7 Steps to Build Matrices Fast (Asana)](https://asana.com/resources/decision-matrix-examples) — Covers **building the selection/comparison matrix itself** and **justification of decisions**: list options, define criteria, assign weights, score each option, compute weighted totals, pick the highest. Directly maps to a model-selection matrix template.

## Key facts
- A weighted decision matrix is built in ~7 steps: identify alternatives, identify criteria, build the grid, fill in scores (e.g. a 1–3 scale when variation is small), add weights, multiply weight × score, and total to find the winner. — source: https://asana.com/resources/decision-matrix-examples
- Criteria should be relevant, measurable, and consolidated to a small set (commonly 4–8); options are listed in rows and ranked dimensions/criteria in columns. — source: https://asana.com/resources/decision-matrix-examples
- A strong evaluation rubric specifies the evaluation dimension, a clear definition of success, a scoring scale, and observable evidence for each score level; separate independent categories (e.g. task completion, accuracy/grounding, completeness, safety, communication style) instead of one blended score. — source: https://www.twine.net/blog/how-to-write-an-llm-evaluation-rubric/
- Scoring scales should match the decision: pass/fail for strict requirements, 3-point for operational decisions, 5-point for tracking gradual improvement; distinguish hard gates from quality preferences. — source: https://www.twine.net/blog/how-to-write-an-llm-evaluation-rubric/
- Pairwise / side-by-side comparison (showing a judge two responses to the same prompt and picking the better one) can reach >80% agreement with human preferences and is useful for selecting better models or prompts during development. — source: https://www.evidentlyai.com/llm-guide/llm-as-a-judge
- Best practice for rubric scoring: evaluate one criterion at a time, clarify the meaning of each score with explicit definitions, use binary/limited-option scales for consistency, and validate the judge against a manually labeled dataset. — source: https://www.evidentlyai.com/llm-guide/llm-as-a-judge
- A practical rubric assertion (Promptfoo `llm-rubric`) takes a natural-language criterion and returns a JSON with a numeric score (0.0–1.0), a reason, and a pass/fail; a result passes only if it meets a configured threshold. — source: https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/llm-rubric/
- Primary/fallback model strategy: try the primary model first; on a 500 error, rate limit, or timeout, automatically switch to the first fallback, with each model getting its own retry count and failover staying transparent to users. — source: https://mastra.ai/blog/model-fallback

## Verification checklist
| URL | HTTP | Supports |
|-----|------|----------|
| https://www.evidentlyai.com/llm-guide/llm-as-a-judge | 200 | General overview: side-by-side comparison + rubric/criteria-based evaluation of model outputs. |
| https://www.twine.net/blog/how-to-write-an-llm-evaluation-rubric/ | 200 | Rubric-based output evaluation; mapping tasks to ranked, independent dimensions; scoring scales. |
| https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/llm-rubric/ | 200 | Hands-on rubric scoring mechanics: criteria, 0–1 score, pass/threshold. |
| https://mastra.ai/blog/model-fallback | 200 | Primary vs. fallback model selection for production workflows. |
| https://asana.com/resources/decision-matrix-examples | 200 | Building the weighted comparison/selection matrix: criteria, weights, scoring, totals, decision. |
