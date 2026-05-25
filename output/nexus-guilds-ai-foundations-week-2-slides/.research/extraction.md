# Extraction — nexus-guilds-ai-foundations-week-2-slides

## GLOBAL CONTEXT
- **What the deck is about:** Week 2 of the Nexus Guilds "AI Foundational — From Professional to AI Engineer" course. It teaches the landscape of major AI model families (Claude, GPT, Gemini, DeepSeek, Llama, Grok) and a repeatable 6-dimension framework for selecting the right model for a given task, culminating in building a personal "AI Tool Selection Matrix."
- **Intended audience:** Working professionals transitioning toward AI-engineer skills — non-deep-technical learners who use AI tools at work and need to make defensible model-selection decisions. Structured as pre-reading plus a hands-on in-class cohort session.
- **Narrative arc:** Opens with a workplace scenario (Andrés must justify three AI subscriptions to a CFO and produce a selection matrix). Part 1 (pre-reading) explains why no single model wins, profiles six model families, introduces a 6-dimension selection framework, and covers model tiers and hidden costs. Part 2 (in-class) reviews the concepts and runs two practical exercises — comparing models head-to-head and building/peer-validating a Selection Matrix — then debriefs and previews Week 3 (AI-assisted development).
- **Total slides:** 22

## SLIDES

### Slide 1 — Title: AI Foundational, Week 2
- **Key text (verbatim-ish):** "NEXUS GUILDS / AI Foundational / From Professional to AI Engineer / Week 2: The Landscape — AI Models & Selection / Yvan Callaou - Mauricio Betancur - Gabriel Cepeda / Pre-Reading: ~1.5 Hours | In-Class Session: 2 Hours / Version 1.0 • March 2026"
- **Visuals:** Dark teal/navy cover slide with subtle grid background. Large white title, teal section/eyebrow text, a short horizontal accent rule above the week details.
- **Concept taught:** Sets the course, week, and topic — selecting among AI models.

### Slide 2 — Andrés's New Challenge (The Three-Tool Problem)
- **Key text (verbatim-ish):** "The Three-Tool Problem — Marketing loves ChatGPT's creativity. Engineering trusts Claude for code reviews. Legal prefers Gemini's citations and its massive context window for contract analysis. The CFO walks in and asks: 'Why do we need three AI subscriptions? Can't we just pick one?' Andrés knows the answer is not that simple. He needs a framework — a clear, defensible way to recommend the right model for the right task. His boss wants an AI Tool Selection Matrix by Friday. This week, you build that matrix alongside Andrés." Red callout: "Bring your Prompt Playbook from Week 1. Prepare at least 3 CRFT prompts: one creative, one code, one analytical."
- **Visuals:** White content card with a person/professional icon, italic emphasis line below the card, and a red-bordered warning/prep callout box with a warning triangle icon at the bottom.
- **Concept taught:** Real-world framing — different teams favor different models for good reasons, so model selection needs a defensible framework.

### Slide 3 — Week 2 Overview
- **Key text (verbatim-ish):** "Part 1: Pre-Reading (~1.5h): Why No Single Model Wins; The Six Model Families; 6-Dimension Selection Framework; Model Tiers & Pricing. Part 2: In-Class Session (2h): The Three-Tool Problem opening; Model families & framework review; Exercise 2.A: Model Comparison; Exercise 2.B: Build your Selection Matrix; Peer validation & debrief. 75% Practical"
- **Visuals:** Two side-by-side cards — left (teal header, book icon) for pre-reading, right (dark header, tools icon) for in-class. Bulleted lists in each; "75% Practical" badge in teal at bottom-right of the in-class card.
- **Concept taught:** Roadmap of the week split into pre-reading theory and a practice-heavy in-class session.

### Slide 4 — Part 1 Divider: Pre-Reading — The AI Model Landscape
- **Key text (verbatim-ish):** "PART 1 / Pre-Reading: The AI Model Landscape / Complete before your in-class session | Estimated time: ~1.5 hours"
- **Visuals:** Full-bleed teal section divider with large white underlined title and an eyebrow "PART 1" label.
- **Concept taught:** Section break marking the start of the self-study pre-reading.

