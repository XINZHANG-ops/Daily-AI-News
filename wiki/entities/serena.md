---
title: "Serena"
slug: serena
type: product
last_updated: 2026-05-03
---

# Serena

## What It Is
Serena is an MCP toolkit providing semantic code retrieval, editing, refactoring, and debugging across 40+ languages. It operates at the symbol level rather than line numbers, backed by LSP language servers, and is described as "the IDE for your coding agent."

## Key Facts

| Attribute | Value |
|-----------|-------|
| Release Date | 2026-05-02 |
| Creator | oraios |
| Stars | 23.8K |
| Forks | 1.6K |
| Languages | 40+ |
| Architecture | LSP-backed, symbol-level operations |

## Significance
Serena advances the coding agent ecosystem by providing semantic understanding rather than text-level code manipulation. Operating at the symbol level via LSP servers means agents can reason about code structure (functions, classes, variables) rather than line numbers, which are fragile across edits. As an MCP server, it integrates with any MCP-compatible coding agent, making it a composable infrastructure piece rather than a standalone tool.

## Connections
- [[entities/mcp-protocol]] — Built on the MCP protocol with 150M+ installs; Serena is a showcase of MCP's evolution from simple tool servers to semantic code infrastructure
- [[entities/claude-code]] — Serena provides the semantic code understanding layer that coding agents like Claude Code need for reliable refactoring across large codebases
- [[entities/codex]] — Competing coding agents benefit from Serena's language-agnostic semantic analysis; lowers the barrier for any agent to perform sophisticated code operations
- [[topics/agentic_ai]] — Part of the agent infrastructure layer maturing beyond raw model capabilities to domain-specific tooling
