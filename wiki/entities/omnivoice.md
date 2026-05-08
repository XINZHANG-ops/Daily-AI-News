---
title: "OmniVoice"
slug: omnivoice
type: repo
last_updated: 2026-05-07
---

# OmniVoice

## What It Is
OmniVoice is an open-source multilingual voice synthesis model from k2-fsa supporting 600+ languages using a diffusion language model architecture. It features voice cloning, voice design via speaker attributes (gender, age, pitch, accent), and ultra-fast inference with real-time factor as low as 0.025 — 40x faster than real-time speech generation.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | k2-fsa |
| Stars | 4,359 |
| Forks | 412 |
| Languages | 600+ |
| Architecture | Diffusion language model |
| Voice Design | Gender, age, pitch, accent controls |
| Inference Speed | RTF 0.025 (40x faster than real-time) |

## Significance
OmniVoice's 600+ language coverage dwarfs proprietary offerings from Google, OpenAI, and Anthropic, which typically support 50-100 languages. The diffusion language model architecture is a departure from the autoregressive or flow-matching approaches used by most commercial TTS systems, potentially offering better sample quality at the cost of inference speed — though the 0.025 RTF figure suggests the diffusion approach has been optimized for real-time use.

The model's appearance in the same week as MOSS-TTS and Cordenex reinforces a pattern: open-source AI is commoditizing capabilities faster than closed labs can monetize them. Voice synthesis, multi-agent coding, and semantic code infrastructure all trending simultaneously suggests the open-source ecosystem is hitting a critical mass where new modalities are being replicated and open-sourced within weeks of proprietary launch.

## Connections
- [[entities/moss-tts]] — MOSS-TTS (20+ languages, 180ms streaming) and OmniVoice (600+ languages, 40x real-time) together prove open-source voice AI is now competitive on both breadth and speed; the proprietary voice moat is evaporating
- [[topics/github_trends]] — Part of the May 7 open-source wave demonstrating AI capabilities democratizing faster than closed labs can differentiate
- [[entities/gemini-3-1-flash-tts]] — Google's proprietary TTS with granular voice control is positioned against open alternatives like OmniVoice; the 600+ language coverage makes OmniVoice more globally accessible than Google's offering
- [[ideas/voice-agent-battleground]] — OmniVoice's 600+ language support means voice agents can now operate in linguistic markets that frontier labs ignore; this could shift voice agent adoption to developing markets first
- [[ideas/commodity-inference-fragmentation]] — OmniVoice's diffusion architecture achieving 40x real-time inference at open-source pricing validates the commodity tier: "good enough" voice synthesis is now free infrastructure, not a premium product
- [[topics/agentic_ai]] — 600+ language voice output enables agentic AI to serve global populations that English-centric proprietary models cannot reach; the voice agent battleground is becoming multilingual by default
