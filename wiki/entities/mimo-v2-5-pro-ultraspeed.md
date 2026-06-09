---
title: "MiMo-V2.5-Pro-UltraSpeed"
slug: mimo-v2-5-pro-ultraspeed
type: model
last_updated: 2026-06-09
---

# MiMo-V2.5-Pro-UltraSpeed

## What It Is
MiMo-V2.5-Pro-UltraSpeed is Xiaomi's updated 1T-parameter MoE model, released June 8, 2026, claiming the first 1T-parameter model to break 1000 tokens/second decode speed (peak ~1200 TPS) on a single standard 8-GPU node. The "UltraSpeed" suffix signals the runtime partnership with TileRT rather than architectural changes — the model itself is a 1T MoE that achieves frontier-class performance through inference optimization rather than chip specialization.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | Xiaomi |
| Release Date | 2026-06-08 |
| Parameters | 1 trillion MoE |
| TPS | 1000+ decode, peak ~1200 |
| Hardware | Single standard 8-GPU node (no Cerebras/Groq/custom silicon) |
| Runtime | TileRT (co-developed partnership) |
| Predecessor | [[entities/mimo-v2-pro]] |

## Significance
MiMo-V2.5-Pro-UltraSpeed is the inference-cost bet of the bifurcated 2026 industry. While Apple pushes on-device sparse MoE for privacy, Xiaomi pushes commodity-hardware TPS for cost. The 1000+ TPS on a standard 8-GPU node is structurally important: it proves frontier-tier serving doesn't require specialized accelerators, which collapses the price-per-token for any lab that can replicate the runtime.

The "commodity 8-GPU" framing is deliberate: it makes the cost comparison to Cerebras/Groq direct. A lab paying $1M/month for Cerebras inference can now serve the same model class on the same 8-GPU commodity node for an order of magnitude less. TileRT becomes the open-source-y runtime that every frontier lab needs to evaluate, and Xiaomi's MiMo becomes the first 1T model to demonstrate the parity.

## Connections
- [[entities/mimo-v2-pro]] — Successor to MiMo-V2-Pro; same 1T MoE base architecture with UltraSpeed runtime optimization
- [[entities/tilert]] — Co-developed runtime; TileRT is the technology that makes UltraSpeed viable
- [[sources/xiaomi]] — Xiaomi is the canonical example of the China-efficiency-advantage thesis in 2026
- [[entities/deepseek-v4]] — DeepSeek's price war depends on similar runtime efficiency; UltraSpeed pushes the frontier of what's possible on commodity hardware
- [[topics/llm_models]] — UltraSpeed is the inference-cost bet of the bifurcated June 2026 industry; pairs with AFM 3 as the on-device extreme
- [[topics/ai_infrastructure]] — Commodity 8-GPU running 1T at 1000 TPS is the proof point that inference cost is a runtime problem, not a hardware problem
- [[ideas/efficiency-frontier]] — UltraSpeed is the new efficiency frontier: 1T params at 1000 TPS on commodity hardware
- [[ideas/china-efficiency-advantage]] — Xiaomi's model of frontier performance from commodity hardware is the structural Chinese advantage
- [[entities/afm-3]] — Apple AFM 3 and Xiaomi UltraSpeed are the two extremes of the bifurcated June 2026 industry: on-device sparse vs commodity 1000 TPS
