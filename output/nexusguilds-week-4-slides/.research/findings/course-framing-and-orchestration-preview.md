# Findings — Module Framing, Deliverables, and the Path to Orchestration (course-framing-and-orchestration-preview)

Role: Project Manager · Language (output): en · Depth: standard · Research language: English

## General source(s)
- [Building Effective Agents (Anthropic, Engineering)](https://www.anthropic.com/engineering/building-effective-agents) — High-level framing for the whole "path to orchestration" arc: defines the spectrum from single LLM calls to workflows to fully autonomous agents, and gives the canonical distinction between orchestrated workflows and self-directing agents. Trusted source (Anthropic).

## Specific sources
- [The Difference Between Using AI and Integrating It (Purple Frog Systems)](https://www.purplefrogsystems.com/2026/02/the-difference-between-using-ai-and-integrating-it/) — Covers the prerequisite "AI user vs AI integrator": using AI = prompt/interface literacy with existing tools; integrating AI = structural, ROI-driven embedding into processes.
- [How to orchestrate AI workflows in 7 steps (Zapier)](https://zapier.com/blog/ai-orchestration-workflows/) — Covers "automation as a spectrum", "multi-step workflow chaining", and "AI orchestration vs single automation": contrasts a single trigger-action automation with orchestration that coordinates multiple AI steps/tools with adaptive logic. Trusted source (Zapier).
- [What is an AI agent? (LangChain)](https://www.langchain.com/blog/what-is-an-agent) — Covers "autonomous AI agents" and "AI orchestration vs single automation": defines an agent as a system that uses an LLM to decide the control flow, and frames a spectrum of agentic capability from routers to fully autonomous agents. Trusted source (LangChain).

## Key facts
- A workflow is a system "where LLMs and tools are orchestrated through predefined code paths," whereas an agent is a system "where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks." — source: https://www.anthropic.com/engineering/building-effective-agents
- Common orchestration patterns for chaining multiple steps include prompt chaining, routing, parallelization, orchestrator-workers, and evaluator-optimizer; you should use the simplest pattern that works and only add agentic complexity when needed. — source: https://www.anthropic.com/engineering/building-effective-agents
- AI usage (the "AI user") is interface literacy — e.g., prompt engineering and using Copilot inside an existing productivity suite — and "a well written prompt does not change how a business operates." — source: https://www.purplefrogsystems.com/2026/02/the-difference-between-using-ai-and-integrating-it/
- AI integration (the "AI integrator") is structural: it targets high-value decision points and requires data pipelines, governance, statistical expertise, and alignment to commercial objectives — it "changes how a business operates." — source: https://www.purplefrogsystems.com/2026/02/the-difference-between-using-ai-and-integrating-it/
- A single automation executes one trigger-action pair (e.g., "Triggering a Slack alert when a deal closes"); orchestration "coordinates entire processes across tools and logic layers" (e.g., qualifying a lead, enriching it with AI, then routing it by region and score). — source: https://zapier.com/blog/ai-orchestration-workflows/
- Unlike rigid rule-based workflow automation, AI orchestration "introduces dynamic logic and adaptive behavior" and "lets systems decide what to do next based on real-time inputs," which is the bridge from chained automations toward agents. — source: https://zapier.com/blog/ai-orchestration-workflows/
- An AI agent is "a system that uses an LLM to decide the control flow of an application"; agentic capability is a spectrum (routers, state machines, up to fully autonomous agents), increasing as the LLM makes more of the decisions. — source: https://www.langchain.com/blog/what-is-an-agent

## Verification checklist
| URL | HTTP | Supports |
|-----|------|----------|
| https://www.anthropic.com/engineering/building-effective-agents | 200 | Workflow vs agent definitions; orchestration patterns (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer). |
| https://www.purplefrogsystems.com/2026/02/the-difference-between-using-ai-and-integrating-it/ | 200 | AI user (using AI = interface literacy) vs AI integrator (structural integration that changes operations). |
| https://zapier.com/blog/ai-orchestration-workflows/ | 200 | Single automation vs orchestration; multi-step chaining of AI steps/tools; dynamic, adaptive orchestration logic. |
| https://www.langchain.com/blog/what-is-an-agent | 200 | Autonomous agent definition (LLM decides control flow); spectrum of agentic capability. |
| https://www.datacamp.com/tutorial/building-langchain-agents-to-automate-tasks-in-python | 403 | DISCARDED — bot-blocked (403), not cited. |
