# Slide 8 — Anatomy of an AI Automation

## What this slide says
This reading (~20 minutes) breaks every AI automation into three universal stages. (1) Trigger — the event that starts it: a new email, form response, file upload, or scheduled time. (2) AI Processing — the LLM acts on the input: classify, summarise, extract, or generate, using CRFT prompts. (3) Delivery — an action is taken with the output: add to a sheet, send a Slack message, create a task, or apply a label. The slide anchors this with an Email Classification example: Trigger (new email in Gmail) → AI ("Classify as Urgent, Question, FYI, or Spam. Respond with only the category name.") → Delivery (apply a Gmail label, optionally forward).

## Key concepts
- Every AI automation has the same three-stage structure: Trigger → AI Processing → Delivery.
- Trigger: the initiating event (email, form, file upload, schedule).
- AI Processing: the LLM step (classify, summarise, extract, generate) driven by CRFT prompts.
- Delivery: the downstream action (sheet row, Slack message, task, label).
- Worked example: Gmail email → classify into four categories → apply a label.
- Callback to CRFT prompting from earlier in the course.

## Linked topics
- [Automation anatomy](../topics/04-automation-anatomy.md)

## Notes for a Project Manager
The Trigger → AI → Delivery template is a ready-made way to specify automation requirements. When a stakeholder asks for an automation, force the conversation into these three boxes: What event starts it? What should the AI do? Where does the result go? If any box is fuzzy, the request isn't ready to build. This structure also makes scoping and testing predictable — each stage can be validated independently, and most failures localize to a single box (a flaky trigger, a weak prompt, or a broken delivery). It's the cleanest mental model for writing a one-line spec or acceptance criteria for any automation in your backlog.
