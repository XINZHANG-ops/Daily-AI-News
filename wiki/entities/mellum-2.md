---
title: "JetBrains Mellum2"
slug: mellum-2
type: model
last_updated: 2026-06-08
---

# JetBrains Mellum2

## What It Is
Mellum2 is JetBrains' second-generation code-specialized language model, a 12B-parameter Mixture-of-Experts (2.5B active per token) released on June 1, 2026 under Apache 2.0 license. Optimized for low-latency text-and-code workloads, it claims 2x faster inference than comparable open models. The positioning is explicit: routing, RAG pipelines, sub-agents, and private deployments — the "agent plumbing" layer for multi-agent coding stacks where frontier models handle planning and refactoring, but routing, completion, retrieval, and test-generation need a fast 2.5B-active model.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Release Date | June 1, 2026 |
| Creator | JetBrains |
| Parameters | 12B total / 2.5B active per token |
| Architecture | Mixture-of-Experts (MoE) |
| License | Apache 2.0 (no MAU clause, no commercial restriction) |
| Use Cases | Routing, RAG pipelines, sub-agents, private deployments, IDE completion |
| Inference Speed | 2x faster than comparable open models |
| Comparison vs Peer Models | StarCoder2, Qwen2.5-Coder-7B, DeepSeek-Coder (all have custom licenses) |

## Significance
Mellum2 is the first serious "agent plumbing" model from a non-Meta, non-Chinese vendor, and the Apache 2.0 license is the real product. Most open code models in the 7-12B range (StarCoder2, Qwen2.5-Coder-7B, DeepSeek-Coder) come with custom licenses that forbid commercial fine-tuning or include MAU clauses (Llama Community License's 700M MAU trigger). Mellum2's pure Apache 2.0 makes it the default sub-agent brain for any IDE vendor that doesn't want to negotiate with Meta or worry about Llama license triggers. The "sub-agent" positioning reflects a fundamental architectural shift: the "agentic IDE" is a fleet of models, not a single brain. Frontier models (Opus 4.8, MAI-Thinking-1) handle the heavy lifting of planning, refactoring, and code generation, but routing, completion, retrieval, and test-generation need a fast 2.5B-active model — Mellum2 is optimized exactly for that role.

The release timing is significant: it lands one week before GitHub's token-billing rollout for Copilot, making Mellum2 the most obvious beneficiary of usage-based pricing — the cheapest viable model with no license restrictions now has a visible per-team cost advantage over Opus 4.8 in autocomplete.

## Connections
- [[sources/jetbrains]] — JetBrains productizes the model for its own IDE fleet; the Apache 2.0 license is also a strategic move to position JetBrains as the alternative to Meta-dominated sub-agent tooling
- [[topics/ai_infrastructure]] — Mellum2 is the first "agent plumbing" model from a non-Meta, non-Chinese vendor under pure Apache 2.0; sets a new open-source baseline for code MoE
- [[topics/agentic_ai]] — "Sub-agent" positioning literally sells the "agentic IDE as fleet, not brain" thesis; multi-agent coding stacks are now an explicit architectural pattern
- [[entities/copilot-agent-tier]] — June 8: GitHub Copilot's token billing makes Mellum2 the cheapest viable model in the Copilot routing table; the strategic beneficiary of usage-based pricing
- [[entities/claude-haiku-4-5]] — Direct competitor for the "fast/cheap" tier in Copilot; Mellum2 has a license advantage (Apache 2.0 vs custom), Haiku 4.5 has a capability advantage
- [[entities/gpt-5.4]] — Mellum2 positioned to take the routing/completion/retrieval/test-gen tasks that GPT-5.4-mini handles in Copilot
- [[entities/claude-opus-4-8]] — Mellum2 handles the routing/completion/retrieval/test-generation plumbing in a multi-agent stack where Opus 4.8 handles planning, refactoring, and code generation
- [[entities/claude-mythos]] — The Mythos 16+ hour autonomous task concept assumes a fleet of sub-agents doing the routine work; Mellum2 is the open-source version of that fleet
- [[ideas/agent-infrastructure-layer]] — Mellum2 + Copilot token billing + Cosmos 3 OpenMDW license all confirm the bifurcated industry: frontier labs raise capability ceiling, infrastructure players lower cost floor
- [[topics/ai_funding]] — Apache 2.0 shifts the funding question for sub-agent models from "can we license it?" to "can we beat it on quality?"; the open-source baseline is now free of Meta-license restrictions
- [[sources/github]] — Mellum2 + GitHub Copilot token billing is the open-source + usage-pricing pairing that defines the agent infrastructure layer's new economics
- [[entities/claude-code]] — Mellum2 is positioned as the sub-agent brain for Claude Code-style multi-agent IDE stacks; in a Mellum2-based fleet, Claude Code would be the planning/refactoring layer
- [[timelines/2026-06]] — June 8: Mellum2 + token billing + Cosmos 3 all land in the same week; the agent infrastructure layer's new economics crystallize
