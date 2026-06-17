---
title: "SearchLeak"
slug: searchleak
type: vulnerability
last_updated: 2026-06-17
---

# SearchLeak

## What It Is
SearchLeak is a critical vulnerability in Microsoft Copilot that allowed attackers to steal 2FA codes and enterprise data. The flaw was a "parameter-to-prompt injection" where external input was improperly handled, allowing an attacker to trick the AI into revealing sensitive authentication tokens.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Target | Microsoft Copilot |
| Type | Parameter-to-Prompt Injection |
| Impact | Theft of 2FA codes, enterprise data leak |
| Patch Date | June 16, 2026 |

## Significance
SearchLeak is a cautionary tale about the "Agentic" shift. When an AI is given high-level permissions (like reading emails or accessing 2FA codes) to be more helpful, a single prompt injection doesn't just leak a chat—it leaks the keys to a user's entire digital identity. It demonstrates that the blast radius of vulnerabilities grows proportionally with the agent's capabilities.

## Connections
- [[sources/microsoft]] — Patched the vulnerability on June 16, 2026
- [[ideas/agentic-blast-radius]] — The definitive case study for why agentic permissions increase the severity of prompt injection attacks
- [[topics/ai_safety]] — Highlights the need for "capability-aware" security models where permissions are dynamically revoked or heavily guarded
- [[entities/internal-safety-collapse]] — Both SearchLeak and Internal Safety Collapse show that the "guardrails" of current LLMs are insufficient for high-stakes production deployment
