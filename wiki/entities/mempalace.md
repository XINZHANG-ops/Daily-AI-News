---
title: "Mempalace"
slug: mempalace
type: repo
last_updated: 2026-06-10
---

# Mempalace

## What It Is
Mempalace is a local-first AI memory system released June 9, 2026, that stores conversations verbatim and retrieves them via semantic search. The system uses a palace/wing/room/drawer layout for organizing memory and achieves 96.6% R@5 on LongMemEval without calling an LLM in the retrieval loop. It ships with an MCP server and Claude Code hooks for automatic conversation saving. Mempalace reached 55.2k stars on GitHub, making it the highest-starred agent memory system of 2026.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Release Date | 2026-06-09 |
| Stars | 55.2k |
| Forks | 7.2k |
| Layout | palace/wing/room/drawer |
| Storage | Local-first, verbatim conversations |
| Retrieval | Semantic search, no LLM in loop |
| LongMemEval | 96.6% R@5 |
| MCP Server | Yes |
| Claude Code Integration | Auto-save hooks |

## Significance
Mempalace's 96.6% R@5 on LongMemEval without LLM in the retrieval loop is the strongest evidence that the agent memory category is not LLM-bound. Existing systems (SupermemoryAI, TrustGraph, etc.) all call an LLM at retrieval time to synthesize context; Mempalace proves that semantic search over verbatim storage is competitive with LLM-mediated retrieval. The cost and latency implications are significant: agent systems that previously spent tokens on every memory lookup can now do it with embedding similarity alone.

The 55.2k stars within 24 hours of release is the highest-viral moment for the agent memory category in 2026. The MCP server and Claude Code hooks for automatic conversation saving mean Mempalace can be deployed as a drop-in memory backend for any Claude Code workflow — the developer experience is "install Mempalace, all my conversations are now searchable forever."

The palace/wing/room/drawer layout is the most distinctive UX decision: memory is organized hierarchically (palace → wings → rooms → drawers), and the user can navigate the hierarchy to find conversations. This is a deliberate departure from the "vector database with chat" pattern most agent memory systems use; Mempalace bets that hierarchical organization is more discoverable than flat semantic search even with a strong underlying retrieval model.

## Connections
- [[topics/agentic_ai]] — Mempalace is the most-viral agent memory system of 2026; the 96.6% R@5 without LLM in loop proves the memory layer can be commoditized below the model
- [[entities/longmemeval]] — 96.6% R@5 is the highest score in the agent memory category in 2026; achieved without LLM in the retrieval loop, breaking the assumption that LLM-mediated retrieval is required for high performance
- [[entities/mcp-protocol]] — Ships with native MCP server, making it composable with Claude Code, Codex, and any MCP-compatible agent; represents the agent memory layer standardized on MCP
- [[entities/claude-code]] — Auto-save hooks integrate Mempalace directly into Claude Code workflows; the canonical "drop-in memory backend for Claude Code" pattern
- [[entities/longmemeval]] — Direct competitor; SupermemoryAI uses LLM-mediated retrieval and reached #1 on LongMemEval, LoCoMo, and ConvoMem earlier in 2026 — Mempalace now beats SupermemoryAI on LongMemEval without LLM in loop
- [[topics/github_trends]] — Mempalace (55.2k), Agent-Reach (25.8k), and Headroom (21.1k) trending on June 9 represent the three layers of the agent stack (memory, internet access, token compression) all open-sourcing within 24 hours
- [[entities/snowey]] — Snowey (June 8) uses FTS5 session search for memory; Mempalace uses semantic search — different technical bets for the same agent memory need, with Mempalace now the higher-viral release
- [[ideas/boring-infrastructure-shift]] — Mempalace represents the memory layer becoming "boring infrastructure" — local-first, MCP-compatible, no LLM in loop; the layer is being commoditized below the model
