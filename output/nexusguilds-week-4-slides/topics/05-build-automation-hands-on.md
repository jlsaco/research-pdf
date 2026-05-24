# Building the Same Automation Three Ways and Your Own

## Summary

This topic covers the hands-on core of Week 4: taking one concrete automation — a new Gmail email is classified by an LLM as Urgent / Question / FYI / Spam and a label is applied — and building it three different ways across the tool spectrum: with Zapier's drag-and-drop visual builder, with Make's HTTP module calling the API directly, and with a raw cURL/Python call from the terminal. Seeing the *same* automation expressed three ways exposes the build-difficulty vs. control trade-off: the underlying API call is identical, but who can build it, how much you see, and how much you can customize change dramatically. The topic then moves to building your own automation from a menu of five common business patterns (email analysis, meeting summarization, application screening, planner/PRD-to-stories, ticket routing), each mapped to the Trigger → AI → Delivery anatomy, with the guiding rule: start simple — one trigger, one AI step, one delivery.

## Prerequisite concepts

- **Trigger → AI → Delivery anatomy** — every automation here follows this three-stage shape (see [Anatomy of an AI Automation](04-automation-anatomy.md)).
- **The tool spectrum** — the four tiers (no-code, low-code, AI-assisted code, full code) that the three implementations sit on (see [The Tool Spectrum](03-tool-spectrum.md)).
- **Zapier visual builder** — building automations no-code with triggers, filters, and actions.
- **Make HTTP modules and visual flows** — calling any API via a configurable "Make a request" module.
- **cURL and scripting API calls** — issuing an HTTP request to an AI model's endpoint from the command line.
- **Build-difficulty vs. control trade-off** — the recurring tension between speed/accessibility and flexibility/control.
- **Common business automations** — email analysis, meeting summaries, application screening, ticket routing.

## Deep dive

**One automation, three implementations.** The exercise fixes the workflow — new Gmail email → LLM classifies as Urgent / Question / FYI / Spam → apply Gmail label — and varies only *how* it is built.

- **Zapier (no-code).** Email categorization is built entirely in the visual builder by applying rules based on sender, subject, or content, typically using a Gmail trigger plus a Filter step and a labeling/logging action. It is the fastest to build and accessible to non-technical people, but flexibility is limited and you do not see the API call underneath.
- **Make (low-code / API-visible).** Make's HTTP "Make a request" module lets you call any API that lacks a native integration. You configure the HTTP method (GET/POST/etc.), URL, headers, query parameters, body (JSON, form-data), and authentication (none, API key, basic, OAuth 2.0). You build visually but you *see the raw request*, which gives more control than pure no-code.
- **cURL / Python (full code).** Calling the AI API directly via cURL uses the Messages endpoint with a few headers and a JSON body — for example:
  ```
  curl https://api.anthropic.com/v1/messages \
    -H "Content-Type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d '{"model":"claude-opus-4-7","max_tokens":1000,"messages":[{"role":"user","content":"..."}]}'
  ```
  This gives maximum control, but you handle everything yourself.

**The key insight:** the same headers and body sent by cURL are exactly what the Make HTTP module sends. The three approaches differ in *difficulty and control, not in the underlying API call*. The build-difficulty vs. control trade-off is the lesson: no-code is faster, cheaper upfront, and usable by non-technical builders but hits logic and customization ceilings; API/code gives full control over logic, data, and security and scales for complex, high-volume systems but requires developer expertise and higher upfront and maintenance cost. A hybrid approach is common — no-code for internal workflows, APIs/code for customer-facing or high-scale features.

**Build your own.** With that trade-off understood, learners build one automation from five common patterns, each fitting Trigger → AI → Delivery: (1) Email Analyser, (2) Meeting Summariser, (3) Application Screener, (4) Planner (PRD → atomic user stories → Jira epic), (5) Ticket Router. These mirror real AI business workflows, which commonly handle classification/routing (deciding whether an email is a customer issue, a sales lead, or noise), summarization of long documents, data extraction, and ticket triage by tone or topic. The payoff is real: one AI-driven IT support workflow handled 28% of tickets automatically, saving 600+ hours/month, by classifying, routing, and responding. The discipline that makes this work is to start simple — a working simple automation beats an incomplete complex one.

## Why it matters for a Project Manager

For a Project Manager, this topic is less about writing code and more about choosing *who builds what, on which tier, and at what cost*. Building the same automation three ways is a concrete map of your delivery options:

- **Outcomes vs. tier:** A no-code Zapier build can ship a working automation in roughly the time of a short task and can be owned by a non-technical team member — ideal for fast wins and internal workflows. The cURL/code version unlocks unlimited control and scale but pulls in developer time and a maintenance commitment.
- **Trade-offs:** Speed and accessibility (no-code) versus control, security, and scalability (code). The same business value can come from either; the difference is staffing, cost curve, and long-term ownership.
- **Timelines:** No-code lowers the cost of trying — you can prototype and validate the workflow before deciding whether the 20% that genuinely needs code is worth a developer's time. The 28%-of-tickets / 600+ hours example shows the kind of ROI to put in a business case.
- **Risk:** "Start simple — one trigger, one AI step, one delivery" is your scope-control rule. It de-risks the first delivery, produces a demonstrable result quickly, and avoids the classic over-engineered, never-finished automation. Plan for the hybrid model: no-code for internal speed, code where scale and control justify the investment.

## Common pitfalls

- **Defaulting to code when no-code would do.** Reaching for a Python script (and a developer's calendar) when a Zapier build would ship the same outcome faster and be maintainable by the team — inflating cost and timeline for no extra value.
- **Building complex on the first pass.** Skipping "start simple" and attempting multi-branch logic immediately, ending with an incomplete automation that never ships. A working simple automation beats an incomplete complex one.
- **Ignoring who maintains it.** Choosing the most powerful tier without asking who will keep it running; high-control code carries a higher maintenance burden than a visual no-code flow.
- **Assuming the tools are fundamentally different.** Treating Make's HTTP module and a cURL call as separate skills — they send the same request. Misreading this leads to over-valuing one tier and mis-estimating effort.

## Sources

- General: [AI workflows: How to use AI in your business (Zapier)](https://zapier.com/blog/ai-workflows/)
- Specific: [Automated email sorting / categorize emails based on criteria (Zapier)](https://zapier.com/automation/use-case/organize-and-categorize-emails-based-on-criteria)
- Specific: [HTTP app — "Make a request" module (Make Apps Documentation)](https://apps.make.com/http)
- Specific: [Get started with Claude — cURL example (Claude Docs)](https://platform.claude.com/docs/en/get-started)
- Specific: [No-code vs API: Which is better for automating? (PandaDoc)](https://www.pandadoc.com/blog/no-code-vs-api/)

## References

1. AI workflows: How to use AI in your business — Zapier. https://zapier.com/blog/ai-workflows/
2. Organize and categorize emails based on criteria — Zapier. https://zapier.com/automation/use-case/organize-and-categorize-emails-based-on-criteria
3. HTTP — Make a request module — Make Apps Documentation. https://apps.make.com/http
4. Get started with Claude (cURL example) — Claude Docs. https://platform.claude.com/docs/en/get-started
5. No-code vs API: Which is better for automating? — PandaDoc. https://www.pandadoc.com/blog/no-code-vs-api/
