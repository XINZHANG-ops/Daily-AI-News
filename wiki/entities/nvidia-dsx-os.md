---
title: "NVIDIA DSX OS"
slug: nvidia-dsx-os
type: product
last_updated: 2026-06-10
---

# NVIDIA DSX OS

## What It Is
NVIDIA DSX OS is the open-source AI factory software stack that runs DGX Cloud, open-sourced by NVIDIA on June 9, 2026. The stack bundles six production components: NVSentinel (Kubernetes-based GPU fault detection), DSX MaxLPS (dynamic power management), KAI Scheduler + Run:ai (GPU-aware placement with fractional GPU support), Dynamo + Grove (disaggregated prefill/decode inference), and NICo/NVCF (inference API lifecycle). NVIDIA claims the integrated stack delivers 40% more GPUs per megawatt at the rack level versus running the components separately. CoreWeave, Lambda, Crusoe, IREN, and Vultr are the launch cloud partners.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Release Date | 2026-06-09 |
| Creator | NVIDIA |
| License | Open source |
| Components | NVSentinel, DSX MaxLPS, KAI Scheduler + Run:ai, Dynamo + Grove, NICo/NVCF |
| Performance Claim | 40% more GPUs per megawatt (rack-level) |
| Launch Cloud Partners | CoreWeave, Lambda, Crusoe, IREN, Vultr |
| Replaces | Closed-source DGX Cloud stack |

## Significance
DSX OS is NVIDIA's strategic response to the simultaneous erosion of its moat on three fronts: hardware (FuriosaAI, Alibaba M890, custom inference silicon), commodity inference runtimes (TileRT, Mellum2), and the software moat it previously locked behind DGX Cloud. By open-sourcing the production stack that runs its highest-margin managed offering, NVIDIA is making a calculated bet: if every cloud runs DSX OS, NVIDIA still controls the GPU underneath — and the integrated stack creates stronger CUDA dependency than the GPU alone ever did.

The 40% more-GPUs-per-megawatt claim is the headline. Megawatt economics are the new battleground for AI infrastructure: data center power, not GPU count, is the binding constraint. If DSX OS delivers a 40% rack-level power efficiency improvement at scale, it functionally adds ~40% to the addressable GPU inventory of every DSX-OS-running cloud — a bigger boost than any new GPU generation on NVIDIA's 2026 roadmap.

The launch partner list (CoreWeave, Lambda, Crusoe, IREN, Vultr) is the second strategic signal: every partner is a specialized AI cloud that competes directly with hyperscalers. By giving them the same software stack as DGX Cloud, NVIDIA is arming the insurgent clouds against AWS/Azure/GCP — which forces the hyperscalers to either adopt DSX OS (deepening NVIDIA's lock) or build competing stacks (which slows them down). Either outcome strengthens NVIDIA.

## Connections
- [[sources/nvidia]] — Released by NVIDIA June 9, 2026 as the open-source twin of the previously closed DGX Cloud stack; the bet is that the software stack creates stronger CUDA dependency than the GPU alone
- [[ideas/nvidia-competitive-moat-eroding]] — DSX OS is NVIDIA's direct response to the chip-moat erosion; by making the production stack open, NVIDIA concedes the chip is becoming commoditized and competes on the software integration
- [[entities/tilert]] — TileRT and DSX OS represent two different software strategies: TileRT proves frontier serving is a runtime problem on commodity hardware, DSX OS proves the integrated production stack is itself a moat even with open-sourced components
- [[topics/ai_infrastructure]] — DSX OS is the first open-source production AI factory stack from a major chip vendor; reframes "AI infrastructure" from "GPU count" to "GPUs per megawatt" — the binding constraint has shifted from chips to power
- [[entities/nvidia-dsx-os]] — DGX Cloud's predecessor container registry; DSX OS represents NVIDIA's pivot from container distribution to integrated production stack
- [[entities/nvidia-dsx-os]] — Launch cloud partner; access to NVIDIA's highest-margin managed offering's underlying stack removes CoreWeave's dependency on DGX Cloud and makes CoreWeave directly competitive with AWS for AI workloads
- [[entities/nvidia-dsx-os]] — Part of DSX OS; disaggregated prefill/decode inference is the architectural bet that long-context agent workloads need split inference stages
- [[entities/nvidia-dsx-os]] — Acquired by NVIDIA; now part of DSX OS as KAI Scheduler; GPU-aware placement with fractional GPU support is the runtime primitive that makes 40% more-GPUs-per-megawatt claim achievable
- [[ideas/open-platform-ai]] — DSX OS is the chip-vendor version of the open-platform thesis: by open-sourcing the production stack, NVIDIA converts a competitive threat (commodity inference runtimes) into a defensive moat (every cloud depends on the same stack)
- [[entities/nvidia-dsx-os]] — Launch cloud partner; DSX OS deployment is Lambda's counter to hyperscaler vertical integration
- [[entities/nvidia-dsx-os]] — (Note: actual source likely "irene" or similar) — Launch cloud partner; IREN's renewable-powered AI cloud becomes more capital-efficient with DSX OS power optimization
