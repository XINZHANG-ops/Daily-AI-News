---
title: "Apple"
slug: apple
last_updated: 2026-06-09
---

# Apple

## Overview
Apple's multi-model strategy for iOS 27 marks a significant shift from exclusive partnerships to a diversified AI approach. By bringing in Google Gemini and Anthropic Claude alongside OpenAI's GPT, Apple is hedging against dependency on any single AI provider.

On June 8, 2026 at WWDC, Apple unveiled AFM 3 — its third-generation Apple Foundation Models family: AFM 3 Core (3B dense on-device), AFM 3 Core Advanced (20B sparse multimodal on-device, 1-4B active per token via IFP routing from NAND), AFM 3 Cloud, ADM 3 Cloud (image), and AFM 3 Cloud Pro (running on NVIDIA-backed cloud infrastructure). AFM 3 is the on-device bet of the bifurcated 2026 industry: while Xiaomi and DeepSeek push inference-cost floors on commodity hardware, Apple pushes capability ceilings on-device by accepting NAND-fetch latency in exchange for privacy, battery life, and zero per-token cost. AFM 3's Gemini-distilled teachers mark the first time Apple has publicly admitted its model lineage, while AFM 3 Cloud Pro on NVIDIA is Apple's first explicit cloud-NVIDIA dependency since the PowerPC-to-Intel and Intel-to-Apple Silicon transitions.

## Timeline

| Date | Event | Details |
|------|-------|---------|
| 2026-05-24 | iOS 27 multi-model support | Siri now taps GPT, Gemini, and Claude—not just OpenAI; Apple hedges platform dependency |
| 2026-05-25 | iOS 27 Siri major overhaul | iOS 27 brings biggest Siri upgrade in years: dedicated app with persistent chat threads, web search, document summarization; first time users can install rival AI via Extensions framework; breaks walled garden |
| 2026-06-08 | AFM 3 announced at WWDC 2026 | Five-model family: AFM 3 Core (3B dense on-device), AFM 3 Core Advanced (20B sparse on-device, 1-4B active via IFP routing from NAND), AFM 3 Cloud, ADM 3 Cloud (image), AFM 3 Cloud Pro (NVIDIA cloud); Gemini-distilled teachers; IFP routing from NAND lets 20B sparse model fit on phones |

## Key Relationships
- [[sources/openai]] — OpenAI considering legal action over Siri integration; claims Apple failed to make "honest effort"
- [[sources/google]] — Gemini integrated into Siri for multi-model support; Gemini also training partner for AFM 3 distillation
- [[sources/anthropic]] — Claude integrated into Siri for multi-model support
- [[sources/nvidia]] — AFM 3 Cloud Pro runs on NVIDIA backbone; first cloud-NVIDIA dependency for Apple since the 1990s
- [[topics/ai_companies]] — Apple's multi-model strategy is a symptom of platform dependency unraveling across the industry

## Connections
- [[topics/ai_companies]] — iOS 27 multi-model strategy ends single-provider dependency; Apple hedges across OpenAI, Google, Anthropic
- [[sources/openai]] — OpenAI legal threat may be negotiating leverage; Apple's multi-model approach is likely here to stay
- [[ideas/ai-utility-layer]] — Apple going multi-model exemplifies platform dependency unraveling; no single AI provider has exclusive access to major platforms anymore
- [[entities/afm-3]] — June 9: Apple's third-generation foundation model family; 5-model lineup including on-device sparse 20B Core Advanced and NVIDIA-backed Cloud Pro
- [[entities/afm-3-cloud-pro]] — June 9: Apple's third platform pivot in three decades; first cloud-NVIDIA dependency since the 1990s
- [[entities/ios-27-siri]] — iOS 27 Siri overhaul is the primary consumer surface for AFM 3
- [[entities/gemini-3-1-pro]] — Gemini-distilled teachers suggest Google remains a training partner for Apple's most capable model even as Apple hedges across multiple providers
- [[topics/llm_models]] — June 9: AFM 3 is the on-device extreme of the bifurcated industry, paired with Xiaomi MiMo-V2.5-Pro-UltraSpeed (1000 TPS on commodity 8-GPU) as the two architectural extremes
- [[entities/siri]] — AFM 3 powers the next-generation Siri experience shipping in iOS 27
- [[ideas/efficiency-frontier]] — IFP routing from NAND with 1-4B active is a new efficiency lever that lets 20B models fit on phones
- [[ideas/local-ai-computing]] — AFM 3 is the most aggressive on-device AI bet from any major consumer platform
- [[ideas/two-track-ai-future]] — AFM 3 is the canonical "on-device private" track alongside Meta Hatch, Xiaomi MiMo, and OpenAI superapp
