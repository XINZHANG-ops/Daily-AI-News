---
title: "Claude Mythos"
slug: claude-mythos
type: model
last_updated: 2026-05-29
---

# Claude Mythos

## What It Is
Claude Mythos is Anthropic's most advanced AI model, specifically designed for cybersecurity applications. Internal documents describe it as "the most capable we've built" with "dramatically higher" scores than Claude Opus 4.6 on coding and cybersecurity benchmarks. The model is capable of discovering previously unknown (zero-day) vulnerabilities in production codebases — abilities Anthropic classified as "unprecedented cybersecurity risks."

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | Anthropic |
| Release Date | Withheld from public release |
| Parameters | ~10 trillion (Claude Mythos 5 confirmed April 22) |
| Primary Use | Cybersecurity vulnerability discovery |
| Access | Restricted to Project Glasswing coalition (40+ partners); EU regulators denied preview access |
| EU Meetings | 4-5 meetings with EU regulators; no access granted |
| Bundesbank Demand | Germany's Bundesbank publicly demanded Mythos access May 12, 2026 |

## Significance
Claude Mythos represents a watershed moment in AI development — the first time a major lab has withheld a frontier model from public release not because of misuse risk by humans, but because the model's own capabilities pose national security concerns. The model discovered thousands of zero-day vulnerabilities including a 27-year-old bug in OpenBSD.

The controversy triggered emergency government response at the highest levels: VP Vance and Treasury Secretary Bessent convened calls with tech and finance CEOs. UK regulators accelerated assessments. The model caused a ~$2T enterprise software selloff.

Project Glasswing was launched as an alternative — a consortium with 40+ partners (Microsoft, Apple, Amazon, Google, NVIDIA, CrowdStrike, Cisco, JPMorgan) sharing defensive insights derived from Mythos discoveries. Anthropic committed $100M in credits to fix the vulnerabilities found.

By April 20, the NSA confirmed partnership with Anthropic through Project Glasswing. Claude Mythos identified thousands of zero-day vulnerabilities through the coalition. This represents the first government-level validation of Mythos capabilities and the restricted-access model for frontier AI safety.

By April 22, central banks worldwide responded. The Bank of England governor warned that Anthropic may have found a way to "crack the whole cyber-risk world open." Intelligence agencies globally scrambled to understand Mythos implications — marking the first time an AI model triggered emergency responses from central banks and intelligence agencies simultaneously.

By May 8, Mozilla detailed using Claude Mythos Preview to identify and patch security vulnerabilities in the Firefox browser codebase. The AI analyzed C++ and Rust code to find memory safety issues and logic bugs that escaped human review. This marked a maturation point for AI-assisted security: a major browser vendor trusting an AI model with production code security.

By May 10, Claude Mythos Preview discovered thousands of additional zero-day vulnerabilities including a 27-year-old bug in OpenBSD and a 17-year-old remote code execution flaw in FreeBSD. The findings prompted Federal Reserve Chairman Jerome Powell and Treasury Secretary Scott Bessent to convene emergency meetings with major US bank CEOs. The IMF flagged AI-powered cyber threats to global banking.

By May 12, 2026, Anthropic's EU access restrictions became a public geopolitical issue. Mythos remains restricted to approximately 12 US tech firms; EU regulators were denied preview access despite 4-5 meetings. Germany's Bundesbank publicly demanded access, warning that European banks cannot test defenses against AI-powered threats they cannot evaluate. Meanwhile, OpenAI granted EU institutions access to GPT-5.5-Cyber through its Trusted Access for Cyber program, creating a structural defensive gap. The controlled rollout via Project Glasswing (~40 companies get early access to patch) represents a new model: responsible disclosure at scale. But the 6-12 month window before adversaries replicate Mythos's capabilities means the security landscape is about to shift dramatically — organizations without AI-assisted security teams will be defending against AI-assisted attackers.

By May 23, Claude Mythos helped partner companies discover over 10,000 cybersecurity vulnerabilities in a single month, including nearly 400 high/critical risks found by Cloudflare alone. This is the first AI model to complete both of the UK AI Security Institute's full cyberattack simulation environments — yet Anthropic has no plans to release it publicly because safeguards aren't strong enough. The irony: the most capable security AI ever built is too dangerous to release. The security implications of withholding vs. releasing frontier AI models just got concrete data points.

**May 28: Claude Mythos Preview Hits 93.9% on SWE-bench**: Claude Mythos Preview achieves 93.9% on SWE-bench Verified, surpassing Claude Opus 4.8 (88.6%) and GPT-5.4 High (85.0%). On the harder SWE-bench Pro benchmark, Mythos scores 77.8% while Opus 4.7 Adaptive drops to 64.3%. This 5.3 percentage point gap between Mythos and Opus 4.8 on SWE-bench Verified represents roughly 1 in 20 solved problems — a substantial lead suggesting Mythos has a fundamentally different architecture optimized for agentic code execution rather than incremental model improvements.

## Connections
- [[sources/anthropic]] — Anthropic developed Mythos as a cybersecurity-specialized model so capable it triggered emergency government meetings; the decision to withhold rather than release reflects a judgment that frontier defensive capability carries offensive risk if broadly available
- [[topics/ai_safety]] — Central to the safety-restricted release debate
- [[ideas/safety-restricted-releases]] — Mythos established the precedent that raw capability alone can justify restriction, creating a new category of "too capable to release" models that governments now reference when drafting AI governance frameworks
- [[entities/project-glasswing]] — The consortium enabling restricted Mythos access
- [[entities/claude-opus-4-7]] — Cyber safeguards from Mythos work embedded in Opus 4.7
- [[sources/mozilla]] — Mozilla's Firefox security audit using Mythos Preview is the first major non-Glasswing production deployment, proving the model's defensive value outside the restricted consortium
- [[ideas/ai-security-auditing-mainstream]] — Mozilla's deployment marks the moment AI security auditing becomes mainstream; not using AI for security audits is becoming negligent
- [[sources/openai]] — OpenAI's GPT-5.4-Cyber lacks a comparable production deployment at a major software vendor; Mozilla's Mythos use gives Anthropic a concrete advantage in the security market, but OpenAI's EU cyber access expansion creates a geopolitical counterweight
- [[ideas/ai-mathematical-discovery]] — Both OpenAI and DeepMind achieved mathematical breakthroughs on the same day as Mythos's 10,000 vulnerability finding, showing AI capability is advancing across domains
- [[ideas/eu-cyber-access-gap]] — Anthropic's refusal to grant EU access despite Bundesbank demands and 4-5 meetings is the core structural vulnerability driving the EU gap
- [[entities/claude-opus-4-8]] — Mythos Preview scores 93.9% on SWE-bench Verified vs Opus 4.8's 88.6%, a 5.3 point gap suggesting Mythos has a fundamentally different architecture optimized for agentic code execution
- [[entities/swe-bench-verified]] — The benchmark that now shows Mythos at 93.9% near human-level performance; the same benchmark shows GPT-5.4 High at 85.0%

