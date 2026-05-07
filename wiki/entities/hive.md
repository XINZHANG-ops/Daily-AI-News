---
title: "Hive"
slug: hive
type: repo
last_updated: 2026-05-06
---

# Hive

## What It Is
Hive is a multi-agent harness for production AI workloads. It features a graph-based execution DAG for agent coordination, role-based evolving memory, self-healing graph evolution on failure, cost enforcement, and human-in-the-loop controls. It is model-agnostic via a unified provider gateway.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | aden-hive |
| Stars | 10.2K |
| Forks | 5.6K |
| Architecture | Graph-based execution DAG |
| Memory | Role-based evolving memory |
| Failure Handling | Self-healing graph evolution |

## Significance
Hive addresses the production-reliability gap in multi-agent systems. Most agent frameworks (Serena, context-mode, Ruflo) focus on coding or semantic infrastructure; Hive focuses on operational resilience: what happens when an agent fails, costs exceed budget, or human approval is required mid-workflow. The self-healing graph evolution — automatically restructuring the execution DAG when agents fail — is a production-grade feature absent from most open-source alternatives. At 10.2K stars, it signals enterprise interest in agents that don't break production pipelines.

## Connections
- [[entities/ruflo]] — Ruflo orchestrates 100+ Claude Code agents as coordinated swarms; Hive provides the production harness (DAG coordination, cost enforcement, self-healing) that would make Ruflo's swarms reliable at enterprise scale
- [[entities/serena]] — Serena provides semantic code operations; Hive provides the execution orchestration layer — together they represent the full stack from code understanding to reliable deployment
- [[topics/agentic_ai]] — Hive's production-focus (cost enforcement, human-in-the-loop, self-healing) signals the agent ecosystem maturing from "can it work?" to "can it run in production?"
- [[ideas/agent-economy-infrastructure]] — Production multi-agent harnesses like Hive are prerequisite infrastructure for agents as economic participants; Stripe's payments and IBM's governance assume agents that don't fail mid-transaction
- [[entities/context-mode]] — 98% context reduction enables agents to run longer; Hive's DAG orchestration enables those long-running agents to coordinate without losing state or exceeding budgets