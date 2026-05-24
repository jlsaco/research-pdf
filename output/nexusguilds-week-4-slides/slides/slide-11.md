# Slide 11 — Exercise 4.A: Three Ways to Automate

## What this slide says
This slide (25 minutes, follow-along) builds the same automation three different ways to show how it looks at different points on the tool spectrum. The shared flow: a new Gmail email triggers an LLM that classifies it as Urgent / Question / FYI / Spam, then a Gmail label is applied. The three implementations are: Zapier (a drag-and-drop visual builder — fastest to build, no code, limited flexibility); Make (a visual flow with an HTTP module calling the API directly, so you see the raw request — more control, you see the API call underneath); and cURL / Python (a terminal command and script hitting the same API with the same prompt — maximum control, you handle everything yourself). It closes with a reflective key question: "Which version would you maintain? Which could your non-technical colleague build?"

## Key concepts
- One identical automation, three implementations spanning No-Code, the API-visible middle, and full code.
- The core trade-off made tangible: build speed and accessibility versus control and flexibility.
- Zapier favours speed and approachability; Make exposes the underlying API call; cURL/Python gives total control at the cost of effort.
- The maintainability question reframes "which is best" as "which fits who will build and own it."

## Linked topics
- [Build automation hands-on](../topics/05-build-automation-hands-on.md)
- [The tool spectrum](../topics/03-tool-spectrum.md)

## Notes for a Project Manager
This exercise is, in effect, a build-versus-buy and total-cost-of-ownership lesson in miniature. The two closing questions — who maintains it, and who could build it — are exactly the questions a PM should ask before greenlighting any automation. The same outcome can be reached at very different cost and bus-factor: a no-code Zapier flow a business analyst can own, versus a Python script only an engineer can touch. When scoping automation work, push the team to default to the lowest-effort tier that meets the need, and reserve code for cases where flexibility genuinely justifies the higher maintenance burden.
