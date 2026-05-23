---
title: "Pydantic AI"
slug: pydantic-ai
type: framework
last_updated: 2026-05-22
---

# Pydantic AI

## What It Is
An AI agent framework using the Pydantic data validation library approach. Version 2.0 introduces "harness-first design" with capabilities as the core primitive—bundling tools, lifecycle hooks, instructions, and model settings into composable units. This architecture mirrors the shift from monolithic agents to modular, composable agent systems.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | Pydantic |
| Stars | 17.2k |
| Forks | 1.3k |
| Version | 2.0 |
| Architecture | Capability composition |

## Significance
Pydantic AI v2.0's "capability composition" architecture reflects the industry shift toward modular agent design. Rather than building single monolithic agents, developers compose systems from discrete capabilities—each capability bundling tools, instructions, and model settings. This makes agents more testable, maintainable, and reusable.

The concurrent release with Google ADK Python signals the agent framework space is consolidating around similar architectural patterns. Both ADK v2 and Pydantic AI v2 offer capability composition—this may become the standard pattern for agent development, similar to how React components standardized UI development.

## Connections
- [[entities/google-adk-python]] — Direct competitor; both launched v2 with similar "capability composition" architectures the same week, signaling industry consolidation around modular agent design
- [[topics/agentic_ai]] — Pydantic AI v2.0 is part of the agent tooling consolidation wave; capability composition enables the "autonomous team" vision
- [[topics/github_trends]] — 17.2k stars shows strong developer adoption; the Python-centric approach leverages Python's dominance in data/ML workflows
- [[ideas/mcp-infrastructure-battleground]] — Like ADK, Pydantic AI supports MCP for tool interoperability