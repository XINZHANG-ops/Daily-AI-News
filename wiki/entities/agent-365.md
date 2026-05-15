---
title: "Agent 365"
slug: agent-365
type: product
last_updated: 2026-05-11
---

# Agent 365

## What It Is
Microsoft's standalone AI agent product, launched GA on May 1, 2026 at $15/user/month. Part of the first new enterprise Microsoft license architecture in a decade. Bundled into M365 E7 along with Copilot and Entra Suite, making agent capabilities inseparable from Microsoft's identity and governance stack.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Release Date | 2026-05-01 (GA) |
| Creator | Microsoft |
| Pricing | $15/user/month standalone |
| Bundle | Included in M365 E7 ($99/user/month) |
| Strategy | AI governance lock-in via identity stack |

## Significance
Agent 365 is Microsoft's bet that AI agent deployment is an enterprise governance problem, not a technology problem. By bundling agent access with Entra Suite identity management, Microsoft makes the security question inseparable from the licensing question — enterprises adopting agent-scale AI automatically adopt Microsoft's governance framework. Combined with GitHub Copilot Agent Tier ($49/agent/month), it creates a full-stack pricing model: per-user for human-facing agents, per-agent for autonomous coding.

On May 11, 2026, Agent 365 went GA with expanded capabilities: Shadow AI Discovery (detecting local agents via Defender/Intune), cross-platform visibility with AWS Bedrock and Google Cloud, Windows 365 for Agents (Cloud PC for agentic workloads), and pre-configured integrations with Genspark, Zensai, Egnyte, Zendesk, and Kore.ai. The critical strategic positioning is as a "$15/user/month toll booth" — a control plane that manages Claude Code, OpenClaw, GitHub Copilot CLI, and even competitors' AWS Bedrock agents. Microsoft is attempting to tax the entire agent ecosystem regardless of which model wins, making governance inseparable from the Microsoft stack. This is the most aggressive enterprise lock-in play since the E7 bundle launch, and it fundamentally reframes Agent 365 from a product to a platform layer.

## Connections
- [[entities/m365-e7]] — Bundled into E7 alongside Copilot and Entra Suite; the governance inseparable from the license
- [[entities/copilot-agent-tier]] — GitHub's $49/agent/month pricing is the developer counterpart to Agent 365's enterprise-user pricing
- [[sources/microsoft]] — Agent 365 is the culmination of Microsoft's decade-long identity-stack strategy: by embedding agent governance into Entra ID and M365 E7, Microsoft taxes every agent deployment in the enterprise at $15/user/month — a toll booth on the agent economy
- [[topics/agentic_ai]] — Agent 365 normalizes per-user AI agent pricing as a standard enterprise line item
- [[ideas/enterprise-ai-lock-in]] — Bundling agents with identity management makes switching costs structural, not just financial
- [[ideas/agent-governance-layer-wars]] — Agent 365's "toll booth" positioning is the most aggressive governance lock-in play since E7; Microsoft taxes the entire agent ecosystem regardless of which model wins
- [[entities/spec-kit]] — Spec-Kit provides deterministic agent validation; Agent 365 provides enterprise governance — the two address different layers of the agent reliability problem
- [[sources/google]] — Agent 365's cross-platform visibility includes Google Cloud; Microsoft is willing to monitor competitor infrastructure if it means owning the governance layer
- [[sources/anthropic]] — Agent 365 manages Claude Code deployments; Anthropic drives revenue while Microsoft captures governance margin — a parasitic but profitable relationship for Microsoft
