---
title: "trymeka/agent"
slug: trymeka-agent
type: repo
last_updated: 2026-05-10
---

# trymeka/agent

## What It Is
trymeka/agent is a state-of-the-art autonomous computer-using agent achieving 72.7% on the WebArena Benchmark. Unlike browser-layer screenshot agents, it uses pure vision as input with OS-level controls — mimicking human visual perception and physical interaction with the operating system. It supports OpenAI o3, Claude Sonnet 4, Claude Opus 4, and Gemini.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Repo | trymeka/agent |
| Stars | 366 |
| Forks | 16 |
| WebArena Score | 72.7% |
| Input Modality | Pure vision (like humans) |
| Control Level | OS-level (not browser-layer) |
| Supported Models | OpenAI o3, Claude Sonnet 4, Claude Opus 4, Gemini |

## Significance
trymeka/agent represents a leap in autonomous agent architecture: OS-level control via pure vision rather than browser-layer screenshots or API integrations. The 72.7% WebArena score is state-of-the-art, but the architectural choice matters more than the number. Most computer-use agents operate within browser sandboxes; trymeka operates at the OS level, enabling actions across any application. The pure-vision approach also means it doesn't depend on specific apps exposing APIs — it sees the screen and clicks like a human. This is a direct challenge to the MCP-centric agent architecture that assumes apps will expose structured interfaces.

## Connections
- [[topics/agentic_ai]] — trymeka/agent's OS-level vision approach challenges the dominant MCP/browser-agent paradigm; if agents can control any app via vision, the protocol layer becomes optional rather than mandatory
- [[entities/agent-squad]] — Agent Squad orchestrates multiple agents via SupervisorAgent; trymeka demonstrates that a single vision-based agent can handle complex multi-app workflows without orchestration overhead
- [[ideas/agent-verticalization]] — Pure vision + OS control makes trymeka immediately applicable to any vertical workflow (finance, legal, design) without building custom connectors for each tool
- [[sources/openai]] — o3 integration shows OpenAI's latest reasoning model applied to visual computer control; this is a different deployment paradigm from Codex's code-focused approach
- [[sources/anthropic]] — Claude Sonnet 4 and Opus 4 integration validates Anthropic's vision capabilities for agentic use cases beyond coding
- [[sources/google]] — Gemini support positions trymeka as model-agnostic, but the pure-vision architecture is particularly complementary to Gemini's multimodal strengths
