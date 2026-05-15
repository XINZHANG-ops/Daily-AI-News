---
title: "frona"
slug: frona
type: repo
last_updated: 2026-05-13
---

# frona

## What It Is
frona is a self-hosted personal AI assistant platform for creating autonomous agents. It features per-principal sandboxing with policy-driven syscall filtering, MCP support with bridge mode, browser automation, and credential vault integration. It supports 15+ LLM providers including Anthropic, OpenAI, Gemini, and DeepSeek.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | fronalabs |
| Stars | 132 |
| Forks | 28 |
| Key Feature | Per-principal sandboxing with policy-driven syscall filtering |
| Protocols | MCP with bridge mode |
| Providers | 15+ LLM providers |

## Significance
frona represents the privacy-first, self-hosted agent stack. Its per-principal sandboxing architecture treats each agent as an isolated security principal — a more rigorous security model than most hosted agent platforms. The MCP bridge mode enables interoperability with the growing MCP ecosystem without requiring cloud dependencies.

Supporting 15+ LLM providers signals a bet against vendor lock-in at the model layer. In an era where compute partnerships are restructuring competitive dynamics, frona's model-agnostic approach offers a hedge against the duopoly forming around OpenAI and Anthropic.

## Connections
- [[topics/github_trends]] — frona's 132 stars signal privacy-first agent infrastructure gaining developer attention
- [[entities/mcp-protocol]] — MCP bridge mode shows the protocol has become table stakes for new agent infrastructure projects
- [[ideas/mcp-infrastructure-battleground]] — frona's decision to build MCP support into its core architecture rather than as a plugin reflects the emerging consensus among new agent frameworks that MCP is becoming as fundamental as HTTP — the protocol layer on which the agent economy runs
- [[ideas/agent-democratization]] — Self-hosted, model-agnostic agent platforms democratize access to agentic AI outside the walled gardens of major labs
- [[entities/agenvoy]] — Both frona and Agenvoy launched the same week with MCP support and multi-provider architectures; the open-source agent stack is converging on interoperability standards