### Slide 5 — Why No Single Model Wins (The Restaurant Analogy)
- **Key text (verbatim-ish):** "Reading 1 | ~20 minutes. The Restaurant Analogy: You wouldn't ask 'What is the best restaurant?' without context. Best for a romantic dinner? A quick lunch? A group of 20? On a budget? AI model selection works the same way. The 'best' model depends on what you are optimising for: quality, speed, cost, context size, specialisation, or ecosystem. The right question is never 'Which model is best?' — it is always 'Which model is best for this specific task, with these constraints?' The six model families you need to know: Claude, GPT, Gemini, DeepSeek, Llama, Grok."
- **Visuals:** White card with a fork-and-knife icon for the restaurant analogy; a teal banner with the reframed "right question"; six colored pills/buttons across the bottom (Claude=orange, GPT=green, Gemini=blue, DeepSeek=purple, Llama=orange, Grok=red).
- **Concept taught:** Core thesis — "best model" is meaningless without task context and optimization criteria.

### Slide 6 — The Six Model Families
- **Key text (verbatim-ish):** "Reading 2 | ~40 minutes. Claude (Anthropic): Code, analysis, 200K context, extended thinking. GPT (OpenAI): Creative writing, multimodal, ecosystem breadth, plugins. Gemini (Google): 1M+ context, web grounding, multimodal (text/image/video). DeepSeek (Chinese AI Lab): Cost-effective, open-weight, strong code & maths. Llama (Meta): Open-source, fine-tuning, on-premise, community. Grok (xAI): Real-time data, reasoning, less filtered responses. Each family has distinct strengths. No single model dominates all categories."
- **Visuals:** 2x3 grid of white cards, each with a colored top border and a brand-style icon (Claude=brain/orange, GPT=robot/green, Gemini=globe/blue, DeepSeek=stacked-server/purple, Llama=code-brackets/orange, Grok=lightning/red). Vendor name in subtitle, strengths in body. Italic summary line at bottom.
- **Concept taught:** Overview of the six major model families, their makers, and signature strengths.

### Slide 7 — Claude (Anthropic)
- **Key text (verbatim-ish):** "Opus 4.5 | Sonnet 4 | Haiku 3.5. Where Claude Excels: Long document analysis (200K+ token context); Code generation and review; Structured analytical tasks; Extended thinking for complex reasoning. The Tiering System: Opus — Most capable, highest cost; Sonnet — Workhorse (most tasks); Haiku — Fastest, cheapest. When to Reach for Claude: 150-page contract to analyse. Code review of a multi-file project. Step-by-step complex business decisions. Structured, precise outputs with minimal hallucination."
- **Visuals:** Orange top accent bar. Left bulleted "Where Claude Excels" list; right white card "The Tiering System" (Opus/Sonnet/Haiku); bottom teal "When to Reach for Claude" panel with a lightbulb icon.
- **Concept taught:** Claude's strengths, its Opus/Sonnet/Haiku tier system, and when to choose it.

### Slide 8 — GPT (OpenAI)
- **Key text (verbatim-ish):** "GPT-4o | o3 | o4-mini. Where GPT Excels: Creative writing and brainstorming; Multimodal tasks (images + text); Function calling (invoke external tools); Broadest plugin/integration ecosystem. Reasoning Models: o3 and o4-mini 'think through' problems before responding. Strong at maths, science, and coding. Trade-off: slower due to extra internal computation. When to Reach for GPT: Creative marketing copy. Process images + text together. Connect to third-party tools via function calling. Team already uses ChatGPT's familiar interface."
- **Visuals:** Green top accent bar. Left bulleted strengths list; right white "Reasoning Models" card; bottom panel "When to Reach for GPT" with lightbulb icon.
- **Concept taught:** GPT's strengths, the o-series reasoning models and their speed trade-off, and when to choose it.

