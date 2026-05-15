---
title: "Siri"
slug: siri
type: product
last_updated: 2026-05-15
---

# Siri

## What It Is
Siri is Apple's voice assistant, originally launched in 2011, now undergoing a fundamental rebuild for iOS 27 via knowledge distillation from Google's Gemini models. The redesigned Siri represents Apple's admission that it cannot build frontier LLMs independently, pivoting from self-reliance to strategic outsourcing for its most visible AI interface.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | Apple (with Gemini distillation from Google) |
| Platform | iOS 27, macOS, watchOS, tvOS, HomePod |
| Release | iOS 27 (expected WWDC 2026 announcement) |
| Architecture | On-device Apple Foundation Models with cloud Gemini reasoning fallback |

## Significance
The Gemini-powered Siri rebuild marks a strategic inflection for Apple: rather than competing with Google and OpenAI on frontier model training, Apple is outsourcing the intelligence layer while retaining control of the interface and distribution. This mirrors Google's broader "Android of AI" strategy — Google provides the model, Apple provides the device. The competitive risk for Apple is that if the Siri experience depends on Gemini, Apple becomes a distribution channel for Google's intelligence rather than an AI platform in its own right.

## Connections
- [[sources/google]] — Google supplies the Gemini models that power Siri's reasoning layer via knowledge distillation; this transforms Google from Apple's search rival into its AI infrastructure provider
- [[topics/ai_companies]] — Apple cannot build frontier LLMs independently and is outsourcing its most visible AI interface to a competitor's model stack — a strategic concession that redefines Apple's AI posture
- [[topics/ai_companies]] — The Siri rebuild is part of the "old guard pivots to survival" pattern: Apple and Google both acknowledge they cannot afford to build frontier models from scratch, choosing partnership over self-reliance
- [[topics/llm_models]] — Siri's on-device Foundation Model plus cloud Gemini fallback represents a hybrid architecture that balances latency, privacy, and capability — a template other device makers may copy
- [[ideas/voice-agent-battleground]] — Siri's WWDC rebuild enters a crowded voice-agent market against ElevenLabs' enterprise verticals, OpenAI's GPT-Realtime-2, and Amazon's Alexa; the winner may be determined by distribution (device pre-installation) rather than raw capability
- [[entities/gemini-3-1-pro]] — The specific Gemini variant distilled for Siri's on-device operation, optimizing for latency and local execution rather than benchmark maximization
