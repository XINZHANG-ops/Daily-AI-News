---
title: "TML-Interaction-Small"
slug: tml-interaction-small
type: model
last_updated: 2026-05-13
---

# TML-Interaction-Small

## What It Is
TML-Interaction-Small is Thinking Machines Lab's first public model — a 276B-parameter mixture-of-experts (MoE) model with 12B active parameters. It processes audio, video, and text in 200ms chunks using time-aligned micro-turns for real-time exchanges with interruption support.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Release Date | May 11, 2026 |
| Creator | Thinking Machines Lab (Mira Murati) |
| Architecture | 276B MoE, 12B active parameters |
| Latency | 200ms chunks |
| Modalities | Audio, video, text |
| Key Feature | Time-aligned micro-turns with interruption support |

## Significance
200ms is the magic number for human-like conversational flow — the latency threshold where interruptions feel natural. TML-Interaction-Small is not just a model release; it's a claim on the "real-time AI" category. OpenAI shipped GPT-Realtime-2 the prior week at $32/M tokens, and now TML hits similar latency with a MoE architecture that's cheaper to run.

Murati's team is betting that cost efficiency at scale beats raw capability, at least for voice-first applications. This represents a different strategic thesis from OpenAI's capability-first approach: TML optimizes for the economics of real-time deployment rather than benchmark supremacy.

## Connections
- [[sources/thinking-machines-lab]] — First model from Mira Murati's lab after departing OpenAI; validates the efficiency-frontier thesis
- [[entities/gpt-realtime-2]] — OpenAI's competing voice pipeline at $32/M tokens; TML undercuts on cost while matching latency
- [[entities/perceptron-mk1]] — Both models launched within 24 hours, revealing an industry-wide race to own "real-time AI" before category definition solidifies
- [[topics/llm_models]] — TML's MoE architecture represents the cost-efficiency counter-position to OpenAI's capability-first approach in voice AI
- [[ideas/voice-agent-battleground]] — TML-Interaction-Small enters the voice model race as a standalone competitor from a well-funded startup, not a feature of an existing text model
- [[ideas/real-time-ai-fragmentation]] — TML is the conversational-latency case study in how real-time AI is splitting into specialized architectures rather than converging on a single model
