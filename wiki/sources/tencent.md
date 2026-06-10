---
title: "Tencent"
slug: tencent
last_updated: 2026-06-10
---

# Tencent

## Overview
Tencent is a Chinese technology conglomerate known for WeChat, gaming, and cloud services. On June 9, 2026, Tencent shipped Hy3, a 295B-MoE (21B active) agent model with a 256K context window and 495-step production workflows in Yuanbao, QQ, and Tencent Docs — the highest production step count disclosed in 2026. Hy3 ships with open weights on GitHub and Hugging Face and $0.18/M pricing on OpenRouter (free for the first two weeks), making it the most aggressive Chinese open-weight agent release of 2026 and a direct head-to-head with Anthropic's Fable 5 on the same day at a 55× lower input-token price.

## Timeline

| Date | Event | Details |
|------|-------|---------|
| 2026-05-23 | L2P Release | Tencent released L2P method for pixel-space image generation, removing VAE bottleneck; T2I-L2P repo gained 80 stars in 24 hours |
| 2026-06-09 | Hy3 preview ships | 295B MoE (21B active), 256K context, integrated fast+slow thinking; 495-step production workflows in Yuanbao, QQ, Tencent Docs; open weights on GitHub + Hugging Face; $0.18/M on OpenRouter (free for 2 weeks); 40% better inference efficiency than comparable MoE baselines; most aggressive Chinese open-weight agent release of 2026 |

## Key Relationships
Tencent is in talks to invest in DeepSeek (alongside Alibaba), showing the company's strategy of partnering with leading AI labs while also developing proprietary technology. The Hy3 release positions Tencent as the only major Chinese tech giant to ship a frontier-tier open-weight agent model with both a low active-parameter count (21B, serviceable on commodity 8-GPU nodes) and a billion-user production deployment footprint across Yuanbao, QQ, and Tencent Docs.

## Connections
- [[entities/t2i-l2p]] — Tencent's breakthrough in pixel-space image generation; removes VAE bottleneck while maintaining low training costs
- [[entities/tencent-hy3]] — June 9: 295B/21B MoE agent model with 495-step production workflows; the largest Chinese open-weight frontier-tier release of 2026
- [[sources/deepseek]] — Tencent in talks to invest in DeepSeek alongside Alibaba; strategic partnership with leading Chinese AI lab; Hy3's 21B active vs V4-Pro's 49B active is the next data point in the China efficiency ladder
- [[topics/llm_models]] — Hy3's 21B active footprint is the smallest among frontier-tier models shipping in 2026, validating the high-sparsity-MoE bet; the 495-step workflows in three production products is the first billion-user agent infrastructure
- [[ideas/china-efficiency-advantage]] — Hy3 is the first Chinese frontier-tier model with a 21B active footprint and the highest production step count; reinforces the China-efficiency thesis with the strongest production data point yet
- [[sources/anthropic]] — Hy3 ships the same day as Fable 5 at $0.18/M vs $10/M input — a 55× gap is the cleanest single-day expression of the bifurcated AI market between premium safety and commodity scale
- [[ideas/pricing-war]] — The $0.18/M input price (free for two weeks) is the most aggressive land-grab pricing in 2026; the OpenRouter distribution ensures Hy3's adoption is decoupled from Tencent's commercial relationships
- [[entities/claude-fable-5]] — Direct same-day competitor; the 55× price gap is structurally a different market segment — Hy3 for cost-sensitive agent workloads, Fable 5 for safety-routed frontier capability
