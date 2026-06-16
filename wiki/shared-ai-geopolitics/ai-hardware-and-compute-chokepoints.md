# AI Hardware and Compute Chokepoints

> Sources: Berkeley "An Evolving AI Supply Chain," 2025; CSIS "The Coming Chip Wars," 2024; Hwang "Computational Power and the Social Impact of AI"; Stanford AI Index 2026
> Raw: `../../raw/minerals/an-evolving-ai-supply-chain-berkeley-1.md`; `../../raw/minerals/mineral-and-chip-chain.md`; `../../raw/china-ai-policy/computational-power-and-the-social-impact-of-artificial-intelligence-tim-hwang.md`; `../../raw/articles/ai-index-report-2026.md`
> Updated: 2026-06-16

## Overview

Above the mineral layer sits a second set of chokepoints in the manufactured AI hardware stack. Each is a single point of failure controlled by one firm or one geography, and they compound: a disruption at any one stalls the whole chain. This page names them so agents can reason about leverage and vulnerability in compute, not just minerals.

## The Compounding Chokepoints

- Logic fabrication: TSMC produces over 90% of the most advanced-node chips, all in Taiwan, using extreme-ultraviolet lithography supplied only by ASML in the Netherlands. This is the tightest geographic single point of failure in the entire stack.
- GPUs and software: NVIDIA holds over 90% of the data-center GPU market, locked in by the CUDA software ecosystem; AMD is around 4%.
- High-bandwidth memory: SK hynix holds over 60% of HBM, a market growing 40 to 45% per year; any HBM shortfall immediately bottlenecks GPU and ASIC output, and supply is pre-sold through 2027.
- Cloud infrastructure: U.S. hyperscalers (Amazon, Google, Microsoft) hold roughly 63% of relevant cloud capacity, making the service layer itself a control point.

Because these stack in series, the system is only as available as its scarcest link, and most links sit with U.S. or allied firms — the mirror image of China's midstream mineral dominance.

## China's Counter-Build

China bought about $38 billion of foreign chipmaking equipment in 2024 despite export controls, and the third phase of its "Big Fund" commits roughly $47 billion. It now dominates legacy chips at 28 nanometers and above, and pursues domestic GPU alternatives to NVIDIA and domestic software frameworks (Huawei MindSpore, Baidu PaddlePaddle) to break dependence on the U.S. stack. Export controls have loopholes, but leading-edge logic remains out of reach, which is why algorithmic efficiency ("software supplements hardware") has become a strategic substitute.

## Compute as Geography and Trend

Global AI compute has grown about 3.3 times per year since 2022, reaching roughly 17.1 million H100-equivalents, with NVIDIA supplying more than 60%. The United States hosts 5,427 data centers, more than ten times any other country. Compute has specific geographies, which is exactly what makes export controls, fabrication concentration, and cloud nationality usable as policy levers rather than abstract market facts.

## Relevance for Actor Knowledge Bases

For a U.S. agent, the manufactured stack is where its structural advantage concentrates, and protecting the TSMC-ASML-NVIDIA-hyperscaler chain is core strategy. For a China agent, every link is a dependency to be indigenized or routed around, and legacy-chip plus efficiency strategy is the hedge. For an EU agent, ASML is its single most powerful piece of leverage in the entire global AI economy, even as it depends on others for nearly everything else.

## See Also

- [AI Mineral Chokepoints and Export Weaponization](ai-mineral-chokepoints-and-export-weaponization.md)
- [AI Chip Control, Cloud Leverage, and U.S.-China Compute](ai-chip-control-cloud-leverage-and-us-china-compute.md)
- [Compute Sovereignty and the Openness Paradox](compute-sovereignty-and-the-openness-paradox.md)
- [AI Index 2026: State of the Race](ai-index-2026-state-of-the-race.md)
