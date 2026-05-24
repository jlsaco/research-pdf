# Module Framing, Deliverables, and the Path to Orchestration

## Summary

This topic ties together the connective tissue of Week 4: the course/module framing, the session agenda, the deliverables and cumulative portfolio, and the preview of where the course is heading next. Module 2 ("The Workshop") moves learners from *AI user* to *AI integrator* — from prompting tools to connecting AI into real workflows. The motivating story (Andrés's "15 Automations Challenge," a team with wildly mixed skill levels) establishes the week's central idea: automation is a spectrum, not a single skill. Week 4's two deliverables — a working Zapier/Make automation and a process map of 5–10 processes — feed directly into Week 5, where the course makes the leap from *automation* to *orchestration*: chaining AI steps into multi-step workflows, designing autonomous agents that make decisions, and mapping cross-departmental AI workflows. Isolated automations are like individual musicians; orchestration is the orchestra.

## Prerequisite concepts

- **AI user vs. AI integrator** — the shift from using AI through an interface to embedding it structurally into processes.
- **Automation as a spectrum** — the framing that automation ranges across tiers and patterns rather than being one skill (see [The Tool Spectrum](03-tool-spectrum.md)).
- **Learning deliverables / portfolio artifacts** — the cumulative artifacts (Compass, Playbook, Selection Matrix, Prototype, Knowledge Guide, Automation + Map).
- **The Trigger → AI → Delivery anatomy** — the shape of the Week 4 automation deliverable (see [Anatomy of an AI Automation](04-automation-anatomy.md)).
- **Process mapping** — the second deliverable and Week 5's raw material (see [Process Mapping and Choosing the Right Tier](06-process-mapping.md)).
- **Multi-step workflow chaining and autonomous agents** — the Week 5 concepts being previewed.
- **AI orchestration vs. a single automation** — the central distinction in the path ahead.

## Deep dive

**From AI user to AI integrator.** Module 2 reframes the learner's role. AI *usage* is interface literacy — prompt engineering and using an assistant inside an existing productivity suite — and, as the framing source puts it, "a well written prompt does not change how a business operates." AI *integration*, by contrast, is structural: it targets high-value decision points and requires data pipelines, governance, and alignment to commercial objectives — it "changes how a business operates." That is the jump Week 4 begins. Andrés's "15 Automations Challenge" dramatizes it: a team with 15 manual processes and skills ranging from fluent Python to never having written a line. The lesson he reaches — automation is a spectrum, not a single skill — is what makes a single strategy work across a mixed-skill team.

**The week's structure and deliverables.** The session is split into a self-paced pre-reading half (APIs, integration patterns, the tool spectrum, automation anatomy) and a 75%-practical in-class half (build three ways, build your own, process mapping, Week 5 preview). It produces two deliverables: a working Zapier or Make automation (Trigger → AI → Delivery, with a note on which tier and why) and a process map of 5–10 processes mapped to tiers. These join a growing portfolio of six artifacts across the course, with "W4: Automation + Map" as the current addition.

**The path to orchestration.** Week 5 is previewed as the move from automation to orchestration. The distinction is precise: a single automation executes one trigger-action pair (e.g., a Slack alert when a deal closes), whereas orchestration "coordinates entire processes across tools and logic layers" (e.g., qualifying a lead, enriching it with AI, then routing it by region and score). Unlike rigid rule-based automation, AI orchestration "introduces dynamic logic and adaptive behavior" and "lets systems decide what to do next based on real-time inputs" — the bridge from chained automations toward agents. In the canonical framing, a *workflow* is a system "where LLMs and tools are orchestrated through predefined code paths," while an *agent* is a system "where LLMs dynamically direct their own processes and tool usage." Common orchestration patterns for chaining steps include prompt chaining, routing, parallelization, orchestrator-workers, and evaluator-optimizer — and the guiding discipline is to use the simplest pattern that works, adding agentic complexity only when needed. An AI agent, more formally, is "a system that uses an LLM to decide the control flow of an application," with agentic capability forming a spectrum from routers up to fully autonomous agents. That spectrum is exactly where Andrés's isolated automations become an orchestra.

## Why it matters for a Project Manager

This topic is the program-level view a Project Manager needs to plan the whole arc, not just one automation:

- **Outcomes:** The user-to-integrator framing reframes the goal from "people who use AI tools" to "processes that operate differently because AI is embedded." That distinction shapes how you set objectives and measure value — interface literacy doesn't change operations; integration does.
- **Trade-offs:** The automation-vs-orchestration distinction tells you when to stop. A single trigger-action automation is cheap and predictable; orchestration adds dynamic, adaptive logic and far more capability — but also more complexity, cost, and failure surface. The "use the simplest pattern that works" rule is your scope discipline at the architecture level.
- **Timelines:** The two Week 4 deliverables are deliberately staged to feed Week 5 — the process map is the raw material for orchestration design. As a PM, treat the portfolio as a dependency chain: each week's artifact is an input to the next, so slippage compounds downstream.
- **Risk:** Mixed-skill teams (Andrés's reality) are a real delivery risk. Framing automation as a spectrum lets you assign work to the right tier and the right builder. The agent spectrum (router → autonomous agent) is also a governance map: more autonomy means more decisions made by the LLM, which raises oversight, testing, and accountability requirements you must plan for.

## Common pitfalls

- **Confusing using AI with integrating AI.** Declaring success because the team writes good prompts — without changing any process. "A well written prompt does not change how a business operates."
- **Jumping to orchestration/agents too early.** Reaching for multi-step, adaptive, agentic workflows when a single automation would meet the need; the guidance is to use the simplest pattern that works.
- **Treating deliverables as disconnected.** Skipping or under-investing in the process map, then lacking the raw material Week 5's orchestration design depends on.
- **Underestimating autonomy risk.** Granting an agent more control over the control flow without proportionally increasing oversight, testing, and governance.
- **Ignoring the mixed-skill reality.** Picking one tier for the whole team instead of using the spectrum to match work to builders' skill levels.

## Sources

- General: [Building Effective Agents (Anthropic, Engineering)](https://www.anthropic.com/engineering/building-effective-agents)
- Specific: [The Difference Between Using AI and Integrating It (Purple Frog Systems)](https://www.purplefrogsystems.com/2026/02/the-difference-between-using-ai-and-integrating-it/)
- Specific: [How to orchestrate AI workflows in 7 steps (Zapier)](https://zapier.com/blog/ai-orchestration-workflows/)
- Specific: [What is an AI agent? (LangChain)](https://www.langchain.com/blog/what-is-an-agent)

## References

1. Building Effective Agents — Anthropic Engineering. https://www.anthropic.com/engineering/building-effective-agents
2. The Difference Between Using AI and Integrating It — Purple Frog Systems. https://www.purplefrogsystems.com/2026/02/the-difference-between-using-ai-and-integrating-it/
3. How to orchestrate AI workflows in 7 steps — Zapier. https://zapier.com/blog/ai-orchestration-workflows/
4. What is an AI agent? — LangChain. https://www.langchain.com/blog/what-is-an-agent
