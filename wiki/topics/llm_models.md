---
title: "LLM Models"
slug: llm_models
last_updated: 2026-04-16
---

# LLM Models

## Overview
The LLM landscape in March-April 2026 has fundamentally shifted from pure benchmark racing to capability-safety negotiations. The most significant development is Anthropic's Claude Mythos — a model so capable at discovering zero-day vulnerabilities that it has been classified as a national security concern and withheld from public release. This marks the first time a major lab has restricted a model not for misuse risk, but because the model itself poses unprecedented cybersecurity risks. Meanwhile, OpenAI's Spud model has completed pretraining with promises to "accelerate the economy," and China's Xiaomi MiMo-V2-Pro emerged as a strong competitor through a "stealth launch" strategy of anonymous testing on OpenRouter before formal reveal.

## Evolution

The period opens with NVIDIA's GTC 2026 announcement of the Vera Rubin platform, signaling the next generation of AI hardware. Within days, Xiaomi's MiMo-V2-Pro appeared anonymously on OpenRouter as "Hunter Alpha," achieving 1426 Elo on GDPval-AA benchmark before being revealed as Xiaomi's trillion-parameter model built by former DeepSeek researcher Luo Fuli.

The Claude Mythos leak on March 26 fundamentally changed the conversation. Nearly 3,000 internal documents exposed a model described internally as "the most capable we've built" with "dramatically higher" scores than Opus 4.6 on coding and cybersecurity benchmarks. The model was found capable of discovering unknown vulnerabilities in production codebases — capabilities described as "unprecedented cybersecurity risks."

OpenAI's GPT-5.4 family launched mid-March with Mini and Nano variants offering near-top-tier performance at accessible price points. The GPT-5.4 "Thinking" variant achieved 75.0% on OSWorld-Verified, a 27.7 percentage point increase over GPT-5.2, enabling native operating system-level computer use.

Google's Gemma 4 release on April 2 marked a strategic shift to Apache 2.0 licensing — fully permissive for the first time. Four variants (2B to 31B) with the 31B dense model ranking #3 on Arena AI's open leaderboard, while the 26B MoE model ranked #6, outperforming models 20x their size.

Alibaba's Qwen3.6-Plus launched April 2 with 1M-token context and agentic coding performance competitive with Claude Opus 4.5, debuting at the top of global usage charts.

Meta surprised the community with Muse Spark (April 8) — their first proprietary model, breaking with the open-source tradition since 2023. The model scores 52 on the Artificial Analysis Intelligence Index v4.0, ranking 4th, excelling at figure understanding (86.4% on CharXiv Reasoning) but struggling with abstract reasoning.

## Key Developments

| Date | Event | Significance |
|------|-------|-------------|
| 2026-03-17 | GPT-5.4 Mini/Nano release | Near-top-tier performance at accessible costs |
| 2026-03-19 | Xiaomi MiMo-V2-Pro revealed as "Hunter Alpha" | Chinese AI "stealth launch" strategy demonstrated |
| 2026-03-26 | Claude Mythos documents leaked | 3,000 internal docs exposed unprecedented cybersecurity risks |
| 2026-04-02 | Google Gemma 4 (Apache 2.0) | First fully permissive Gemma release, 31B ranks #3 on Arena |
| 2026-04-02 | Qwen3.6-Plus launches | 1M context, tops global usage charts on debut |
| 2026-04-05 | Claude Mythos 5 (10T params) confirmed | First widely recognized 10-trillion-parameter model |
| 2026-04-08 | Meta Muse Spark (proprietary) | Breaks Meta's open-source tradition, ranks 4th |
| 2026-04-10 | Claude Opus 4.6: 80.8% on SWE-bench | Near-tie with Gemini 3.1 Pro (80.6%) on production-relevant coding |
| 2026-04-14 | GPT-5.4-Cyber released | OpenAI's defensive cybersecurity model variant |
| 2026-04-16 | Stanford HAI: US-China gap effectively closed | Top models within 2.7 points on Arena benchmark |

## Patterns & Insights

The "stealth launch" pattern has emerged as a major trend — Xiaomi's MiMo-V2-Pro tested anonymously as "Hunter Alpha" on OpenRouter before formal reveal, allowing unbiased benchmark data collection before brand expectations distorted assessment. This approach is being adopted more widely.

The capability-safety tension has reached unprecedented levels. Claude Mythos represents a new category: models restricted not because humans might misuse them, but because the model itself could discover vulnerabilities that outpace defender response. This has triggered government-level concern, with VP Vance and Treasury Secretary convening emergency calls with tech CEOs.

Benchmark saturation is becoming evident. ARC-AGI-3 saw every frontier model score under 1% on tasks 100% of humans solved on first try. Traditional benchmarks are failing to keep pace with capability gains.

## Connections
- [[sources/anthropic]] — Claude Mythos developed and leaked by Anthropic; 10-trillion-parameter Mythos 5 confirmed
- [[sources/openai]] — GPT-5.4 family, Spud completion, GPT-5.4-Cyber release
- [[sources/google]] — Gemma 4 Apache 2.0 release, Gemini 3.1 Pro near-tie with Claude Opus 4.6
- [[entities/claude-mythos]] — Central to this period; too dangerous to release publicly
- [[entities/gpt-5.4]] — OpenAI's flagship model family with Thinking, Mini, Nano, Cyber variants
- [[entities/gemma-4]] — Google's first fully permissive open model, ranked #3 on Arena
- [[ideas/safety-restricted-releases]] — Claude Mythos established the precedent for capability-based release restrictions
