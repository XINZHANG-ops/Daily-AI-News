---
title: "Headroom"
slug: headroom
type: repo
last_updated: 2026-06-10
---

# Headroom

## What It Is
Headroom is an open-source token compression tool released June 9, 2026, that compresses tool outputs, logs, files, and RAG chunks before they reach an LLM. The tool claims 60–95% fewer tokens with no answer-quality loss, and ships as a library, a proxy, and an MCP server. Headroom reached 21.1k GitHub stars within 24 hours of release.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Release Date | 2026-06-09 |
| Stars | 21.1k |
| Forks | 1.4k |
| Type | Library + proxy + MCP server |
| Compression Claim | 60–95% fewer tokens, no answer-quality loss |
| Targets | Tool outputs, logs, files, RAG chunks |
| Integration | Drop-in for Claude Code, Codex, and any MCP-compatible agent |

## Significance
Headroom addresses the single largest cost driver in production agent systems: tool output tokens. When an agent runs `gh pr view` or `kubectl get pods`, the raw output can be 5,000–50,000 tokens; most of it is irrelevant to the agent's task. Headroom's 60–95% token reduction with "no answer-quality loss" claim is the strongest data point in the compression category in 2026. The MCP-server shipping form means any agent can adopt Headroom by adding it to the tool list — no code changes required.

The 21.1k stars within 24 hours of release reveals that the agent cost optimization category is the new venture thesis. Earlier 2026 tools in this category (context-mode, Atomr Infer, vLLM optimizations) targeted the model-serving layer; Headroom targets the tool-output layer where the actual token waste happens. The "library + proxy + MCP server" trifecta is the same productization pattern as Mempalace and Agent-Reach — every agent infrastructure tool is shipping in all three forms to maximize adoption.

The 60–95% claim is broad; if Headroom can deliver 60% reduction on average across typical tool outputs, the cost savings for production agents are massive. Combined with Fable 5's 2× Opus 4.8 pricing and Hy3 at $0.18/M, the inference cost curve is now being attacked from three directions simultaneously: model price (Hy3), model tier (Fable 5 vs Opus 4.8), and tool output compression (Headroom).

## Connections
- [[topics/agentic_ai]] — Headroom is the canonical tool-output compression layer for agents; 21.1k stars in 24 hours reveals the demand
- [[topics/github_trends]] — Headroom (21.1k), Mempalace (55.2k), and Agent-Reach (25.8k) trending on June 9 represent the three layers of the agent stack (token compression, memory, internet access) all open-sourcing within 24 hours
- [[entities/agent-reach]] — Co-trending; the three together address tokens, memory, and internet — the three cost/latency bottlenecks of agentic systems
- [[entities/mempalace]] — Co-trending; all three shipping as library + proxy + MCP server
- [[entities/mcp-protocol]] — Ships as MCP server; the canonical "drop-in token compression" tool for MCP-compatible agents
- [[entities/context-mode]] — Earlier 2026 tool targeting context optimization; Headroom is the next-generation version with broader targets (tool outputs, logs, files, RAG chunks)
- [[entities/atomr-infer]] — Earlier 2026 tool targeting model-serving cost; Headroom targets tool-output cost; together they cover both ends of the agent cost stack
- [[ideas/commodity-inference-fragmentation]] — Headroom is the third layer of the inference cost fragmentation (model price, model tier, tool output compression); the cost stack is being attacked from every direction
- [[sources/anthropic]] — Headroom particularly targets Claude Code workflows where tool outputs are the largest token sink; the cost economics of Fable 5 (released same day) make tool-output compression more valuable, not less
