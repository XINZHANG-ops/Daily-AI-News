---
title: "Mistral"
slug: mistral
last_updated: 2026-05-06
---

# Mistral

## Overview
Mistral AI is a French AI lab positioning itself as the geopolitically neutral, regulatorily compliant European alternative to US AI labs. The company released Mistral Ultra 2 on April 29, scoring 78.4% on SWE-bench Verified — positioning it firmly in the enterprise coding market at a price point 20% below DeepSeek's already aggressive pricing, while offering EU data residency guarantees that no US lab can replicate.

## Timeline

| Date | Event | Details |
|------|-------|---------|
| 2026-04-29 | Mistral Ultra 2 released | 78.4% SWE-bench, €2/M tokens, 1M context, native MCP support, EU data residency |
| 2026-05-02 | Mistral Medium 3.5 + Vibe released | First "merged" flagship: 128B dense transformer (not MoE), 256K context, configurable reasoning-effort toggle per request, SWE-Bench Verified 77.6%, AIME25 86.3%; self-hostable on 4 GPUs at FP8; Vibe cloud coding agents bundled — vertically integrated model + agent stack |
| 2026-05-05 | EU AI Act Phase 2 fine | €11.2M provisional penalty for training-data transparency failures; privacy-first positioning calculated to reduce regulatory exposure |
| 2026-05-05 | Work Mode and Remote Agents in Vibe | On-device agentic "Work Mode" for complex multi-step tasks in Le Chat; "Remote Agents in Vibe" for async cloud execution; API pricing $1.5/$7.5 per million tokens |

## Key Relationships
- **Azure AI Foundry**: Mistral Ultra 2 available on Azure, giving Microsoft a European-aligned model to counter Google-Anthropic and OpenAI dominance
- **DeepSeek**: Both competing on price-performance in enterprise coding; DeepSeek at $1.74/M vs Mistral at €2/M ($2.17/M)
- **EU AI Act**: Mistral's EU data residency directly addresses compliance requirements the EU AI Act fine on Meta just amplified

## Connections
- [[entities/mistral-ultra-2]] — The flagship model released April 29; EU-compliant alternative for enterprise coding
- [[entities/mistral-medium-3-5]] — 128B dense model with reasoning toggle; one-model-for-all design pattern
- [[entities/vibe]] — Vertically integrated cloud coding agents; Mistral following Anthropic's Claude Code growth strategy
- [[topics/llm_models]] — Competing in the cost-performance frontier alongside DeepSeek V4-Pro-Max and Claude Opus 4.7
- [[ideas/institutional-gap]] — Mistral's EU data residency positioning exploits the regulatory-reputational siege on US tech
- [[entities/mistral-medium-3-5]] — Official May 5 launch adds Work Mode (on-device agentic mode) and Remote Agents in Vibe (async cloud execution); EU AI Act €11.2M fine makes privacy-first positioning more urgent
- [[ideas/boring-infrastructure-shift]] — Work Mode and Remote Agents are the boring infrastructure for reliable agent execution — not exciting capabilities but the plumbing that makes agents deployable at scale
- [[ideas/government-pre-testing]] — EU AI Act Phase 2 fines (€11.2M on Mistral, €8.4M on Stability AI) prove Europe is taking a harder line than the US, creating a balkanized regulatory landscape
- [[topics/ai_safety]] — EU fines and Work Mode's user-controlled execution are two sides of the same coin: regulatory pressure driving technical architecture toward user sovereignty
