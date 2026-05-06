---
title: "Agent Squad"
slug: agent-squad
type: framework
last_updated: 2026-05-05
---

# Agent Squad

## What It Is
A flexible multi-agent orchestration framework featuring intelligent intent classification and a SupervisorAgent that coordinates teams of specialized agents in parallel. It maintains conversation context across agent handoffs and supports AWS Bedrock, Anthropic, and OpenAI models.

## Key Facts

| Attribute | Value |
|-----------|-------|
| GitHub Stars | 7.6k |
| Forks | 720 |
| Orchestration Pattern | SupervisorAgent with parallel dispatch |
| Supported Providers | AWS Bedrock, Anthropic, OpenAI |

## Significance
Agent Squad sits in the growing "agent orchestration" layer between raw model APIs and end-user applications. Its model-agnostic design and cross-provider support position it as a neutral orchestration alternative to OpenAI's Symphony (OpenAI-centric) and Anthropic's Claude Code (Claude-only). The 7.6K stars suggest strong developer interest in frameworks that avoid vendor lock-in at the orchestration layer.

## Connections
- [[topics/agentic_ai]] — multi-agent orchestration framework enabling parallel specialized agent teams; part of the maturing agent stack between model APIs and end-user applications
- [[entities/symphony]] — both address agent orchestration, but Symphony is OpenAI-centric while Agent Squad is model-agnostic across Bedrock, Anthropic, and OpenAI
- [[entities/ruflo]] — Ruflo orchestrates 100+ Claude Code swarms at enterprise scale; Agent Squad is a general-purpose framework for smaller teams across any model provider
- [[sources/openai]] — supports OpenAI models alongside Anthropic and Bedrock, reflecting demand for multi-provider orchestration
- [[sources/anthropic]] — Claude is one of the models Agent Squad can route to; framework-agnostic design avoids Claude-only lock-in
