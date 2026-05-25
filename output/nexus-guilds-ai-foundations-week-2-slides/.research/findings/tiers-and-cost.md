# Findings — Model Tiers, Pricing & the Cost Iceberg (tiers-and-cost)

Research done in English (output will be translated to Spanish later).
Depth = standard: 1 general source + 3+ specific authoritative sources. 7 sources verified live.

## General source(s)
- [LLM API Pricing Comparison In 2026: Every Major Model, Ranked By Cost (CloudZero)](https://www.cloudzero.com/blog/llm-api-pricing-comparison/) — Broad, high-level overview of the LLM pricing landscape in 2026: input vs. output token pricing, the full price range across budget-to-frontier models, and the "cheapest per token isn't cheapest per task" idea (the cost iceberg).

## Specific sources
- [Pricing — Anthropic/Claude Docs (high-priority trusted source)](https://platform.claude.com/docs/en/about-claude/pricing) — Authoritative first-party pricing showing the flagship/balanced/lightweight tiers (Opus/Sonnet/Haiku), separate input vs. output token rates per million tokens, prompt caching and batch discounts, and an explicit "use the right model for the task" cost-optimization note. Covers: flagship vs. balanced vs. lightweight tiers; input vs. output token pricing.
- [AI Cost Controls: Budgets, Throttling & Model Tiering (Clarifai)](https://www.clarifai.com/blog/ai-cost-controls) — Model tiering strategy with economy/mid/premium tiers and per-tier price bands, plus budgets and throttling. Covers: model tiering for cost reduction; flagship vs. balanced vs. lightweight tiers.
- [LLM routing: overview, strategies, and tools (Merge.dev)](https://www.merge.dev/blog/llm-routing) — Defines LLM routing, routing simple tasks to cheaper models, and the trade-offs/savings. Covers: model routing for cost reduction.
- [LLM Total Cost of Ownership 2025: Build vs Buy Math (Ptolemay)](https://www.ptolemay.com/post/llm-total-cost-of-ownership) — GPU infrastructure costs, MLOps staffing, integration/maintenance burden, and build-vs-buy break-even thresholds. Covers: GPU infrastructure costs; integration/maintenance cost; total cost of ownership (TCO).
- [Avoid LLM Vendor Lock-in: A Guide To Portability (CustomGPT)](https://customgpt.ai/how-to-avoid-llm-vendor-lock-in/) — Six switching-cost breakpoints (prompt rewrites, tool-calling differences, API coupling, embedding lock-in, operational dependencies, behavior drift) and portability strategies. Covers: vendor lock-in / switching costs; prompt portability.

## Key facts
- Output tokens cost 2x to 6x more than input tokens because generation demands more compute than comprehension. — source: https://www.cloudzero.com/blog/llm-api-pricing-comparison/
- 2026 LLM API pricing spans from ~$0.10 per million input tokens for budget models (e.g., GPT-4.1 Nano) to ~$30 per million input tokens for frontier reasoning models (e.g., GPT-5.4 Pro). — source: https://www.cloudzero.com/blog/llm-api-pricing-comparison/
- The cheapest model per token is not the cheapest model per task; real cost depends on retries and prompt overhead (system instructions often consume 35–50% of input tokens). This is the "cost iceberg." — source: https://www.cloudzero.com/blog/llm-api-pricing-comparison/
- Claude's tiers (first-party rates, per million tokens, MTok): flagship Opus 4.5/4.6/4.7 = $5 input / $25 output; balanced Sonnet 4.5/4.6 = $3 input / $15 output; lightweight Haiku 4.5 = $1 input / $5 output. — source: https://platform.claude.com/docs/en/about-claude/pricing
- Anthropic's own cost guidance: use Haiku for simple tasks, Sonnet for most production workloads, and Opus for the most complex reasoning; plus prompt caching, batch operations, and usage monitoring. — source: https://platform.claude.com/docs/en/about-claude/pricing
- Prompt caching cuts repeated-context cost dramatically (a cache hit costs 10% of standard input price); the Batch API gives a 50% discount on both input and output tokens. — source: https://platform.claude.com/docs/en/about-claude/pricing
- Model tiering routes by complexity across an economy tier ($0.25–$4/M), mid-tier ($3–$15/M), and premium tier ($15–$75/M); intelligent routing has produced 30–70% cost reductions while maintaining quality. — source: https://www.clarifai.com/blog/ai-cost-controls
- LLM routing is logic that picks a model per request by task type, quality, cost, latency, safety, and availability — routing simple tasks to cheaper models and reserving premium models for prompts that need them. It can backfire on tasks needing deep reasoning or via frequent fallbacks. — source: https://www.merge.dev/blog/llm-routing
- Self-hosting a 7B model on H100 spot instances can cost ~$0.013 per 1K tokens, but the advantage disappears if GPU utilization drops below ~70%. — source: https://www.ptolemay.com/post/llm-total-cost-of-ownership
- Hidden TCO of self-hosting includes MLOps staffing (~1 mid-level engineer per 4–6 GPUs), 10–15% redundancy overhead, and compliance/audit costs; below ~$50k/yr API spend favors a cheap hosted model, above ~$500k/yr self-hosting almost always wins on cost. — source: https://www.ptolemay.com/post/llm-total-cost-of-ownership
- LLM vendor lock-in is more severe than typical SaaS lock-in: switching a provider requires rewriting prompts, tools, retrieval, and operations because business logic is encoded in model-specific prompts and behaviors. — source: https://customgpt.ai/how-to-avoid-llm-vendor-lock-in/
- Six switching-cost breakpoints: prompt rewrites, tool-calling/JSON differences, API/SDK coupling, embedding re-indexing, operational dependencies, and behavior drift; portability is mitigated by centralizing model selection, a stable agent blueprint, portable retrieval, verification tests, and staged rollouts with fallback. — source: https://customgpt.ai/how-to-avoid-llm-vendor-lock-in/

## Verification checklist
| URL | HTTP | Supports |
|-----|------|----------|
| https://www.cloudzero.com/blog/llm-api-pricing-comparison/ | 200 | General overview: input vs output pricing, 2026 price range, cost-iceberg ("cheapest per token ≠ cheapest per task"). |
| https://platform.claude.com/docs/en/about-claude/pricing | 200 | First-party tier pricing (Opus/Sonnet/Haiku = flagship/balanced/lightweight), input vs output rates, caching/batch discounts, model-choice cost guidance. |
| https://www.clarifai.com/blog/ai-cost-controls | 200 | Model tiering (economy/mid/premium tiers + price bands), routing-based 30–70% cost reduction, budgets/throttling. |
| https://www.merge.dev/blog/llm-routing | 200 | LLM routing definition, routing simple tasks to cheaper models, savings and trade-offs. |
| https://www.ptolemay.com/post/llm-total-cost-of-ownership | 200 | TCO: GPU infra cost, MLOps staffing/maintenance, build-vs-buy break-even thresholds. |
| https://customgpt.ai/how-to-avoid-llm-vendor-lock-in/ | 200 | Vendor lock-in switching costs, prompt portability, six breakpoints + mitigation strategies. |
| https://docs.claude.com/en/docs/about-claude/pricing | 200 | Redirect (302) to platform.claude.com pricing; final destination verified live and used as the canonical Claude pricing source. |
