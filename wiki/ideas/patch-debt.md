---
title: "Patch Debt"
slug: patch-debt
last_updated: 2026-05-24
---

# Patch Debt

## The Insight
Claude Mythos Preview found 10,000 critical vulnerabilities in one month, but only 97 were patched—a 100:1 ratio that reveals a fundamental bottleneck: AI can discover vulnerabilities faster than humans can fix them. This creates a new category of "patch debt" that compounds daily. Security teams need AI-assisted patching workflows, not just AI-assisted discovery. Otherwise, the vulnerability gap widens indefinitely.

## Evidence
- [[entities/claude-mythos]] — One month: 10,000 critical vulnerabilities found, only 97 patched; 100:1 ratio reveals AI-driven discovery outpaces human patching capacity
- [[sources/anthropic]] — Project Glasswing: Claude Mythos for cybersecurity; the model remains restricted to prevent misuse, but enterprise partners get access through the coalition
- [[topics/ai_safety]] — The discovery-patching gap is a new safety concern: more vulnerabilities known but unfixed may be worse than fewer vulnerabilities known

## Implications
The patch debt crisis has three implications:
1. **Security teams must adopt AI-assisted patching**: Not just AI for discovery, but AI for proposing and validating patches
2. **Vulnerability disclosure becomes paradoxical**: Finding more bugs without fixing them could increase risk if bad actors also gain access to AI-assisted discovery
3. **Capability restrictions may backfire**: Claude Mythos remains restricted partly because it's too good at finding vulnerabilities—but if the patching bottleneck exists regardless, restriction doesn't solve the underlying problem

## Connections
- [[entities/claude-mythos]] — The 100:1 ratio is the empirical basis for this idea; Glasswing project demonstrates AI can find vulnerabilities faster than humans fix them
- [[topics/ai_safety]] — Patch debt creates a new category of safety risk: known but unfixed vulnerabilities may be exploited by adversaries who also have AI assistance
- [[ideas/safety-restricted-releases]] — Claude Mythos restriction was partly about preventing misuse, but patch debt suggests restriction alone doesn't solve the vulnerability gap