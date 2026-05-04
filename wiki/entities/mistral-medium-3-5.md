---
title: "Mistral Medium 3.5"
slug: mistral-medium-3-5
type: model
last_updated: 2026-05-03
---

# Mistral Medium 3.5

## What It Is
Mistral Medium 3.5 is a 128B dense transformer (not MoE) that unifies chat, reasoning, and code capabilities in a single model with a configurable reasoning-effort toggle per request. It features 256K context, SWE-Bench Verified 77.6%, AIME25 86.3%, and can be self-hosted on 4 GPUs at FP8 precision.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Release Date | 2026-05-02 |
| Creator | Mistral AI |
| Architecture | 128B dense transformer |
| Context Window | 256K tokens |
| SWE-Bench Verified | 77.6% |
| AIME25 | 86.3% |
| Pricing | $1.50/$7.50 per million tokens |
| Self-hosting | 4 GPUs at FP8 |

## Significance
The reasoning-effort toggle is the key design innovation: instead of shipping separate "reasoning" and "chat" models (OpenAI's o-series vs GPT series), Mistral lets one model switch modes per-request. At $1.50/$7.50 per million tokens, it undercuts GPT-4o on input but sits in premium territory on output. The 77.6% SWE-bench score places it between Devstral 2 (72.2%) and Claude Opus 4.5 territory — solid but not category-defining. The real strategic play may be the bundled Vibe cloud coding agents: Mistral is betting enterprises want vertically integrated model + agent stacks, not just APIs.

## Connections
- [[entities/vibe]] — Mistral bundled Vibe cloud coding agents with Medium 3.5; the model + agent stack strategy competes with standalone coding agents like Claude Code and Codex
- [[sources/mistral]] — Medium 3.5 is Mistral's first "merged" flagship, complementing the enterprise-focused Ultra 2
- [[entities/mistral-ultra-2]] — Ultra 2 scored 78.4% SWE-bench at €2/M; Medium 3.5 at 77.6% is nearly equivalent but adds the reasoning toggle and Vibe agent integration
- [[entities/claude-opus-4-7]] — Medium 3.5's 77.6% SWE-bench lags Opus 4.7's 87.6% but the reasoning toggle and lower price point target a different market segment
- [[topics/llm_models]] — The unified chat+reasoning model with per-request toggle represents a design pattern alternative to the multi-model approach of OpenAI and Anthropic
