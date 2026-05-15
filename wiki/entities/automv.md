---
title: "AutoMV"
slug: automv
type: repo
last_updated: 2026-05-03
---

# AutoMV

## What It Is
AutoMV is a training-free multi-agent system that auto-generates full-length music videos from songs. It uses Screenwriter, Director, and Verifier agents with character consistency banks, lip-sync via Qwen-Wan 2.2, and beat-aligned editing at approximately $10-20 per music video.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Release Date | 2026-05-02 |
| Creator | multimodal-art-projection |
| Stars | 104 |
| Forks | 19 |
| Cost per MV | ~$10-20 |
| Architecture | Multi-agent (Screenwriter + Director + Verifier) |

## Significance
AutoMV demonstrates the maturation of multi-agent architectures for creative production. The training-free design means it composes existing models rather than requiring fine-tuning, and the Screenwriter-Director-Verifier agent division mirrors human creative workflows. At $10-20 per full music video, it represents a dramatic cost reduction from traditional production while the character consistency banks solve one of the hardest problems in AI video: maintaining visual identity across scenes.

## Connections
- [[entities/mova]] — Both tackle AI video generation; MOVA provides synchronized audio-video generation as a foundation model while AutoMV orchestrates multiple components into complete music videos
- [[entities/qwen-3-6]] — AutoMV's use of Qwen-Wan 2.2 for lip-sync reveals a supply-chain shift: Chinese open-source models are no longer just domestic alternatives but foundational components in global creative AI pipelines, integrated by international developers who value cost efficiency over brand recognition
- [[topics/agentic_ai]] — Exemplifies the multi-agent orchestration pattern where specialized agents (Writer, Director, Verifier) collaborate on complex creative tasks
- [[ideas/application-layer-shift]] — AutoMV is an application-layer composition of existing models rather than a new foundation model; the value is in the orchestration, not the raw capability
