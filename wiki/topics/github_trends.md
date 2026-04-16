---
title: "GitHub Trends"
slug: github_trends
last_updated: 2026-04-16
---

# GitHub Trends

## Overview
The GitHub landscape in March-April 2026 is defined by the explosion of agent frameworks, the democratization of coding assistants, and the rapid commoditization of agent architectures. The most striking story is claw-code — a clean-room Python rewrite of Claude Code's architecture — reaching 100K stars in hours after Anthropic accidentally leaked Claude Code's source. This demonstrated that the "harness layer" is now as contested as model weights.

## Evolution

**Agent Frameworks Mature**: The period sees agent frameworks rapidly evolving from experimental prototypes to production-grade infrastructure. Microsoft Agent Framework v1.0 (April 2) provides enterprise-grade Python/.NET support with graph-based workflows, OpenTelemetry integration, and human-in-the-loop capabilities. AgentScope reaches production-ready status with MCP/A2A protocol support.

**Coding Agent Wars**: Claude Code's viral success spawned intense competition. Cursor 3 pivots from IDE to agent orchestration with parallel fleet approach. OpenClaw crosses 302,000 stars as the fastest-growing open-source project in history. Google's Gemini CLI enters the terminal agent race with 1M context and Apache 2.0 licensing.

**Agent Memory and Skills**: The skills ecosystem matures significantly. obra/superpowers reaches 155K stars as the complete software development methodology for coding agents. Hermes Agent crosses 35K stars with multi-platform support and browser integration. EvoSkill enables automatic skill discovery from failed trajectories.

**Efficient Inference**: Multiple projects address the efficiency frontier. Bonsai 8B (PrismML) achieves 40 tokens/sec on iPhone through 1-bit quantization. Ollama 0.19 doubles Apple Silicon performance via MLX integration. flash-moe runs 397B MoE at 4.4 tokens/sec on MacBook Pro.

**Browser and Web Automation**: LightPanda (Zig-built headless browser) achieves 11x faster performance and 16x less memory than Chrome headless. browser-use enables AI agents to control browsers for web automation.

## Notable Repositories

| Repo | Stars | Description |
|------|-------|-------------|
| obra/superpowers | 155K+ | Agentic skills framework for coding agents |
| ultraworkers/claw-code | 181K+ | Clean-room Claude Code rewrite, 100K in hours |
| nousresearch/hermes-agent | 35K+ | Self-improving agent with multi-platform support |
| microsoft/agent-framework | 9K+ | Enterprise multi-language agent framework |
| agentscope-ai/CoPaw | 15K+ | Personal AI assistant with multi-channel support |
| lightpanda-io/browser | 18K+ | Zig-built headless browser, 11x faster |
| HKUDS/nanobot | 39K+ | Ultra-lightweight universal agent harness |
| KeygraphHQ/shannon | 31K+ | White-box AI pentester, 96.15% XBOW success |

## Patterns & Insights

The "harness layer" has emerged as a critical battleground. claw-code's explosive growth demonstrates that closed-source agent architectures can be rapidly replicated — the competitive moat is narrower than assumed. This has implications for business models built on agent frameworks.

The multi-agent orchestration trend is accelerating. frameworks like microsoft/agent-framework, AgentScope, and CoPaw enable complex agent teams with specialized roles, parallel execution, and workflow orchestration.

The open-source agent ecosystem is rapidly converging on standards. MCP (97M+ installs), A2A protocol support, and cross-platform compatibility are becoming baseline expectations.

The efficiency frontier is democratizing access. 1-bit quantization, MLX optimization, and native hardware acceleration mean frontier-class models can now run on consumer devices.

## Connections
- [[entities/claude-code]] — Leaked source code spawned claw-code phenomenon
- [[entities/claw-code]] — Clean-room rewrite, 100K stars in hours
- [[entities/mcp-protocol]] — 97M installs, becoming foundational infrastructure
- [[entities/openclaw]] — 302K stars, fastest-growing open-source project
- [[ideas/agent-democratization]] — Open-source frameworks democratizing agentic AI
