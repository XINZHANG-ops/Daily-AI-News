---
title: "Heretic"
slug: heretic
type: tool
last_updated: 2026-05-27
---

# Heretic

## What It Is
Heretic is a tool that can remove safety guardrails from open-source AI models in under 10 minutes. Discovered by researchers in May 2026, it has been downloaded over 13 million times, making it essentially commodity infrastructure for model hardening—or attack, depending on intent. The tool targets models including Gemma 3 and Llama 3.3.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Discovery Date | 2026-05-26 |
| Download Count | 13 million+ |
| Removal Time | Under 10 minutes |
| Target Models | Gemma 3, Llama 3.3 |
| Type | Guardrail stripping tool |

## Significance
The 13 million downloads of Heretic underscore how widespread guardrail-stripping capabilities already are. This is not a niche tool—it's commodity infrastructure that anyone can access. The under-10-minute removal time renders current RLHF (Reinforcement Learning from Human Feedback) alignment efforts fragile against determined adversaries.

More critically, Heretic creates an asymmetric regulatory challenge: responsible AI providers invest heavily in alignment work that adversaries can strip effortlessly. The EU AI Act's "sufficiently capable" model threshold becomes almost meaningless when a 10-minute download defeats months of safety work.

This represents an arms race that decisively favors attackers. While defenders invest months in safety research, attackers can strip those protections in minutes with freely available tools.

## Connections
- [[entities/gemma-4]] — One of the target models for Heretic guardrail stripping; Google's open-source model can be easily modified to remove safety features
- [[entities/llama-4]] — Another target; Meta's open-weight model similarly vulnerable to guardrail removal
- [[topics/ai_security]] — Heretic exemplifies the asymmetric regulatory challenge where defenders invest months while attackers strip in minutes
- [[ideas/alignment-reality-check]] — Heretic demonstrates that RLHF alignment is fundamentally fragile against adversaries; the 13M downloads show this capability is already widespread