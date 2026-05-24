# Extraction — nexusguilds-week-4-slides

## GLOBAL CONTEXT
- **What the deck is about:** Week 4 of the Nexus Guilds "AI Foundational" course, titled "The Interface — APIs, Automation & Integration." It teaches how to connect AI to real workflows via APIs and no-code/low-code automation tools (Zapier, Make, code), framing automation as a spectrum of four tiers rather than a single skill.
- **Intended audience:** Working professionals transitioning "From Professional to AI Engineer" — a mixed-skill cohort ranging from non-coders to fluent Python developers. Module 2 ("The Workshop") moves learners from AI *user* to AI *integrator*.
- **Narrative arc:** Opens with a framing story (Andrés's "15 Automations Challenge") establishing automation as a spectrum. Part 1 (pre-reading, ~1.5h) builds conceptual foundations: what an API is, five integration patterns, the four-tier tool spectrum, and the anatomy of an AI automation (Trigger → AI → Delivery). Part 2 (in-class, 2h, 75% practical) is hands-on: three ways to build the same automation, building one's own automation, and a process-mapping workshop. The deck closes with deliverables, a portfolio recap, and a preview of Week 5 (automation → orchestration).
- **Total slides:** 16

## SLIDES

### Slide 1 — Title: AI Foundational / Week 4: The Interface
- **Key text (verbatim-ish):** "NEXUS GUILDS — AI Foundational — From Professional to AI Engineer. Week 4: The Interface — APIs, Automation & Integration. Yvan Callaou - Gabriel Cepeda. Pre-Reading: ~1.5 Hours | In-Class Session: 2 Hours | 75% Practical. Version 1.0 • May 2026."
- **Visuals:** Dark navy title slide with a subtle grid background. Teal "NEXUS GUILDS" eyebrow label, large white "AI Foundational" headline, teal italic subtitle, and a short teal divider rule above the week/instructor metadata.
- **Concept taught:** Sets up the course identity and Week 4 scope (APIs, automation, integration) with timing and the 75%-practical emphasis.

### Slide 2 — Welcome to Module 2: The Workshop
- **Key text (verbatim-ish):** "You are now an AI user. Module 2 takes you from user to AI integrator — connecting AI to real workflows through APIs, automation, and agents. The 15 Automations Challenge: Andrés's team has 15 manual processes to automate: classifying emails, summarising meetings, screening applications, drafting posts, routing tickets. The problem? Wildly different skill levels — 3 code Python fluently, 5 have never written a line. His boss says: 'Find a strategy that works for everyone.' Tonight, Andrés discovers automation is a spectrum, not a single skill. ACTION REQUIRED: Create free Zapier account (zapier.com) + free Make account (make.com) + have Gmail/Google account ready."
- **Visuals:** Light slide with bold black headline. A teal banner restates the module premise. A white callout card with a person icon presents "The 15 Automations Challenge" story. A red-bordered warning box (with alert triangle icon) holds the "ACTION REQUIRED" account-setup prerequisites.
- **Concept taught:** Module framing — moving from AI user to integrator — plus the motivating story that automation is a spectrum, and the prerequisite tool accounts students must set up.

### Slide 3 — Week 4 Overview
- **Key text (verbatim-ish):** "Part 1: Pre-Reading (~1.5h): What Is an API? • Five Integration Patterns • The Tool Spectrum (4 tiers) • Anatomy of an AI Automation. Part 2: In-Class Session (2h): 4.A: Three Ways to Automate (demo) • 4.B: Build Your First Automation • 4.C: Process Mapping Workshop • Preview: Week 5 agents & orchestration. 75% Practical."
- **Visuals:** Two side-by-side cards. Left card (teal header, book icon) lists Part 1 pre-reading topics; right card (dark header, plug icon) lists Part 2 in-class topics, with a teal "75% Practical" tag at the bottom.
- **Concept taught:** Roadmap of the week split into pre-reading (conceptual) and in-class (practical) halves.

### Slide 4 — Part 1 Section Divider: APIs and the Automation Spectrum
- **Key text (verbatim-ish):** "PART 1 — APIs and the Automation Spectrum. Complete before your in-class session | Estimated time: ~1.5 hours."
- **Visuals:** Full-bleed teal section-divider slide with grid texture, "PART 1" eyebrow, large white title, and a divider rule above the instruction line.
- **Concept taught:** Transition marker introducing the self-paced pre-reading block.

### Slide 5 — What Is an API?
- **Key text (verbatim-ish):** "Reading 1 | ~25 minutes. The Restaurant Analogy: You (client) give your order to the waiter (API). The waiter takes it to the kitchen (server/model). The kitchen prepares the food and the waiter brings it back (response). You never go into the kitchen yourself. When you call an AI model's API: your prompt is the order, the AI model is the kitchen, and the API is the waiter. The Four API Concepts: Request / Response — Send prompt, get output back; Authentication — API key proves who you are; Rate Limits — Max requests per minute/hour; Endpoints — Different URLs for different capabilities."
- **Visuals:** White callout card (lightbulb icon) holds the restaurant analogy. Below, a 2x2 grid of four colored cards: Request/Response (blue, arrows icon), Authentication (purple, key icon), Rate Limits (red, gauge icon), Endpoints (green, node-tree icon).
- **Concept taught:** Demystifies APIs via the restaurant/waiter analogy and the four core API concepts.

### Slide 6 — Five Integration Patterns
- **Key text (verbatim-ish):** "Reading 2 | ~20 minutes. Synchronous — Send request, wait, proceed — Form submit → API → result on page. Event-Driven — Trigger fires → background processing — New email → classify → route. Batch — Collect items, process together on schedule — Nightly: process all day's tickets. Streaming — Receive partial results as generated — ChatGPT tokens appearing word by word. Tool Use — AI decides which tools to invoke mid-response — Claude calls weather API + calculator. Start with Event-Driven: trigger fires → AI processes → result delivered. This is what Zapier and Make are built for."
- **Visuals:** Five stacked rows, each with a colored left accent bar (blue, green, purple, orange, red), a bold pattern name, a definition, and an italic example. A teal footer banner highlights the "Start with Event-Driven" guidance.
- **Concept taught:** The five ways systems integrate with APIs, with Event-Driven flagged as the entry point for no-code automation tools.

### Slide 7 — The Tool Spectrum
- **Key text (verbatim-ish):** "Reading 3 | ~25 minutes. 1. No-Code — Zapier, Make — Simple triggers, linear flows — Maint: Low. 2. Low-Code — Retool, n8n — Custom logic, branching, DB connections — Maint: Medium. 3. AI-Assisted Code — Cursor + API, Replit + API — Full flexibility, complex business logic — Maint: Med-High. 4. Full Code — Python SDK, Node.js SDK — Unlimited — production systems, scale — Maint: High. 80% of automation needs can be solved at No-Code. Reserve code for the 20% that genuinely needs it."
- **Visuals:** Four stacked tier rows, each with a numbered colored circle (1 purple, 2 blue, 3 green, 4 orange) and a tool-category icon (cursor, wrench, code brackets, rocket), the tier name and example tools, a capability description, and an italic maintenance level on the right. A teal footer banner states the 80/20 rule.
- **Concept taught:** The four-tier automation tool spectrum, with the 80/20 heuristic favoring no-code for most needs.

### Slide 8 — Anatomy of an AI Automation
- **Key text (verbatim-ish):** "Reading 4 | ~20 minutes. 1. Trigger — The event that starts it — New email, form response, file upload, scheduled time. 2. AI Processing — LLM processes the input — Classify, summarise, extract, generate — using CRFT prompts! 3. Delivery — Action taken with the output — Add to sheet, send Slack msg, create task, apply label. Email Classification Example: Trigger: new email in Gmail → AI: 'Classify as Urgent, Question, FYI, or Spam. Respond with only the category name.' → Delivery: apply Gmail label + optional forward."
- **Visuals:** Three-box left-to-right flow diagram (Trigger → AI Processing → Delivery) with numbered colored circles (1 blue, 2 purple, 3 green) and green arrows between boxes. A shaded panel below gives the concrete Email Classification Example.
- **Concept taught:** The universal three-stage structure of any AI automation, anchored by a worked email-classification example (note the callback to CRFT prompts).

### Slide 9 — Part 2 Section Divider: In-Class: The Interface
- **Key text (verbatim-ish):** "PART 2 — In-Class: The Interface. APIs, Automation & Integration | 2 Hours | 75% Practical."
- **Visuals:** Full-bleed teal section-divider slide matching Slide 4's style: "PART 2" eyebrow, large white title, divider rule, and metadata line.
- **Concept taught:** Transition marker into the hands-on in-class portion.

### Slide 10 — Session Plan
- **Key text (verbatim-ish):** "0:00-0:10 Opening: 'The 15 Automations' story + Self-Study 2 debrief — Conceptual. 0:10-0:25 Core Teaching: API fundamentals, Tool Spectrum, integration patterns — Conceptual. 0:25-0:50 Exercise 4.A: Three Ways to Automate (Zapier / Make / cURL) — Practical. 0:50-1:30 Exercise 4.B: Build Your First Automation (trigger → AI → delivery) — Practical. 1:30-1:50 Exercise 4.C: Process Mapping Workshop (5-10 processes) — Practical. 1:50-2:00 Preview: Week 5 agents and multi-step orchestration — Conceptual."
- **Visuals:** Six stacked timeline rows, each with a left accent bar (teal for conceptual blocks, green for practical blocks), a time range, an activity label, and a right-side Conceptual/Practical tag.
- **Concept taught:** Minute-by-minute agenda for the 2-hour session, color-coded by conceptual vs. practical.

### Slide 11 — Exercise 4.A: Three Ways to Automate
- **Key text (verbatim-ish):** "25 minutes | Same automation, 3 implementations | Follow along. New Gmail email → LLM classifies as Urgent / Question / FYI / Spam → Apply Gmail label. Zapier: Visual builder: drag-and-drop trigger, AI action, label action. Fastest to build. No code. Limited flexibility. Make: Visual flow with HTTP module calling the API directly. You see the raw request. More control. You see the API call underneath. cURL / Python: Terminal command and script calling the same API with the same prompt. Maximum control. You handle everything yourself. Key question: Which version would you maintain? Which could your non-technical colleague build?"
- **Visuals:** A teal banner states the shared automation flow. Below, three column cards with colored headers — Zapier (purple), Make (blue), cURL/Python (orange) — each describing the implementation and its trade-off in italics. A shaded footer holds the reflective "Key question."
- **Concept taught:** The same automation built three ways across the tool spectrum, surfacing the build-difficulty vs. control trade-off and the maintainability question.

### Slide 12 — Exercise 4.B: Build Your Automation
- **Key text (verbatim-ish):** "40 minutes | Zapier or Make | Trigger → AI → Delivery. 1. Email Analyser — Trigger: Email — AI Step: Resume — Delivery: Slack Message. 2. Meeting Summariser — Trigger: New file in Drive — AI Step: Summarise notes — Delivery: Send to Slack. 3. Application Screener — Trigger: Email with 'Application' — AI Step: Extract + rate fit — Delivery: Add to Sheet. 4. Planner — Trigger: New PRD — AI Step: Generate atomic user stories — Delivery: An Epic in Jira. 5. Ticket Router — Trigger: Form / email — AI Step: Categorise + urgency — Delivery: Create task + priority. Start simple. One trigger, one AI step, one delivery. A working simple automation beats an incomplete complex one."
- **Visuals:** Five column cards, each topped with a numbered colored circle (1 blue, 2 green, 3 purple, 4 orange, 5 red) and an automation name, then a Trigger / AI Step / Delivery breakdown. A red-bordered warning footer (alert icon) gives the "Start simple" guidance.
- **Concept taught:** A menu of five build-your-own automation options, each mapped to the Trigger → AI → Delivery anatomy, with advice to keep the first build minimal.

### Slide 13 — Exercise 4.C: Process Mapping
- **Key text (verbatim-ish):** "20 minutes | In pairs | Map 5-10 processes to Tool Spectrum tiers. [Table] Process | Volume | Tier | Justification | Effort. Classify customer emails | 200/day | No-Code | Simple classification, Zapier handles it | 2 hours. Generate sales proposals from CRM | 20/week | Low-Code | Needs CRM integration + branching logic | 1 day. Analyse contracts vs compliance rules | 5/week | AI-Assisted Code | Complex business logic + long documents | 3 days. Document: process name, volume/frequency, recommended tier, justification, and estimated effort. This feeds directly into Week 5's agent design exercises. How to Choose Your Tier: 1. Who will build it? 2. Who will maintain it? 3. How complex is the logic? 4. What scale do you need?"
- **Visuals:** A 5-column worked-example table (teal header row) with three sample rows mapping processes to tiers/effort. Below it, an italic instruction on what to document, then a "How to Choose Your Tier" section with four numbered decision questions laid out horizontally.
- **Concept taught:** A pair workshop to map real processes to the appropriate tool-spectrum tier, using four decision criteria; output feeds Week 5.

### Slide 14 — Week 4 Deliverables
- **Key text (verbatim-ish):** "Working Automation: A functional Zapier or Make automation with trigger → AI step → delivery. Screenshot or share link + note on which tier and why. Process Map: 5-10 processes mapped to Tool Spectrum tiers with justification. Feeds into Week 5 agent design. Your Portfolio: 6 Artefacts — W1: Compass | W1+: Playbook | W2: Selection Matrix | W3: Prototype | SS2: Knowledge Guide | W4: Automation + Map."
- **Visuals:** Two large deliverable cards with teal left accent bars and icons (plug = Working Automation, signpost = Process Map). Below, a "Your Portfolio: 6 Artefacts" row of six chips, with the final chip "W4: Automation + Map" highlighted in teal as the current week's addition.
- **Concept taught:** The two required Week 4 deliverables and how they fit into the growing cumulative course portfolio.

### Slide 15 — Looking Ahead: Week 5
- **Key text (verbatim-ish):** "Andrés's automations are running — emails classified, meetings summarised. But they're isolated. Marketing's content pipeline doesn't talk to Sales' lead qualification. Individual automations are like individual musicians. Andrés needs an orchestra. Next week: chaining AI steps into multi-step workflows, designing agents that make decisions autonomously, and mapping cross-departmental AI workflows. Week 5 is where AI integration becomes AI orchestration. Week 5: From Automation to Orchestration — Multi-step workflows chaining AI processes together; Autonomous agents that make decisions and take actions; Cross-departmental AI workflow mapping. Bring your Process Map from Exercise 4.C — it's the raw material for Week 5."
- **Visuals:** Dark navy slide. A teal-tinted panel (lightbulb icon) holds the Andrés "orchestra" narrative bridge. Below, a teal "Week 5: From Automation to Orchestration" heading with three arrow-bulleted topics, and a teal footer banner reminding students to bring their Process Map.
- **Concept taught:** Narrative and content preview of Week 5 — the leap from isolated automations to orchestrated, multi-step, agentic, cross-departmental workflows.

### Slide 16 — Closing Quote
- **Key text (verbatim-ish):** "'The expert in anything was once a beginner.' NEXUS GUILDS — AI Foundational • Week 4 • v1.0 • March 2026. Source Meridian."
- **Visuals:** Full-bleed teal closing slide with a large white italic motivational quote, a short divider rule, the "NEXUS GUILDS" wordmark, course/version metadata, and "Source Meridian" attribution at the bottom. (Note: this slide's date reads "March 2026" while the title slide reads "May 2026" — a likely versioning inconsistency.)
- **Concept taught:** Encouraging closer reinforcing that mastery starts from being a beginner; provides course branding and attribution.
