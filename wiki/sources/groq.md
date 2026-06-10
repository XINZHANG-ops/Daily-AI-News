---
title: "Groq"
slug: groq
last_updated: 2026-06-09
---

# Groq

## Overview
Groq is an AI hardware company founded by Jonathan Ross (former Google TPU architect) that designs Language Processing Units (LPUs) — deterministic, low-latency inference accelerators optimized for LLM serving. Its LPU-based inference service peaks at ~750 tokens/second on frontier-scale models and is widely deployed for low-latency conversational AI use cases.

Groq's value proposition rests on the LPU's deterministic latency and per-request speed advantage over commodity GPU serving. That advantage was matched and exceeded on June 8, 2026, when Xiaomi + TileRT released MiMo-V2.5-Pro-UltraSpeed, claiming 1000+ TPS decode speed (peak ~1200 TPS) on a standard 8-GPU commodity node — running faster than Groq's LPU peak without any custom silicon.

## Why It Matters
- **LPU architecture**: Groq's chips use a deterministic dataflow architecture (no external memory fetches mid-inference) to deliver predictable sub-millisecond per-token latency.
- **Speed tier**: Groq LPU peaks at ~750 TPS — historically the second-fastest cloud inference option behind Cerebras WSE-3 (~969 TPS). Both were exceeded by Xiaomi + TileRT on June 8, 2026.
- **Specialized-silicon bet**: Groq represents the "language model serving needs custom silicon" thesis. The Xiaomi + TileRT result is the first clear evidence that software/runtime innovation can match LPU-class throughput on commodity hardware.

## Competitive Position (June 2026)

| Provider | Peak TPS | Hardware Type |
|----------|----------|---------------|
| GPT-5.5 | ~68 | Commodity GPU |
| Claude Opus 4.6 | ~71 | Commodity GPU |
| Gemini Flash | ~192 | Google TPU |
| **Groq LPU** | **~750** | **Custom LPU** |
| Cerebras WSE-3 | ~969 | Wafer-scale ASIC |
| **Xiaomi + TileRT (UltraSpeed)** | **~1200** | **Commodity 8-GPU** |

## Connections
- [[entities/tilert]] — TileRT's software-only 1000+ TPS on commodity 8-GPU node undercuts Groq's LPU value proposition
- [[entities/mimo-v2-5-pro-ultraspeed]] — The Xiaomi release that exceeded Groq LPU's peak TPS on commodity hardware
- [[sources/xiaomi]] — Co-developer (with TileRT) of the model that exceeded Groq's LPU peak
- [[sources/cerebras]] — Sibling specialized-silicon provider; both were outperformed by Xiaomi + TileRT on June 8, 2026
- [[topics/ai_infrastructure]] — Groq is the canonical LPU example; its moat was broken on June 8, 2026
- [[ideas/commodity-inference-fragmentation]] — The Groq → Xiaomi + TileRT shift exemplifies how software innovation is fragmenting the specialized-silicon moat
- [[ideas/efficiency-frontier]] — Groq represents the LPU extreme of the efficiency frontier; the June 8 result pulls the frontier toward software/runtime innovation
