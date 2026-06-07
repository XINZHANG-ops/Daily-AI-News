---
title: "OpenAI Lockdown Mode"
slug: openai-lockdown-mode
type: feature
last_updated: 2026-06-07
---

# OpenAI Lockdown Mode

## What It Is
OpenAI Lockdown Mode is a security feature for ChatGPT Business and select personal accounts, released June 6, 2026. It disables live web browsing, image retrieval, deep research, and agent mode to protect against prompt-injection attacks. The launch followed the Meta Instagram breach where attackers exploited Meta's AI customer support agent to exfiltrate customer data.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | OpenAI |
| Release Date | 2026-06-06 |
| Affected Products | ChatGPT Business, select personal accounts |
| Disabled Features | Live browsing, image retrieval, deep research, agent mode |
| Trigger Event | Meta Instagram breach (prompt injection via customer-support agent) |
| Equivalent | iOS Lockdown Mode (Apple, 2022); Security Lockdown (Android) |

## Significance
Lockdown Mode is OpenAI admitting that the agentic era has a security crisis that model alignment alone cannot solve. Stripping browsing, retrieval, research, and agent mode is functionally equivalent to rolling ChatGPT back to a 2023 chat-only product — and OpenAI is willing to take that UX hit to keep the enterprise market. The Meta Instagram breach is the proximate trigger: attackers used prompt injection to exfiltrate customer data through a customer-support agent, and that incident is now the canonical "agentic security" case study the way SolarWinds was for supply-chain attacks. The interesting move is the parallel: Anthropic has been pushing Effort Control (the inverse — give users MORE agency) while OpenAI is offering MORE restriction. Both companies are trying to solve the same trust problem from opposite directions, which suggests neither has cracked it and the security layer is moving up the stack toward OS-level sandboxes.

## Connections
- [[sources/openai]] — OpenAI-developed as a defensive posture for enterprise customers
- [[sources/anthropic]] — Anthropic's Effort Control is the philosophical opposite; both solving the same trust problem differently
- [[entities/claude-mythos]] — Mythos discovered thousands of vulnerabilities showing attack surfaces that Lockdown Mode cannot address
- [[entities/agent-365]] — Microsoft's competing agent platform with its own governance layer
- [[topics/ai_security]] — Lockdown Mode is the canonical "model-level restriction" response to agentic security crisis
- [[ideas/trust-architecture-broken]] — Lockdown Mode acknowledges that current AI trust architecture is fundamentally broken for agentic use
- [[ideas/indirect-prompt-injection-threat]] — Meta Instagram breach validated the IPI threat model
- [[sources/meta]] — Meta Instagram breach is the proximate trigger; attacker exploited Meta's customer-support agent
- [[ideas/agentic-catch-up-game]] — OpenAI's response shows the security dimension of the agentic race is about catch-up
- [[entities/ibm-sovereign-core]] — IBM's enterprise governance infrastructure is the alternative to model-level restriction; sandboxes the data and compute instead
