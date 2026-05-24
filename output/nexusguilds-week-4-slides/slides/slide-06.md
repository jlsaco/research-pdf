# Slide 6 — Five Integration Patterns

## What this slide says
This reading (~20 minutes) presents the five ways systems integrate with APIs. Synchronous: send a request, wait, then proceed (e.g., form submit → API → result on page). Event-Driven: a trigger fires and processing happens in the background (e.g., new email → classify → route). Batch: collect items and process them together on a schedule (e.g., nightly processing of the day's tickets). Streaming: receive partial results as they're generated (e.g., ChatGPT tokens appearing word by word). Tool Use: the AI decides which tools to invoke mid-response (e.g., Claude calling a weather API plus a calculator). The slide advises starting with Event-Driven — trigger fires → AI processes → result delivered — because that is exactly what Zapier and Make are built for.

## Key concepts
- Synchronous: blocking request/response; caller waits for the result.
- Event-Driven: a trigger kicks off background processing.
- Batch: items are collected and processed together on a schedule.
- Streaming: partial results stream back as they are produced.
- Tool Use: the AI autonomously calls tools during a response.
- Recommended entry point: Event-Driven, the model behind no-code tools (Zapier, Make).

## Linked topics
- [Integration patterns](../topics/02-integration-patterns.md)

## Notes for a Project Manager
These patterns are really a vocabulary for describing how a process behaves, which helps you size and prioritize work. Synchronous fits user-facing, real-time needs; Batch fits high-volume, non-urgent jobs and is often the cheapest to run; Event-Driven is the sweet spot for most workflow automation and the easiest to deliver with no-code tools. When intake a request, identifying the pattern early tells you which tool tier and which team member can build it. The guidance to "start with Event-Driven" is a useful default for quick wins — it lets non-technical team members ship automations on Zapier or Make without engineering involvement.
