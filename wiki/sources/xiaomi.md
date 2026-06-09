---
title: "Xiaomi"
slug: xiaomi
last_updated: 2026-06-09
---

# Xiaomi

## Overview
Xiaomi is a Chinese consumer electronics and smartphone giant that has emerged as one of the most aggressive players in the AI model race. Through its MiMo family (developed by former DeepSeek researcher Luo Fuli), Xiaomi has consistently demonstrated the "China efficiency advantage" thesis: achieving frontier-class benchmark performance at significantly lower cost than Western competitors. Xiaomi's AI strategy pairs with its consumer device distribution (world's #3 smartphone vendor) to make on-device AI a product differentiator.

On June 8, 2026, Xiaomi and TileRT released MiMo-V2.5-Pro-UltraSpeed, claiming the first 1T-parameter model to break 1000 tokens/second decode speed (peak ~1200 TPS) on a single standard 8-GPU node — no Cerebras, no Groq, no custom silicon. This is the inference-cost bet of the bifurcated 2026 industry.

## Timeline

| Date | Event | Details |
|------|-------|---------|
| 2026-05-04 | MiMo-V2-Pro revealed as "Hunter Alpha" | Anonymous OpenRouter testing before formal reveal; 1T params, 42B active; GDPval-AA Elo 1426; cost 67% less than Claude Sonnet 4.6 for agentic tasks |
| 2026-06-08 | MiMo-V2.5-Pro-UltraSpeed released | First 1T model to break 1000 TPS decode on commodity 8-GPU node; co-developed with TileRT runtime; peak ~1200 TPS; explicitly positions against Cerebras/Groq |

## Key Relationships
- **DeepSeek**: Talent pipeline. MiMo built by former DeepSeek researcher Luo Fuli.
- **TileRT**: Runtime partner for UltraSpeed; software-only 1000 TPS on commodity hardware.
- **Cerebras/Groq**: Direct competitive targets. UltraSpeed's commodity 8-GPU approach undercuts specialized silicon.
- **Apple**: Strategic counter-position. Xiaomi bets on commodity 1000 TPS; Apple bets on on-device sparse MoE. The two extremes of the bifurcated 2026 industry.

## Connections
- [[entities/mimo-v2-pro]] — Predecessor model (1T MoE, 42B active) that established Xiaomi's stealth-launch pattern
- [[entities/mimo-v2-5-pro-ultraspeed]] — UltraSpeed release with TileRT, the inference-cost bet of June 2026
- [[entities/tilert]] — Co-developed runtime that makes UltraSpeed's 1000 TPS possible on commodity hardware
- [[entities/deepseek-v4]] — Sibling model in the Chinese open-weight triangle; same efficiency philosophy
- [[sources/deepseek]] — Luo Fuli, former DeepSeek researcher, is the architect of MiMo; talent migration pattern
- [[topics/llm_models]] — UltraSpeed is the inference-cost extreme of the bifurcated June 2026 industry
- [[topics/ai_infrastructure]] — Commodity 8-GPU running 1T at 1000 TPS is the proof that inference is a runtime problem, not a hardware problem
- [[ideas/efficiency-frontier]] — Xiaomi is the canonical example of efficiency-frontier thesis in 2026
- [[ideas/china-efficiency-advantage]] — Xiaomi + TileRT demonstrates China's structural advantage in extracting frontier performance from commodity hardware
- [[entities/afm-3]] — Apple AFM 3 is the on-device extreme; Xiaomi MiMo UltraSpeed is the commodity-compute extreme; the two define the bifurcated 2026 industry
