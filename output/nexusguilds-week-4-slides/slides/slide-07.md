# Slide 7 — The Tool Spectrum

## What this slide says
This reading (~25 minutes) lays out the four-tier tool spectrum for building automations. Tier 1, No-Code (Zapier, Make): simple triggers and linear flows, low maintenance. Tier 2, Low-Code (Retool, n8n): custom logic, branching, and database connections, medium maintenance. Tier 3, AI-Assisted Code (Cursor + API, Replit + API): full flexibility and complex business logic, medium-to-high maintenance. Tier 4, Full Code (Python SDK, Node.js SDK): unlimited capability for production systems and scale, high maintenance. The headline heuristic: about 80% of automation needs can be solved at No-Code; reserve code for the 20% that genuinely needs it.

## Key concepts
- The build options form a spectrum of four tiers, trading simplicity for power.
- Tier 1 No-Code (Zapier, Make): simple, linear, low maintenance.
- Tier 2 Low-Code (Retool, n8n): branching and DB connections, medium maintenance.
- Tier 3 AI-Assisted Code (Cursor/Replit + API): complex logic, med-high maintenance.
- Tier 4 Full Code (Python/Node SDK): unlimited, production-scale, high maintenance.
- 80/20 rule: most needs fit No-Code; reserve code for the genuinely hard 20%.
- Higher tiers mean more capability but more ongoing maintenance.

## Linked topics
- [Tool spectrum](../topics/03-tool-spectrum.md)

## Notes for a Project Manager
This is the single most useful slide for a PM because it converts "how should we build this?" into a defensible tiering decision. The maintenance column is the part to internalize: every step up the spectrum increases ongoing ownership cost, not just build cost — so a Full Code solution you can't staff to maintain is a liability, not a win. The 80/20 rule is a prioritization and cost-control principle: default to No-Code, and require explicit justification before approving anything that needs code. Use the tiers as estimation anchors (low-code = days, code = weeks) and as a way to match work to the right people on a mixed-skill team.
