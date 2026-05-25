# Findings — The Six Model Families (model-families-overview)

Topic covers the six major LLM vendors/model families taught in the slides —
Anthropic (Claude), OpenAI (GPT/o-series), Google (Gemini), DeepSeek, Meta
(Llama), and xAI (Grok) — plus the prerequisite concepts: open-weight vs.
closed/proprietary models, reasoning/extended-thinking models, multimodality,
web grounding, and self-hosting/fine-tuning.

Note on dates: searches surfaced aggregator pages naming very recent versions
(e.g., "GPT-5.5", "Gemini 3.x", "Grok 4.x", "Claude Opus 4.7"). For the vendor
profiles below, version-specific and capability claims are tied to first-party
vendor docs wherever possible; the comparison aggregator is used only for the
high-level "who is good at what" framing.

## General source(s)
- [Best AI Models 2026: ChatGPT vs Claude vs Gemini vs Grok vs DeepSeek vs Llama (T-Minus AI)](https://www.tminusai.com/models) — high-level side-by-side comparison of all six families across pricing, context window, speed, coding, and ideal use cases. Good for the "one winner per use case" framing.

## Specific sources
- [Models overview — Claude API Docs (Anthropic)](https://platform.claude.com/docs/en/about-claude/models/overview) — authoritative Anthropic source for the Opus / Sonnet / Haiku tier structure, context windows, vision/multimodal support, and pricing. Covers the Anthropic vendor profile.
- [Extended thinking — Claude API Docs (Anthropic)](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) — authoritative source for the reasoning / extended-thinking prerequisite concept (how step-by-step reasoning works in current models).
- [Models — Gemini API (Google AI for Developers)](https://ai.google.dev/gemini-api/docs/models) — authoritative Google source for the Gemini Pro/Flash/Flash-Lite variants, multimodal inputs (text, image, audio, video, PDF), and grounding tools (Google Search, code execution, URL context). Covers the Google vendor profile + web-grounding + multimodality prerequisites.
- [Practical Guide for Model Selection (OpenAI Cookbook)](https://developers.openai.com/cookbook/examples/partners/model_selection_guide/model_selection_guide) — authoritative OpenAI source distinguishing general-purpose GPT models (GPT-4o/4.1) from o-series reasoning models (o3/o4-mini). Covers the OpenAI vendor profile + reasoning-models prerequisite.
- [DeepSeek-R1 Release — DeepSeek API Docs](https://api-docs.deepseek.com/news/news250120) — first-party DeepSeek source for R1 as an MIT-licensed open-weight reasoning model, distillation/commercial use, and API pricing. Covers the DeepSeek vendor profile + open-weight prerequisite.
- [Llama (language model) — Wikipedia](https://en.wikipedia.org/wiki/Llama_(language_model)) — covers Meta's Llama as a source-available / open-weight family, the contested "open-source" label, the community license, and fine-tuning/self-hosting (e.g., llama.cpp). Covers the Meta vendor profile.
- [The Complete Guide to Grok AI (DataNorth AI)](https://datanorth.ai/blog/the-complete-guide-to-grok-ai) — covers xAI's Grok: maker, reasoning focus, real-time X + web access, and multimodal input (used because xAI's own x.ai and help.x.com pages returned HTTP 403). Covers the xAI vendor profile + web-grounding prerequisite.
- [Open-Source vs Closed-Source AI Models (MindStudio)](https://www.mindstudio.ai/blog/open-source-vs-closed-source-ai-models-agentic-workflows) — clarifies the open-weight vs. closed/proprietary distinction, self-hosting (data privacy, cost, latency), and that closed models can't be fine-tuned by end users. Covers the open-weight vs. closed + self-hosting/fine-tuning prerequisites.

## Key facts
- Claude is organized in three tiers: Opus (most capable, complex reasoning/agentic coding), Sonnet (best balance of speed and intelligence), and Haiku (fastest, near-frontier intelligence). — source: https://platform.claude.com/docs/en/about-claude/models/overview
- All current Claude models support text and image input, text output, multilingual capabilities, and vision; current top models offer a 1M-token context window while Haiku offers 200k tokens. — source: https://platform.claude.com/docs/en/about-claude/models/overview
- Reasoning / extended thinking lets a model produce internal step-by-step `thinking` content before its final answer, improving complex problem solving; budget can be controlled via a token budget. — source: https://platform.claude.com/docs/en/build-with-claude/extended-thinking
- OpenAI splits its lineup into general-purpose GPT models (e.g., GPT-4o for real-time multimodal, GPT-4.1 for long context) and o-series reasoning models (o3, o4-mini) specialized for deep, multi-step logical reasoning and tool use. — source: https://developers.openai.com/cookbook/examples/partners/model_selection_guide/model_selection_guide
- Gemini ships in Pro / Flash / Flash-Lite variants, is natively multimodal (text, image, audio, video, PDF), and supports built-in grounding tools including Google Search, code execution, and URL context. — source: https://ai.google.dev/gemini-api/docs/models
- DeepSeek-R1 is an MIT-licensed open-weight reasoning model with performance on par with OpenAI o1; outputs may be used freely for fine-tuning/distillation, and API pricing is roughly $0.14–$0.55 per million input tokens and $2.19 per million output tokens. — source: https://api-docs.deepseek.com/news/news250120
- Meta's Llama is a source-available / open-weight family (weights downloadable under a community license with an acceptable-use policy); it can be fine-tuned and self-hosted (e.g., via llama.cpp), and its "open-source" label is disputed by the Open Source Initiative. — source: https://en.wikipedia.org/wiki/Llama_(language_model)
- xAI's Grok (founded by Elon Musk, March 2023) emphasizes reasoning plus real-time access to the X platform and the broader web for current-events grounding, and supports multimodal input (text, images, voice). — source: https://datanorth.ai/blog/the-complete-guide-to-grok-ai
- "Open-weight" is more precise than "open-source": open-weight means trained parameters are downloadable/runnable, while true open-source would also include training data and code; closed/proprietary models (Claude, GPT, Gemini) are API-only and cannot be fine-tuned by end users, whereas open-weight models can be self-hosted and fine-tuned. — source: https://www.mindstudio.ai/blog/open-source-vs-closed-source-ai-models-agentic-workflows
- Self-hosting an open-weight model keeps data inside your own infrastructure and can cut per-inference costs significantly at scale, at the cost of running your own GPU infrastructure. — source: https://www.mindstudio.ai/blog/open-source-vs-closed-source-ai-models-agentic-workflows
- At a high level: ChatGPT is the broadest all-purpose choice, Claude leads long-form/technical writing and agentic coding, Gemini suits Google-ecosystem workflows, Grok excels for live X context, DeepSeek is among the cheapest capable models, and Llama is the best-known open-weight option. — source: https://www.tminusai.com/models

## Verification checklist
| URL | HTTP | Supports |
|-----|------|----------|
| https://www.tminusai.com/models | 200 | High-level six-family comparison and per-use-case strengths (fetched + curl). |
| https://platform.claude.com/docs/en/about-claude/models/overview | 200 | Claude Opus/Sonnet/Haiku tiers, context windows, vision/multimodal, pricing (fetched + curl). |
| https://platform.claude.com/docs/en/build-with-claude/extended-thinking | 200 | Reasoning / extended-thinking concept and mechanics (fetched + curl). |
| https://ai.google.dev/gemini-api/docs/models | 200 | Gemini variants, multimodal inputs, grounding tools (fetched + curl). |
| https://developers.openai.com/cookbook/examples/partners/model_selection_guide/model_selection_guide | 200 | GPT vs o-series reasoning-model distinction and selection guidance (fetched + curl). |
| https://api-docs.deepseek.com/news/news250120 | 200 | DeepSeek-R1 MIT open-weight reasoning model, licensing, pricing (fetched + curl). |
| https://en.wikipedia.org/wiki/Llama_(language_model) | 200 | Llama open-weight/source-available status, license, fine-tuning/self-hosting (fetched + curl). |
| https://datanorth.ai/blog/the-complete-guide-to-grok-ai | 200 | xAI Grok maker, real-time X/web access, reasoning, multimodal (fetched + curl). |
| https://www.mindstudio.ai/blog/open-source-vs-closed-source-ai-models-agentic-workflows | 200 | Open-weight vs. closed/proprietary, self-hosting, fine-tuning (fetched + curl). |
