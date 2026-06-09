---
title: "TileRT"
slug: tilert
type: product
last_updated: 2026-06-09
---

# TileRT

## What It Is
TileRT is the inference runtime Xiaomi partnered with to deliver MiMo-V2.5-Pro-UltraSpeed's claimed 1000+ tokens/second decode on a single standard 8-GPU node — no Cerebras, no Groq, no custom silicon. The runtime achieves 1000+ TPS (peak ~1200 TPS) on a 1T-parameter MoE model on commodity 8-GPU hardware, demonstrating that the inference-cost floor can be broken through runtime innovation rather than specialized accelerators.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | Xiaomi (partnership) |
| Date | 2026-06-08 |
| Model | MiMo-V2.5-Pro-UltraSpeed (1T params) |
| Hardware | Single standard 8-GPU node (commodity) |
| Performance | 1000+ TPS decode (peak ~1200 TPS) |
| Achievement | First 1T model to break 1000 TPS on commodity 8-GPU nodes |

## Significance
TileRT is the runtime-equivalent of NVIDIA's "model-as-CUDA-distribution" play applied to inference: it weaponizes commodity 8-GPU hardware to deliver performance previously associated with custom silicon. By proving 1T-parameter models can serve at 1000+ TPS on standard nodes, TileRT collapses the price-per-token for serving frontier-tier models on commodity infrastructure.

The strategic significance: every lab currently paying for Cerebras/Groq contracts (or building custom silicon) now has a software-only path to similar TPS. The cost-per-token of frontier model serving is no longer a function of hardware specialization — it is a function of runtime quality. This shifts competitive advantage from "who can build the best chip" to "who can build the best runtime," a category where the marginal innovator doesn't need $5B+ in capex.

## Connections
- [[sources/xiaomi]] — Co-developed with Xiaomi for the MiMo-V2.5-Pro-UltraSpeed release
- [[entities/mimo-v2-pro]] — Successor model in Xiaomi's MiMo family; TileRT is the runtime that makes V2.5-Pro-UltraSpeed viable on commodity hardware
- [[entities/cerebras]] — Cerebras and Groq's business model is directly threatened by TileRT's software-only 1000 TPS on commodity hardware
- [[entities/groq]] — Groq's LPU hardware advantage is undercut by TileRT's runtime innovation on commodity 8-GPU nodes
- [[topics/ai_infrastructure]] — TileRT is the proof point that inference cost is now a runtime problem, not a hardware problem
- [[ideas/efficiency-frontier]] — 1000+ TPS on 1T params from commodity hardware is the new efficiency frontier; runtime innovation replaces chip specialization
- [[ideas/china-efficiency-advantage]] — Xiaomi + TileRT demonstrates China's structural advantage in extracting frontier performance from commodity hardware
- [[sources/deepseek]] — DeepSeek's price wars depend on similar runtime efficiency; TileRT's open approach is an extension of the same philosophy
- [[ideas/commodity-inference-fragmentation]] — TileRT exemplifies how commodity inference is fragmenting; software-only TPS parity with custom silicon breaks the hardware moat
