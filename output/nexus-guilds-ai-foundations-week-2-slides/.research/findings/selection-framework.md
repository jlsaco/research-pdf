# Findings — The 6-Dimension Selection Framework (selection-framework)

Research done in English (output will be translated to Spanish later).
Role: Student. Depth: standard (1 general + 3+ specific authoritative sources).

## General source(s)
- [How to Choose LLM Models: Balancing Quality, Speed, Price, Latency, and Context Window (Mehmet Ozkaya, Medium)](https://mehmetozkaya.medium.com/how-to-choose-llm-models-balancing-quality-speed-price-latency-and-context-window-c6c2bcf0f296) — High-level intro framing LLM selection as a balance across multiple dimensions (quality, speed, price, latency, context window); good plain-language overview for students. NOTE: page content verified live via WebFetch; a raw `curl` returns 403 (Medium bot-blocking) but the page loads and supports the claim.

## Specific sources
- [Beyond vibes: How to properly select the right LLM for the right task (AWS Machine Learning Blog)](https://aws.amazon.com/blogs/machine-learning/beyond-vibes-how-to-properly-select-the-right-llm-for-the-right-task/) — Covers "defining requirements before evaluation" and benchmarking models on your own task: define criteria first, build a ground-truth dataset, run comparative evals, then decide. Also lists multiple quality dimensions. (Doubles as a strong general/authoritative framework source.)
- [Weighted decision matrix: A tool for pro-level prioritization (airfocus)](https://airfocus.com/blog/weighted-decision-matrix-prioritization/) — Covers the "weighted decision matrix / weighted scoring" prerequisite: options as rows, criteria as columns, weights, scores, weighted totals, pick highest.
- [Decision Matrix Examples: 7 Steps to Build Matrices Fast (Asana)](https://asana.com/resources/decision-matrix-examples) — Reinforces the weighted-scoring method with a clean 7-step process and a worked example (cost weighted higher than communication).
- [Tokens and Context Windows in LLMs (GeeksforGeeks)](https://www.geeksforgeeks.org/artificial-intelligence/tokens-and-context-windows-in-llms/) — Covers the "context window / tokens" prerequisite: token = smallest unit of text; context window = span of tokens the model can consider at once.
- [Key metrics for LLM inference — LLM Inference Handbook (BentoML)](https://bentoml.com/llm/inference-optimization/llm-inference-metrics) — Covers "time-to-first-token vs. total latency": defines TTFT, end-to-end latency (E2EL), TPOT, inter-token latency.

## Key facts
- The selection framework balances multiple dimensions; the general source names five (quality, speed, price, latency, context window), and a 6th dimension typically adds something like "fit/requirements match" or splitting speed vs. latency. — source: https://mehmetozkaya.medium.com/how-to-choose-llm-models-balancing-quality-speed-price-latency-and-context-window-c6c2bcf0f296
- Price is typically measured per million tokens (price per 1M tokens), which lets buyers compare cost across models. — source: https://mehmetozkaya.medium.com/how-to-choose-llm-models-balancing-quality-speed-price-latency-and-context-window-c6c2bcf0f296
- Proper LLM selection means defining evaluation criteria FIRST, building a ground-truth dataset, running comparative evals on the same benchmarks, then deciding from data instead of "vibes." — source: https://aws.amazon.com/blogs/machine-learning/beyond-vibes-how-to-properly-select-the-right-llm-for-the-right-task/
- No single metric captures what makes an LLM response "good"; selection requires balancing dimensions by use-case priority (e.g., accuracy may outweigh cost for critical apps; cost/speed may win for routine tasks). — source: https://aws.amazon.com/blogs/machine-learning/beyond-vibes-how-to-properly-select-the-right-llm-for-the-right-task/
- A weighted decision matrix works by: list options (rows), list criteria (columns), assign each criterion a weight by importance, score each option per criterion, multiply score × weight, sum to a total, and pick the highest total. — source: https://airfocus.com/blog/weighted-decision-matrix-prioritization/
- Weighting ensures more important criteria have more influence on the final choice (e.g., cost weighted higher than communication in the worked example); 5–8 criteria is a practical sweet spot. — source: https://asana.com/resources/decision-matrix-examples
- A token is the basic unit of text a model processes (a word, sub-word, or punctuation); the context window is the span of tokens the model can consider at once when generating. — source: https://www.geeksforgeeks.org/artificial-intelligence/tokens-and-context-windows-in-llms/
- Context windows have grown dramatically (e.g., GPT-3 ~2,048 tokens vs. Llama 3.1 8B ~128,000 tokens), and the window covers input + output combined. — source: https://www.geeksforgeeks.org/artificial-intelligence/tokens-and-context-windows-in-llms/
- Time to First Token (TTFT) = time to produce the first token after a request (how fast it starts responding); End-to-End Latency (E2EL) = time from request to the final token. Total latency ≈ TTFT + generation time. — source: https://bentoml.com/llm/inference-optimization/llm-inference-metrics
- TTFT drives perceived responsiveness while time-per-output-token (TPOT) drives perceived speed; two systems with identical total latency can feel very different depending on when output starts. — source: https://bentoml.com/llm/inference-optimization/llm-inference-metrics

## Verification checklist
| URL | HTTP | Supports |
|-----|------|----------|
| https://mehmetozkaya.medium.com/how-to-choose-llm-models-balancing-quality-speed-price-latency-and-context-window-c6c2bcf0f296 | 403 curl / loaded+verified via WebFetch | General overview of selecting LLMs across quality/speed/price/latency/context; price per 1M tokens |
| https://aws.amazon.com/blogs/machine-learning/beyond-vibes-how-to-properly-select-the-right-llm-for-the-right-task/ | 200 | Define requirements/criteria first, build ground truth, run task-specific comparative evals; multi-dimension scoring |
| https://airfocus.com/blog/weighted-decision-matrix-prioritization/ | 200 | Weighted decision matrix mechanics (options, criteria, weights, scores, weighted total) |
| https://asana.com/resources/decision-matrix-examples | 200 | 7-step weighted scoring method with worked example; criteria-count guidance |
| https://www.geeksforgeeks.org/artificial-intelligence/tokens-and-context-windows-in-llms/ | 200 | Definitions of tokens and context window; context-window size examples |
| https://bentoml.com/llm/inference-optimization/llm-inference-metrics | 200 | TTFT vs end-to-end latency definitions; TPOT/inter-token latency; UX impact |
