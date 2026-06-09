---
title: "Apple AFM 3"
slug: afm-3
type: model
last_updated: 2026-06-09
---

# Apple AFM 3

## What It Is
Apple Foundation Models 3, announced at WWDC 2026 on June 8, is Apple's third-generation on-device and cloud foundation model family. The five-model lineup is Apple's most ambitious AI bet yet: AFM 3 Core (3B dense on-device), AFM 3 Core Advanced (20B sparse multimodal on-device, 1-4B active per token via IFP routing from NAND), ADM 3 Cloud (image generation), AFM 3 Cloud, and AFM 3 Cloud Pro (running on NVIDIA-backed cloud infrastructure). The 20B sparse on-device model is the first Apple-shipping sparse MoE on a phone, with weights stored in NAND and IFP-fetched per layer.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | Apple |
| Release Date | 2026-06-08 (WWDC 2026) |
| Models | 5 (Core 3B, Core Advanced 20B sparse, Cloud, ADM 3 Cloud image, Cloud Pro) |
| On-Device Sparse | 20B total / 1-4B active, IFP routing from NAND |
| Cloud Pro Backbone | NVIDIA |
| Training Teachers | Gemini-distilled |
| Platform | iOS 27 |

## Significance
AFM 3 is the on-device bet of the bifurcated 2026 industry: while Xiaomi and DeepSeek push inference-cost floors on commodity hardware, Apple is doing the opposite — pushing capability ceilings on-device by accepting NAND-fetch latency in exchange for privacy, battery life, and zero per-token cost. The 20B sparse with 1-4B active is materially different from a 3-4B dense model: it can hold frontier-class knowledge in NAND and only pay the compute cost of the active experts per token. Gemini-distilled teachers are the first time Apple has publicly admitted its model lineage — likely a tradeoff to ship a competitive multimodal model on aggressive WWDC timelines.

The IFP routing from NAND is the under-discussed innovation: persistent storage of 20B parameters with selective per-layer fetch means the model can be larger than RAM, fundamentally changing the on-device frontier. AFM 3 Cloud Pro on NVIDIA is Apple's first explicit cloud-NVIDIA dependency since the 1990s PowerPC-to-Intel and Intel-to-Apple Silicon transitions — a third platform pivot in three decades.

## Connections
- [[sources/apple]] — Released at WWDC 2026 as part of iOS 27; represents the third Apple AI platform pivot in three decades (PowerPC→Intel→Apple Silicon→NVIDIA cloud for Pro tier)
- [[entities/siri]] — AFM 3 powers the next-generation Siri experience shipping in iOS 27
- [[entities/gemini-3-1-pro]] — Gemini-distilled teachers suggest Google remains a training partner for Apple's most capable model even as Apple hedges across multiple providers for Siri
- [[entities/ios-27-siri]] — iOS 27 Siri overhaul is the primary consumer surface for AFM 3
- [[topics/llm_models]] — AFM 3 is the on-device bet of the June 2026 bifurcated industry; pairs with Xiaomi MiMo-V2.5-Pro-UltraSpeed as the two architectural extremes (sparse-on-device vs high-TPS-compute)
- [[ideas/efficiency-frontier]] — IFP routing from NAND with 1-4B active is a new efficiency lever that lets 20B models fit on phones without frontier compute
- [[ideas/local-ai-computing]] — AFM 3 is the most aggressive on-device AI bet from any major consumer platform; on-device sparse MoE with 1-4B active reframes what "private AI" means for consumers
- [[sources/nvidia]] — AFM 3 Cloud Pro on NVIDIA backbone is a notable dependency; Apple has not relied on NVIDIA for cloud since the pre-Apple-Silicon era
- [[ideas/two-track-ai-future]] — AFM 3 is the canonical "on-device private" track alongside Meta Hatch (consumer-bundling), Xiaomi MiMo (inference-cost), and OpenAI (cloud-superapp) as the four application-layer bets
