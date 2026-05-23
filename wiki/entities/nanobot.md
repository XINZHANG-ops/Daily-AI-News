---
title: "nanobot"
slug: nanobot
type: repo
last_updated: 2026-05-05
---

# nanobot

## What It Is
An ultra-lightweight personal AI agent built in approximately 4,000 lines of Python — 99% smaller than mainstream alternatives like Claude Code (512K lines). It supports multi-platform chat (Telegram, Discord, Slack, WhatsApp, Feishu), 11+ LLM providers, MCP protocol integration, long-term memory, cron scheduling, and a WebUI, all while using only ~100MB of RAM.

## Key Facts

| Attribute | Value |
|-----------|-------|
| GitHub Stars | 41.7k |
| Forks | 7.3k |
| Language | Python (~4,000 lines) |
| RAM Usage | ~100MB |
| LLM Providers | 11+ |
| Protocols | MCP |

## Significance
nanobot demonstrates that sophisticated agent functionality does not require massive codebases. At 41.7K stars, it has become one of the most popular lightweight agent frameworks — validating a "small core, composable tools" philosophy that contrasts sharply with the monolithic architecture of enterprise coding agents. Its multi-platform chat support and MCP compatibility make it a genuine universal agent harness rather than a terminal-only tool.

## Connections
- [[topics/agentic_ai]] — nanobot represents the lightweight personal agent category; its 4K-line footprint vs Claude Code's 512K lines shows the full spectrum of agent complexity, from minimal harnesses to full IDE replacements
- [[entities/mcp-protocol]] — MCP support enables nanobot to integrate with any MCP-compatible tool ecosystem without building custom adapters
- [[entities/claude-code]] — Claude Code is the 512K-line enterprise standard; nanobot proves 99% smaller implementations can deliver comparable multi-platform agent functionality for personal use
- [[entities/corecoder]] — both represent the minimal-code agent philosophy, but nanobot adds multi-platform chat and MCP while CoreCoder focuses purely on terminal coding
- karpathy's "configuration over code" principle (105K stars via CLAUDE.md) — resonates with nanobot's minimal-implementation approach
