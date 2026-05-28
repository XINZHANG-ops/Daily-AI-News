---
title: "SymJack"
slug: symjack
type: vulnerability
last_updated: 2026-05-27
---

# SymJack

## What It Is
SymJack is a critical security vulnerability discovered in May 2026 that exploits the display-to-filesystem gap in AI coding agents. The attack technique allows adversaries to achieve remote code execution (RCE) by hijacking symbolic links (symlinks) during file operations. It specifically targets AI coding agents including Claude Code, Gemini CLI, Cursor, Copilot, and Grok Build.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Discovery Date | 2026-05-26 |
| Researcher | Adversa AI |
| Type | Symlink hijacking / RCE |
| Affected Agents | Claude Code, Gemini CLI, Cursor, Copilot, Grok Build |
| Severity | Critical |

## Significance
SymJack exposes a fundamental architectural flaw in how AI coding agents handle file system operations. The vulnerability exploits the gap between what users see on screen (the display) and where the system actually writes files. Users approve what they see, but the system can write to arbitrary locations via symlink manipulation.

This is not a bug to patch—it represents a systemic flaw in the human-in-the-loop design that the entire AI coding agent category shares. The "human approval step" that these tools market as security proves to be UI theater against sophisticated attacks like SymJack.

## Connections
- [[entities/claude-code]] — One of the primary targets of SymJack vulnerability; demonstrates that even the most popular AI coding agents share fundamental architectural flaws
- [[entities/cursor]] — Affected by SymJack; cursor's file system operation design allows symlink hijacking
- [[entities/grok-build]] — Affected by SymJack; xAI's coding agent vulnerable to the same attack vector
- [[entities/antigravity-cli]] — Google's shift to closed-source Antigravity may be partly motivated by security concerns like SymJack
- [[topics/ai_security]] — SymJack is one of three vulnerabilities (with TrustFall and Mini Shai-Hulud) discovered in the same week, exposing the broken trust architecture in AI coding agents
- [[ideas/ai-security-auditing-mainstream]] — These vulnerabilities signal that security auditing of AI agents has moved from niche research to mainstream enterprise concern