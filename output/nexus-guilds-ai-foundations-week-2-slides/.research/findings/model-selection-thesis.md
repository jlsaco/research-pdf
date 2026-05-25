# Findings — Why No Single Model Wins (model-selection-thesis)

## General source(s)
- [The best large language models (LLMs) in 2026 — Zapier](https://zapier.com/blog/best-llm/) — General/introductory overview of frontier LLMs that explicitly frames "best" as task-dependent rather than a single winner; good for LLM basics and what differentiates frontier models. (Trusted source: Zapier.)

## Specific sources
- [LLM providers offer a trade-off between accuracy and speed — Epoch AI](https://epoch.ai/data-insights/llm-apis-accuracy-runtime-tradeoff) — Covers the optimization trade-off subtopic (quality vs. speed/cost) with concrete measurements of the accuracy-vs-runtime frontier.
- [Multi-LLM routing strategies for generative AI applications on AWS — AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/) — Covers task-fit vs. absolute "best" and the enterprise multi-model strategy subtopic: why companies route across several models for cost, task specialization, and latency.
- [Line Goes Up? Inherent Limitations of Benchmarks for Evaluating Large Language Models — arXiv (Fodor, 2025)](https://arxiv.org/html/2502.14318v1) — Covers the "benchmark limitations / why absolute rankings mislead" subtopic, supporting the task-fit-over-leaderboard thesis.
- [LLM Benchmarks Explained: Significance, Metrics & Challenges — Orq.ai](https://orq.ai/blog/llm-benchmarks) — Accessible explainer on what benchmarks are, their metrics, and their limitations; bridges LLM basics with why benchmark "winners" don't guarantee real-world task fit.

## Key facts
- "Best" is not a single winner — it is the model that hits your quality bar at the latency and cost your workflow can tolerate; rankings should be taken "with a grain of salt." — source: https://zapier.com/blog/best-llm/
- Cutting an LLM's error rate in half typically slows the model by roughly 2x to 6x depending on the task (e.g., GPQA Diamond ~6.0x, OTIS Mock AIME ~2.8x, MATH Level 5 ~1.7x), showing quality and speed are in direct tension. — source: https://epoch.ai/data-insights/llm-apis-accuracy-runtime-tradeoff
- Frontier (efficiency-optimal) models often carry "turbo/flash/mini/nano" labels, evidence that vendors ship multiple points on the speed–quality curve rather than one universally optimal model. — source: https://epoch.ai/data-insights/llm-apis-accuracy-runtime-tradeoff
- Enterprises adopt multi-model strategies because no single model optimally addresses all requirements; routing simple queries to cheap/fast models (e.g., Claude 3 Haiku) and hard ones to stronger models (e.g., Claude 3.5 Sonnet) maximizes quality while controlling cost. — source: https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/
- Routing scenarios include differing task types, varying complexity, multiple domains, and tiered SaaS offerings; semantic routing can classify in ~0.1s vs ~0.6s for LLM-assisted routing, reducing latency. — source: https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/
- Benchmark scores are an unreliable indicator of general capability: benchmarks leak into training data (Goodhart's law / contamination), and few provide evidence that high scores predict real-world task performance. — source: https://arxiv.org/html/2502.14318v1
- Models can drop up to ~70% in performance when tasks add irrelevant information or are minorly reformatted, indicating reliance on superficial patterns rather than robust reasoning — so a leaderboard "winner" may not win on your task. — source: https://arxiv.org/html/2502.14318v1
- Key benchmark limitations are data contamination, narrow task focus (limited real-world applicability), and benchmark saturation, which together undermine using a single benchmark to crown a "best" model. — source: https://orq.ai/blog/llm-benchmarks

## Verification checklist
| URL | HTTP | Supports |
|-----|------|----------|
| https://zapier.com/blog/best-llm/ | 200 | General LLM overview; "best" is task-dependent, not a single winner. |
| https://epoch.ai/data-insights/llm-apis-accuracy-runtime-tradeoff | 200 | Quantified accuracy-vs-speed trade-off (2x–6x slowdown to halve errors). |
| https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/ | 200 | Enterprise multi-model/routing rationale: cost, task-fit, latency. |
| https://arxiv.org/html/2502.14318v1 | 200 | Inherent benchmark limitations; high scores ≠ real-world capability. |
| https://orq.ai/blog/llm-benchmarks | 200 | What benchmarks are, metrics, and their limitations (contamination, narrow focus, saturation). |
