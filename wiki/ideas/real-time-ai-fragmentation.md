---
title: "Real-Time AI Fragmentation"
slug: real-time-ai-fragmentation
last_updated: 2026-05-13
---

# Real-Time AI Fragmentation

## The Insight
The "real-time AI" category is fragmenting into use-case-specific architectures rather than converging on a single general-purpose model. On May 11-12, 2026, two models launched targeting the same 200ms latency threshold but from entirely different directions: Thinking Machines Lab's TML-Interaction-Small optimizes conversational flow, while Perceptron AI's Mk1 targets physical embodiment for manufacturing and robotics.

## Evidence
- [[entities/tml-interaction-small]] — 276B-parameter MoE with 12B active params; 200ms audio/video/text processing for human-like conversational flow; Murati's team bets cost efficiency beats raw capability for voice-first applications
- [[entities/perceptron-mk1]] — Physical AI model for video understanding and embodied reasoning; founded by former FAIR scientists; targets manufacturing, robotics, geospatial, and security
- [[entities/gpt-realtime-2]] — OpenAI's competing voice pipeline at $32/M tokens launched the prior week; TML undercuts on cost while matching latency
- [[topics/llm_models]] — The simultaneous launches reveal that "real-time AI" is not one market but multiple: conversational, physical, visual, and spatial each need different architectures

## Implications
If real-time AI fragments into domain-specific models, the competitive landscape shifts from "who has the best general model?" to "who owns the best architecture for each use case?" This favors specialized teams with deep domain expertise over generalist labs. It also means the integration layer — how these specialized models are composed into end-user experiences — becomes the critical infrastructure battleground.

The 200ms threshold itself may become a commodity. The differentiator will be what a model can do within that latency budget: hold a natural conversation, control a robotic arm, or analyze a security camera feed. The implication for investors and enterprises is that real-time AI portfolios should be diversified across architectures, not concentrated on a single provider.

## Connections
- [[sources/thinking-machines-lab]] — Mira Murati's lab validates that efficiency-first architectures can compete with OpenAI's capability-first approach in voice AI
- [[sources/openai]] — GPT-Realtime-2's premium pricing ($32/M tokens) may be vulnerable to MoE-based competitors if latency parity holds
- [[topics/agentic_ai]] — Real-time fragmentation means agent orchestration layers must handle heterogeneous model pipelines, not just route to "the best model"
- [[ideas/voice-agent-battleground]] — Voice models are becoming a distinct competitive dimension; TML-Interaction-Small proves startups can enter this space with focused architectures
