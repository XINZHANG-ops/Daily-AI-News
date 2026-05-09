---
title: "cocoindex"
slug: cocoindex
type: repo
last_updated: 2026-05-08
---

# cocoindex

## What It Is
cocoindex is an open-source incremental engine for long-horizon AI agents. It provides a framework for building persistent, stateful agents that maintain context and execute tasks over extended time periods with automatic state management and recovery. With 9,018 stars on GitHub, it addresses a critical gap in agent infrastructure: most agents lose state between sessions or fail when interrupted, making them unsuitable for multi-day or multi-week workflows.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Repo | cocoindex-io/cocoindex |
| Stars | 9,018 |
| Forks | 670 |
| Focus | Long-horizon agent state management |
| License | Open source |

## Significance
cocoindex represents a maturation in agent infrastructure beyond the "prompt-and-pray" paradigm. By treating agent state as a first-class citizen with incremental updates and automatic recovery, it enables agents to handle tasks that span hours, days, or weeks — such as research projects, multi-step business processes, or persistent monitoring. The incremental engine design mirrors how databases handle transactions, applying the same reliability principles to agent execution.

## Connections
- [[topics/agentic_ai]] — cocoindex fills the state-management gap that prevents agents from operating reliably over long time horizons; most existing frameworks assume agents complete tasks within a single session
- [[entities/ouroboros]] — Both repos trending May 8 signal a shift from prompt-driven to specification-driven agent architectures; cocoindex handles persistence while ouroboros handles declarative behavior
- [[entities/nanobot]] — nanobot's ultra-lightweight philosophy (4K lines) contrasts with cocoindex's incremental-engine approach, showing the agent ecosystem diverging between minimal harnesses and production-grade infrastructure
- [[entities/hive]] — Hive provides production multi-agent orchestration with self-healing DAGs; cocoindex complements this by solving the state-persistence layer that Hive's execution DAGs need for reliable long-horizon workflows
- [[ideas/agent-economy-infrastructure]] — Long-horizon agents are prerequisites for autonomous economic participation; cocoindex's state recovery makes it viable for agents to manage transactions and commitments that span days or weeks
- [[ideas/boring-infrastructure-shift]] — State management and recovery is exactly the kind of "boring infrastructure" the agent layer needs to move from demos to production deployments
