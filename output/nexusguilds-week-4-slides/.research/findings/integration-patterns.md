# Findings — Five Integration Patterns for Connecting AI Systems (integration-patterns)

## General source(s)
- [API Integration Patterns – REST, RPC, GraphQL, Polling, WebSockets and WebHooks](https://www.freecodecamp.org/news/api-integration-patterns/) — High-level overview that splits integration into two broad families: request-response (REST, RPC, GraphQL) and event-driven (Polling, WebSockets, WebHooks). Good framing for "five patterns" and the synchronous-vs-event-driven divide.

## Specific sources
- [What is a webhook? (Red Hat)](https://www.redhat.com/en/topics/automation/what-is-a-webhook) — Event-driven architecture & webhooks: defines webhooks as event-driven HTTP callbacks and contrasts the webhook "push" model with the polling "pull" model; covers automation/GitOps triggers.
- [The Differences Between Synchronous and Asynchronous APIs (Nordic APIs)](https://nordicapis.com/the-differences-between-synchronous-and-asynchronous-apis/) — Synchronous vs asynchronous processing: caller blocks/waits vs caller continues and is notified later; use cases for each.
- [Batch API guide (OpenAI, trusted source)](https://developers.openai.com/api/docs/guides/batch) — Batch processing: asynchronous groups of requests, ~50% lower cost, 24-hour completion window; ideal when immediate responses aren't needed.
- [Streaming (LangChain docs, trusted source)](https://docs.langchain.com/oss/python/langchain/streaming) — Streaming responses / token streaming: streaming LLM tokens as they are generated to display output progressively and improve perceived responsiveness.
- [Function calling (OpenAI, trusted source)](https://developers.openai.com/api/docs/guides/function-calling) — LLM tool use / function calling: model returns a structured tool call (name + arguments), the application executes it, returns the output, and the model produces a final response.

## Key facts
- API integrations fall into two broad families: request-response (REST, RPC, GraphQL) and event-driven (Polling, WebSockets, WebHooks). — source: https://www.freecodecamp.org/news/api-integration-patterns/
- WebSockets provide a persistent, two-way communication channel for real-time bidirectional data, more resource-efficient than repeated polling. — source: https://www.freecodecamp.org/news/api-integration-patterns/
- A webhook is a lightweight, event-driven HTTP communication: the client registers a URL and the server pushes the payload automatically when the event occurs, instead of the client polling at intervals. — source: https://www.redhat.com/en/topics/automation/what-is-a-webhook
- Webhook triggers enable event-driven automation (e.g., a git change automatically launches an automation/deploy task without human intervention). — source: https://www.redhat.com/en/topics/automation/what-is-a-webhook
- Synchronous: the client makes a request and waits/blocks for the server's response before proceeding; best for real-time, low-latency, immediate-confirmation cases. — source: https://nordicapis.com/the-differences-between-synchronous-and-asynchronous-apis/
- Asynchronous: the client submits the request and continues working; the server processes independently and notifies later (e.g., callbacks/webhooks); best for long-running jobs and scalability. — source: https://nordicapis.com/the-differences-between-synchronous-and-asynchronous-apis/
- The Batch API processes large groups of requests asynchronously at ~50% lower cost, completing within a 24-hour window; ideal for jobs that don't need immediate responses (evals, classification, embeddings). — source: https://developers.openai.com/api/docs/guides/batch
- Streaming displays LLM output progressively by emitting tokens as they are generated, rather than waiting for the full response, which improves perceived responsiveness. — source: https://docs.langchain.com/oss/python/langchain/streaming
- Function/tool calling flow: (1) call the model with available tools, (2) model returns a tool call (function name + JSON arguments), (3) the application executes the function, (4) the tool output is sent back to the model, (5) the model returns a final response (or more tool calls). The model itself does not execute the function. — source: https://developers.openai.com/api/docs/guides/function-calling

## Verification checklist
| URL | HTTP | Supports |
|-----|------|----------|
| https://www.freecodecamp.org/news/api-integration-patterns/ | 200 | General overview of six integration patterns split into request-response vs event-driven families. |
| https://www.redhat.com/en/topics/automation/what-is-a-webhook | 200 | Defines webhooks as event-driven HTTP callbacks; webhook push vs polling pull; automation triggers. |
| https://nordicapis.com/the-differences-between-synchronous-and-asynchronous-apis/ | 200 | Synchronous (caller blocks) vs asynchronous (caller continues, notified later) distinction and use cases. |
| https://developers.openai.com/api/docs/guides/batch | 200 | Batch API: async groups of requests, ~50% cheaper, 24h completion, for non-immediate jobs. |
| https://docs.langchain.com/oss/python/langchain/streaming | 200 | Token streaming: emit LLM tokens as generated for progressive output and better perceived responsiveness. |
| https://developers.openai.com/api/docs/guides/function-calling | 200 | Function/tool calling flow: model returns structured tool call, app executes, output returned, model finalizes. |
