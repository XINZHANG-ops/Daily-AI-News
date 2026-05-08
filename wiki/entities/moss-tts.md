---
title: "MOSS-TTS"
slug: moss-tts
type: repo
last_updated: 2026-05-07
---

# MOSS-TTS

## What It Is
MOSS-TTS is an open-source text-to-speech model family developed by OpenMOSS, supporting 20+ languages with voice cloning from just 3 seconds of audio, real-time streaming synthesis (180ms time-to-first-byte), and voice design from natural text descriptions. The family includes 8B, 1.7B, and 0.1B parameter variants, enabling deployment from edge devices to cloud infrastructure.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | OpenMOSS |
| Stars | 1,765 |
| Forks | 189 |
| Languages | 20+ |
| Voice Cloning | 3-second audio sample |
| Streaming Latency | 180ms TTFB |
| Variants | 8B, 1.7B, 0.1B parameters |

## Significance
MOSS-TTS represents the rapid commoditization of voice AI. Features that were proprietary differentiators for closed labs just months ago — real-time voice cloning, multilingual synthesis, voice design from text — are now available as open-source models with edge-deployable variants. The 0.1B parameter model enables on-device TTS without cloud dependency, addressing privacy and latency concerns that enterprise users increasingly prioritize.

The model's appearance alongside OmniVoice (600+ languages) in the same week's GitHub trends signals that open-source voice AI is outpacing closed-source differentiation. Unlike text models where frontier labs maintain benchmark leads, voice synthesis appears to be converging on "good enough" faster — the marginal utility of proprietary voice models over open alternatives is shrinking.

## Connections
- [[entities/omnivoice]] — OmniVoice's 600+ language coverage and 40x real-time inference speed represent the same open-source voice democratization trend; together they prove voice AI is becoming a commodity faster than text LLMs
- [[topics/github_trends]] — Part of the May 7 open-source voice wave alongside OmniVoice and Cordenex, showing AI tooling commoditization accelerating across modalities
- [[topics/agentic_ai]] — Real-time streaming TTS (180ms) and voice cloning enable agent-to-human voice interaction at production quality; agents can now synthesize personalized voices for notifications, calls, and alerts without cloud latency
- [[entities/gemini-3-1-flash-tts]] — Google's proprietary granular voice control TTS competes in the same space but MOSS-TTS's open-source edge deployment and 20+ language support challenge Google's licensing model
- [[ideas/voice-agent-battleground]] — MOSS-TTS and OmniVoice validate that voice is fragmenting into a distinct battleground where open-source alternatives match proprietary quality, unlike text where frontier labs still lead
- [[ideas/agent-democratization]] — Open-source voice models lower the barrier for building multimodal agents that speak naturally; the 0.1B edge variant means even Raspberry Pi-class devices can host agent voice output
