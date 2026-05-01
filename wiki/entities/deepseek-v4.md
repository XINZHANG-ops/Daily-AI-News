---
title: "DeepSeek-V4"
slug: deepseek-v4
type: model
last_updated: 2026-04-30
---

# DeepSeek-V4

## What It Is
DeepSeek-V4 is DeepSeek's flagship model family released April 24, 2026. Available in three variants:
- **V4-Pro**: 1.6T total parameters with 49B active params per inference
- **V4-Pro-Max**: 1.6T total/49B active — the cost-performance leader at $1.74/M tokens
- **V4-Flash**: 284B total with 13B active params — the commodity inference champion at $0.14/$0.28 per million tokens

All variants feature enhanced agentic coding, world-class reasoning, and 1M token context as default. Open weights available on Hugging Face.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Release Date | 2026-04-24 |
| Creator | DeepSeek |
| Variants | V4-Pro (1.6T/49B), V4-Pro-Max (1.6T/49B, $1.74/M), V4-Flash (284B/13B, $0.14/$0.28/M) |
| Context | 1M tokens (default) |
| License | Open weights on Hugging Face |
| SWE-bench | V4-Pro-Max: 80.6%, V4-Flash: 78% |

## Significance
DeepSeek-V4's April 30 pricing revelation fundamentally reshapes the AI economics debate. V4-Flash at $0.28/M output tokens is 100x cheaper than GPT-5.5 (~$30/M) and 35x cheaper than Claude Opus 4.7 (~$10/M), while scoring 78% on SWE-bench — "good enough" for the majority of production tasks where absolute benchmark leadership doesn't justify 100x cost premium. The V4-Pro-Max at $1.74/M represents the mid-market sweet spot: 2.6x cheaper than Claude Opus 4.7 with comparable 80.6% SWE-bench. This 100x cost gap is structural, not temporary — it reflects China's efficiency advantage and DeepSeek's open-source community leverage. For enterprises, the question shifts from "which model is best?" to "which model is good enough at what cost?"

## Connections
- [[sources/deepseek]] — Released by DeepSeek on April 24, 2026; Tencent/Alibaba investment talks ongoing
- [[topics/llm_models]] — The commodity-inference challenger to GPT-5.5 and Claude Opus 4.7
- [[ideas/us-china-ai-fragmentation]] — Named in US AI companies' distillation accusations; China tech backing
- [[topics/ai_companies]] — Tencent proposing up to 20% stake; major Chinese tech validating DeepSeek
- [[entities/deepgemm]] — DeepSeek's FP8 GEMM kernels enabling efficient inference
- [[ideas/efficiency-frontier]] — 100x cost gap with frontier models validates efficiency-as-competitive-advantage thesis
