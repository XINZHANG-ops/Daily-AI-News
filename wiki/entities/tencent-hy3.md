---
title: "Tencent Hy3"
slug: tencent-hy3
type: model
last_updated: 2026-06-10
---

# Tencent Hy3

## What It Is
Tencent Hy3 is a 295B-parameter mixture-of-experts (21B active) agent model released as a preview on June 9, 2026, with open weights on GitHub and Hugging Face and immediate availability on OpenRouter at $0.18/M input tokens. The model features a 256K context window and an integrated fast + slow thinking controller that already powers 495-step agent workflows in Yuanbao, QQ, and Tencent Docs — the highest reported step count of any production agent deployment. Tencent claims 40% better inference efficiency than comparable MoE baselines, and the model is free on OpenRouter for the first two weeks.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Release Date | 2026-06-09 (preview) |
| Creator | Tencent |
| Total Parameters | 295B |
| Active Parameters | 21B |
| Context Window | 256K |
| Thinking Modes | Fast + slow (integrated controller) |
| Production Step Count | 495-step workflows in Yuanbao, QQ, Tencent Docs |
| OpenRouter Price | $0.18 / M input (free for first 2 weeks) |
| Weights | Open on GitHub + Hugging Face |
| Inference Efficiency | 40% better than comparable MoE (per Tencent claim) |

## Significance
Hy3 is the most aggressive Chinese open-weight agent model release of 2026. The 295B/21B active MoE profile lands in the same "frontier-capable, commodity-cost" bracket as DeepSeek V4-Pro (1.6T/49B) but with a substantially lower active footprint — 21B active is small enough to serve on a single 8-GPU node with TileRT-style runtimes, while the 256K context makes it viable for the long-trajectory agent workloads that production systems like Yuanbao actually need. The 495-step workflow benchmark is the highest production step count disclosed in 2026 and is the most concrete evidence that Tencent has crossed from "research model" to "production agent infrastructure."

The $0.18/M OpenRouter pricing — released the same day Anthropic priced Fable 5 at $10/M — is the cleanest possible expression of the bifurcated AI market: a 55× input-token price gap between the two flagships on the same day. For workloads where the safety-routing overhead of Fable 5 is not required, Hy3 at $0.18/M is the economic choice. The "free for two weeks" promotion is a land grab: every agent developer who integrates Hy3 during the free window has switching costs when the price goes to $0.18.

The 495-step production workflows matter strategically because they directly counter the agentic-coding moat that Anthropic and OpenAI have been building. Tencent's QQ, Yuanbao, and Tencent Docs collectively serve over a billion users in China; if those workflows can be agent-automated at Hy3-class capability, the agent-economy narrative shifts to the largest internet platforms in the world.

## Connections
- [[sources/tencent]] — Released by Tencent June 9, 2026; 495-step workflows in Yuanbao, QQ, and Tencent Docs represent Tencent's first production agent infrastructure at the frontier-tier
- [[entities/claude-fable-5]] — Shipped the same day; the 55× input-token price gap ($0.18/M vs $10/M) is the cleanest single-day expression of the bifurcated AI market between "premium safety" and "commodity scale" pricing
- [[ideas/china-efficiency-advantage]] — Hy3 is the first Chinese frontier-tier MoE to ship with a 21B active footprint; smaller than DeepSeek V4-Pro (49B active) by 2.3× while claiming the highest production step count; reinforces the China-efficiency thesis at the model level
- [[ideas/pricing-war]] — The $0.18/M input price undercuts every other frontier-tier model on OpenRouter; with the free two-week window, Hy3 is the most aggressive land-grab pricing in 2026
- [[topics/llm_models]] — 295B/21B MoE is the smallest active-parameter frontier-tier model to ship in 2026; the architecture bets that high total-parameter sparsity (295B) + small active (21B) is the optimal frontier-agent cost profile
- [[entities/tencent-hy3]] — Hy3's 21B active vs V4-Pro's 49B active is the next data point in the Chinese efficiency ladder; both are positioned to be served on commodity 8-GPU hardware with TileRT-style runtimes
- [[sources/anthropic]] — Tencent shipping Hy3 the same day as Fable 5 is the first direct head-to-head between a Chinese frontier agent model and an American frontier safety-routed model on the same week; represents the maturation of the bifurcated AI market
- [[ideas/open-platform-ai]] — Open weights on GitHub and Hugging Face plus OpenRouter distribution is the open-platform strategy applied at the agent-model layer; the open weights ensure Hy3's adoption is decoupled from Tencent's commercial interests
- [[topics/agentic_ai]] — 495-step production workflows in three separate Tencent products (Yuanbao, QQ, Tencent Docs) is the first time a single model release has demonstrated this step count in production; the agentic era's first billion-user agent infrastructure