### Slide 9 — Gemini (Google)
- **Key text (verbatim-ish):** "Gemini 2.5 Pro | Gemini 2.5 Flash. Where Gemini Excels: 1M+ token context (5-7 full books!); Native web grounding with cited sources; Multimodal: text, images, audio, video; Deep Research with verified citations. Flash vs. Pro: Flash — Speed & efficiency (like Haiku). Best for high-throughput. Pro — Full power. The right choice for most professional tasks. When to Reach for Gemini: 500-page document that exceeds other models' limits. Research report with verifiable sources. Mix of text, images, and video in one query. Legal team wants grounded claims."
- **Visuals:** Blue top accent bar. Left bulleted strengths list; right white "Flash vs. Pro" card; bottom panel "When to Reach for Gemini" with lightbulb icon.
- **Concept taught:** Gemini's strengths (huge context, grounding, multimodal), the Flash vs. Pro tiers, and when to choose it.

### Slide 10 — DeepSeek, Llama & Grok
- **Key text (verbatim-ish):** "DeepSeek (V3 | R1 reasoning): Cost-effective with premium performance. Open-weight (self-host for privacy). Strong code & maths benchmarks. Warning: Self-hosting needs GPU infrastructure. 'Free weights' ≠ free to run. Llama (Meta) (Llama 4 Scout | Maverick): Open-source with massive community. On-premise for data residency. Fine-tune on proprietary data. Avoid vendor lock-in. Warning: Requires technical team for deployment and maintenance. Grok (xAI) (Grok 3 | Grok 3 Mini): Real-time data access & trends. Strong reasoning. Less filtered responses for legitimate business needs. Warning: Less filtered = stronger output validation needed. Check content policies."
- **Visuals:** Three white cards in a row (DeepSeek/purple, Llama/orange, Grok/red) each with brand icon, model tags, a body description, and a red-tinted warning box with a warning triangle at the bottom.
- **Concept taught:** Profiles of the three remaining families plus their key caveats (infra cost, deployment effort, content-policy risk).

### Slide 11 — The 6-Dimension Framework
- **Key text (verbatim-ish):** "Reading 3 | ~30 minutes. Quality: Accuracy, reasoning, creativity, coherence. Speed: Time to first token, total generation time. Cost: Price per million tokens at expected volume. Context Window: Max tokens per request (document length). Specialisation: Strength in code, creative, analysis, maths. Ecosystem: APIs, docs, integrations, community, tools. No model wins on all six — that is the fundamental insight that makes this framework useful."
- **Visuals:** 2x3 grid of white cards, each with a colored left accent and an icon (Quality=crown, Speed=lightning, Cost=$, Context Window=stacked layers, Specialisation=star, Ecosystem=plug). Bold italic insight line at bottom.
- **Concept taught:** The six evaluation dimensions that structure all model-selection decisions.

### Slide 12 — How to Use the Framework
- **Key text (verbatim-ish):** "1. Define Requirements: List what matters most for this task. Rank the six dimensions by importance for your use case. 2. Evaluate Candidates: Test 2-3 models against your actual task. Use your own prompts, data, and evaluation criteria. 3. Document & Recommend: Record findings in the AI Tool Selection Matrix. Include primary and fallback models for each task. The Weighted Decision: Not all dimensions are equally important for every task. A creative writing task might weight Quality (40%) and Speed (20%) heavily but care little about Context Window (5%). A legal document analysis might weight Context Window (35%) and Quality (35%) but accept higher cost. Define your weights before you evaluate — it prevents post-hoc rationalisation."
- **Visuals:** Three numbered circular step badges (1=blue, 2=green, 3=dark red) with titles and descriptions across the top; a wide white "The Weighted Decision" card with lightbulb icon below.
- **Concept taught:** The 3-step process (define, evaluate, document) and the idea of weighting dimensions before testing.

### Slide 13 — Quick-Reference Comparison
- **Key text (verbatim-ish):** Table columns: Model | Quality | Speed | Cost | Context | Specialisation | Ecosystem. Claude: ★★★★★ / ★★★ / ★★★ / 200K+ / Code, Analysis / ★★★★. GPT: ★★★★★ / ★★★★ / ★★★ / 128K / Creative, Multi / ★★★★★. Gemini: ★★★★ / ★★★★ / ★★★★ / 1M+ / Research, Multi / ★★★★. DeepSeek: ★★★★ / ★★★ / ★★★★★ / 128K / Code, Maths / ★★★. Llama: ★★★★ / ★★★ / ★★★★★* / Varies / Fine-tunes / ★★★★. Grok: ★★★★ / ★★★★ / ★★★ / 128K / Real-time, Reason / ★★★. "*Llama weights are free, but self-hosting requires infrastructure investment. This is a snapshot from early 2026. The framework (how to evaluate) is durable. The specific ratings are perishable."
- **Visuals:** Six-row comparison table with a teal header row, star ratings, and a footnote plus a pink-tinted caveat banner about the ratings being a perishable early-2026 snapshot.
- **Concept taught:** Side-by-side star-rated comparison of all six families across the six dimensions, with a caution that ratings age quickly.

