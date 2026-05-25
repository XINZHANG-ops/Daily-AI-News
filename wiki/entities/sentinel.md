---
title: "Sentinel"
slug: sentinel
type: repo
last_updated: 2026-05-24
---

# Sentinel

## What It Is
A phantom tool-call detector for autonomous LLM agents. Sentinel uses layered detection—registry exact match, embedding similarity, and Gemini Flash verification—to detect when agents hallucinate non-existent tools.

## Key Facts

| Attribute | Value |
|-----------|-------|
| GitHub | yehor04/sentinel |
| Function | Hallucination detection for agent tool calls |
| Detection Methods | Registry exact match, embedding similarity, Gemini Flash verification |
| Release Date | 2026-05-24 |

## Significance
Sentinel addresses a critical security vulnerability: agents inventing non-existent tools. Combined with Forge (reliability layer), these two repos form a complementary pair—Forge ensures correct tool execution while Sentinel detects when tools are hallucinated entirely. Together they provide end-to-end tool-calling reliability.

## Connections
- [[topics/github_trends]] — New May 24 entry; addresses agent hallucination as a distinct security concern
- [[topics/agentic_ai]] — Phantom tool-call detector; complements reliability layers like Forge for complete agent safety
- [[entities/forge]] — Released same day; Forge handles retry/error recovery while Sentinel handles hallucination detection—both needed for production agent reliability