---
title: "GemTTS"
slug: gemtts
type: product
last_updated: 2026-05-14
---

# GemTTS

## What It Is
GemTTS is an agent-friendly Gemini text-to-speech CLI written in Rust. It supports expressive tags like [whispers], [laughs], [warmly], multi-speaker dialogue, and 30 prebuilt voice timbres. Designed specifically for AI agents, it features JSON output support and self-documenting capabilities.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Repo | paperfoot/gemtts |
| Stars | 28 |
| Forks | 3 |
| Language | Rust |
| Creator | paperfoot |
| Key Features | Expressive tags, multi-speaker, 30 timbres, JSON output |

## Significance
GemTTS represents the emerging category of "agent-native" tools — software designed from the ground up for AI agents rather than adapted from human-facing interfaces. The expressive tag system ([whispers], [laughs]) treats voice generation as a programmable API with emotional parameters rather than a static output. The Rust implementation and JSON output signal that the tool is built for integration into agent pipelines where reliability and structured data matter more than graphical interfaces. At only 28 stars, it is early-stage but indicative of the tooling layer emerging around agentic voice interactions.

## Connections
- [[entities/gemini-3-1-flash-tts]] — Google's official Gemini TTS offering; GemTTS is an open-source, agent-specific alternative built on the same model family
- [[topics/github_trends]] — GemTTS's May 14 launch alongside Scenema Audio and Atomr Infer signals that agent-native audio tooling has become a recognized open-source category, not just a feature bolted onto larger frameworks
- [[sources/google]] — GemTTS is designed specifically for Gemini ecosystem integration, reflecting Google's system-layer strategy: rather than competing on raw TTS quality alone, it bundles audio generation into the broader Gemini Intelligence stack that spans vision, reasoning, and voice
- [[ideas/voice-agent-battleground]] — Voice AI is fragmenting into specialized tools; GemTTS targets the agent-orchestration niche while ElevenLabs targets enterprise scale
- [[entities/moss-tts]] — Open-source TTS with 20+ languages; GemTTS differentiates through agent-specific features (JSON output, expressive tags) rather than language coverage
