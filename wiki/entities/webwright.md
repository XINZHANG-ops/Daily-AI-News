---
title: "Webwright"
slug: webwright
type: repo
last_updated: 2026-05-13
---

# Webwright

## What It Is
Webwright is a terminal-based web agent harness developed by Microsoft, achieving state-of-the-art results: 86.7% on Online-Mind2Web and 60.1% on Odyssey long-horizon tasks. It uses a code-as-action paradigm with a workspace-as-state architecture. The core agent loop is minimal at approximately 450 lines.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | Microsoft |
| Stars | 2.4K |
| Forks | 312 |
| Online-Mind2Web | 86.7% |
| Odyssey | 60.1% |
| Architecture | Code-as-action with workspace-as-state |
| Core Loop | ~450 lines |

## Significance
Webwright's SOTA performance with a minimal ~450-line core loop challenges the assumption that web agents need complex browser-automation frameworks. The code-as-action paradigm — where the agent generates executable code to interact with web pages rather than using structured APIs — is a shift in how agents perceive and act on digital environments.

The workspace-as-state architecture treats the agent's working directory as its memory, making state management explicit and inspectable. This is philosophically different from the hidden state of neural-network-based agents. Microsoft's open-sourcing of Webwright signals that the web-agent layer is becoming a commodity, and the competitive moat will lie in what agents do with web access rather than how they achieve it.

## Connections
- [[sources/microsoft]] — Webwright is Microsoft's open-source entry into the web-agent category; its minimal design (~450 lines) contrasts with the complexity of proprietary web-agent systems
- [[topics/github_trends]] — 2.4K stars for a minimal web-agent harness achieving SOTA proves developers value simplicity and inspectability over feature-rich complexity
- [[topics/agentic_ai]] — Code-as-action paradigm challenges the MCP/browser-agent approach; if agents can generate code to interact with the web, structured APIs become optional
- [[entities/trymeka-agent]] — Pure vision + OS-level control at 72.7% WebArena represents another minimalist philosophy; Webwright's code-as-action is a third paradigm alongside vision-based and API-based approaches
- [[ideas/agent-infrastructure-layer]] — Webwright's workspace-as-state design is a convergent evolution with other infrastructure projects: explicit, inspectable state management is becoming preferred over hidden neural state
