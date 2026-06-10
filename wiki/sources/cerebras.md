---
title: "Cerebras"
slug: cerebras
last_updated: 2026-06-09
---

# Cerebras

## Overview
Cerebras Systems is an AI hardware company known for its Wafer-Scale Engine (WSE) chip — the largest commercially available processor — designed to accelerate deep learning training and inference. Its inference service (Cerebras Inference) is one of the fastest cloud inference offerings in the market, peaking at ~969 tokens/second on frontier-scale models, and has positioned itself as the premium choice for low-latency LLM serving.

Cerebras's business model depends on specialized hardware commanding a pricing premium over commodity GPU offerings. That model came under direct threat on June 8, 2026, when Xiaomi + TileRT released MiMo-V2.5-Pro-UltraSpeed, claiming 1000+ TPS decode speed (peak ~1200 TPS) on a standard 8-GPU commodity node — exceeding Cerebras's peak without any specialized silicon.

## Why It Matters
- **Inference speed leader (until June 2026)**: Cerebras Inference was the reference for "what is the fastest frontier-model serving available commercially," peaking at ~969 TPS — the bar Xiaomi/TileRT just cleared on commodity hardware.
- **Wafer-scale moat**: WSE-3 uses a wafer-sized chip (~46,225 mm²) with 900,000 cores, designed to eliminate the memory bandwidth bottleneck of multi-GPU clusters.
- **Specialized-silicon bet**: Cerebras represents the thesis that frontier AI serving requires purpose-built accelerators. The Xiaomi + TileRT result is the first direct evidence that runtime + quantization innovation can match specialized-silicon throughput.

## Competitive Position (June 2026)

| Provider | Peak TPS | Hardware Type |
|----------|----------|---------------|
| GPT-5.5 | ~68 | Commodity GPU |
| Claude Opus 4.6 | ~71 | Commodity GPU |
| Gemini Flash | ~192 | Google TPU |
| Groq LPU | ~750 | Custom LPU |
| **Cerebras WSE-3** | **~969** | **Wafer-scale ASIC** |
| **Xiaomi + TileRT (UltraSpeed)** | **~1200** | **Commodity 8-GPU** |

## Connections
- [[entities/tilert]] — TileRT's software-only 1000+ TPS on commodity 8-GPU node directly undercuts Cerebras's specialized-silicon value proposition
- [[entities/mimo-v2-5-pro-ultraspeed]] — The Xiaomi release that exceeded Cerebras's peak TPS on commodity hardware
- [[sources/xiaomi]] — Co-developer (with TileRT) of the model that broke Cerebras's speed record on commodity silicon
- [[topics/ai_infrastructure]] — Cerebras is the canonical specialized-silicon example; its moat was broken on June 8, 2026
- [[ideas/commodity-inference-fragmentation]] — The Cerebras → Xiaomi + TileRT shift exemplifies how software innovation is fragmenting the specialized-silicon moat
- [[ideas/efficiency-frontier]] — Cerebras represents one extreme of the efficiency frontier (specialized hardware); the June 8 result pulls the frontier toward software/runtime innovation
