---
title: "cc-sdd"
slug: cc-sdd
type: repo
last_updated: 2026-05-11
---

# cc-sdd

## What It Is
cc-sdd (Claude Code Spec-Driven Development) is an open-source tool that enforces spec-first coding inside Claude Code. It rejects code that doesn't match its specification, ensuring that agent-generated code adheres to formal requirements rather than approximating them.

## Key Facts

| Attribute | Value |
|-----------|-------|
| GitHub Stars | 1.3K+ |
| Platform | Claude Code |
| Core Feature | Spec-first coding enforcement |
| Behavior | Rejects code that doesn't match specification |

## Significance
cc-sdd directly addresses one of Claude Code's biggest production risks: the agent generates code that looks correct but violates implicit requirements. By making the specification explicit and enforcing it automatically, cc-sdd turns Claude Code from a coding assistant into a spec-compliant development system. This is particularly important for enterprise adoption, where code must match architectural standards, security policies, and regulatory requirements.

The 1.3K stars suggest strong resonance with developers already using Claude Code who have encountered the "looks right but isn't" problem. As a Claude Code plugin rather than a standalone tool, cc-sdd benefits from the massive Claude Code user base and could see rapid adoption if Anthropic officially supports the spec-driven workflow.

## Connections
- [[topics/github_trends]] — 1.3K stars; niche but important — targets the specific gap between Claude Code's execution speed and enterprise compliance requirements
- [[topics/agentic_ai]] — cc-sdd makes Claude Code enterprise-ready by adding governance to generation; without spec enforcement, agent coding remains a prototype tool
- [[entities/spec-kit]] — Spec-Kit validates agent behavior against JSON specs; cc-sdd enforces spec compliance during code generation — the two form a spec-driven pipeline
- [[entities/gaai-framework]] — GAAI-framework generates specs from natural language; cc-sdd enforces those specs during coding — three tools could form a complete SDD toolchain
- [[ideas/spec-driven-development-movement]] — cc-sdd is the enforcement layer of the SDD movement; specs without enforcement are just documentation
- [[sources/anthropic]] — Claude Code is the platform; cc-sdd is the governance layer Anthropic hasn't built yet. If Anthropic adopts spec-driven workflows natively, it could differentiate from OpenAI's execution-first approach
- [[entities/claude-code]] — cc-sdd addresses Claude Code's primary enterprise objection: "It generates fast but I can't verify it matches requirements." Spec enforcement answers that objection