### Slide 14 — Model Tiers & Pricing
- **Key text (verbatim-ish):** "Reading 4 | ~20 minutes. Flagship: Highest capability. Complex analysis, high-stakes decisions. (Opus 4.5, GPT-4o, Gemini 2.5 Pro, Grok 3). Balanced: Strong capability at moderate cost. The workhorse for most professional work. (Sonnet 4, o3, DeepSeek-V3). Lightweight: Fastest, cheapest. Classification, summarisation, high-volume tasks. (Haiku 3.5, o4-mini, Flash, Grok 3 Mini). The 80/20 Rule of Model Tiers: 80% of AI tasks can be handled by the balanced tier. This tiering strategy alone can reduce AI costs by 40-60% compared to routing everything through the flagship."
- **Visuals:** Three white cards (Flagship/crown/orange, Balanced/scales/green, Lightweight/lightning/blue) with example models; bottom teal banner "The 80/20 Rule of Model Tiers" with lightbulb icon.
- **Concept taught:** Three capability/price tiers across vendors, and the cost-saving 80/20 routing strategy favoring the balanced tier.

### Slide 15 — The Cost Iceberg
- **Key text (verbatim-ish):** "Token pricing is only the visible part of the cost. API Costs: Per million tokens (input & output priced separately). Output tokens typically cost 3-5x more than input. Infrastructure Costs: For self-hosted models: GPU servers at $10K-50K+ per year each. Integration Costs: Developer time to build and maintain API integrations, error handling, monitoring. Switching Costs: Once prompts, workflows, and integrations are built for one model, switching requires rework. This is vendor lock-in. Key takeaway: Choosing the right tier within a family is just as important as choosing the right family."
- **Visuals:** Four stacked horizontal bars, each with a colored left accent (API=blue, Infrastructure=purple, Integration=green, Switching=red) and a label + description. Italic key-takeaway line at bottom.
- **Concept taught:** Total cost of ownership extends well beyond token pricing — infrastructure, integration, and switching/lock-in costs.

### Slide 16 — Part 2 Divider: In-Class — The Landscape
- **Key text (verbatim-ish):** "PART 2 / In-Class: The Landscape / Model Comparison & Selection Matrix | 2 Hours | 75% Practical"
- **Visuals:** Full-bleed teal section divider with large white title, "PART 2" eyebrow, and a short accent rule.
- **Concept taught:** Section break starting the hands-on in-class session.

### Slide 17 — Session Plan
- **Key text (verbatim-ish):** "0:00-0:10 Opening: 'The Three-Tool Problem' + Playbook highlights — Conceptual. 0:10-0:25 Core Teaching: Model families, 6-Dimension Framework — Conceptual. 0:25-1:10 Exercise 2.A: Model Comparison Challenge (3 prompts × 3 models) — Practical. 1:10-1:50 Exercise 2.B: Build & peer-validate your Selection Matrix — Practical. 1:50-2:00 Debrief: Did the 'best' model vary by task? — Practical. By the end of tonight, Andrés has his answer. So will you."
- **Visuals:** Five stacked time-blocked rows (white cards with colored left accents — blue for conceptual, green for practical) listing time, activity, and a Conceptual/Practical tag. Italic closing line at bottom.
- **Concept taught:** The 2-hour agenda showing the practical-heavy structure of the session.

