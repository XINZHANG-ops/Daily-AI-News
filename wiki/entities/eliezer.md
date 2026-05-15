---
title: "Eliezer"
slug: eliezer
type: repo
last_updated: 2026-05-09
---

# Eliezer

## What It Is
Eliezer is a tiny (~6,000 lines of TypeScript) self-hosted AI agent with a self-editing protocol — it can modify its own source code. Features include a Progressive Web App with push notifications, task scheduling, persistent SQLite memory with automatic context compaction, and compatibility with multiple LLM APIs (Kimi, Claude, Grok). At 3.2K stars, it represents the minimalist self-improving agent philosophy.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Stars | 3.2k |
| Forks | 412 |
| Language | TypeScript |
| Size | ~6,000 lines |
| Key Feature | Self-editing protocol (modifies own code) |

## Significance
Eliezer's self-editing protocol is the most philosophically significant feature. Most agents are static programs that call external APIs; Eliezer can rewrite its own implementation, creating a genuine self-modification loop within a constrained, auditable codebase. The 6K-line footprint makes this auditable — unlike Claude Code's 512K lines, a human can read Eliezer's entire source in an afternoon.

The automatic context compaction (SQLite memory that prunes old context) addresses a real operational problem that plagues long-running agents: context window bloat. The PWA-with-push-notifications architecture treats the agent as an asynchronous personal assistant rather than a synchronous chatbot — a design pattern that mirrors Perplexity's remote-control Mac mini concept.

## Connections
- [[entities/nanobot]] — Both are ultra-lightweight personal agents (Eliezer 6K lines TypeScript, nanobot 4K lines Python); together they validate that sophisticated agent functionality requires minimal code when designed with restraint
- [[ideas/agent-democratization]] — Eliezer's "bring your own LLM API key" model and tiny footprint democratize agent ownership; users aren't locked into any provider's infrastructure
- [[topics/agentic_ai]] — Self-editing agents represent a maturity level beyond tool-use; Eliezer proves this can be done safely in a small, auditable codebase rather than requiring frontier-model scale
- [[entities/ouroboros]] — Eliezer and ouroboros converge on the same problem from opposite directions: Eliezer uses runtime code mutation to let agents evolve behavior dynamically, while ouroboros uses declarative OS-level specification to constrain agent behavior structurally — together they represent the full spectrum of agent self-governance approaches
- [[entities/perplexity-computer]] — Eliezer's PWA with push notifications and task scheduling mirrors Perplexity's always-on agent concept, but at 1/1000th the infrastructure cost
- [[sources/perplexity]] — Perplexity's $200/month Max tier and Eliezer's BYO-key model represent opposite ends of the personal agent pricing spectrum; both converge on the same always-on, multi-platform vision
