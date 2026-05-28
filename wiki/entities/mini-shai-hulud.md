---
title: "Mini Shai-Hulud"
slug: mini-shai-hulud
type: vulnerability
last_updated: 2026-05-27
---

# Mini Shai-Hulud

## What It Is
Mini Shai-Hulud is a security vulnerability discovered in May 2026 that achieves persistence in AI coding agents by injecting malicious settings files. These settings files re-execute across sessions, allowing attackers to maintain persistent access even after the initial attack vector is closed. Discovered alongside SymJack and TrustFall, it represents the third major vulnerability in the coordinated disclosure.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Discovery Date | 2026-05-26 |
| Researcher | Adversa AI |
| Type | Persistence via settings injection |
| Affected Agents | Claude Code, Gemini CLI, Cursor, Copilot, Grok Build |
| Severity | Critical |

## Significance
Mini Shai-Hulud demonstrates that AI coding agents can be compromised not just for immediate remote code execution, but for persistent access across sessions. By injecting malicious configurations into settings files that are loaded on startup, attackers can maintain a foothold even after the initial vulnerability is patched.

The name "Shai-Hulud" (the giant sandworms from Frank Herbert's Dune) suggests the scale and persistence of this threat—once embedded, it's difficult to root out. This vulnerability, combined with SymJack and TrustFall, exposes the fundamental trust problem in AI coding agents: the human approval step that these tools market as security is UI theater against sophisticated attacks.

## Connections
- [[entities/claude-code]] — Affected by Mini Shai-Hulud; settings file injection allows persistent compromise
- [[entities/symjack]] — First vulnerability in the coordinated disclosure; exploits display-to-filesystem gap
- [[entities/trustfall]] — Second vulnerability; exploits reflexive trust in folder prompts
- [[topics/ai_security]] — All three vulnerabilities expose broken trust architecture; enterprises must assume adversarial environments
- [[ideas/ai-security-auditing-mainstream]] — These vulnerabilities mark a turning point in enterprise security posture toward AI coding agents