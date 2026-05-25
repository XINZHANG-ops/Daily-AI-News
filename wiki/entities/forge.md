---
title: "Forge"
slug: forge
type: repo
last_updated: 2026-05-24
---

# Forge

## What It Is
An open-source reliability layer for self-hosted LLM tool-calling. Forge takes an 8B model from 53% to 99% on agentic tasks through guardrails including retry nudges, step enforcement, and error recovery.

## Key Facts

| Attribute | Value |
|-----------|-------|
| GitHub | antoinezambelli/forge |
| Function | Tool-calling reliability for self-hosted LLMs |
| Performance | 53% → 99% on agentic tasks (8B model) |
| Key Features | Retry nudges, step enforcement, error recovery |

## Significance
Forge addresses the critical reliability gap in self-hosted LLM deployments. By adding guardrails, it enables 8B models to achieve near-perfect tool-calling success rates, making smaller models viable for production agentic workflows. This democratizes access to reliable AI agents by reducing compute requirements.

## Connections
- [[topics/github_trends]] — New May 24 entry; represents the infrastructure layer needed for reliable self-hosted agent deployments
- [[topics/agentic_ai]] — Tool-calling reliability layer; enables 8B models to achieve 99% agentic task success
- [[entities/sentinel]] — Phantom tool-call detector released same day; together Forge + Sentinel provide end-to-end tool-calling reliability (correct execution + hallucination detection)