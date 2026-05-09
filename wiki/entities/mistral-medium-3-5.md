---
title: "Mistral Medium 3.5"
slug: mistral-medium-3-5
type: model
last_updated: 2026-05-09
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

On May 5, Mistral officially launched Medium 3.5 with "Work Mode" in Le Chat — an on-device agentic mode for complex multi-step tasks — and "Remote Agents in Vibe," allowing coding agents to run asynchronously in the cloud and notify users when complete. These are infrastructure features for reliable agent execution, not capability breakthroughs. The EU AI Act Phase 2 fine of €11.2M on Mistral (for training-data transparency failures) landed the same week, making the privacy-first positioning — agents running on user-controlled environments — more urgent. By moving agent execution to user-controlled environments, Mistral reduces its regulatory exposure.

## Connections
- [[entities/vibe]] — Mistral bundled Vibe cloud coding agents with Medium 3.5; the model + agent stack strategy competes with standalone coding agents like Claude Code and Codex
- [[sources/mistral]] — Medium 3.5 is Mistral's first "merged" flagship, complementing the enterprise-focused Ultra 2; official May 5 launch adds Work Mode and Remote Agents in Vibe; EU AI Act €11.2M fine makes privacy-first positioning more urgent
- [[entities/mistral-ultra-2]] — Ultra 2 scored 78.4% SWE-bench at €2/M; Medium 3.5 at 77.6% is nearly equivalent but adds the reasoning toggle and Vibe agent integration
- [[entities/claude-opus-4-7]] — Medium 3.5's 77.6% SWE-bench lags Opus 4.7's 87.6% but the reasoning toggle and lower price point target a different market segment
- [[topics/llm_models]] — The unified chat+reasoning model with per-request toggle represents a design pattern alternative to the multi-model approach of OpenAI and Anthropic
- [[ideas/boring-infrastructure-shift]] — Work Mode and Remote Agents are the boring infrastructure for reliable agent execution — not exciting capabilities but the plumbing that makes agents deployable at scale
- [[ideas/government-pre-testing]] — EU AI Act Phase 2 fines (€11.2M on Mistral, €8.4M on Stability AI) prove Europe is taking a harder line than the US, creating a balkanized regulatory landscape
