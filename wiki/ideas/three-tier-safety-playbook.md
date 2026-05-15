---
title: "Three-Tier Safety Playbook"
slug: three-tier-safety-playbook
last_updated: 2026-05-13
---

# Three-Tier Safety Playbook

## The Insight
The "three-tier" model approach — standard access for general users, verified access for vetted professionals, and permissive access for authorized red teaming — is becoming the new safety playbook for capability-restricted AI models. Anthropic pioneered this with Claude Mythos's controlled rollout (~12 partners), and OpenAI copied the structure with Daybreak while expanding distribution to 8+ security vendors simultaneously.

## Evidence
- [[entities/claude-mythos]] — Withheld from public release; restricted to ~12 US tech firms via Project Glasswing; standard/verified/permissive access tiers established the precedent
- [[entities/openai-daybreak]] — Three GPT-5.5 variants (standard, Trusted Access, permissive red-team) targeting Anthropic Mythos; 8+ security vendor distribution partners
- [[entities/gpt-5.5-cyber]] — OpenAI's Trusted Access for Cyber (TAC) program expanded to hundreds of organizations and EU institutions; the verified-defender tier predates Daybreak
- [[sources/anthropic]] — Anthropic's principled exclusion from Pentagon contracts is the commercial consequence of maintaining strict tiered access; EU regulators denied preview access
- [[sources/openai]] — OpenAI imposed identical Cyber restrictions on May 1 after mocking Anthropic's Mythos restrictions as "fear-based marketing"; liability now overrides competitive posturing

## Implications
This architecture is likely to become the template for all future frontier model releases in sensitive domains (cybersecurity, bio, autonomous systems). It creates a structured way to deploy powerful capabilities without fully releasing them, while still allowing vetted researchers and defenders to access them.

However, the tiered approach also creates geopolitical dependencies. Anthropic's refusal to grant EU regulators Mythos preview access — despite 4-5 meetings and Bundesbank demands — shows that tiered restrictions can disadvantage allies. OpenAI's EU Trusted Access expansion is explicitly geopolitical: "Europe's many defenders, not just the few." The safety playbook is becoming a foreign policy tool.

The 6-12 month window before adversaries replicate these capabilities makes the dependency particularly acute. If tiered access delays allied defenders while attackers develop independent capabilities, the safety architecture may inadvertently create security gaps rather than closing them.

## Connections
- [[ideas/safety-restricted-releases]] — The three-tier playbook is the operationalization of the capability-based restriction precedent Claude Mythos established
- [[ideas/eu-cyber-access-gap]] — The EU access gap is the geopolitical cost of the three-tier model when the creator restricts access to allies
- [[topics/ai_safety]] — The AI cybersecurity race is now a three-way contest (OpenAI Daybreak, Anthropic Mythos, Perceptron Mk1), each with different tiered-access implementations
- [[entities/perceptron-mk1]] — Perceptron's embodied agents add a third competitor, potentially requiring a fourth tier (physical-system access) in the safety playbook
