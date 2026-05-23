---
title: "Google ADK Python"
slug: google-adk-python
type: framework
last_updated: 2026-05-22
---

# Google ADK Python

## What It Is
An open-source, code-first Python framework for building AI agents. It enables developers to build, evaluate, and deploy sophisticated multi-agent systems with workflow runtime and task delegation capabilities. Released as Google's entry into the agent framework space alongside Pydantic AI and other agent development frameworks.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Release Date | 2026-05-22 |
| Creator | Google |
| Stars | 19.8k |
| Forks | 3.4k |
| Type | Agent development framework |

## Significance
Google ADK Python (Agent Development Kit) represents Google's formal entry into the agent framework space. The "code-first" approach differentiates it from low-code agent builders—developers write Python code to define agent behavior, workflow, and delegation patterns. This positions ADK as a competitor to Pydantic AI, LangChain, and other Python-based agent frameworks.

The 19.8k stars in under a day signals strong developer interest in a Google-backed agent framework. Combined with Google's other I/O 2026 announcements (Gemini 3.5 Flash, Spark, Omni), ADK completes Google's agent stack: model (Flash/Spark) → framework (ADK) → deployment (Vertex AI).

## Connections
- [[entities/pydantic-ai]] — Direct competitor; both are code-first Python frameworks for building agents; ADK vs Pydantic AI represents Google's vs Pydantic's approach to agent development
- [[topics/agentic_ai]] — ADK is part of the agent tooling consolidation; Google ADK v2 and Pydantic AI v2 both launched with similar "capability composition" architectures
- [[sources/google]] — Google's agent development framework; leverages Google's infrastructure (Vertex AI, TPUs) for deployment
- [[entities/gemini-3-5-flash]] — ADK integrates with Gemini models; Flash's low cost makes ADK-built agents economically attractive
- [[ideas/mcp-infrastructure-battleground]] — ADK's MCP support positions it in the protocol standardization battle for agent interoperability