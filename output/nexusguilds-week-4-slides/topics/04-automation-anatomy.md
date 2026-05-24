# Anatomy of an AI Automation (Trigger → AI → Delivery)

## Summary

Every AI automation, no matter which tier of the [tool spectrum](03-tool-spectrum.md) it lives in, shares the same three-part anatomy: a **Trigger** (the event that starts it — a new email, a form response, a file upload, a scheduled time), an **AI Processing** step (the LLM classifies, summarizes, extracts, or generates — using well-designed CRFT prompts), and a **Delivery** step (an action taken with the output — add to a sheet, send a Slack message, create a task, apply a label). The deck's worked example is email classification: a new Gmail email triggers an AI step that classifies it as Urgent, Question, FYI, or Spam, and delivery applies the matching Gmail label. Understanding this universal structure lets you design any automation from a blank page by answering three questions: what starts it, what does the AI do, and what happens with the result.

## Prerequisite concepts

- Automation triggers — email, form, file upload, scheduled time.
- LLM processing tasks — classify, summarize, extract, generate.
- Output delivery actions — write to a sheet, message a channel, create a task, label.
- Prompt design for automations (CRFT prompts) — making the AI step reliable.
- The "When this happens, do that" automation model.

## Deep dive

An AI automation is, at heart, the classic automation pipeline — trigger → processing → action — with an AI step inserted exactly where human judgment used to be needed. Zapier frames this as AI being "automation with a brain," and gives a concrete chain: a webhook pulls user data, ChatGPT classifies and prioritizes the issue, and a Notion record is created. The structure is always the same three stages.

**1. Trigger.** A trigger is "an event that starts a Zap." Common triggers include a new form submission, a new incoming email, a new file in a drive, or a scheduled time. The mental model is "When this happens..." — the trigger defines the *when*.

**2. AI Processing.** This is the stage that distinguishes an *AI* automation from a plain one. The LLM reads the input and performs a judgment task: classifying (deciding whether an email is a customer issue, a sales lead, or ignorable), summarizing long documents, extracting structured fields, or drafting and generating responses. The quality of this stage depends almost entirely on the prompt. Prompts for automations should be clear and explicit, control output format and verbosity, and use examples and XML-style structure — because an autonomous, agentic step cannot ask clarifying questions, the prompt must define success and the exact output shape up front. In the email example, the prompt is tightly scoped: "Classify as Urgent, Question, FYI, or Spam. Respond with only the category name" — note how it constrains the output to a single, predictable value that the delivery step can act on.

**3. Delivery.** Delivery is "an event a Zap performs after it's triggered" — the action taken with the AI's output. Examples include applying a Gmail label, sending a Slack message, adding a row to a sheet, or creating a task. This is the "...do that" half of the model.

A concrete end-to-end example ties the three stages together: a Gmail "new email" trigger feeds an LLM classify step (sorting into categories such as Support, Sales, Complaints, Information, or Other), which then drives delivery — drafting a labeled response, applying the Gmail label, and logging the result to Google Sheets. The same skeleton scales to many business cases: an email analyser (email → summarize → Slack), a meeting summariser (new file → summarize → Slack), an application screener (email → extract and rate fit → sheet), or a ticket router (form/email → categorize and rate urgency → create prioritized task).

The practical design discipline is to start simple: one trigger, one AI step, one delivery. A working simple automation beats an incomplete complex one. Because the AI step's output is consumed by a downstream delivery action, making that output narrow and predictable (as the classification prompt does) is what keeps the whole automation reliable.

## Why it matters for a Project Manager

The trigger → AI → delivery anatomy is a planning and communication tool, not just an engineering pattern. It lets you specify, estimate, and de-risk any automation in three questions:

- **It turns vague requests into scoped work.** "Automate our intake" becomes three concrete decisions: what is the trigger, what should the AI do, and where does the output go. Each is independently estimable, and gaps surface immediately ("we never decided where the result lands").
- **The AI step is where the risk concentrates.** Triggers and delivery actions are usually well-understood connectors. The AI step is the one whose output quality is uncertain — so that is where to focus testing, acceptance criteria, and prompt iteration. Treat a vague prompt as an unfinished requirement.
- **"Start simple" is a delivery strategy.** One trigger, one AI step, one delivery ships a working result fast and creates something to learn from. Resist scope creep that turns a first automation into a multi-branch system before the basic version proves value.
- **Reusable skeleton, predictable estimates.** Because every automation shares the same anatomy, your team builds estimating intuition quickly, and the [process-mapping](06-process-mapping.md) exercise can slot each candidate process into the same template.

The outcome you want: every proposed automation is described as a concrete trigger, a defined AI task with a constrained output, and a specific delivery action — before it enters the plan.

## Common pitfalls

- **Leaving the AI output unconstrained.** If the prompt does not pin down the exact output shape, the delivery step gets unreliable input and the whole automation becomes flaky. Constrain the output (as the "respond with only the category name" example does).
- **Skipping prompt rigor.** Because the AI step runs autonomously and cannot ask questions, a fuzzy prompt is a defect. Demand explicit, example-backed prompts with defined success criteria.
- **Building complex before building working.** Multi-branch first attempts often never ship. Insist on one-trigger / one-AI-step / one-delivery for the first version.
- **Forgetting the delivery decision.** Teams sometimes nail the trigger and the AI step but leave "what happens with the result" undefined, producing output nobody acts on.
- **Assuming the AI step is reliable like a connector.** Triggers and deliveries are deterministic; the AI step is probabilistic and needs validation and monitoring.

## Sources

- General: [AI workflows: How to use AI in your business (Zapier)](https://zapier.com/blog/ai-workflows/)
- Specific: [Workflow automation: Definition, tutorial, and tools (Zapier)](https://zapier.com/blog/workflow-automation/)
- Specific: [Automated email classification & response system with Gmail, GPT, and Sheets (n8n template)](https://n8n.io/workflows/7839-automated-email-classification-and-response-system-with-gmail-gpt-and-sheets/)
- Specific: [Prompting best practices (Claude Docs)](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices)

## References

1. Zapier — *AI workflows: How to use AI in your business*. https://zapier.com/blog/ai-workflows/
2. Zapier — *Workflow automation: Definition, tutorial, and tools*. https://zapier.com/blog/workflow-automation/
3. n8n — *Automated email classification & response system with Gmail, GPT, and Sheets*. https://n8n.io/workflows/7839-automated-email-classification-and-response-system-with-gmail-gpt-and-sheets/
4. Anthropic — *Prompting best practices (Claude Docs)*. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices
