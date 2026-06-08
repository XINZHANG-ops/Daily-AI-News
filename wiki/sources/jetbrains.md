---
title: "JetBrains"
slug: jetbrains
last_updated: 2026-06-08
---

# JetBrains

## Overview
JetBrains is a Prague-based IDE vendor (IntelliJ IDEA, PyCharm, WebStorm, etc.) that entered the foundation model business with Mellum2 — a 12B-parameter Apache 2.0 code-specialized Mixture-of-Experts model released June 1, 2026. Mellum2 is the first serious "agent plumbing" model from a non-Meta, non-Chinese vendor, and the pure Apache 2.0 license is the real product: most 7-12B open code models (StarCoder2, Qwen2.5-Coder-7B, DeepSeek-Coder) have custom licenses that forbid commercial fine-tuning, while Llama Community License's 700M MAU clause is a real risk for IDE vendors. Mellum2 is positioned for routing, RAG pipelines, sub-agents, and private deployments in multi-agent coding stacks — JetBrains is selling the idea that the "agentic IDE" is a fleet, not a brain.

## Timeline

| Date | Event | Details |
|------|-------|---------|
| 2026-06-01 | Mellum2 released | 12B MoE (2.5B active per token), Apache 2.0; 2x faster inference than comparable open models; first non-Meta, non-Chinese "agent plumbing" model |

## Key Relationships
- **Open-source ecosystem (vs Meta / DeepSeek)**: Mellum2's Apache 2.0 license is the strategic alternative to Llama Community License (Meta) and custom-restrictive open code model licenses (DeepSeek-Coder)
- **IDE vendors (Cursor, Codeium, etc.)**: Mellum2 is positioned as the default sub-agent brain for any IDE vendor that doesn't want to negotiate with Meta
- **GitHub**: Token billing rollout (June 8) makes Mellum2 the most obvious beneficiary — cheapest viable model with no license restrictions in the Copilot routing table

## Connections
- [[entities/mellum-2]] — Released June 1, 2026; the company's first open-weight foundation model; pure Apache 2.0 makes it the default sub-agent brain for the multi-agent coding stack
- [[topics/ai_infrastructure]] — Mellum2 + Copilot token billing + Cosmos 3 OpenMDW license all confirm the bifurcated industry: frontier labs raise capability ceiling, infrastructure players lower cost floor
- [[topics/ai_funding]] — Apache 2.0 shifts the funding question for sub-agent models from "can we license it?" to "can we beat it on quality?"; the open-source baseline is now free of Meta-license restrictions
- [[entities/copilot-agent-tier]] — Mellum2 has a visible per-team cost advantage in Copilot's token billing — no license royalty, no MAU clause
- [[entities/claude-haiku-4-5]] — Direct competitor for the "fast/cheap" tier in Copilot; Mellum2 has a license advantage (Apache 2.0 vs custom), Haiku 4.5 has a capability advantage
- [[sources/github]] — Mellum2 + GitHub Copilot token billing is the open-source + usage-pricing pairing that defines the agent infrastructure layer's new economics
- [[ideas/agent-infrastructure-layer]] — Mellum2 is the first serious "agent plumbing" model from a non-Meta, non-Chinese vendor; positions JetBrains as an alternative to the Meta-dominated sub-agent tooling
- [[ideas/agent-verticalization]] — JetBrains verticalizes the model to its own IDE use case while opening it as the default for the broader IDE ecosystem
- [[timelines/2026-06]] — June 8: Mellum2 + token billing + Cosmos 3 all land in the same week; the agent infrastructure layer's new economics crystallize
