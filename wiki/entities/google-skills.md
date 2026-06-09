---
title: "google/skills"
slug: google-skills
type: repo
last_updated: 2026-06-09
---

# google/skills

## What It Is
The official Google repository of Agent Skills for Google products and technologies — modular, reusable capability packs that agents can load on demand across Gemini, Cloud, Workspace, and developer APIs. Released as a top-3 trending GitHub repo on June 9, 2026 (12.8k stars, 986 forks), the repo formalizes Google's commitment to a standardized "skills" abstraction for agent capabilities.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | Google |
| Stars (June 9) | 12.8k |
| Forks | 986 |
| Type | Agent capability library |
| Targets | Gemini, Cloud, Workspace, developer APIs |
| Trending | Top 3 on GitHub (June 9, 2026) |

## Significance
google/skills is Google's answer to the agent capability problem that has fragmented across vendors. Each agent framework (LangChain, LlamaIndex, Haystack, Agno, OpenAI's tools API, Anthropic's MCP servers) has its own way of packaging capabilities. Google's bet: if you can ship a "skills" abstraction that works across all your surfaces (Gemini for consumer, Cloud for enterprise, Workspace for productivity), the abstraction itself becomes the moat.

The 100+ curated skills shipped via the Antigravity integration in NotebookLM is the canonical use case. Each skill is a modular, reusable capability pack (browser automation, code execution, data analysis, document generation) that any compatible agent can load. The standards battle is now: Google's Skills vs Anthropic's MCP servers vs OpenAI's tools API vs LangChain's tool abstractions. The winner of this standards war will own the agent capability distribution layer for the next decade.

## Connections
- [[sources/google]] — Released by Google as part of the Antigravity/NotebookLM launch; positions Google as the agent capability standard
- [[entities/antigravity-platform]] — Antigravity is the runtime that consumes skills; skills are the capability packs Antigravity agents load
- [[entities/mcp-protocol]] — Anthropic's MCP is the competing standard; Skills vs MCP is the canonical agent capability standards battle
- [[topics/agentic_ai]] — Skills abstraction represents the maturation of agent capability distribution; moves from "wire 20 different APIs" to "load one skill pack"
- [[topics/github_trends]] — Trending on June 9, 2026 alongside last30days-skill and turbovec — three infrastructure-layer repos trending simultaneously
- [[ideas/protocol-standardization]] — google/skills is Google's bet on the Skills standard; will compete with MCP for agent capability distribution dominance
- [[entities/last30days-skill]] — Concurrent trending repo; both reflect the "skill" abstraction becoming a category of its own
- [[ideas/agent-infrastructure-layer]] — Skills is the latest layer of the agent infrastructure stack to crystallize
