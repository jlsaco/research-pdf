# Findings — What an API Is and How AI Model APIs Work (apis-fundamentals)

## General source(s)
- [Introduction to web APIs — MDN](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Client-side_APIs/Introduction) — Beginner-friendly definition of what an API is, the "interface/contract" idea, and the difference between browser APIs and third-party (remote service) APIs. Good for the client-server / interface foundation.
- [API — Wikipedia](https://en.wikipedia.org/wiki/API) — High-level, vendor-neutral definition: an API is a connection between programs, used for machine-to-machine communication. Covers the request/response (API call → API response) pattern and names endpoints; notes web APIs typically use HTTP with JSON/XML payloads.

## Specific sources
- [API overview — Claude API Docs (platform.claude.com)](https://platform.claude.com/docs/en/api/overview) — Covers LLM/AI model API basics: a RESTful API at `https://api.anthropic.com`, named endpoints (Messages API `POST /v1/messages`, Models API `GET /v1/models`, etc.), request/response format, response headers (`request-id`), AND authentication via the `x-api-key` header with keys from the Console. Covers the API-endpoints, AI-model-API-basics, and API-authentication/keys prerequisites.
- [Rate limits — Claude API Docs (platform.claude.com)](https://platform.claude.com/docs/en/api/rate-limits) — Covers the rate-limiting prerequisite: RPM/token-per-minute limits, usage tiers, the token bucket algorithm, 429 errors, and the `retry-after` / `anthropic-ratelimit-*` response headers.

> Note: the original trusted-source URLs `https://docs.anthropic.com/en/api/overview` and `https://docs.claude.com/en/api/rate-limits` return HTTP 301 redirects to the canonical `platform.claude.com` URLs cited above (both resolve 200). The canonical URLs are used here.

## Key facts
- An API (Application Programming Interface) is an interface/contract that lets two software systems communicate across a boundary using agreed-upon signals, hiding internal complexity and exposing only the useful parts. — source: https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Client-side_APIs/Introduction
- APIs are an "under the hood" mechanism for machine-to-machine communication; the message that triggers a service is an "API call" and the reply is the "API response." The individual calls are also known as endpoints. — source: https://en.wikipedia.org/wiki/API
- Web APIs typically use HTTP request messages plus a defined response structure, usually in JSON or XML format. — source: https://en.wikipedia.org/wiki/API
- The Claude (AI model) API is a RESTful API at `https://api.anthropic.com`; clients send requests to specific endpoints such as the Messages API (`POST /v1/messages`) and receive a structured response. — source: https://platform.claude.com/docs/en/api/overview
- Authentication: every request must include the `x-api-key` header (an API key generated in the Console) plus `anthropic-version` and `content-type` headers; keys can be segmented across workspaces to control spend. — source: https://platform.claude.com/docs/en/api/overview
- Every API response includes a `request-id` (globally unique request identifier) and `anthropic-organization-id` header. — source: https://platform.claude.com/docs/en/api/overview
- Rate limits cap how much an organization can use the API; for the Messages API they are measured in requests per minute (RPM), input tokens per minute (ITPM), and output tokens per minute (OTPM), and increase automatically by usage tier. — source: https://platform.claude.com/docs/en/api/rate-limits
- Rate limiting uses the token bucket algorithm (capacity is continuously replenished). Exceeding a limit returns a 429 error with a `retry-after` header indicating how long to wait. — source: https://platform.claude.com/docs/en/api/rate-limits

## Verification checklist
| URL | HTTP | Supports |
|-----|------|----------|
| https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Client-side_APIs/Introduction | 200 | Beginner definition of an API as an interface/contract; browser vs third-party APIs (client-server foundation). |
| https://en.wikipedia.org/wiki/API | 200 | Vendor-neutral API definition, API call/response pattern, endpoints, HTTP+JSON/XML for web APIs. |
| https://platform.claude.com/docs/en/api/overview | 200 | AI model API basics: REST endpoints (Messages API), request/response format, `x-api-key` authentication and API keys, response headers. (docs.anthropic.com/docs.claude.com 301-redirect here.) |
| https://platform.claude.com/docs/en/api/rate-limits | 200 | Rate limits (RPM/ITPM/OTPM), usage tiers, token bucket algorithm, 429 + `retry-after`. (docs.claude.com 301-redirects here.) |
