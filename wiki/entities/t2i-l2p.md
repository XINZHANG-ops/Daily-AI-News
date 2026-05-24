---
title: "L2P (Latent to Pixel)"
slug: t2i-l2p
type: method
last_updated: 2026-05-23
---

# L2P (Latent to Pixel)

## What It Is
L2P (Latent to Pixel) is Tencent's method for transferring latent diffusion models into pixel-space generation, removing the VAE bottleneck while maintaining low training costs. The accompanying T2I-L2P GitHub repository gained 80 stars in its first 24 hours.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | Tencent |
| Release Date | May 23, 2026 |
| Key Innovation | Eliminates VAE encoder/decoder as bottleneck |
| Result | High-resolution output without quality loss of traditional pixel diffusion or computational cost of pure latent models |
| Early Traction | 80 stars in 24 hours on GitHub |

## Significance
 L2P addresses a fundamental limitation in image generation: the VAE bottleneck. Latent diffusion models use a VAE to compress images to latent space, but the encoder/decoder becomes a quality bottleneck. Tencent's approach bypasses this by transferring to pixel-space directly, achieving high-resolution output without the trade-offs of either approach. The rapid star count shows the community's appetite for practical image generation improvements.

## Connections
- [[sources/tencent]] — Tencent's research breakthrough in image generation; the company is innovating in practical AI tools
- [[topics/github_trends]] — 80 stars in 24 hours shows community enthusiasm for practical image generation improvements
- [[topics/llm_models]] — The innovation connects to broader trends in making AI generation more accessible and practical
- [[entities/claude-code]] — AI coding agents can now work with more sophisticated image generation pipelines