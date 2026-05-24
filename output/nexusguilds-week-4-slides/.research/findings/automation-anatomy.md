# Findings — Anatomy of an AI Automation (Trigger -> AI -> Delivery) (automation-anatomy)

## General source(s)
- [AI workflows: How to use AI in your business (Zapier)](https://zapier.com/blog/ai-workflows/) — High-level framing of an AI automation as the classic trigger -> processing -> action pipeline with an AI step inserted where judgment is needed (e.g. webhook pulls data -> ChatGPT classifies/prioritizes -> Notion record created). Describes AI as "automation with a brain."

## Specific sources
- [Workflow automation: Definition, tutorial, and tools (Zapier)](https://zapier.com/blog/workflow-automation/) — Covers the **trigger** and **action/delivery** prerequisite concepts: defines a trigger as "an event that starts a Zap" (e.g. new lead in a form, new email) and an action as "an event a Zap performs after it's triggered" (e.g. send an email / notify the Sales team). Establishes the "When this happens, do that" model.
- [Automated email classification & response system with Gmail, GPT, and Sheets (n8n template)](https://n8n.io/workflows/7839-automated-email-classification-and-response-system-with-gmail-gpt-and-sheets/) — Concrete end-to-end example covering **email trigger -> LLM classify/generate -> delivery actions**: Gmail "new email" trigger, GPT classifies into Support/Sales/Complaints/Information/Other, then drafts a labeled response and logs results to Google Sheets.
- [Prompting best practices (Claude Docs)](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices) — Covers **prompt design for automations**: be clear and explicit, control output length/format, use examples and XML structure, and design prompts for agentic/autonomous systems where the model can't ask clarifying questions.

## Key facts
- An AI automation follows a three-part anatomy: a trigger fires, an AI/processing step interprets/decides, and an action delivers the output. Zapier frames this as AI being "automation with a brain," with a concrete chain of "webhook pulls user data -> ChatGPT classifies and prioritizes the issue -> a Notion record is created." — source: https://zapier.com/blog/ai-workflows/
- A trigger is "an event that starts a Zap" — common triggers include a new form submission or a new incoming email; an action is "an event a Zap performs after it's triggered" (e.g. send an email). The model is "When this happens, do that." — source: https://zapier.com/blog/workflow-automation/
- AI processing tasks inside an automation include reading, classifying (e.g. deciding whether an email is a customer issue, a sales lead, or ignorable), summarizing long documents, and drafting/generating responses. — source: https://zapier.com/blog/ai-workflows/
- A typical email-classification automation wires an email trigger to an LLM classify step to delivery actions: Gmail new-email trigger -> GPT classifies into Support/Sales/Complaints/Information/Other -> draft response generated, Gmail label applied, and results logged to Google Sheets. — source: https://n8n.io/workflows/7839-automated-email-classification-and-response-system-with-gmail-gpt-and-sheets/
- Prompts for automations should be clear and explicit, control output format/verbosity, and use examples and XML tags — because an autonomous/agentic step cannot ask clarifying questions, the prompt must define success and the exact output shape up front. — source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices

## Verification checklist
| URL | HTTP | Supports |
|-----|------|----------|
| https://zapier.com/blog/ai-workflows/ | 200 | General trigger->AI->action anatomy; AI can read/classify/summarize/draft; AI step sits inside an otherwise predictable workflow. |
| https://zapier.com/blog/workflow-automation/ | 200 | Definitions of trigger ("event that starts a Zap") and action ("event a Zap performs after it's triggered"); "When this happens, do that." |
| https://n8n.io/workflows/7839-automated-email-classification-and-response-system-with-gmail-gpt-and-sheets/ | 200 | Concrete email trigger -> GPT classify (5 categories) -> draft/label/log delivery actions. |
| https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices | 200 | Prompt design for automations: be explicit, control output format, use examples/XML, design for autonomous/agentic steps. |
