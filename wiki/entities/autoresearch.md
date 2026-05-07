---
title: "AutoResearch"
slug: autoresearch
type: repo
last_updated: 2026-05-06
---

# AutoResearch

## What It Is
AutoResearch is an autonomous LLM research agent built by Andrej Karpathy that experiments overnight on a single GPU. Given a small training codebase (train.py, prepare.py, program.md), it iterates autonomously: modifying code, training for 5 minutes, evaluating validation bits-per-byte, and keeping improvements. The project is self-contained with minimal dependencies.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | Andrej Karpathy |
| Stars | 79.2K |
| Forks | 11.6K |
| GPU Requirement | Single GPU |
| Training Loop | 5 minutes per iteration |
| Metric | Validation bits-per-byte |

## Significance
AutoResearch represents a new category of autonomous scientific agent — one that doesn't just write code but runs experiments, evaluates results, and iterates without human supervision. At 79.2K stars, it signals strong demand for AI agents that can perform end-to-end research workflows. The minimal-dependency, self-contained design aligns with the post-MCP-vulnerability trend toward reducing supply chain risk. By operating on a single GPU, it makes autonomous research accessible to individual researchers and small labs, not just hyperscalers.

## Connections
- [[entities/andrej-karpathy-skills]] — AutoResearch extends Karpathy's "configuration over code" philosophy into autonomous experimentation; both projects emphasize minimal, self-contained systems
- [[topics/agentic_ai]] — AutoResearch is a scientific-agent archetype: an AI that performs the full research loop (hypothesis, experiment, evaluation, iteration) without human-in-the-loop
- [[topics/github_trends]] — 79.2K stars makes it the highest-starred new repo of May 6; validates demand for autonomous research agents
- [[entities/ml-intern]] — Hugging Face's ML engineer agent focuses on paper reading and model deployment; AutoResearch focuses on training-code iteration — complementary approaches to automating ML research
- [[sources/openai]] — Karpathy's projects often set patterns that OpenAI later productizes; AutoResearch's overnight-experiment paradigm may inform future Codex or research-agent products
- [[ideas/agent-verticalization]] — AutoResearch is a vertical agent for scientific experimentation, not general-purpose coding — another data point that the agent layer is fragmenting by profession