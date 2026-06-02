---
title: "nano-brain"
slug: nano-brain
type: repo
last_updated: 2026-06-01
---

# nano-brain

## What It Is
A tiny brain for AI agents. Local MCP server with persistent memory featuring hybrid search (BM25 + vector + LLM reranking) across sessions, codebases, and notes. Provides agents with long-term memory and retrieval capabilities.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Release Date | 2026-06-01 |
| Creator | nano-step |
| Stars | 4 |
| Forks | 1 |
| Type | Local MCP server with persistent memory |
| Key Feature | Hybrid search (BM25 + vector + LLM reranking) |

## Significance
Nano-brain addresses a key limitation of current AI agents: lack of persistent memory across sessions. While Claude Code and similar agents excel within a session, they forget everything when the session ends. Nano-brain provides hybrid search combining BM25 (keyword), vector (semantic), and LLM reranking for optimal retrieval.

The local MCP server approach means data stays on the user's machine — important for privacy-sensitive enterprise use cases. The hybrid search approach recognizes that no single retrieval method is optimal for all queries.

## Connections
- [[topics/github_trends]] — Trending repo for June 1, 2026; small but notable for addressing agent memory gap
- [[topics/agentic_ai]] — Nano-brain provides the memory infrastructure agents need for truly persistent assistance
- [[entities/mcp-protocol]] — Built as an MCP server; uses Model Context Protocol for standardized agent-tool communication
- [[ideas/local-ai-computing]] — Local-only approach keeps data on-device; privacy-first alternative to cloud memory services
- [[ideas/agent-economy-infrastructure]] — Memory infrastructure is essential for agent-to-agent commerce; agents need shared memory to negotiate and transact
