# Five Integration Patterns for Connecting AI Systems

## Summary

Once you understand what an [API](01-apis-fundamentals.md) is, the next question is *how* systems actually exchange data with it. The deck presents five integration patterns: **Synchronous** (send a request, wait, then proceed), **Event-Driven** (a trigger fires and processing happens in the background), **Batch** (collect items and process them together on a schedule), **Streaming** (receive partial results as they are generated), and **Tool Use** (the AI itself decides which tools to invoke mid-response). Each suits a different timing and workload. The slide's key guidance is to "start with Event-Driven" — a trigger fires, AI processes, a result is delivered — because that is precisely the pattern no-code tools like Zapier and Make are built for, making it the easiest on-ramp for the rest of Week 4.

## Prerequisite concepts

- Synchronous vs asynchronous processing — does the caller wait or continue?
- Event-driven architecture and webhooks — push vs pull triggering.
- Batch processing — grouping work to run on a schedule.
- Streaming responses and token streaming — progressive output from an LLM.
- LLM tool use / function calling — the model requesting an action mid-response.

## Deep dive

At the most general level, API integrations fall into two broad families: **request-response** (you ask, you get an answer — REST, RPC, GraphQL) and **event-driven** (something happens, and the system reacts — polling, WebSockets, webhooks). The deck's five patterns sit across these two families.

**Synchronous.** The client makes a request and blocks — it waits for the server's response before doing anything else. This is best for real-time, low-latency cases where you need immediate confirmation, such as a form submit that returns a result on the same page. It is simple to reason about, but the caller is stuck waiting.

**Event-Driven.** Instead of waiting, the client continues and is notified later when something happens. The core mechanism is the **webhook**: a lightweight, event-driven HTTP callback where the client registers a URL and the server *pushes* the payload automatically when the event occurs — rather than the client repeatedly *polling* to ask "is it ready yet?" Webhook triggers are what enable hands-off automation (for example, a change automatically launching a downstream task with no human in the loop). This push model is the heart of the "trigger fires → AI processes → result delivered" flow, and it is what Zapier and Make are built around. (More broadly, this is **asynchronous** processing: the request is submitted, the caller moves on, and the result is delivered later via a callback or webhook — ideal for long-running jobs and scalability.)

**Batch.** Rather than handling items one at a time, you collect them and process the group together, usually on a schedule (e.g. "nightly, process all the day's tickets"). A Batch API processes large groups of requests asynchronously at roughly 50% lower cost, completing within a 24-hour window. It is ideal when immediate responses are not needed — classification, evaluations, embeddings — and trades latency for cost and throughput.

**Streaming.** Instead of waiting for a full response, the system emits tokens as they are generated, displaying output progressively — the way text appears word by word in a chat interface. This does not make the work faster, but it dramatically improves *perceived* responsiveness, which matters for user-facing experiences.

**Tool Use (function calling).** Here the AI decides, mid-response, which tools to invoke. The flow is: (1) call the model with the available tools, (2) the model returns a structured tool call — a function name plus JSON arguments, (3) your application executes that function, (4) the tool output is sent back to the model, (5) the model returns a final response (or requests more tools). Crucially, **the model does not execute the function itself** — your code does. This is the most flexible pattern and the conceptual bridge to the agents and orchestration previewed for Week 5.

The takeaway is to match the pattern to the need: synchronous for instant confirmation, event-driven for reactive automation, batch for cheap bulk work, streaming for responsive UX, and tool use for autonomous decisions. For learning and for most business automations, event-driven is the right starting point.

## Why it matters for a Project Manager

The integration pattern is an early architectural decision with direct consequences for timeline, cost, and user experience — so it belongs in scoping conversations, not just in engineering:

- **Event-driven is usually the lowest-risk delivery path.** Because it is the native model for no-code tools, choosing it often means a faster build with non-specialist effort. When a team proposes a synchronous or custom approach for something that is naturally event-driven, ask why.
- **Batch is a cost lever, not a feature.** If a workload tolerates delay (overnight reports, bulk classification), batching can roughly halve AI run-costs. That is a budget conversation worth having explicitly.
- **Streaming is a UX decision, not a performance fix.** It improves how fast something *feels* without changing actual completion time. Use it to manage expectations for user-facing features; do not let it be sold as a speed improvement.
- **Tool use raises the autonomy and the risk.** Letting the AI decide which actions to take is powerful but harder to test and govern. Treat it as a higher-complexity, higher-oversight tier — closely related to the [automation anatomy](04-automation-anatomy.md) and the upper tiers of the [tool spectrum](03-tool-spectrum.md).

The outcome you want: confirm the chosen pattern matches the real-world timing requirement (instant vs reactive vs scheduled) before estimates are locked.

## Common pitfalls

- **Forcing synchronous waits on slow work.** Making a user (or system) block on a long AI call leads to timeouts and poor experience; long jobs belong in event-driven or batch flows.
- **Polling when a webhook would do.** Constant polling wastes resources and adds latency. Prefer event-driven webhooks where the source system supports them.
- **Mistaking streaming for speed.** Streaming improves perceived responsiveness only; total processing time is unchanged.
- **Underestimating tool-use complexity.** Because the model chooses actions dynamically, these flows are harder to test exhaustively and need extra guardrails and review time.
- **Ignoring batch's latency window.** Batch can take up to a full day to complete; never use it where users expect a near-real-time answer.

## Sources

- General: [API Integration Patterns — REST, RPC, GraphQL, Polling, WebSockets and WebHooks (freeCodeCamp)](https://www.freecodecamp.org/news/api-integration-patterns/)
- Specific: [What is a webhook? (Red Hat)](https://www.redhat.com/en/topics/automation/what-is-a-webhook)
- Specific: [The Differences Between Synchronous and Asynchronous APIs (Nordic APIs)](https://nordicapis.com/the-differences-between-synchronous-and-asynchronous-apis/)
- Specific: [Batch API guide (OpenAI)](https://developers.openai.com/api/docs/guides/batch)
- Specific: [Streaming (LangChain docs)](https://docs.langchain.com/oss/python/langchain/streaming)
- Specific: [Function calling (OpenAI)](https://developers.openai.com/api/docs/guides/function-calling)

## References

1. freeCodeCamp — *API Integration Patterns: REST, RPC, GraphQL, Polling, WebSockets and WebHooks*. https://www.freecodecamp.org/news/api-integration-patterns/
2. Red Hat — *What is a webhook?* https://www.redhat.com/en/topics/automation/what-is-a-webhook
3. Nordic APIs — *The Differences Between Synchronous and Asynchronous APIs*. https://nordicapis.com/the-differences-between-synchronous-and-asynchronous-apis/
4. OpenAI — *Batch API guide*. https://developers.openai.com/api/docs/guides/batch
5. LangChain — *Streaming*. https://docs.langchain.com/oss/python/langchain/streaming
6. OpenAI — *Function calling*. https://developers.openai.com/api/docs/guides/function-calling
