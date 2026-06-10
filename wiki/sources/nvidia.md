---
title: "NVIDIA"
slug: nvidia
last_updated: 2026-06-10
---

# NVIDIA

## Overview
NVIDIA remains the indispensable infrastructure provider for AI, with Blackwell generating $11 billion in Q4 FY2026 revenue and Vera Rubin announcing 10x performance per watt over Blackwell. On May 1, GB300 Blackwell Ultra enters mass production at TSMC's N3P node with 288GB HBM3e, 10 TB/s bandwidth, and NVLink 6 — delivering 35x lower cost-per-token and 50x better throughput per megawatt for agentic AI workloads. The company shipped 1.56 petaflops FP4 compute with Huawei's Atlas 350 accelerator claiming 2.8x better performance than NVIDIA's H20 chip — the first credible domestic AI chip competition in China.

## Timeline

| Date | Event | Details |
|------|-------|---------|
| 2026-03-17 | GTC 2026: Vera Rubin announced | 10x performance per watt over Blackwell |
| 2026-03-17 | GTC: NemoClaw stack released | Open-source for OpenClaw agents |
| 2026-03-17 | GTC: Disney Olaf robot unveiled | Physical AI showcase |
| 2026-03-17 | GTC: Open-H, Cosmos-H, GR00T-H | Healthcare robotics datasets |
| 2026-03-17 | GTC: AWS 1M+ GPUs commitment | Blackwell, Rubin, Groq 3 LPUs |
| 2026-03-25 | Blackwell $11B Q4 revenue | Mass production underway |
| 2026-03-25 | Huawei Atlas 350 claims 2.8x H20 | First credible Chinese AI chip competition |
| 2026-04-01 | DeepSeek outage speculation | Service down 7+ hours; upgrade speculation |
| 2026-04-06 | GTC 2026: AI security focus | CrowdStrike: secure AI at architecture stage |
| 2026-04-16 | Five hyperscalers control 66% AI compute | NVIDIA GPUs still 60%+ of total |
| 2026-04-14 | NVIDIA launches Ising | World's first open quantum AI model family |
| 2026-04-18 | Ising delivers 2.5x faster quantum error correction | 3x more accurate than traditional approaches |
| 2026-04-22 | Vast Data raises $1B at $30B valuation | NVIDIA-backed AI infrastructure startup |
| 2026-05-01 | GB300 Blackwell Ultra enters mass production | Ships to Microsoft Azure, Google Cloud, Meta in May; 288GB HBM3e, 10 TB/s, 35x lower cost/token for agentic AI |
| 2026-05-01 | Pentagon includes Nvidia in 8-company classified AI coalition | Nemotron models deployed on classified networks; Nvidia also participates in Ineffable Intelligence $1.1B seed (hedging across LLM/RL paradigms) |
| 2026-05-05 | CEO says China should not get latest chips | Calibrated diplomacy: restrict frontier chips while selling older inventory; underlying reality is 90% Asian supply chain, need Chinese revenue to amortize R&D |
| 2026-05-05 | Huawei targets $12B AI chip sales (60%+ growth) | Chinese domestic AI chips becoming viable alternatives; DeepSeek V4 Huawei-chip-adapted variant proves Chinese labs can train frontier models on domestic silicon |
| 2026-05-05 | NVIDIA China market share below 60% | 2M H200 orders (~$54B potential) reportedly not yet approved by Beijing; deliberate protection of domestic players like Huawei and 寒武纪 |
| 2026-05-05 | Blackwell architecture: thermal efficiency vs geopolitics | Blackwell achieves 3.5 GHz clock speeds, 1.8 TB/s memory bandwidth but requires advanced cooling; excluded from China while NVIDIA continues supplying other markets; $1T Blackwell/Rubin demand through 2027 |
| 2026-05-21 | Nvidia faces competition from Alibaba M890, FuriosaAI | Alibaba's new M890 AI chip and Korean FuriosaAI challenge Nvidia's 80%+ AI chip market share; Singapore partnership for embodied AI research hub is Nvidia's hedge |
| 2026-05-29 | Gamma-World released | NVIDIA's generative multi-agent world model generating coherent future frames from multiple agents; features Simplex Rotary Agent Encoding and Sparse Hub Attention for efficient simulation; 187 GitHub stars |


| 2026-05-31 | Cosmos 3 released | First fully open omnimodel for physical AI; native vision reasoning and multimodal generation; Super (32B) and Nano (8B) variants; Nano optimized for edge robot deployment |
| 2026-05-31 | Agent Toolkit launched | NemoClaw blueprints and OpenShell runtime; positions NVIDIA as infrastructure layer for physical AI agents |
| 2026-06-04 | Nemotron 3 Ultra unveiled | 550B MoE (55B active) hybrid Mamba-Transformer with NVFP4 4-bit quantization; 5x throughput on Blackwell tensor cores; license shifts from restrictive to OpenMDW-1.1 — weaponizing openness as CUDA moat; companion Content Safety (4B) and ASR (40+ langs) |
| 2026-06-09 | DSX OS open-sourced | Bundles NVSentinel, DSX MaxLPS, KAI Scheduler + Run:ai, Dynamo + Grove, NICo/NVCF; 40% more GPUs per megawatt at rack level; launch partners CoreWeave, Lambda, Crusoe, IREN, Vultr; open-sources the production stack that previously ran DGX Cloud as a closed managed offering |
## Key Relationships
- **OpenAI**: Strategic investor and primary GPU customer.
- **Anthropic**: GPU supplier and Project Glasswing coalition member.
- **Microsoft**: Deep Azure integration and GPU deployment.
- **AMD**: Competition in AI chip market.
- **Vast Data**: Backed $1B funding round, AI storage infrastructure.

