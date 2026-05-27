---
title: "Gemini 3.5 Flash"
slug: gemini-3-5-flash
type: model
last_updated: 2026-05-26
---

# Gemini 3.5 Flash

## What It Is
Google's frontier-level model at half the price, approximately 4× faster than other frontier models. Released at Google I/O 2026 as the API-centric answer to Anthropic's Claude Sonnet and OpenAI's GPT-5.4 in the mid-tier model market. Now the default model for Google Search's AI Mode. On May 22, 2026, the API went General Availability with specific pricing and 1M token context window.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Release Date | 2026-05-19 (I/O), GA 2026-05-22 |
| Creator | Google |
| Type | Frontier-level API model |
| Input Price | $1.50/M tokens |
| Output Price | $9.00/M tokens |
| Context Window | 1M tokens |
| Terminal-Bench 2.1 Score | 76.2% |
| Speed | ~4× faster than other frontier models |
| Default For | Google Search AI Mode |

## Significance
Gemini 3.5 Flash represents Google's pivot from consumer search to API-centric revenue. The "half price" positioning signals a price war in the mid-tier model market. With "AI Mode" as the distribution channel, every Google Search user (billions of queries/day) becomes a potential Flash user — creating massive scale effects: more queries = more RL signal = faster iteration. This could make Flash the most deployed model in history by Q3 2026.

The GA release on May 22, 2026 adds concrete pricing ($1.50/M input, $9.00/M output) and Terminal-Bench 2.1 score of 76.2%. This is significant because Flash beat Gemini 3.1 Pro — the first time a Flash model outperformed its Pro sibling. At 76.2%, Flash undercuts Claude Haiku ($1.25/M input, $5/M output) while delivering 5-8x context window and superior coding performance. This challenges Anthropic's model hierarchy: if Flash beats Pro, what's Sonnet's moat? Google's aggressive positioning suggests they're optimizing for developer adoption over margin.

## Connections
- [[sources/google]] — Gemini 3.5 Flash is Google's answer to API market commoditization; the half-price strategy leverages Google's infrastructure advantage; GA release on May 22, 2026 with specific pricing confirms the commitment to API revenue
- [[entities/gemini-spark]] — Both released at Google I/O 2026; Flash is the API product, Spark is the consumer agent product
- [[entities/gemini-omni]] — Flash and Omni are part of Google's I/O 2026 trio — Flash for API, Spark for consumer, Omni for world model
- [[topics/llm_models]] — Gemini 3.5 Flash intensifies the mid-tier model price war; Google's infrastructure allows frontier performance at commodity pricing; 76.2% on Terminal-Bench 2.1 proves Flash isn't just cheap — it's genuinely competitive
- [[sources/anthropic]] — Competes directly with Claude Sonnet and Haiku; Google's $180-190B capex enables aggressive pricing that pressures Anthropic's margins; the 76.2% Terminal-Bench 2.1 score challenges Claude's coding superiority
- [[entities/google-adk-python]] — Both released at Google I/O 2026; Flash provides the model, ADK provides the framework — Google completing the model → framework → deployment stack
- [[entities/terminal-bench-2]] — Scored 76.2% on Terminal-Bench 2.1 (May 22, 2026), the first Flash model to outperform its Pro sibling — a significant milestone in Google's pricing-over-margin strategy