---
title: "TrustFall"
slug: trustfall
type: vulnerability
last_updated: 2026-05-27
---

# TrustFall

## What It Is
TrustFall is a critical security vulnerability discovered in May 2026 that weaponizes the "folder trust" prompt mechanism in AI coding agents. The attack technique exploits the reflexive trust that developers place in folder permission prompts, allowing adversaries to gain unauthorized access and execute arbitrary code. It was discovered alongside SymJack and Mini Shai-Hulud as part of a coordinated security disclosure.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Discovery Date | 2026-05-26 |
| Researcher | Adversa AI |
| Type | Privilege escalation / RCE via prompt manipulation |
| Affected Agents | Claude Code, Gemini CLI, Cursor, Copilot, Grok Build |
| Severity | Critical |

## Significance
TrustFall exploits a psychological vulnerability rather than a technical one. Developers have been trained to reflexively accept folder trust prompts—it's a friction point that interrupts workflow, so users habitually click "allow." TrustFall weaponizes this behavior by crafting prompts that appear legitimate but actually grant expanded permissions.

Like SymJack and Mini Shai-Hulud, TrustFall demonstrates that the human approval step marketed as security by AI coding agent vendors is fundamentally inadequate against determined adversaries. These vulnerabilities represent architectural flaws in human-in-the-loop design, not bugs that can be simply patched.

## Connections
- [[entities/claude-code]] — Primary target of TrustFall; the folder trust prompt is a key part of its permission model
- [[entities/symjack]] — Discovered simultaneously with TrustFall; together they form a triad of critical vulnerabilities in AI coding agents
- [[entities/mini-shai-hulud]] — Third vulnerability in the same coordinated disclosure; all three exploit different aspects of the human-in-the-loop design
- [[topics/ai_security]] — TrustFall is one of three vulnerabilities revealing the broken trust architecture in AI coding agents
- [[ideas/ai-security-auditing-mainstream]] — The coordinated disclosure of these vulnerabilities marks a turning point in enterprise security posture toward AI coding agents