---
title: "MCP Protocol"
slug: mcp-protocol
type: protocol
last_updated: 2026-05-02
---

# MCP Protocol

## What It Is
The Model Context Protocol (MCP) is Anthropic's open protocol for connecting AI models to data sources and tools. It has become the dominant standard for building AI agents.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | Anthropic |
| Total Installs | 150M+ |
| Monthly Installs | 97M+ (March 2026) |
| Status | Donated to Linux Foundation |
| Adoption | Anthropic, OpenAI, Microsoft, Google |

## Significance
MCP crossed 97 million installs in March 2026, signaling its transition from experimental standard to foundational infrastructure. Its donation to the Linux Foundation and adoption by all major AI labs has made it the de facto standard for agent tool integration.

On April 21, 2026, security researchers discovered a critical "by design" flaw in MCP enabling arbitrary command execution across 7,000+ servers and 150 million downloads. The vulnerability affects MCP SDKs in Python, TypeScript, Java, and Rust. Anthropic declined to fix the architectural issue, citing it as "expected behavior" — effectively classifying a remote code execution vulnerability as an acceptable feature. This has raised serious questions about MCP's security model as it becomes foundational infrastructure for AI agents worldwide.

## Connections
- [[sources/anthropic]] — Created by Anthropic; vulnerability disclosed April 21
- [[topics/ai_safety]] — Critical supply chain vulnerability affecting 150M+ installations
- [[topics/github_trends]] — 97M installs, foundational infrastructure for agents
- [[ideas/safety-restricted-releases]] — Anthropic's "expected behavior" stance represents a new approach to security vulnerabilities
- [[entities/aws-mcp-server]] — AWS MCP Server with 15,000 API operations is the most comprehensive MCP implementation to date; validates the protocol as enterprise-grade infrastructure and addresses the supply chain security concerns the April 21 vulnerability exposed
- [[ideas/agent-economy-infrastructure]] — AWS MCP Server provides the cloud resource access layer that agents need to manage enterprise infrastructure at scale; "Skills" feature packages AWS tribal knowledge as reusable primitives
