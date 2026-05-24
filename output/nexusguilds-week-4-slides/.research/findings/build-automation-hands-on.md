# Findings — Building the Same Automation Three Ways and Your Own (build-automation-hands-on)

## General source(s)
- [AI workflows: How to use AI in your business (Zapier)](https://zapier.com/blog/ai-workflows/) — High-level overview of AI-powered business automations and the common patterns (classification/routing, summarization, extraction, lead handling, ticket triage); frames how the same automation can be expressed as a workflow.

## Specific sources
- [Automated email sorting / categorize emails based on criteria (Zapier)](https://zapier.com/automation/use-case/organize-and-categorize-emails-based-on-criteria) — Covers building an email-classification automation in Zapier's visual builder (rule/filter-based sorting by sender, subject, content). Maps to the "Zapier visual builder" prerequisite and the "email analysis / classification" automation example.
- [HTTP app — "Make a request" module (Make Apps Documentation)](https://apps.make.com/http) — Documents Make's HTTP module for sending custom API calls (GET/POST/etc., URL, headers, body, JSON, auth) to any API or web service. Maps to "Make HTTP modules and visual flows" and to calling an AI API from Make.
- [Get started with Claude — cURL example (Claude Docs)](https://platform.claude.com/docs/en/get-started) — Shows the exact cURL command to call the AI API from the command line (Messages endpoint, headers, JSON body). Maps to "cURL and scripting API calls."
- [No-code vs API: Which is better for automating? (PandaDoc)](https://www.pandadoc.com/blog/no-code-vs-api/) — Compares building the same automation with no-code vs API/code, covering control, flexibility, difficulty, cost, and scalability. Maps to "build-difficulty vs control tradeoff."

## Key facts
- AI business workflows commonly handle classification/routing (e.g., reading an email and deciding whether it is a customer issue, a sales lead, or noise), summarization of long documents, data extraction, and ticket triage by tone or topic. — source: https://zapier.com/blog/ai-workflows/
- Real-world example: an AI-driven IT support workflow handled 28% of tickets automatically, saving 600+ hours/month, by classifying, routing, and responding. — source: https://zapier.com/blog/ai-workflows/
- In Zapier, email categorization is built no-code in the visual builder by applying rules based on sender, subject, or content, typically using a Gmail/Outlook trigger plus Filter by Zapier and labeling/logging actions. — source: https://zapier.com/automation/use-case/organize-and-categorize-emails-based-on-criteria
- Make's HTTP "Make a request" module lets you call any API that lacks a native Make integration: you configure HTTP method (GET/HEAD/POST/PUT/PATCH/DELETE/OPTIONS), URL, headers, query parameters, and body (JSON, multipart/form-data, x-www-form-urlencoded), plus auth (none, API key, basic, OAuth 2.0). — source: https://apps.make.com/http
- Calling the AI API directly via cURL uses the Messages endpoint with three headers and a JSON body, e.g.: `curl https://api.anthropic.com/v1/messages -H "Content-Type: application/json" -H "x-api-key: $ANTHROPIC_API_KEY" -H "anthropic-version: 2023-06-01" -d '{"model":"claude-opus-4-7","max_tokens":1000,"messages":[{"role":"user","content":"..."}]}'`. — source: https://platform.claude.com/docs/en/get-started
- The same headers/body sent by cURL are exactly what a Make HTTP module sends — the three approaches (Zapier, Make HTTP, cURL) differ in difficulty and control, not in the underlying API call. — sources: https://platform.claude.com/docs/en/get-started ; https://apps.make.com/http
- Build-difficulty vs control tradeoff: no-code is faster, accessible to non-technical users (drag-and-drop), and cheaper upfront but hits logic/customization ceilings; API/code gives full control over logic, data, and security and scales for complex/high-volume systems but requires developer expertise and higher upfront/maintenance cost. A hybrid approach is common (no-code for internal workflows, APIs for customer-facing features). — source: https://www.pandadoc.com/blog/no-code-vs-api/

## Verification checklist
| URL | HTTP | Supports |
|-----|------|----------|
| https://zapier.com/blog/ai-workflows/ | 200 | General overview of AI business automations and common patterns (classification, summarization, extraction, ticket routing, lead handling); WebFetch confirmed examples. |
| https://zapier.com/automation/use-case/organize-and-categorize-emails-based-on-criteria | 200 | Building email-classification/sorting automation in Zapier's visual builder by sender/subject/content; WebFetch confirmed. |
| https://apps.make.com/http | 200 | Make HTTP "Make a request" module for custom API calls (methods, URL, headers, body, auth); WebFetch confirmed. |
| https://platform.claude.com/docs/en/get-started | 200 | cURL example calling the AI Messages endpoint with required headers and JSON body; WebFetch confirmed (docs.claude.com 302-redirects here). |
| https://www.pandadoc.com/blog/no-code-vs-api/ | 200 | No-code vs API tradeoffs: control, flexibility, difficulty, cost, scalability, hybrid recommendation; WebFetch confirmed. |
