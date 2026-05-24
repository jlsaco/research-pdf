# Process Mapping and Choosing the Right Tier

## Summary

This topic covers the Week 4 process-mapping workshop: working in pairs to map 5–10 real business processes onto the four tiers of the automation tool spectrum. For each process you document its name, volume/frequency, recommended tier, a justification, and an estimated effort — for example, "classify customer emails / 200 a day / No-Code / Zapier handles simple classification / ~2 hours" versus "analyse contracts vs. compliance rules / 5 a week / AI-Assisted Code / complex business logic + long documents / ~3 days." The choice of tier is driven by four decision questions: Who will build it? Who will maintain it? How complex is the logic? What scale do you need? The output is more than an exercise — it becomes the raw material for Week 5's agent-design work. The deeper skill here is classic business process mapping (identify, document, sequence, analyze) combined with sound automation-prioritization criteria.

## Prerequisite concepts

- **Business process mapping** — documenting what a process does, who is responsible, and how success is measured.
- **The tool spectrum** — the four tiers you map processes onto (see [The Tool Spectrum](03-tool-spectrum.md)).
- **Evaluating process volume and frequency** — weighing how often a process runs and at what volume.
- **Decision criteria for tooling** — who builds, who maintains, logic complexity, and required scale.
- **Effort estimation** — turning a tier choice into a realistic build estimate (hours vs. days).
- **The Trigger → AI → Delivery anatomy** — how each mapped process will eventually be built (see [Anatomy of an AI Automation](04-automation-anatomy.md)).

## Deep dive

**What process mapping is.** Business process mapping defines what a business does, who is responsible, to what standard, and how success is measured; its purpose is to make the organization more effective and to surface improvement opportunities. The classic methodology proceeds through process identification, information gathering, mapping, and analysis (then installing new methods and managing the process). A practical 6-step version: select a process, document all activities, sequence the steps, draw the flowchart with standard symbols, get team feedback, then identify improvements. Different map types fit different needs — a simple flowchart for basic flows, swimlane maps for cross-functional roles, value-stream maps for lean/waste analysis, SIPOC for scoping, and BPMN when the map will drive automation or system integration.

**Mapping processes to tiers.** Once a process is mapped, the workshop assigns it to a tool-spectrum tier using four questions: *Who will build it? Who will maintain it? How complex is the logic? What scale do you need?* These map onto established tool-selection criteria: assess workflow complexity (simple data passing vs. multi-step logic), integration with your existing tech stack, estimated monthly task volume for cost planning, and scalability (SSO, permissions, pricing growth). The no-code/low-code split follows the same logic: no-code targets non-technical builders with visual, pre-built components but a lower customization ceiling; low-code requires some coding skill and suits developers or tech-savvy users when logic is more complex or deeper customization is needed.

**Prioritizing what to automate.** Not every process deserves automation, and not in any order. Prioritize processes that are high-volume/high-frequency, manual and repetitive, standardized (ideally under a ~15–20% exception rate), and rule-based with clear, consistent logic. A crucial nuance: a complex process that runs only once a month has less operational impact than a simpler one that runs constantly — weigh volume × frequency, not complexity alone. A complete decision framework weighs repetitiveness, frequency and volume, complexity and risk, customer impact, and resource requirements, and then validates the choice with a pilot and ROI metrics before broad rollout. This is exactly how the worked table behaves: 200 emails/day at low complexity earns a 2-hour no-code build, while a low-volume but logic-heavy contract review lands at AI-assisted code and a multi-day effort. The finished map then feeds directly into Week 5's agent-design exercises (see [Module Framing, Deliverables, and the Path to Orchestration](07-course-framing-and-orchestration-preview.md)).

## Why it matters for a Project Manager

Process mapping and tier selection are, in effect, the Project Manager's intake and triage process for an automation portfolio:

- **Outcomes:** A process map turns a vague "let's automate things" into a prioritized, sized backlog. Each row carries a recommended tier and an effort estimate — the inputs you need to sequence work and forecast capacity.
- **Trade-offs:** The four questions (who builds / who maintains / how complex / what scale) are exactly the trade-offs you own. Pushing a process up the spectrum buys flexibility and scale at the cost of developer time and ongoing maintenance; keeping it no-code keeps it cheap and team-owned but caps complexity.
- **Timelines:** Effort estimates ("~2 hours" vs. "~3 days") are first-pass story points. Combined with volume × frequency, they let you prioritize the high-ROI, high-frequency, rule-based processes first and defer the low-volume, logic-heavy ones.
- **Risk:** Prioritization criteria are risk controls. Favoring standardized, low-exception, rule-based processes steers you away from brittle automations; the pilot-and-ROI step keeps you from over-investing before value is proven. Document volume, tier, justification, and effort so every automation decision is defensible to stakeholders.

## Common pitfalls

- **Choosing the tier by complexity alone.** A logic-heavy process that runs five times a month may matter less than a simple one running constantly — weigh volume × frequency, not difficulty.
- **Automating non-standardized processes.** Mapping a process with a high exception rate (above ~15–20%) onto automation produces fragile flows that break on edge cases.
- **Skipping the "who maintains it" question.** Picking a powerful tier without naming an owner leaves automations that no one can fix when they drift.
- **Over-mapping / analysis paralysis.** Producing exhaustive BPMN diagrams when a simple flowchart would do, and never reaching the prioritization and build steps.
- **No pilot or ROI check.** Committing to broad rollout before validating value on a single process — the framework explicitly calls for a pilot first.

## Sources

- General: [Business process mapping — Wikipedia](https://en.wikipedia.org/wiki/Business_process_mapping)
- General: [What Is Process Mapping? Steps, Types, Examples & Template — Asana](https://asana.com/resources/process-mapping)
- Specific: [How to choose the best automation software — Zapier](https://zapier.com/blog/how-to-choose-the-best-automation-software/)
- Specific: [Low-code vs. no-code: Key differences and benefits — Zapier](https://zapier.com/blog/low-code-vs-no-code/)
- Specific: [Select Business Processes for Automation: a Comprehensive Checklist — ProcessMaker](https://www.processmaker.com/blog/select-business-processes-for-automation-a-comprehensive-checklist/)
- Specific: [How to decide which processes to automate: A practical guide — Qntrl](https://www.qntrl.com/blog/automate-process.html)

## References

1. Business process mapping — Wikipedia. https://en.wikipedia.org/wiki/Business_process_mapping
2. What Is Process Mapping? Steps, Types, Examples & Template — Asana. https://asana.com/resources/process-mapping
3. How to choose the best automation software — Zapier. https://zapier.com/blog/how-to-choose-the-best-automation-software/
4. Low-code vs. no-code: Key differences and benefits — Zapier. https://zapier.com/blog/low-code-vs-no-code/
5. Select Business Processes for Automation: a Comprehensive Checklist — ProcessMaker. https://www.processmaker.com/blog/select-business-processes-for-automation-a-comprehensive-checklist/
6. How to decide which processes to automate: A practical guide — Qntrl. https://www.qntrl.com/blog/automate-process.html
