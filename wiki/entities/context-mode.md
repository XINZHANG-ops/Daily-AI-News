---
title: "Context Mode"
slug: context-mode
type: product
last_updated: 2026-05-02
---

# Context Mode

## What It Is
An MCP server for context window optimization in AI coding agents. Sandboxes tool output to achieve up to 98% context reduction across 12+ platforms including Claude Code, Gemini CLI, VS Code Copilot, Cursor, and OpenCode. TypeScript-based with 116 releases in its history. 11.9K stars.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Stars | 11.9K |
| Forks | 820 |
| Creator | mksglu |
| Platforms | Claude Code, Gemini CLI, VS Code Copilot, Cursor, OpenCode, 7+ more |
| Compression | Up to 98% context reduction |
| Tech Stack | TypeScript, MCP protocol |

## Significance
Context window management is becoming the critical infrastructure problem for agentic AI. As agents run continuously (the Symphony model) and generate massive tool output, context windows fill up with noise. Context Mode's 98% reduction rate directly addresses the economics: less context means faster inference, lower cost, and better agent decisions. The 12+ platform support signals that context optimization is not tied to any single vendor — it's a horizontal infrastructure layer. This is the practical response to the Five Eyes guidance warning about agent reliability: cleaner context means fewer unpredictable behaviors.

## Connections
- [[entities/mcp-protocol]] — Built on MCP, Context Mode demonstrates the protocol's utility as infrastructure plumbing; also highlights the irony that MCP both creates (150M installs vulnerability) and solves (context optimization) problems
- [[entities/symphony]] — Symphony's "every task gets an agent" model generates massive context pressure that Context Mode is designed to relieve; they're complementary infrastructure layers
- [[entities/claude-code]] — Primary target platform; Claude Code's context window management has been a pain point driving power users to seek optimization tools
- karpathy's CLAUDE.md skills approach — Both address agent quality: behavioral principles improve what the agent does, Context Mode improves what the agent sees
- [[topics/agentic_ai]] — Context optimization is becoming a prerequisite for agent reliability at scale; 98% reduction means agents can run longer and handle more complex tasks
- [[ideas/agent-economics]] — Context reduction directly lowers cost-per-task by reducing token consumption; 98% compression is a massive economic lever for agent-scale deployment
