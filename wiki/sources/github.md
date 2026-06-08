---
title: "GitHub"
slug: github
last_updated: 2026-05-13
---

# GitHub

## Overview
GitHub is the dominant platform for AI-assisted coding, having crossed 275 million commits per week and 17 million AI agent PRs in March 2026. On April 29, GitHub announced a Copilot Agent Tier at $49 per autonomous agent per month — the first major platform to monetize agent-scale usage, becoming a tollbooth on the agent economy it helped create.

## Timeline

| Date | Event | Details |
|------|-------|---------|
| 2026-04-29 | Copilot Agent Tier announced | $49/agent/month; free tier capped at 500 commits/month |
| 2026-04-27 | 275M commits/week, 17M AI PRs in March | Platform strain from agent-scale usage made the paywall economics necessary |
| 2026-05-13 | MCP Server secret scanning reaches GA | Allows AI coding agents and IDEs to scan code for exposed secrets before committing or opening PRs; honors existing push protection settings; signals MCP moving from experimental to production dependency |

## Key Relationships
- **Microsoft**: GitHub parent company; Azure AI Foundry integration
- **Claude Code, Codex, Cursor**: All depend on GitHub for CI/CD integration; now face $49/agent/month economics
- **OpenAI**: Codex competes directly with Copilot

## Connections
- [[entities/copilot-agent-tier]] — The pricing tier just announced; creates a paywall on agent-scale usage
- [[topics/github_trends]] — AI agents opened 17M PRs in March vs 4M in September 2025; scale created unsustainable free-tier economics
- [[ideas/agent-economics]] — GitHub becoming a tollbooth on the agent economy is the first platform-level monetization of agent usage
- [[entities/copilot-agent-tier]] — June 8: token billing replaces per-seat subscription pricing for enterprise accounts; metered usage across all Copilot models (including third-party routed) makes cost directly proportional to model selection — Opus 4.8 and GPT-5.5 at visible dollar premium vs Haiku 4.5 and Mellum2
- [[entities/mellum-2]] — June 8: Apache 2.0 release from JetBrains is the strategic beneficiary of GitHub's token billing — the cheapest viable model with no license restrictions is now the default sub-agent routing target
- [[topics/ai_funding]] — June 8: token billing captures upside when frontier models trend to $5-25/M output and protects margin when users migrate to cheaper models — same playbook as Snowflake on data warehousing
- [[entities/claude-mythos]] — June 8: Anthropic's 90% internal Claude adoption implies Mythos-class models are on the premium end of the new token billing — the model selected for autonomous agent tasks (Mythos 16+ hour duration) will be the most expensive per-token in the lineup
- [[sources/anthropic]] — June 8: GitHub Copilot's token billing is the most consequential enterprise pricing shift in the agentic-coding era; it makes Anthropic's enterprise Claude Opus 4.6 the most expensive autocomplete option in the lineup
- [[ideas/agent-economics]] — June 8: per-token billing replaces per-seat — the agent economy's first platform-level monetization of usage at scale; enterprise buyers can now see exactly which team is using which model
