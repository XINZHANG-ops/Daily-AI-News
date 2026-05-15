---
title: "Agenvoy"
slug: agenvoy
type: repo
last_updated: 2026-05-13
---

# Agenvoy

## What It Is
Agenvoy is an agentic runtime written in Go with multi-provider concurrent dispatch, self-improving error memory via ToriiDB, and OS-native sandboxing. It features 7 LLM providers, an MCP client adapter, in-process subagents, and semantic search with OpenAI embeddings.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | agenvoy |
| Stars | 101 |
| Forks | 15 |
| Language | Go |
| Key Feature | Multi-provider concurrent dispatch |
| Memory | ToriiDB self-improving error memory |
| Sandboxing | OS-native |

## Significance
Agenvoy brings systems-language performance (Go) to the agent orchestration layer. The ToriiDB self-improving error memory is a novel approach to agent learning — rather than requiring manual prompt engineering for failure cases, the system automatically encodes error patterns into retrievable memory.

The MCP client adapter and 7-provider support show that interoperability and model-agnosticism are becoming default features for new agent infrastructure. Agenvoy's OS-native sandboxing (rather than container-based) suggests a lower-level, higher-performance security model suitable for edge deployment.

## Connections
- [[topics/github_trends]] — Agenvoy's 101 stars show Go-based agent runtimes gaining traction in the infrastructure layer
- [[entities/mcp-protocol]] — MCP client adapter shows the protocol has become a default integration target for new agent projects
- [[ideas/mcp-infrastructure-battleground]] — Agenvoy's native MCP support confirms that new agent infrastructure projects now treat MCP as the default integration layer, not an optional add-on — the protocol has crossed from experimental to foundational
- [[entities/frona]] — Both launched the same week with MCP support and multi-provider architectures; the open-source agent stack converges on interoperability
- [[topics/agentic_ai]] — ToriiDB's self-improving error memory represents a maturation in agent state management: agents that learn from their own failures without human intervention
