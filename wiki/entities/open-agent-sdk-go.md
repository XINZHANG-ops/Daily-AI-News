---
title: "open-agent-sdk-go"
slug: open-agent-sdk-go
type: repo
last_updated: 2026-05-01
---

# open-agent-sdk-go

## What It Is
A lightweight open-source Go SDK for building AI agents. It runs the full agent loop in-process with 32 built-in tools, MCP support, session management, subagents, and permissions. No CLI or subprocess required.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Stars | 151 |
| Forks | 23 |
| URL | https://github.com/codeany-ai/open-agent-sdk-go |
| Language | Go |
| Built-in Tools | 32 |
| Features | MCP support, session management, subagents, permissions, in-process agent loop |

## Significance
open-agent-sdk-go brings the lightweight, zero-dependency philosophy to Go-based AI agent development. The in-process agent loop (no CLI or subprocess) means lower latency and simpler deployment compared to agents that shell out to external processes.

The MCP support positions it within the dominant agent protocol ecosystem, while the "no subprocess" design addresses security concerns around agent execution.

## Connections
- [[topics/github_trends]] — Trending May 1 with 151 stars
- [[entities/mcp-protocol]] — The Open Agent SDK's built-in MCP support signals that Go developers building production agents now expect protocol-native tooling rather than adapter-based integration, accelerating MCP's transition from experimental standard to infrastructure default
- [[ideas/agent-democratization]] — A lightweight Go SDK specifically for production agents lowers the infrastructure barrier for developers who prefer compiled languages and static binaries, expanding agent democratization beyond the Python-centric AI community