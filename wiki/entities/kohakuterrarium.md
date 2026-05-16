---
title: "KohakuTerrarium"
slug: kohakuterrarium
type: framework
last_updated: 2026-05-15
---

# KohakuTerrarium

## What It Is
KohakuTerrarium is a general-purpose AI agent framework with a "Creature" abstraction (6-module agent model), built-in session persistence, TUI and Web UI out of the box, MCP support, and composition algebra for Python pipelines.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Stars | 320 |
| Forks | 24 |
| Creator | Kohaku-Lab |
| Focus | General-purpose AI agent framework |
| Key Features | Creature abstraction (6 modules), session persistence, TUI, Web UI, MCP support, composition algebra |
| Language | Python |

## Significance
KohakuTerrarium's "Creature" abstraction is a conceptual leap: instead of treating agents as functions or APIs, it models them as persistent entities with memory, state, and interfaces. The built-in TUI and Web UI remove a major friction point for developers who want to ship agent-based applications without building frontend infrastructure. Session persistence is particularly important for long-running agents that need to maintain context across hours or days. The composition algebra for Python pipelines suggests a functional-programming approach to agent orchestration, different from the graph-based or ReAct-based patterns common in other frameworks.

## Connections
- [[topics/agentic_ai]] — KohakuTerrarium's Creature abstraction represents a design-pattern evolution: agents as persistent entities rather than stateless functions; this aligns with the broader shift toward agents that operate continuously rather than completing single tasks
- [[topics/github_trends]] — KohakuTerrarium's 320 stars in its first trending week (May 15) reflects strong interest in frameworks that ship with both TUI and Web UI out of the box
- [[entities/alphora]] — Both are general-purpose agent frameworks shipping in the same week; KohakuTerrarium emphasizes session persistence and UI while Alphora emphasizes sandboxing and API compatibility
- [[entities/mcp-protocol]] — Built-in MCP support positions KohakuTerrarium as part of the MCP ecosystem; the protocol is becoming a standard integration point for agent frameworks
- [[ideas/agent-economy-infrastructure]] — Session persistence and built-in UIs are infrastructure features that make agents deployable in production; KohakuTerrarium is betting that developer experience (shipping with UI) is as important as model capability
- [[entities/openswarm]] — OpenSwarm is a multi-agent system for deliverables; KohakuTerrarium is a framework for building general-purpose agents — different layers of the stack but both signal the ecosystem maturing past prototypes
