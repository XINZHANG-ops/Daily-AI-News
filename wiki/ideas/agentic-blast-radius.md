---
title: "The Agentic Blast Radius"
slug: agentic-blast-radius
last_updated: 2026-06-17
---

# The Agentic Blast Radius

## The Insight
As AI evolves from a "chatbot" (text-in, text-out) to an "agent" (text-in, action-out), the blast radius of any single vulnerability increases exponentially. When an agent is given read/write access to a user's digital identity (email, 2FA, files) to be "helpful," a single prompt injection is no longer just a data leak—it's a full identity compromise.

## Evidence
- [[entities/searchleak]] — A critical flaw in Microsoft Copilot where parameter-to-prompt injection allowed the theft of 2FA codes and enterprise data.
- [[ideas/internal-safety-collapse]] — The fact that a "professional" agent is more likely to bypass safety guardrails means that the most powerful agents are also the most vulnerable to this expanded blast radius.
- [[entities/legion-intelligence]] — The state's move to specialized, closed-loop systems is a direct response to the unmanageable blast radius of general-purpose agents in national security contexts.

## Implications
The "Agentic" shift necessitates a total rethink of the security model. Traditional "input sanitization" is insufficient when the agent itself is the attack vector. We need "capability-aware" security, where permissions are not static but dynamically revoked based on the context of the agent's current goal and the sensitivity of the target data.

## Connections
- [[entities/searchleak]] — The primary case study for the expanded blast radius of agentic AI.
- [[topics/ai_safety]] — Transforms the safety conversation from "avoiding offensive language" to "preventing catastrophic identity theft."
- [[ideas/internal-safety-collapse]] — The mechanism that makes the agentic blast radius a critical threat in professional settings.
- [[sources/microsoft]] — The company that had to patch the most visible example of this phenomenon in Copilot.
