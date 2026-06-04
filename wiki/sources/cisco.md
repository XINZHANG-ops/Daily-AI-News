---
title: "Cisco"
slug: cisco
last_updated: 2026-06-04
---

# Cisco

## Overview
Cisco Systems is a global leader in networking equipment and cybersecurity. In 2026, Cisco has emerged as a key independent voice in AI security research, publishing the canonical multi-turn vulnerability study that exposed a structural weakness in all 15 tested frontier AI models.

## Timeline

| Date | Event | Details |
|------|-------|---------|
| 2026-06-02 | Multi-turn vulnerability study published | Cisco tested 15 flagship AI models from OpenAI, Anthropic, Google, Amazon, and xAI; all showed dramatically higher failure rates under multi-turn attacks vs single-turn; xAI Grok 4.1 Fast jumped from 34.1% to 88.3% failure rate |

## Key Relationships
- [[sources/openai]] — OpenAI models were among the 15 tested; Cisco's findings implicate OpenAI's safety claims
- [[sources/anthropic]] — Claude had the lowest failure rates (2.19-3.64% single-turn, 11.16-16.20% multi-turn) but still demonstrated the structural vulnerability
- [[sources/google]] — Gemini models were part of the tested cohort
- [[sources/xai]] — xAI's Grok 4.1 Fast showed the most dramatic multi-turn jump; the headline finding of the study

## Connections
- [[ideas/multi-turn-structural]] — Cisco is the source of the canonical research that established multi-turn vulnerability as a structural property of frontier AI
- [[topics/ai_security]] — Cisco's research reframed how enterprises should evaluate AI security; single-turn benchmarks are now considered insufficient
- [[topics/ai_safety]] — The multi-turn finding directly challenges the safety narratives AI labs have been selling
- [[ideas/ai-security-auditing-mainstream]] — Cisco's research is the empirical foundation for the call to make multi-turn testing standard in security audits