## Connections
- [[entities/vera-rubin]] — Next-gen platform, 10x perf/watt
- [[entities/ising]] — World's first open quantum AI model family
- [[entities/gb300]] — GB300 Blackwell Ultra, mass production May 2026; 35x lower cost/token for agentic AI
- [[entities/nemotron-3-ultra]] — June 4: 550B MoE with NVFP4 4-bit quantization; the model-as-CUDA-distribution play; OpenMDW-1.1 license weaponizes openness as chip moat
- [[entities/blackwell-architecture]] — Current-generation architecture with 3.5 GHz clocks, 1.8 TB/s bandwidth; thermal challenges but massive demand; China exclusion creates bifurcated market
- [[sources/vast-data]] — NVIDIA-backed storage startup, $1B raise
- [[sources/openai]] — $30B investment commitment
- [[sources/anthropic]] — GPU supplier and infrastructure partner
- [[ideas/us-china-ai-fragmentation]] — NVIDIA's China dilemma accelerates hardware decoupling; Huawei's $12B target and DeepSeek V4 Huawei variant prove domestic silicon can train frontier models
- [[ideas/institutional-gap]] — TSMC 3nm yield crisis (52%) and China decoupling simultaneously pressure NVIDIA's cost structure from supply and demand sides
- [[entities/cosmos-3]] — June 8: Cosmos 3 (launched May 31) is the most strategically important NVIDIA release of 2026 — locks the "physical AI" category to CUDA at the same moment robotics foundation models are about to commoditize; OpenMDW 1.1 license is deliberately not OSI-approved so NVIDIA can forbid non-CUDA deployers from commercial use
- [[entities/nvidia-dsx-os]] — June 9: open-sourcing the DGX Cloud production stack is NVIDIA's strategic response to chip-moat erosion; 40% more GPUs per megawatt is the new headline (data center power, not GPU count, is the binding constraint); the launch partner list (CoreWeave, Lambda, Crusoe, IREN, Vultr) arms specialized AI clouds against the hyperscalers
- [[entities/nvidia-dsx-os]] — Part of DSX OS; disaggregated prefill/decode inference is the architectural bet that long-context agent workloads need split inference stages
- [[entities/nvidia-dsx-os]] — Acquired by NVIDIA; now part of DSX OS as KAI Scheduler; GPU-aware fractional placement is the runtime primitive that makes the 40% more-GPUs-per-megawatt claim achievable
- [[ideas/nvidia-competitive-moat-eroding]] — DSX OS is NVIDIA's direct response: concede the chip is becoming commoditized, compete on the integrated production stack
- [[ideas/open-platform-ai]] — DSX OS is the chip-vendor version of the open-platform thesis: by open-sourcing the production stack, NVIDIA converts a competitive threat (commodity inference runtimes like TileRT) into a defensive moat (every cloud depends on the same stack)
- [[entities/nvidia-dsx-os]] — Launch cloud partner; access to DGX Cloud's underlying stack removes CoreWeave's dependency on hyperscalers for the highest-margin NVIDIA offering
- [[entities/nemotron-3-ultra]] — June 8: layered with Cosmos 3, NVIDIA has now locked two new categories (frontier hybrid-reasoning, physical AI) to CUDA in a single week; the playbook (open weights + non-OSI license + coalition) is the same for both
- [[topics/physical_ai]] — June 8: Cosmos Coalition with six robotics startups (Agile Robots, Black Forest Labs, Generalist, LTX, Runway, Skild AI) is the lock-in play — Cosmos 3 weights are open, but the only training/inference stack that gets full speed is NVIDIA's
- [[ideas/agent-infrastructure-layer]] — June 8: NVIDIA's two-category CUDA lock-in (Nemotron 3 Ultra + Cosmos 3) is the strategic capstone to the May 2026 "infrastructure layer" pattern; physical AI was the missing piece
- [[sources/anthropic]] — June 8: Anthropic's 90% internal Claude adoption depends on NVIDIA hardware scaling; Mythos Preview's 16+ hour task duration requires the throughput only Blackwell-class silicon can deliver
- [[timelines/2026-06]] — June 8: NVIDIA's category-locking week (Nemotron 3 Ultra + Cosmos 3) is the most consequential infrastructure move of 2026; both releases use the same OpenMDW 1.1 license, suggesting a deliberate strategic pattern
