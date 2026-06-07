---
title: "Maia 200"
slug: maia-200
type: chip
last_updated: 2026-06-07
---

# Maia 200

## What It Is
Maia 200 is Microsoft's second-generation custom AI accelerator, co-designed with the MAI model family released June 6, 2026. The chip delivers a 1.4x efficiency boost over its predecessor and underpins MAI-Thinking-1, MAI-Code-1-Flash, MAI-Image-2.5, and the rest of the seven-model MAI portfolio. Maia 200 is the silicon foundation of Microsoft's full-stack vertical integration play.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | Microsoft |
| Generation | 2nd-generation custom AI silicon |
| Efficiency | 1.4x over predecessor |
| Co-designed Models | MAI-Thinking-1, MAI-Code-1-Flash, MAI-Image-2.5, MAI-Voice-2, MAI-Transcribe-1.5 |
| Strategy | Full-stack vertical integration (chip → model → agent → distribution) |

## Significance
Maia 200 is the real story behind Microsoft's "seven models, one day" announcement. By co-designing the chip and the model family together, Microsoft achieves a coupled optimization that closed competitors cannot match: NVIDIA's chips run everyone's models but not optimally for any one vendor, while Maia 200 is purpose-built for MAI workloads. The 1.4x efficiency boost is not huge in isolation, but combined with M365 Copilot's 20M+ paid enterprise seats as distribution, it lets Microsoft price below AWS Bedrock and Google Vertex while gradually weaning the product off GPT-class models. Microsoft is the only hyperscaler with paired foundation models + in-house training chips + distribution through M365 Copilot — a three-layer position that competitors must either replicate (years of work) or partner for (ceding margin).

## Connections
- [[sources/microsoft]] — Microsoft-developed as part of vertical-integration play; co-designed with MAI family
- [[entities/mai-family]] — The model family co-designed with Maia 200 silicon; represents coupled chip+model optimization
- [[entities/gb300]] — NVIDIA's competing chip; Maia 200 represents Microsoft's effort to escape NVIDIA dependency for training
- [[entities/blackwell-architecture]] — The NVIDIA architecture Maia 200 is positioned against
- [[sources/nvidia]] — Maia 200 directly threatens NVIDIA's chip dominance; could shift training/inference workloads in-house
- [[ideas/vertical-integration]] — Maia 200 is the canonical case study: chip + model + agent + distribution in one company
- [[sources/openai]] — Maia 200 + MAI lets Microsoft gradually reduce OpenAI dependency
- [[sources/anthropic]] — Anthropic depends on Microsoft Azure for compute; Maia 200 gives Microsoft leverage
- [[topics/ai_infrastructure]] — Maia 200 is part of the custom-silicon wave reshaping AI infrastructure economics
- [[topics/agentic_ai]] — Maia 200 + MAI family powers Windows Agent Runtime, making Windows a first-class agent platform
