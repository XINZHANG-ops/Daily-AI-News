---
title: "Agent-Context"
slug: agent-context
type: repo
last_updated: 2026-04-28
---

# Agent-Context

## What It Is
VS Code extension that lets AI coding tools see reference projects by attaching external folders via symlinks. Solves the context problem for agents working on new features — when an agent needs to understand patterns from existing projects, Agent-Context makes those projects visible to the AI tool.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Stars | 2 |
| Forks | 0 |
| Platform | VS Code |
| Purpose | Context injection for AI coding agents |

## Significance
The core problem Agent-Context addresses is that AI coding agents typically only see the project they're working in. When onboarding a new feature or understanding a legacy codebase, developers often want the AI to reference similar patterns from other projects — but those projects aren't in the working directory. Agent-Context solves this by symlinking external folders into the workspace, making them visible to the AI tool without requiring the agent to manually copy files or maintain context windows.

This is a lightweight, practical tool addressing a real friction point in agentic AI workflows.

## Connections
- [[topics/github_trends]] — Tooling to improve AI coding agent context awareness
- [[entities/codex]] — Codex competes in the general coding agent space; Agent-Context improves context for any agent
- [[topics/agentic_ai]] — Part of the agent tooling ecosystem solving workflow friction
