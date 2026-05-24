# What an API Is and How AI Model APIs Work

## Summary

An API (Application Programming Interface) is the contract that lets two software systems talk to each other across a boundary. The deck explains it with the restaurant analogy: you (the client) give your order to the waiter (the API), the waiter carries it to the kitchen (the server or AI model), and brings the prepared result back as a response — you never enter the kitchen yourself. When you call an AI model's API, your prompt is the order, the model is the kitchen, and the API is the waiter. Four concepts govern every such integration: request/response, authentication (the API key that proves who you are), rate limits (how many requests you may send), and endpoints (different URLs for different capabilities). This topic is the foundation for everything else in Week 4 — the integration patterns, tool spectrum, and automation anatomy all assume you know what is happening when a system "calls an API."

## Prerequisite concepts

- The client-server model: one program asks (client), another answers (server).
- The HTTP request/response cycle — how web systems exchange messages.
- API authentication and API keys — proving identity to a service.
- Rate limiting — caps on how often you can call a service.
- API endpoints — distinct URLs for distinct capabilities.
- LLM/AI model API basics — sending a prompt and receiving a structured response.

## Deep dive

An API is an interface, or contract, that lets two software systems communicate across a boundary using agreed-upon signals. It hides internal complexity and exposes only the useful parts, so the caller never needs to know how the other side works internally. Vendor-neutrally, an API is simply a connection between programs for machine-to-machine communication: the message that triggers a service is an "API call" and the reply is the "API response." Web APIs typically carry these messages over HTTP with payloads structured as JSON or XML.

Applying this to AI, an AI model's API works the same way. The Claude API, for example, is a RESTful API at `https://api.anthropic.com`; a client sends a request to a specific endpoint — such as the Messages API (`POST /v1/messages`) — and receives a structured response. Different endpoints expose different capabilities, which is exactly the "different URLs for different capabilities" idea on the slide.

The four API concepts map directly onto real mechanics:

- **Request/Response** — You send a prompt and get output back. This is the API call and the API response.
- **Authentication** — Every request must include credentials. With Claude, that is the `x-api-key` header containing a key generated in the Console (alongside `anthropic-version` and `content-type` headers). Keys can be segmented across workspaces to control spend — a useful governance lever.
- **Rate limits** — Limits cap how much an organization can use the API. For the Messages API they are measured in requests per minute (RPM), input tokens per minute (ITPM), and output tokens per minute (OTPM), and they rise automatically as your usage tier increases. The mechanism is a token bucket algorithm, and exceeding a limit returns an HTTP 429 error with a `retry-after` header telling you how long to wait.
- **Endpoints** — Distinct URLs route to distinct capabilities (e.g. a Messages endpoint versus a Models endpoint). Responses also carry useful metadata such as a globally unique `request-id`, which is invaluable for support and debugging.

Together these four concepts explain not just how to make one call, but how integrations behave under load, cost, and failure — the practical concerns that show up the moment an automation runs in production. From here, the natural next step is understanding the [integration patterns](02-integration-patterns.md) that determine *when* and *how* those calls are made.

## Why it matters for a Project Manager

You will rarely write the API call yourself, but the four concepts are the vocabulary you need to scope work, manage risk, and read estimates honestly:

- **Authentication = a dependency and a security item.** Every integration needs credentials. Who owns the API key, where it is stored, and who can rotate it are real backlog items and audit questions — not afterthoughts.
- **Rate limits = a scope and timeline constraint.** A solution that works in a demo can fail at production volume if it hits RPM or token limits. When someone says "it'll just call the AI," ask what the expected request volume is and whether it fits the rate tier; the answer affects both architecture and cost.
- **Endpoints and request/response = the integration surface.** The number of distinct endpoints a vendor exposes is a rough proxy for integration effort. More capabilities can mean more value but also more to test and maintain.
- **Cost is metered.** Because usage is measured in tokens and requests, AI features have a recurring run-cost, not just a build cost. Factor that into the business case and into the trade-off between tiers in the [tool spectrum](03-tool-spectrum.md).

The outcome you want from this topic is the ability to ask the right questions — volume, auth ownership, failure handling, cost — before committing a timeline.

## Common pitfalls

- **Treating the API key as harmless.** Leaking a key exposes spend and data. Confirm keys live in a secrets manager, not in spreadsheets, chat messages, or committed code.
- **Ignoring rate limits until launch.** A 429 error under real load is a predictable failure, not a surprise. Validate expected volume against the rate tier during planning.
- **Assuming all responses succeed.** Real integrations must handle 429s (respecting `retry-after`) and other errors gracefully; "happy path only" estimates undercount the work.
- **Confusing "has an API" with "is easy to integrate."** Many endpoints, complex auth, and tight rate limits all add effort. The existence of an API is a starting point, not a guarantee of low cost.

## Sources

- General: [Introduction to web APIs — MDN](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Client-side_APIs/Introduction)
- General: [API — Wikipedia](https://en.wikipedia.org/wiki/API)
- Specific: [API overview — Claude API Docs](https://platform.claude.com/docs/en/api/overview)
- Specific: [Rate limits — Claude API Docs](https://platform.claude.com/docs/en/api/rate-limits)

## References

1. MDN Web Docs — *Introduction to web APIs*. https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Client-side_APIs/Introduction
2. Wikipedia — *API*. https://en.wikipedia.org/wiki/API
3. Anthropic — *API overview (Claude API Docs)*. https://platform.claude.com/docs/en/api/overview
4. Anthropic — *Rate limits (Claude API Docs)*. https://platform.claude.com/docs/en/api/rate-limits
