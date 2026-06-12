---
title: "NEO-unify"
slug: neo-unify
type: framework
last_updated: 2026-06-11
---

# NEO-unify

## What It Is
NEO-unify (Native Unified Paradigm) is an architectural framework for multimodal AI that eliminates the separation between encoders (e.g., vision encoders) and the core model. Instead of translating images into tokens for an LLM, NEO-unify processes multiple modalities within a single, unified neural structure.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Concept | Native Unified Paradigm |
| Primary Goal | Eliminating modality-specific bottlenecks |
| Key Implementation | SenseNova-U1 |

## Significance
NEO-unify represents a departure from the "CLIP-style" encoder-decoder architecture. By treating multimodal data as a single stream of information, it allows for more fluid transitions between understanding and generating across different senses, which is critical for the next generation of embodied and creative AI.

## Connections
- [[entities/sensenova-u1]] — The primary model implementation demonstrating the power of the NEO-unify paradigm.
- [[topics/llm_models]] — A fundamental shift in how multimodal models are designed, moving from modular to unified architectures.
