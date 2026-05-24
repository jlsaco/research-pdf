# Slide 5 — What Is an API?

## What this slide says
This reading (~25 minutes) demystifies APIs with the restaurant analogy: you (the client) give your order to the waiter (the API), who takes it to the kitchen (the server/model); the kitchen prepares the food and the waiter brings it back (the response) — you never enter the kitchen yourself. Applied to AI: your prompt is the order, the AI model is the kitchen, and the API is the waiter. The slide then introduces four core API concepts: Request/Response (send a prompt, get output back), Authentication (an API key proves who you are), Rate Limits (the maximum requests per minute/hour), and Endpoints (different URLs for different capabilities).

## Key concepts
- An API is an intermediary that carries requests to a system and brings back responses.
- Restaurant analogy: client → waiter (API) → kitchen (server/model) → response.
- For AI: prompt = order, model = kitchen, API = waiter.
- Request/Response: the basic send-and-receive cycle.
- Authentication: an API key identifies and authorizes the caller.
- Rate Limits: caps on how many requests you can make per time window.
- Endpoints: distinct URLs exposing different capabilities.

## Linked topics
- [APIs fundamentals](../topics/01-apis-fundamentals.md)

## Notes for a Project Manager
You don't need to write API calls, but understanding these four concepts lets you scope and de-risk projects. Authentication means someone must manage API keys (a security and ownership concern — who holds the key, where it's stored). Rate Limits translate directly into throughput planning: if a process must handle 200 emails a day, rate limits and per-call costs determine feasibility and budget. Endpoints map to features, so "can we do X?" often reduces to "is there an endpoint for X?" The restaurant analogy is a handy way to explain to non-technical stakeholders why integration work is real work — the kitchen still has to cook, and waiting/throughput is a constraint you plan around.
