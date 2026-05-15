---
title: "Scenema Audio"
slug: scenema-audio
type: product
last_updated: 2026-05-14
---

# Scenema Audio

## What It Is
Scenema Audio is a zero-shot expressive voice cloning and speech generation system. It can generate anything from short clips to full-length audiobooks with realistic emotional delivery, pacing, and breath control. It is built on an audio diffusion transformer extracted from LTX 2.3's 22 billion parameter audiovisual model.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Repo | ScenemaAI/scenema-audio |
| Stars | 6 |
| Forks | 1 |
| Base Model | LTX 2.3 (22B parameter audiovisual model) |
| Key Feature | Zero-shot expressive voice cloning |

## Significance
Scenema Audio demonstrates a trend in open-source audio AI: extracting specialized subsystems from large multimodal models and releasing them as standalone tools. By pulling the audio diffusion transformer out of LTX 2.3's 22B audiovisual model, the creators are making a bet that audio-specific tooling is more valuable than the full multimodal stack for voice practitioners. The "zero-shot" capability — generating expressive speech without speaker-specific training — is the key differentiator that could make audiobook production, podcasting, and voice agent development accessible without proprietary APIs.

## Connections
- [[topics/github_trends]] — Scenema Audio's May 14 launch alongside GemTTS and Atomr Infer establishes agent-native audio as a distinct open-source category, separate from both general music-generation tools and enterprise voice APIs — a niche created by the specific needs of multimodal agents that generate and manipulate sound autonomously
- [[entities/moss-tts]] — Both offer open-source voice synthesis; Scenema Audio differentiates through zero-shot expressive cloning from a 22B base model
- [[entities/omnivoice]] — OmniVoice covers 600+ languages at 40x real-time; Scenema Audio trades breadth for depth of emotional expression
- [[ideas/voice-agent-battleground]] — Open-source voice tools are fragmenting by use case: language coverage (OmniVoice), enterprise features (ElevenLabs), agent integration (GemTTS), and expressive cloning (Scenema Audio)
- [[topics/llm_models]] — Extracting audio transformers from 22B multimodal models suggests the open-source ecosystem is learning to "mine" capabilities from large foundation models, a pattern that could accelerate democratization