### Slide 18 — Exercise 2.A: Model Comparison
- **Key text (verbatim-ish):** "45 minutes | Work with a partner | 3 prompts × 3 models. 1. Creative Task: 200-word product launch for 'FitMind' AI fitness app. Energetic, professional tone. 2. Code Task: Python function: top 3 scorers from list of dicts. Handle edge cases + pytest tests. 3. Analysis Task: Retail: online -15%, in-store +8%, CSAT steady 4.2/5. Top 3 explanations + data sources. Run each prompt on: Claude | ChatGPT | Gemini (minimum). Rate each output 1-5: Quality, Speed, Format, Usefulness, Surprise Factor."
- **Visuals:** Three numbered task cards (orange/green/blue circle badges). A centered "Run each prompt on" line naming the three tools, and a white rating card listing the five 1-5 rating criteria.
- **Concept taught:** Hands-on head-to-head comparison: run the same three task-types across three models and rate them on five criteria.

### Slide 19 — Exercise 2.B: Selection Matrix
- **Key text (verbatim-ish):** "40 minutes | Build + Peer Validate. Table: Task Category | Priority Dims | Recommended | Fallback | Justification. Python code review (security focus) | Quality #1, Specialisation #2 | Claude Sonnet 4 | GPT-4o | Claude's code analysis + 200K context for multi-file reviews. Marketing copy (product launch) | Quality #1, Speed #2 | GPT-4o | Claude Sonnet 4 | GPT produces more engaging, natural-sounding creative text. Contract analysis (200+ pages) | Context #1, Quality #2 | Gemini 2.5 Pro | Claude Opus 4.5 | Gemini's 1M+ context handles full contracts in one pass. Build your own matrix with at least 5 task categories from your work, then swap with a partner. Peer Validation Scenarios: 1. Legal team: 200-page contract, overnight. 2. Startup: 50K support tickets/month. 3. CEO: compelling board vision document. 4. Data team: fine-tune on proprietary data."
- **Visuals:** Five-column example matrix table (teal header) with three filled-in rows; italic instruction line; bottom two-column list of four peer-validation scenarios.
- **Concept taught:** Build the deliverable — a Selection Matrix mapping tasks to ranked dimensions, primary/fallback models, and justifications — then stress-test it via peer scenarios.

### Slide 20 — Week 2 Deliverable
- **Key text (verbatim-ish):** "AI Tool Selection Matrix: A personalised decision framework mapping task categories to recommended AI models, with priority dimensions, fallback models, and justifications. Peer-tested with at least 3 scenarios. Created during: In-class exercises (throughout). Your Growing Portfolio: Week 1 — AI Engineer's Compass; Week 1+ — Prompt Playbook (ongoing); Week 2 — AI Tool Selection Matrix."
- **Visuals:** Top white card with a teal matrix/table icon describing the deliverable. Below, "Your Growing Portfolio" with three small cards for Week 1, Week 1+, and Week 2 artifacts.
- **Concept taught:** Defines the graded Week 2 artifact and situates it within the cumulative course portfolio.

### Slide 21 — Looking Ahead: Week 3
- **Key text (verbatim-ish):** "Andrés presents his Matrix to the CFO. Response: 'Exactly what we needed. But here's the next challenge — our engineering team says building AI integrations takes too long. They heard about tools that let you describe an app in plain English and it builds itself. Is that real?' It is real. Next week: the full spectrum of AI-assisted development. From no-code builders (Replit Agent, Bolt.new) to agentic coding environments (Cursor, Claude Code). You build something real. Week 3: AI-Assisted Development: No-code app builders: describe what you want, watch it appear; Agentic coding: AI as your pair programmer; Build a real, working prototype — with AI doing most of the coding. Setup before Week 3: Create Replit account | Install Cursor | GitHub account ready."
- **Visuals:** Dark teal slide. Italic narrative quote in a translucent box with lightbulb icon; teal "Week 3" heading; three arrow bullets; a bottom setup-instructions strip.
- **Concept taught:** Teaser/bridge to Week 3 (AI-assisted development) plus prerequisite setup tasks.

### Slide 22 — Closing Quote
- **Key text (verbatim-ish):** "'The expert in anything was once a beginner.' NEXUS GUILDS / AI Foundational • Week 2 • v1.0 • March 2026 / Source Meridian"
- **Visuals:** Full-bleed teal closing slide with a large centered italic motivational quote, a short horizontal rule, and centered branding/footer text.
- **Concept taught:** Motivational closing and deck attribution/branding.
