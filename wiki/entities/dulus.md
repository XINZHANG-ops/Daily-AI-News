---
title: "Dulus"
slug: dulus
type: repo
last_updated: 2026-05-16
---

# Dulus

## What It Is
Dulus is a lightweight autonomous AI agent inspired by Claude Code. It supports multiple LLM providers (Claude, GPT, Gemini, DeepSeek, Qwen), includes 27 built-in tools, MCP integration, voice input, Telegram bridge, and sub-agents. It is a Python reimplementation designed to work with any model.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | KevRojo |
| Stars | 215 |
| Forks | 28 |
| Language | Python |
| Key Feature | Multi-provider support with 27 built-in tools |

## Significance
Dulus represents the open-source ecosystem's rapid replication of Claude Code's design patterns. At 215 stars, it is early but significant as a "Claude Code for any model" — explicitly built to avoid vendor lock-in by supporting Anthropic, OpenAI, Google, DeepSeek, and Qwen simultaneously.

The multi-provider architecture signals a maturation in agent design: developers no longer assume a single model provider will dominate. Instead, they build routing layers that dispatch to the best model for each task. Dulus's 27 built-in tools and MCP integration show that the "agent as tool orchestrator" pattern — pioneered by Claude Code — is becoming the default open-source architecture.

## Connections
- [[entities/claude-code]] — Explicitly inspired by Claude Code's design patterns; multi-provider support is the key differentiator from the original
- [[entities/mcp-protocol]] — MCP integration is table stakes for new agent frameworks; Dulus follows the protocol-as-infrastructure pattern
- [[topics/github_trends]] — Part of the May 16 agent-framework wave alongside evonic and AgentClaw; all three converge on multi-agent, multi-provider architectures
- [[ideas/agentic-is-default]] — Dulus's "works with any model" philosophy exemplifies the agentic shift: the interface (autonomous tool orchestration) matters more than the underlying model
- [[entities/evonic]] — Both target multi-agent orchestration but from different angles: Dulus is lightweight personal agent, evonic is enterprise-scale platform