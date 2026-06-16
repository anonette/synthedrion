# An Evolving AI Supply Chain

> Extracted from: `An_Evolving_AI_Supply_Chain_-_Berkeley-1.pdf`

An Evolving AI Supply Chain

NIKHIL RAGAV MULANI

2024-2025 TECH POLICY FELLOW

an evolving ai supply chain
2
Contents
1
Executive Summary
3
2
Data: Scarcity and Cost
6
2.1
Data Value and Availability
6
2.2
Data Licensing
7
2.3
Tacit Knowledge
8
3
Compute: Optionality and Control
9
3.1
Compute Services Market
9
3.2
Cloud Sovereignty
10
4
Hardware: Specialization and Geopolitics
12
4.1
Hardware Market
12
4.2
Geopolitical Controls
14
5
Critical Minerals: Concentration and Negotiation
16
5.1
Supply Constraints
16
5.2
Key Countries
18
6
Capital: Ownership and Interdependency
20
6.1
Venture & Growth
20
6.2
Corporate
21
6.3
Sovereign
23
7
Conclusion
24

an evolving ai supply chain
3
1
Executive Summary
This paper identiﬁes key areas of change and uncertainty across
the frontier AI model development supply chain and describes how
disparate supply chain segments are interconnected. The scope of
the paper includes capital investments, critical minerals, datasets,
compute services, and hardware.
While reading, watch the margin
for callouts of relationships between
different supply chain segments. See
below for an example of how this will
appear:
Capital →Model Developers
The market dynamics of 2025 underscore the scale and pace of
change across the supply chain. A massive capacity build-out is
underway. Investors, including venture and growth funds, sovereign
wealth funds, and the leading model developers themselves, are
pouring tens of billions into compute infrastructure, with signiﬁcant
data center investments announced across the world.1,2 Meanwhile,
the United States continues to calibrate its trade strategy, oscillating
between expanding restrictions on advanced chip trade with China in
late 2024 and granting speciﬁc export licenses for advanced NVIDIA
and AMD GPUs in mid-2025.3
Over the next decade, the AI supply chain will likely become more
multi-polar as nations and companies invest in creating alternative
options for compute and hardware for frontier-scale AI development.
The growing use of AI to support model and hardware development
will also lead the supply chain in new and unexpected directions.
Geopolitical jockeying will intensify due to the perceived economic
and national security stakes of owning access to and jurisdiction over
parts of the AI supply chain.
Data: Scarcity and Cost
• Increasing data scarcity, the rise of synthetic and multi-modal data,
and complex licensing agreements are increasing the cost barrier
to ﬁnding and using high-quality data
• Over-reliance on synthetic data could pose signiﬁcant challenges.
The market for specialized data curation and processing compa-
nies is growing rapidly
Compute: Optionality and Control
• Computational power is concentrated among three major cloud
providers, while there is explosive growth in demand for compute
resources
• As a result, a market in specialized AI clouds ("neoclouds") is
growing, countries are pursuing publicly-funded "cloud sovereignty,"
and decentralized compute is growing as an area of research

an evolving ai supply chain
4
Hardware: Specialization and Geopolitics
• Advanced chips, high-bandwidth memory, and network intercon-
nects are critical inputs into AI development
• NVIDIA maintains a dominant market position supported by
its CUDA platform. Meanwhile, custom ASICs are attracting
increasing investment and usage from frontier model developers
• The U.S. has attempted to restrict China’s access to cutting-edge
hardware, but China has made signiﬁcant progress in their domes-
tic hardware ecosystem despite these restrictions
Critical Minerals: Concentration and Negotiation
• Various critical minerals are necessary for manufacturing hard-
ware, building data centers, and supplying power to data centers.
Production and processing of these minerals is highly concen-
trated, particularly in China
• Throughout 2025, the U.S. government has been attempting to
reduce exposure to dependence on China through investments
to support domestic minerals companies, as well as engagements
with countries including Ukraine and Australia
Capital: Ownership and Interdependency
• Immense capital investment is ﬂowing into the AI supply chain,
driven by venture and growth ﬁrms, hyperscalers, and sovereign
wealth funds
• Strategic partnerships and blended ﬁnancing agreements are
creating deeply intertwined alliances between hardware providers,
model developers, and governments
This paper does not aim to be comprehensive. The AI supply
chain is vast, and each segment within it comprises its own supply
chain. If one attempted to do a complete mapping, they would
encounter overwhelming fractal complexity.

an evolving ai supply chain
5
Figure 1: Supply Chain for Frontier
AI Model Development

an evolving ai supply chain
6
2
Data: Scarcity and Cost
This segment covers the data and data preparation that feed into
model training, ﬁne-tuning, testing, and evaluation.
Datasets can range from trillions of tokens of text scraped from the
open web, to curated image libraries, to proprietary domain-speciﬁc
data (e.g., private bio-data, medical records, code repositories), as
well as human-generated annotations that label or rate content for
supervised learning and reinforcement learning from human feed-
back (RLHF). There is little evidence for exactly how data scaling will
unfold beyond current limits. The future could include increasingly
autonomous "self-training" paradigms (involving model interaction
with or observation of subject-matter experts and/or workplaces).
Model Developers ↑Data
Risks of current trajectories include inaccessibility of certain data criti-
cal for high-value applications due to cost of licensing, as well as data
contamination feedback loops (public AI-generated content and/or
private synthetic data polluting training datasets) that could degrade
data quality and model performance over time. Model developers
are aware of the potential constraints and are seeking to collect and
leverage their own proprietary datasets or license access to ongoing
supplies of high-quality data.
2.1
Data Value and Availability
As frontier models scale, they are fed increasingly large amounts of
data. Language model training datasets have grown 3.7-3.8x annually
from 2010 through 2024.4 This growth is driving increased invest-
ment in a set of activities focused on data sourcing, data generation,
and licensing. High-quality data has been described as a "fossil fuel"
for frontier model development, in that it is a limited resource that
could be exhausted soon.5 Researchers project that the stock of high-
quality public text data could be exhausted for training purposes
between 2026 and 2032.6 This imposes a notable constraint on devel-
opers’ abilities to keep improving model performance, as systematic
studies have found that "data quality" can be highly indicative of
model performance.7,8
Although large-scale internet data will eventually be exhausted,
proprietary data can continue to add marginal but potentially sig-
niﬁcant value for pre-training, ﬁne-tuning, and evaluation as AI
capabilities evolve. This means much remains unknown about the
total volume and exhaustibility of these datasets. Examples of these
datasets include those related to high-value economic and scientiﬁc
tasks (e.g., legal reasoning and document preparation, experimenta-

an evolving ai supply chain
7
tion in specialized domains), as well as sensitive security tasks (e.g.,
cybersecurity vulnerability identiﬁcation). Much of this data might
not even be digitized yet (e.g., educational and healthcare records).
Multi-Modal Data
Expanding data sourcing across modalities (e.g., video, image,
and audio in addition to text) can help alleviate data scarcity. How-
ever, multimodal training is much more expensive than text-only
training, due to its increased computational demands.9 Additionally,
Data →Compute
extensive costs are associated with licensing high-quality data and
successfully pairing and annotating multimodal sources.
Synthetic Data
Leading model developers, including OpenAI, Google DeepMind,
and Meta, use synthetic data in their post-training and reﬁnement
pipelines.10 Some believe that synthetic data generation and self-
Model Developers ↑Data
teaching could help to overcome most limitations imposed by a lack
of access to data. However, in early research, too much reliance on
synthetic data has been shown to cause noticeable degradation in
model performance.11
2.2
Data Licensing
Given the constraints of public data volume and synthetic data
quality, model developers who can secure ongoing access to large,
high-quality, and proprietary datasets will have an advantage. Ope-
nAI, lacking a large user-generated content ecosystem comparable
to Google, X, or Meta, has pursued a strategy of securing multi-year
licensing partnerships with major publishers. Notable agreements
include a multi-year deal with News Corp, potentially worth up
to $250 million over ﬁve years, as well as partnerships with Axel
Springer, The Atlantic, Vox Media, the Financial Times, and The As-
sociated Press.12 Annual licensing fees for text archives often fall in
the $1 million to $5 million range, and rates for video content reach
up to $4 per minute for premium formats.13 Amazon, Perplexity, and
Microsoft have also been particularly proactive in securing licensing
for archives of leading media outlets.14
Leading AI Data Companies
As the demand for high-quality and specialized data increases, a
growing number of companies are speciﬁcally offering services to
model developers in areas such as data collection, annotation, and
curation, as well as adjacent services including model evaluation,
reinforcement learning from human feedback, red-teaming, and
content moderation. These companies include Scale AI, Surge AI,
Appen, and iMerit.15

an evolving ai supply chain
8
2.3
Tacit Knowledge
This segment of data curation and preparation companies is likely
to grow over time, especially as some particularly valuable types of
data do not yet exist in a readily accessible form. For example, much
important information about how to reason about a novel scientiﬁc
question,16 conduct a military operation,17 take a "wise" approach
to a legal or judicial decision,18 or leverage emotion and cultural
resonance to ﬁnd a compromise in a high-stakes negotiation19 exists
as some combination of tacit knowledge, social capital, and wisdom
that only experienced and seasoned professionals such as a tenured
researcher, military general, judge, or seasoned arbitration lawyer
could possess or intuit. The ability to convey the "hard-to-distill"
aspects of human relationships and decision-making to an AI system
will become increasingly valuable as models become more adept in
their general-purpose capabilities.

an evolving ai supply chain
9
3
Compute: Optionality and Control
This section covers cloud services and high-performance computing
platforms necessary for frontier-scale training and inference.
Large amounts of computational power ("compute") supplied
by data centers are essential for training and deploying frontier
AI models. Over half of the supply of such compute is currently
concentrated in the hands of three American companies: Amazon,
Microsoft, and Google.20 Each company is spending unprecedented
amounts of capital in order to continue building out data centers.21
Capital ↑Compute
In tandem, the amount of compute required to train frontier-scale AI
models has doubled approximately every six months.22
Compute ↑Model Developers
Due to the necessity of increased volumes of compute access
for AI R&D and the dependence on a few American companies
for such a large volume of compute, there are commercial (e.g.,
new specialized clouds / "neoclouds"), government (e.g., publicly
funded compute infrastructure), and technical efforts (e.g., around
decentralized compute platforms) to build new compute offerings.
Services and tools for decentralized training and deployment are
growing as an area of innovation, driven by their potential strategic
value. Countries and regions that cannot realistically match the
scale of the U.S. or China in raw computing power are building out
publicly subsidized infrastructure and focusing their computing
allocations on specialized research areas or strategic applications
where they can excel.
3.1
Compute Services Market
Organizations in the compute segment include major cloud providers
(like Amazon Web Services, Microsoft Azure, and Google Cloud),
specialized AI compute companies (e.g. CoreWeave, Lambda Labs),
high-performance computing (HPC) centers (such as national super-
computers or research labs), and emerging dedicated AI compute
clusters (like NVIDIA’s DGX Cloud or sovereign AI compute initia-
tives).
Specialized AI Clouds (“Neoclouds”)
While hyperscalers expand their capacity, a new class of spe-
cialized AI cloud providers, known as "neoclouds," has emerged,
offering dedicated access to the high-performance GPUs that have
been in persistent short supply. These companies have achieved rapid
growth and signiﬁcant valuations by catering speciﬁcally to AI-native
companies and enterprises with demanding training and inference

an evolving ai supply chain
10
needs. CoreWeave is a leading neocloud. Its success is built on land-
mark, multi-year contracts with leading model developers, including
a $22.4 billion deal with OpenAI23 and a $14.2 billion deal with Meta,
cementing its role as a key infrastructure provider.24 Lambda Labs
and G42 are examples of other rapidly growing neoclouds. These
ﬁrms received priority in GPU supply from NVIDIA. NVIDIA is keen
Hardware ↑Compute
to diversify beyond the Big Tech clouds, especially as Google, Ama-
zon, and Microsoft each increasingly invest in their own proprietary
ASIC chip designs.25 Lambda Labs raised enormous debt and equity
ﬁnancing, sometimes coupled with multi-year, paid-upfront customer
commitments.26
3.2
Cloud Sovereignty
The global cloud market is increasingly viewed through a geopolitical
lens. U.S.-based Amazon, Google, and Microsoft held ~63% of the
market, as of Q2 2025.27 This has created dependencies that other
nations are now actively seeking to mitigate, particularly due to how
it reduces domestic control over user privacy, creates great exposure
to geopolitical and trade uncertainty, and dilutes future economic
returns from AI development and deployment.28
Perceiving it as a matter of national security and economic compet-
itiveness, nations are investing billions to build and control locally-
based compute infrastructure.29 As a result, a class of countries could
Capital →Compute
develop as emerging advanced computing hubs within their regions
and help reduce their dependence on American giants, particularly
for strategic AI use-cases. These nascent hubs include South Korea,
the United Kingdom, France, India, the United Arab Emirates, and
Saudi Arabia.30 These countries are not nearly at the level of the U.S.
or China in terms of their infrastructure capacity, but their invest-
ments and planned initiatives position them to have signiﬁcantly
more capacity in the coming years than most other countries in the
world.
Compute Centralization
The convenience and efﬁciency of large cloud platforms create
natural points of political and commercial control, which can be
beneﬁcial for monitoring and preventing misuse of AI models.31
However, centralization can also bottleneck access to services and
create exposure to unfair market behavior and security vulnera-
bilities. Alongside growing national compute investments, these
concerns are also motivating widespread interest in decentralized
compute. Decentralized compute platforms aim to aggregate globally
distributed hardware to offer lower-cost AI training and inference.
Prominent decentralized platforms include Petals,32 DiLoCo,33 and

an evolving ai supply chain
11
crypto-incentivized networks like Bittensor.34
Such platforms could also favor data security by allowing users to
process data locally. However, decentralized approaches considerably
lag traditional centralized clusters in scale and efﬁciency. The leading
AI companies use tens of thousands of tightly coupled GPUs to
train models with hundreds of billions of parameters (for instance,
Meta’s Llama-3 405B trained on 16,000 GPUs), whereas decentralized
platforms face high latency, heterogeneous hardware, and reliability
challenges.35

an evolving ai supply chain
12
4
Hardware: Specialization and Geopolitics
This section covers the advanced chips used in AI training and infer-
ence and associated components such as networking and memory.
4.1
Hardware Market
Many types of hardware are critical to frontier AI model develop-
ment. Here, "hardware" refers to the chips used for training and
inference, as well as supporting devices that enable the creation of
clusters and data centers.
Table 1: Hardware for frontier AI model development
Category
Type
Companies
Chips for training and
inference
GPUs
NVIDIA, AMD
Chips for training and
inference
ASICs
Google (TPUs), OpenAI (Broadcom chip), Amazon
(Trainium/Inferentia), Meta (MTIA), Microsoft (Maia)
Supporting Hardware
High-bandwidth
memory (HBM)
SK hynix, Samsung, Micron
Supporting Hardware
Network interconnects
NVIDIA, Broadcom, Arista, Cisco
Supporting Hardware
Advanced packaging
TSMC
Key actors in this segment include chip designers, semiconductor
foundries that manufacture chips, and ﬁrms that create supporting
hardware (e.g., HBM, interconnects) and provide essential chip fab-
rication equipment (e.g., ASML for lithography machines). NVIDIA
remains the undisputed leader in the AI chip market, holding a
market share of over 90% in 2025 for GPUs used for data centers.36
AMD held about 4% of the market for AI chips used in servers.37
Specialized AI chips designed by hyperscalers (such as Google TPUs
or Amazon’s Trainium and Inferentia chips) make up a smaller but
growing portion of the market for AI servers.
Low-Level Libraries
NVIDIA CUDA
NVIDIA’s CUDA (Compute Uniﬁed Device Architecture) software
is key to its dominance as a chip provider. CUDA is valuable for
enabling parallel computing for AI training and other applications.
Hardware →Software Dependencies
Its maturity, extensive libraries (e.g. cuDNN and cuBLAS), and broad
support across all major AI frameworks create a powerful lock-in
effect, making it the default choice for developers and a formidable

an evolving ai supply chain
13
competitive advantage for NVIDIA.38 Many AI libraries are CUDA-
optimized, so switching to a non-CUDA GPU involves costs and
friction.
AMD ROCm
The primary challenger to CUDA is AMD’s ROCm (Radeon Open
Compute platform). While historically lagging in maturity and
adoption, ROCm made signiﬁcant strides by 2025. Its open-source
nature and improving compatibility with key frameworks, such
as PyTorch and DeepSpeed, have made it an increasingly viable
alternative.39 AMD’s 2025 acquisition of compiler company Brium
was explicitly aimed at challenging NVIDIA’s dominance by making
it easier to port AI workloads onto AMD hardware.40
Specialized AI Chips
In response to NVIDIA’s market power, as well as to achieve
greater cost efﬁciency and performance in AI training and deploy-
ment, many of the leading AI model developers and cloud providers
are investing heavily in developing custom-designed Application-
Speciﬁc Integrated Circuits (ASICs). This has created a bifurcation
Model Developers →Hardware
in the AI chip market: a general-purpose market dominated by
NVIDIA, and a market of ASICs optimized for speciﬁc, frontier-scale
AI workloads. This ASIC landscape includes Google’s TPUs, Ama-
zon’s Trainium and Inferentia (also used by Anthropic), Microsoft’s
MAIA, OpenAI’s chip partnership with Broadcom, and Meta’s MTIA.
Table 2: ASICs from leading AI model developers
Company
ASIC
Maturity
Hardware–Software Co-Design
Ecosystem Openness
Google
TPUs
Widely Deployed
Designed with use of AI systems
(AlphaChip). Optimizing for antici-
pated needs of GDM model roadmap.
Only available via
GCP; supports open pro-
gramming frameworks.
Amazon
Trainium
Widely Deployed
Designed using input from An-
thropic’s model roadmap, in addition
to Amazon’s AI platforms.
Only available via
AWS; supports open pro-
gramming frameworks.
Amazon
Inferentia
Widely Deployed
—
Only available via
AWS; supports open pro-
gramming frameworks.
OpenAI
In-development
Concept, expected
2029
Designed using in-house AI tools
and optimizing for OpenAI model
roadmap.
TBD.
Microsoft
Maia
Limited Deploy-
ment
Designed using input from Ope-
nAI’s model roadmap.
Only available via
Azure.
Continued on next page

an evolving ai supply chain
14
Table 2: ASICs from leading AI model developers (continued)
Company
ASIC
Maturity
Hardware–Software Co-Design
Ecosystem Openness
Meta
MTIA
Pilot
Optimized for Meta’s deep learn-
ing recommendation systems.
Internal only
If model developers or cloud providers continue to develop and
adopt proprietary chips, this could increase fragmentation across
software and hardware stacks used for AI development, leading to
isolated and separate frontier AI development environments. Closed
ecosystems might make external auditing more challenging, as it is
difﬁcult to inspect a black-box service built with proprietary software
and running on a custom chip.41
Memory and Interconnect
Training frontier-scale models is not only limited by raw com-
pute, but also by how fast data can be shuttled between chips and
memory. Memory bandwidth is the rate at which data can be read
or written between processing units (also called "cores") and memory.
Bandwidth is a key limiter of efﬁciency for frontier-scale training
and inference, and is an area where more specialized chips outper-
form less specialized ones. GPUs and AI-speciﬁc ASICs typically use
high-bandwidth memory (HBM), which has a bit less total capacity
than CPU memory modules but allows very high speed for accessing
memory. Due to its value for AI training and inference, the growth
of the market for HBM had an annual rate of 40-45% between 2023
and 2025.42 HBM has limited suppliers, including SK hynix and Sam-
sung from Korea and Micron from the U.S. SK hynix is the current
market leader, controlling over 60% of the market.43 Any shortfall in
HBM supply immediately bottlenecks GPU and ASIC production.44
Micron’s entire HBM3 output for 2024 was reportedly pre-sold to just
a few customers.
4.2
Geopolitical Controls
Hardware is a strategic chokepoint in the context of geopolitical
competition to lead on AI. The most advanced GPUs and ASICs
rely on manufacturing processes capable of producing the most
performant chip designs.45 Today, >90% of more efﬁcient chips are
produced by TSMC in Taiwan, using EUV lithography equipment
supplied only by ASML in the Netherlands.46,47
Since 2022, the U.S. and allied countries have implemented a
ﬂuctuating export control regime to bar China from obtaining the

an evolving ai supply chain
15
most advanced AI chips and the manufacturing equipment for such
chips.48 The rationale for these controls was based on the theory
that access to such chips and the relevant manufacturing technology
could make the difference in reducing the gap in AI capabilities be-
tween the U.S. and China. By mid-2025, the export control regime
had become signiﬁcantly less restrictive after the Trump administra-
tion set up a licensing regime to allow some exports of previously
restricted NVIDIA and AMD chips under fees and conditions.49
Liang Wang, founder of leading Chinese AI model developer
DeepSeek, has stated that access to leading-edge chips has been a key
limiter for his company’s ability to advance the state-of-the-art in AI
model development.50
According to a 2025 U.S. congressional report, these controls have
impeded China’s advanced chipmaking "with some success" but still
have "signiﬁcant gaps," as Chinese ﬁrms were able to buy $38 billion
worth of foreign chipmaking gear in 2024 alone.51 Exploitations of
export control loopholes include purchasing restricted equipment
that is smuggled through entities and/or countries that have not been
formally speciﬁed for export controls, leveraging cloud access via
subsidiaries abroad, or purchasing slightly lower-tier hardware in
bulk.52,53,54
In response to export controls, China has attempted to spur rapid
domestic advancement in semiconductors by ramping up funding.
The Chinese government’s "Big Fund" (the China Integrated Circuit
Industry Investment Fund) initiated its third phase of funding in
2024, consisting of $47 billion set to be disbursed over the course of
15 years.55,56, Funding focus areas include scaling up advanced chip
Capital →Hardware
manufacturing, innovation in AI ASIC design, and capacity to manu-
facture high-bandwidth memory.57 China now dominates production
of legacy-generation chips (28 nm and above) and has developed
advanced AI chip designs (e.g. Huawei’s Ascend58). President Xi Jin-
ping has emphasized "self-reliance" in AI hardware, backing research
into indigenous lithography and advanced packaging.59
While the U.S. continues to hold the lead in the most advanced AI
chips, the past 5-10 years saw China dramatically improve its AI chip
capabilities.60

an evolving ai supply chain
16
5
Critical Minerals: Concentration and Negotiation
This section covers minerals that are essential for producing chips,
data center infrastructure, and energy.
Figure 2: Top Producing Countries
for Critical Minerals for Frontier
AI.
Darker shading indicates more
dominance across more critical
minerals.
A variety of processed critical minerals are necessary for hardware
manufacturing, data center buildouts, and power production within
the frontier AI supply chain.61 Chips (including GPUs and ASICs)
require silicon wafers and chemical processing. Interconnects, which
allow fast data transfer between chips, require elements such as
cobalt and tungsten. Copper is necessary for chip wiring that carries
Critical Minerals →Hardware
both information and power. Data center server racks hold high-
capacity hard drives that use powerful magnets made of rare-earth
elements (including neodymium, praseodymium, and dysprosium)
in their motors, which allow for read/write operations. Data centers
require an extremely stable power supply, and their backup power
units often utilize lithium-ion batteries, which incorporate cobalt,
nickel, and graphite among their mineral components. As energy
Critical Minerals →Compute
needs grow for an increasing number of data centers, alternative
energy sources will need to be expanded, and these will also require
wind turbines built with rare-earth magnets and solar panels con-
structed with silicon and silver. Power infrastructure, in general,
tends to require large amounts of copper and aluminum for power
cables, transformers, and other electrical equipment.
5.1
Supply Constraints
The global production and processing of minerals critical to the AI
supply chain are highly concentrated, creating signiﬁcant supply

an evolving ai supply chain
17
chain vulnerabilities. China, in particular, holds a dominant position
not just in the mining of certain minerals but, more strategically, in
the midstream processing and reﬁning stages for nearly all of them.
The U.S. Geological Survey (USGS) estimates that a thirty percent
supply disruption of gallium (critical for compound semiconductors
used in power systems, among many other things) could cause a
more than $600 billion decline in U.S. economic output (approxi-
mately a 2.1% reduction of national GDP).62 In the wake of the new
trade rules China placed on rare-earth elements in October 2025,63
preparing for potential supply disruptions and to ﬁnd avenues to
secure supplies has become increasingly important.
Table 3: Critical Minerals for Frontier AI Supply Chain
Mineral Name
Function in AI Supply Chain
Top 3 Producing Countries
(with % of global supply, 2024
est.)
Silicon
Fundamental semiconductor substrate for chips.
China (80%), Russia (6%),
Brazil (4%)
Gallium
Compound semiconductors (GaAs, GaN) for
high-frequency AI chips and 5G.
China (90%+), Germany,
Kazakhstan, South Korea
(combined < 10%)
Germanium
Fiber optics for data centers, high-speed inte-
grated circuits.
China (60%+), Belgium,
Russia
Rare Earth Elements
(REEs)
Magnets (Neodymium, Dysprosium), polishing
(Cerium), dielectrics (Lanthanum, Yttrium).
China (70%), United States
(12%), Australia (6%)
Copper
Wiring in chips, data center power distribution,
and cooling systems.
Chile (24%), DRC (11%),
Peru (8%)
Lithium
Primary component of lithium-ion batteries for
data center energy storage.
Australia (47%), Chile (30%),
China (15%)
Cobalt
Cathode material in lithium-ion batteries; intercon-
nects in semiconductors.
Democratic Republic of
Congo (74%), Indonesia (10%),
Russia (4%)
Nickel
Cathode material in high-energy-density lithium-
ion batteries.
Indonesia (50%), Philippines
(9%), New Caledonia (6%),
Russia (6%)
Manganese
Cathode material in LFP and manganese-rich
batteries.
South Africa (33%), Gabon
(18%), Australia (14%)
Graphite (Natural)
Anode material in lithium-ion batteries.
China (69%), Mozambique
(12%), Madagascar (5%)
Sources: Government of Canada; Z2Data; SFA Oxford; USGS Mineral Commodity Summaries.

an evolving ai supply chain
18
5.2
Key Countries
United States
The Trump administration has been particularly active in the
critical minerals arena. They have used a combination of executive
orders, federal funding mechanisms, and direct equity investments
to bolster domestic production and processing of critical minerals.
These actions demonstrate a clear and deliberate strategy to use the
ﬁnancial and legal power of the U.S. government to onshore and
de-risk the foundational layers of the hardware supply chain.
Departmental Authorities
A March 2025 Trump Administration executive order designated
minerals security as a national security imperative and established
the National Energy Dominance Council (NEDC), chaired by the
Secretary of the Interior, to oversee progress.64 This EO expanded
the deﬁnition of "minerals" beyond the ofﬁcial critical minerals list
to include strategically vital commodities like copper, uranium, and
gold, thereby widening the scope of federal support. The order di-
rects agencies such as the Department of Defense (DOD), Department
of the Interior, and Department of Energy to expedite permitting for
priority mining projects on federal lands and to leverage ﬁnancing
programs to support domestic projects. The U.S. International Devel-
opment Finance Corporation (DFC), traditionally focused on overseas
development, has been empowered alongside the DOD to issue loans
and guarantees for domestic mineral production under the Defense
Production Act (DPA).
Ukrainian Critical Minerals
The Trump administration has signed a strategic minerals agree-
ment with Ukraine, aiming to jointly invest in Ukraine’s signiﬁcant
deposits of lithium, graphite, titanium, and other resources through a
Reconstruction Investment Fund managed by the DFC.65 This deal is
structured to provide Ukraine with reconstruction capital while giv-
ing the U.S. a stake in securing a European supply chain for minerals
directly relevant to AI and defense technologies.
Public Stakes in Minerals Companies
Domestically, the government has taken direct equity stakes in
key mining companies. It acquired a 5% stake in Lithium Ameri-
Capital →Critical Minerals
cas, as well as a 5% stake in the company’s Thacker Pass lithium
joint-venture with General Motors in Nevada, a crucial resource for
battery production.66 Similarly, the DOD has made signiﬁcant equity
investments in MP Materials, the owner of the Mountain Pass mine
in California, the only at-scale rare earth mining and processing site
in North America.67

an evolving ai supply chain
19
China
China remains the most dominant player, a position built not just
on mining output but also dominance over midstream processing
and reﬁning.68 This dominance gives Beijing immense leverage,
which it has demonstrated through the imposition of export controls
on materials like gallium, germanium, and certain rare earths.69
Australia
Australia is strategically positioning itself as a signiﬁcant, reliable
supplier of critical minerals to Western allies. Its "Critical Minerals
Strategy 2023-2030" aims to leverage its vast resources70 to move
beyond simple extraction and into downstream processing.71 The
Australian government is actively supporting this goal through
ﬁnancial mechanisms like the $2 billion Critical Minerals Facility,72
which invests in domestic critical minerals mining and processing
projects, and through exploring joint investments with the United
States.73,74
Chile
In South America, Chile holds a powerful position due to its
lithium reserves located in the Atacama salt ﬂats, which account for
approximately 30% of global production.75 The Chilean government
has sought to exert greater state control over lithium production.76
Democratic Republic of Congo (DRC)
The Democratic Republic of Congo (DRC) is the source of over
70% of the world’s cobalt, an essential mineral for high-energy-
density batteries.77 China has established a dominant presence in the
DRC’s cobalt sector, controlling a signiﬁcant portion of the industrial
mines and processing facilities.78,79

an evolving ai supply chain
20
6
Capital: Ownership and Interdependency
This section covers major investors funding each segment of the
frontier AI supply chain.
Frontier AI development is increasingly capital-intensive, due
to the infrastructure costs required to advance along the scaling
trajectory and to hire scarce talent. Forecasts currently expect ~$1
trillion in global investment in AI by 2027.80 This investment has
been driven by optimism about the potential for AI to be valuable
across all industry sectors. Goldman Sachs senior global economist
Joseph Briggs predicts that generative AI will automate 25% of all
work tasks in the United States, raise national productivity by 9%,
and raise GDP growth by 6.1% cumulatively over the next decade.81
The companies driving this investment include venture and
growth capital ﬁrms, as well as the capital expenditures and ven-
ture investments of hardware and software companies throughout
the AI supply chain, and a growing set of sovereign wealth funds
that deploy capital as an extension of national strategies.
Capital ↑Hardware
Capital →Data
Capital ↑Model Developers
6.1
Venture & Growth
Table 4: Venture & Growth Investors in the Frontier AI Supply Chain
Investor Name
Home Country
Flagship AI Investments
Focus
Areas
Est. Capital
Deployed in AI
Andreessen
Horowitz (a16z)
USA
OpenAI, Mistral AI, xAI,
Databricks
Models,
Data
Participated in
rounds for xAI and
Mistral AI alone in
2024–2025.
Lightspeed Venture
Partners
USA
Anthropic, Mistral AI,
Stability AI
Models
Led Anthropic’s
$3.5B Series E; lead
investor in Mistral’s
seed round.
Sequoia Capital
USA
OpenAI, xAI, NVIDIA
Models,
Hardware
Early investor in
NVIDIA
Thrive Capital
USA
OpenAI, Anthropic, Any-
sphere, Isomorphic Labs
Models,
AI Science
Invested $1B in
recent OpenAI round
and participated in
$6.6B secondary sale.
Continued on next page

an evolving ai supply chain
21
Table 4: Venture & Growth Investors in the Frontier AI Supply Chain (continued)
Investor Name
Home Country
Flagship AI Investments
Focus
Areas
Est. Capital
Deployed in AI
SoftBank Group /
Vision Fund
Japan
OpenAI, ARM, Stargate,
Intel
Models,
Hardware,
Compute
Lead investor in
OpenAI’s Stargate
initiative; invested
$2B in Intel.
6.2
Corporate
An unparalleled investment cycle is taking place among hyperscalers,
hardware companies, and model developers. In addition to large
capital expenditures, they are making strategic partnerships that
involve making substantial investments in each other alongside
agreements on supply and demand transactions.
Table 5: Corporate Investors in the Frontier AI Supply Chain
Investor Name
Home Country
Flagship AI Supply Chain Investments
Est. Capital Deployed in
AI
NVIDIA
USA
OpenAI, xAI, Mistral AI, CoreWeave, Co-
here, Intel
Up to $100B committed to
OpenAI; $5B in Intel; Poten-
tially $2B in xAI; participated
in Mistral’s Series C.
Microsoft
USA
OpenAI, Mistral AI, HiddenLayer
$10B+ investment in
OpenAI; strategic partnership
and investment in Mistral AI.
Google
USA
Anthropic, Isomorphic Labs, Lightmatter
Multi-billion-dollar invest-
ments in Anthropic.
OpenAI
USA
AMD
The OpenAI–AMD part-
nership includes a warrant
that gives OpenAI the option
to acquire up to 160 million
shares of AMD, equivalent to
a stake of roughly 10%.
ASML
Netherlands
Mistral AI
EUR 1.3B (approx. $1.4B)
in Mistral AI.

an evolving ai supply chain
22
Strategic Investments
To secure the unprecedented amounts of compute necessary to
train frontier models, AI companies are entering into complex and
long-duration agreements with hardware companies that blend ele-
ments of debt ﬁnancing, equity investment, and strategic partnership.
Model Developers ↑Hardware
These agreements are creating deeply intertwined alliances that
secure supply for one party and demand for the other.
Mistral-ASML One example is the strategic partnership between
Dutch semiconductor equipment manufacturer ASML and French
AI leader Mistral AI, announced in September 2025.82 In this deal,
ASML invested €1.3 billion as the lead investor in Mistral AI’s Series
C funding round, acquiring an approximately 11% stake in the
company. The rationale extends beyond ﬁnancial investment. The
agreement establishes a long-term collaboration to integrate Mistral’s
AI models into ASML’s product portfolio and R&D processes, aiming
to accelerate innovation in lithography systems. For ASML, the
partnership provides access to AI tools and expertise. For Mistral AI,
it provides not only substantial growth capital but also a strategic
partnership with an irreplaceable player in the hardware supply
chain and a powerful endorsement of its technology. The deal also
grants ASML a seat on Mistral AI’s Strategic Committee, giving it an
advisory role in the company’s future direction.
NVIDIA-OpenAI Another such agreement took place between
NVIDIA and OpenAI, announced in September 2025.83 This agree-
ment involves a commitment from NVIDIA to invest up to $100
billion in OpenAI, tied to the deployment of at least 10 gigawatts
of NVIDIA systems for OpenAI’s next-generation AI infrastructure.
The ﬁrst phase, utilizing the NVIDIA Vera Rubin platform, is set to
begin in the second half of 2026. For OpenAI, it secures compute for
training future models. For NVIDIA, it locks-in a key customer and
solidiﬁes leadership as the primary hardware supplier for frontier AI
development. The deal involves co-design of both companies’ hard-
ware and software roadmaps, aimed at creating a vertically-aligned
development ecosystem.
AMD-OpenAI In a direct challenge to NVIDIA’s dominance, Ope-
nAI also signed a multi-billion-dollar deal with AMD in October
2025.84 The agreement covers the deployment of 6 gigawatts of AMD
Instinct GPUs over several years, beginning in late 2026. Critically,

an evolving ai supply chain
23
the deal includes a warrant that gives OpenAI the option to acquire
up to 160 million shares of AMD, equivalent to a stake of roughly
10%. This structure allows OpenAI to diversify its compute supply
chain away from a single provider. For AMD, it provides valida-
tion of its AI hardware and software stack from the leading model
developer.
6.3
Sovereign
Nations are leveraging their authority and sovereign wealth funds to
make investments across the AI supply chain. State-backed owner-
ship stakes are increasingly common and include countries across the
globe, such as Saudi Arabia, Oman, Qatar, the UAE, Singapore, the
U.S., China, Taiwan, and Korea.
Table 6: Sovereign Investors in the Frontier AI Supply Chain
Investor Name
Home
Country
Flagship AI Invest-
ments
Focus
Areas
Details
Public Investment
Fund (PIF)
Saudi
Arabia
xAI (via Kingdom
Holdings), Softbank,
Humain
Models,
Compute
Undisclosed
Mubadala / MGX
UAE
OpenAI, xAI,
Anthropic, Databricks
Models,
Compute,
Hardware
Participated in
OpenAI’s $6.6B
secondary sale;
bought Anthropic
shares through FTX
bankruptcy auction
Oman Investment
Authority
Oman
xAI, Salience Labs
Models,
Hardware
Undisclosed
Qatar Investment
Authority
Qatar
xAI, Anthropic,
Blue Owl
Models,
Compute
Participated in
Anthropic’s $13B
Series F
Temasek Holdings
Singapore
OpenAI (via Alpha
Intelligence Capital),
Aligned Data Centers,
Tencent, Alibaba
Models,
Data Cen-
ter Infra.,
Hardware
Portfolio share
in China at 18% of
S$434B total portfolio
(as of March 2025).
U.S. Government
USA
Intel, Lithium
Americas, MP Materi-
als
Hardware,
Critical
Minerals
$8.9B equity stake
in Intel
Continued on next page

an evolving ai supply chain
24
Table 6: Sovereign Investors in the Frontier AI Supply Chain (continued)
Investor Name
Home
Country
Flagship AI Invest-
ments
Focus
Areas
Details
China Integrated
Circuit Industry
Investment Fund
(“Big Fund”)
China
SMIC, Hua Hong
Semiconductor,
Yangtze Memory
Technologies (YMTC)
Hardware
$47.5B (Phase III
fund) being invested
across Chinese semi-
conductor manufactur-
ers over 15 years
National Develop-
ment Fund (Taiwan)
Taiwan
TSMC
Hardware
Holds ↓6–7% of
TSMC
National Pension
Service of Korea
South
Korea
Samsung Electron-
ics
Hardware
Holds ↓7–8% of
Samsung Electronics
7
Conclusion
There are profound interdependencies within the frontier AI supply
chain. This paper aims to illustrate how the AI supply chain is un-
dergoing substantial change across every segment, and how change
happening in one part of the supply chain is tied to change in other
segments. To attempt to summarize just a few of these interdepen-
dencies:
• The increasing scarcity of high-quality datasets directly fuels the
demand for synthetic and multi-modal data, which in turn grows
demand for compute services
• Escalating demand for compute, concentrated among a few major
cloud providers, has spurred the emergence of specialized "neo-
clouds" and national efforts towards "cloud sovereignty," impacting
investment ﬂows from venture ﬁrms, hyperscalers, and sovereign
funds
• Worries about over-reliance on a near-monopoly NVIDIA has
prompted leading AI model developers to invest heavily in custom
ASICs, creating a nascent bifurcation in the hardware market
• Hardware advancements rely on a steady supply of critical miner-
als, whose concentrated production and processing, particularly
in China, create signiﬁcant vulnerabilities that are the subject of
geopolitical maneuvering
• The mix of private and public capital ﬂowing into the AI model

an evolving ai supply chain
25
supply chain intertwines the fates of hardware providers, model
developers, cloud services, and government investment programs
The AI model supply chain will no doubt continue to evolve rapidly
over the coming decades. Several research topics emerge from our
discussion as ripe for further exploration:
• How data scaling will unfold beyond current limits, particularly
concerning the potential for data contamination feedback loops
from public AI-generated content and private synthetic data
• The extent to which decentralized compute platforms could pose
meaningful challenges to centralized cloud services for frontier-
scale AI development
• How increased fragmentation across software and hardware
stacks due to proprietary chip development could impact model
robustness and security
• The potential for severe disruption from supply shocks or restric-
tions for critical minerals
Aside from the above, breakthroughs in model capabilities, increased
geopolitical attention, and signiﬁcant macro events such as large-
scale conﬂicts or market crashes could all continue to signiﬁcantly
alter the structure of the supply chain.

an evolving ai supply chain
26
Notes
1. Kristina Fort and Nikhil Mulani, “AI Oases: Leveraging Gulf AI Ambitions for U.S. Strategic Inﬂuence”, SSRN, https://papers.ssrn.
com/sol3/papers.cfm?abstract_id=5344463
2. Epoch AI, “GPU Clusters”, https://epoch.ai/data/gpu-clusters?view=table
3. Associated Press, “Under New, Unusual Agreement, U.S. Will Get a 15% Cut of Nvidia and AMD Chip Sales to China”, PBS
NewsHour, https://www.pbs.org/newshour/politics/under-new-unusual-agreement-u-s-will-get-a-15-cut-of-nvidia-and-a
md-chip-sales-to-china
4. Epoch AI, “Dataset Size Trend”, https://epoch.ai/data-insights/dataset-size-trend
5. Kylie Robison, “OpenAI Cofounder Ilya Sutskever Says the Way AI Is Built Is About to Change”, The Verge, https://www.theverge.c
om/2024/12/13/24320811/what-ilya-sutskever-sees-openai-model-data-training
6. Epoch AI, “Will We Run Out of Data? Limits of LLM Scaling Based on Human-Generated Data”, https://epoch.ai/blog/will-we-r
un-out-of-data-limits-of-llm-scaling-based-on-human-generated-data
7. ScienceDirect, “The effects of data quality on machine learning performance on tabular data”, https://www.sciencedirect.com/scie
nce/article/pii/S0306437925000341
8. Zahra Shojaei et al., “On the Data Advantage in the Large Multi-Modal Model Era”, arXiv, https://arxiv.org/abs/2507.00038
9. Forbes, “The Extreme Cost of Training AI Models”, https://www.forbes.com/sites/katharinabuchholz/2024/08/23/the-extreme-c
ost-of-training-ai-models/
10. Zeyu Gan and Yong Liu, “Towards a Theoretical Understanding of Synthetic Data for Model Training”, arXiv, https://arxiv.org/ab
s/2410.01720
11. S. Alemohammad et al., “Self-Consuming Generative Models Go MAD”, arXiv, https://arxiv.org/abs/2307.01850; Shiyin Ouyang
et al., “Position: Sora Shows That Data Is More Important Than Compute”, arXiv, https://arxiv.org/abs/2503.14023
12. Press Gazette, “Who’s suing AI and who’s signing: Penske Media sues Google over AI Overviews”, https://pressgazette.co.uk/p
latforms/news-publisher-ai-deals-lawsuits-openai-google/
13. Transparency Coalition, “Financial Times says: AI developers must legally license training data”, https://www.transparencycoalitio
n.ai/news/financial-times-says-ai-developers-must-legally-licensing-training-data
14. Press Gazette, “Who’s suing AI and who’s signing: Penske Media sues Google over AI Overviews”, https://pressgazette.co.uk/p
latforms/news-publisher-ai-deals-lawsuits-openai-google/
15. MarketsAndMarkets, “AI Training Dataset Market Surges to $9.58 billion by 2029”, https://www.globenewswire.com/news-release/2
025/08/12/3131847/0/en/AI-Training-Dataset-Market-Surges-to-9-58-billion-by-2029-Dominated-by-Scale-AI-US-Appen-Aus
tralia-AWS-US.html
16. Institute for Progress, “Teaching AI How Science Actually Works”, https://ifp.org/teaching-ai-how-science-actually-works/
17. The Alan Turing Institute, “AI Won’t Replace the General: Algorithms, Decision Making, and Battleﬁeld Command”, https:
//www.turing.ac.uk/news/publications/ai-wont-replace-general-algorithms-decision-making-and-battlefield-command
18. AI Impacts, “Towards the Operationalization of Philosophy and Wisdom”, https://aiimpacts.org/towards-the-operationalizatio
n-of-philosophy-wisdom/
19. Francesco Aquilar and Mauro Galluccio, “Psychological and Political Strategies for Peace Negotiation”, https://link.springer.com/
book/10.1007/978-1-4419-7430-3
20. Statista Research Department, “Worldwide Market Share of Leading Cloud Infrastructure Service Providers”, Statista, https:
//www.statista.com/chart/18819/worldwide-market-share-of-leading-cloud-infrastructure-service-providers/
21. Bloomberg, “The AI Race Has Big Tech Spending $344 Billion This Year”, https://www.bloomberg.com/news/articles/2025-08-01/
big-tech-s-big-bet-on-ai-driving-344-billion-in-spend-this-year
22. Jaime Sevilla et al., “Compute Trends Across Three Eras of Machine Learning”, arXiv, https://arxiv.org/abs/2202.05924
23. Reuters, “Exclusive: CoreWeave expands OpenAI pact”, https://www.reuters.com/business/coreweave-expands-openai-pact-wit
h-new-65-billion-contract-2025-09-25/

an evolving ai supply chain
27
24. Reuters, “CoreWeave signs $14 billion AI infrastructure deal with Meta”, https://www.reuters.com/technology/coreweave-signs-1
4-billion-ai-deal-with-meta-bloomberg-news-reports-2025-09-30/
25. See “Hardware” section below for more
26. DataGravity, “Year in Review: the Great GPU”, https://www.datagravity.dev/p/2023-year-in-review-the-great-gpu; Reuters,
“CoreWeave, Nvidia sign $6.3 billion cloud computing capacity order”, https://www.reuters.com/business/coreweave-nvidia-sig
n-63-billion-cloud-computing-capacity-order-2025-09-15/
27. Statista Research Department, “Worldwide Market Share of Leading Cloud Infrastructure Service Providers”, Statista, https:
//www.statista.com/chart/18819/worldwide-market-share-of-leading-cloud-infrastructure-service-providers/
28. Financial Times, “Can Europe break free of American tech supremacy?”, https://www.ft.com/content/5e25c397-61d1-4b48-b5c5-6
5561a4c9df2
29. Zoe Hawkins, Vili Lehdonvirta, and Boxi Wu, “AI Compute Sovereignty: Supply Chain Risks and Policy Options”, SSRN, https:
//papers.ssrn.com/sol3/papers.cfm?abstract_id=5312977
30. Epoch AI, “GPU Clusters”, https://epoch.ai/data/gpu-clusters?view=table
31. Girish Sastry et al., “Computing Power and the Governance of Artiﬁcial Intelligence”, arXiv, https://arxiv.org/abs/2402.08797
32. Petals, “Petals”, https://petals.dev/
33. PRIMEIntellect, “OpenDiLoCo: An Open-Source Framework for Globally Distributed Low-Communication Training”, https:
//www.primeintellect.ai/blog/opendiloco
34. Bittensor, “Bittensor Paradigm”, https://bittensor.com/about
35. Haotian Dong et al., “Beyond A Single AI Cluster: A Survey of Decentralized LLM Training”, arXiv, https://arxiv.org/html/2503.
11023v1
36. IoT Analytics, “Leading Generative AI Companies”, https://iot-analytics.com/leading-generative-ai-companies/
37. Ibid
38. sanj.dev, “AMD vs NVIDIA AI Performance: Real-World Analysis 2025”, https://sanj.dev/post/amd-vs-nvidia-ai-workloads-per
formance-2025
39. sanj.dev, “AMD vs NVIDIA AI Performance: Real-World Analysis 2025”, https://sanj.dev/post/amd-vs-nvidia-ai-workloads-per
formance-2025
40. TechCrunch, “AMD takes aim at Nvidia’s AI hardware dominance with Brium acquisition”, https://techcrunch.com/2025/06/04/am
d-takes-aim-at-nvidias-ai-hardware-dominance-with-brium-acquisition/
41. Vitalik Buterin, “The importance of full-stack openness and veriﬁability”, https://vitalik.eth.limo/general/2025/09/24/openness
_and_verifiability.html
42. TrendForce, “HBM and 2.5D Packaging: the Essential Backbone Behind AI Server”, https://www.trendforce.com/news/2023/06/26/h
bm-and-2-5d-packaging-the-essential-backbone-behind-ai-server/
43. Reuters, “SK Hynix says readying HBM4 production as it seeks to retain lead over rivals”, https://www.reuters.com/world/sk-hynix
-says-readying-hbm4-production-it-seeks-retain-lead-over-rivals-2025-09-12
44. The Economist, “Memory chips could be the next bottleneck for AI”, https://www.economist.com/business/2024/10/24/memory-chi
ps-could-be-the-next-bottleneck-for-ai
45. The manufacturing process is usually referred to by “process node” capabilities, measured by the size of chip components in
nanometers (e.g, 7 nm, 5 nm, 3 nm). More efﬁcient chips have smaller component measurements.
46. The Economist, “The Semiconductor Choke Point”, https://www.economist.com/asia/2024/06/13/the-semiconductor-choke-point
47. Alexandre Ferreira Gomes and Jelle van den Wijngaard, “How AI Chips Became a Tool of Global Power”, IE, https://www.ie.edu/i
nsights/articles/how-ai-chips-became-a-tool-of-global-power
48. Bureau of Industry and Security, “Commerce Implements New Export Controls on Advanced Computing and Semiconductor
Manufacturing Items to the People’s Republic of China (PRC)”, https://www.bis.doc.gov/index.php/documents/about-bis/newsroo
m/press-releases/3158-2022-10-07-bis-press-release-advanced-computing-and-semiconductor-manufacturing-controls-fin

an evolving ai supply chain
28
al/file
49. Nicholas Gordon, “U.S.-China chip war: How Trump’s Nvidia-AMD deal has redeﬁned Washington’s export control policy”, Fortune,
https://fortune.com/asia/2025/08/14/us-china-trump-revenue-share-export-controls-nvidia-amd/
50. Zhou Xin and Che Pan, “What DeepSeek’s success means for Nvidia and costly GPU-driven AI growth”, South China Morning Post,
https://www.scmp.com/tech/tech-trends/article/3296625/what-deepseeks-success-means-nvidia-and-costly-gpu-driven-a
i-growth
51. U.S. House Select Committee on the CCP, “Selling the Forges of the Future”, https://selectcommitteeontheccp.house.gov/sites/
evo-subsites/selectcommitteeontheccp.house.gov/files/evo-media-document/selling-the-forges-of-the-future.pdf
52. CNAS, “New Paper Warns AI Chip Smuggling to China May Undermine U.S. National Security Interests”, https://www.cnas.org/p
ress/press-release/new-paper-warns-ai-chip-smuggling-to-china-may-undermine-u-s-national-security-interests
53. Center for Strategic & International Studies (CSIS), “Understanding U.S. Allies’ Current Legal Authority to Implement AI and
Semiconductor Export Controls”, https://www.csis.org/analysis/understanding-us-allies-current-legal-authority-impleme
nt-ai-and-semiconductor-export
54. U.S. House Select Committee on the CCP, “Selling the Forges of the Future”, https://selectcommitteeontheccp.house.gov/media/
reports/selling-the-forges-of-the-future
55. The Diplomat, “China’s Big Fund: Xi’s Boldest Gamble Yet for Chip Supremacy”, https://thediplomat.com/2024/06/chinas-big-f
und-3-0-xis-boldest-gamble-yet-for-chip-supremacy/
56. See “Capital” section for more on China’s “Big Fund”
57. Ibid
58. Lennart Heim (blog), “Huawei’s next AI Accelerator: Ascend 910C”, https://blog.heim.xyz/huawei-ascend-910c/
59. Kyle Chan et al., “China’s Evolving Industrial Policy for AI”, RAND Corporation, https://www.rand.org/pubs/perspectives/PEA40
12-1.html
60. Zijing Wu, “China seeks to triple output of AI chips in race with the US”, Financial Times, https://www.ft.com/content/64caeab8-a
326-4626-98fb-e1bf665827d3
61. SFA (Oxford), “Critical Minerals in Artiﬁcial Intelligence”, https://www.sfa-oxford.com/knowledge-and-insights/critical-miner
als-in-low-carbon-and-future-technologies/critical-minerals-in-artificial-intelligence/
62. Ross L. Manley et al., "A model to assess industry vulnerability to disruptions in mineral commodity supplies", ScienceDirect,
https://www.sciencedirect.com/science/article/pii/S0301420722003348
63. Ana Swanson and Meaghan Tobin, “China’s Rare Earth Restrictions Aim to Beat U.S. at Its Own Game”, The New York Times,
https://www.nytimes.com/2025/10/16/business/economy/china-rare-earths-supply-chain.html
64. Gracelin Baskaran and Meredith Schwartz, “Unpacking Trump’s New Critical Minerals Executive Order”, Center for Strategic &
International Studies (CSIS), https://www.csis.org/analysis/unpacking-trumps-new-critical-minerals-executive-order
65. Gracelin Baskaran and Meredith Schwartz, “What to Know About the Signed U.S.-Ukraine Minerals Deal”, Center for Strategic &
International Studies (CSIS), https://www.csis.org/analysis/what-know-about-signed-us-ukraine-minerals-deal
66. Ernest Scheyder, “US government takes 5% stakes in Lithium Americas and joint venture with GM”, Reuters https://www.reuters.
com/business/autos-transportation/us-government-take-5-stake-lithium-americas-joint-venture-with-general-motors-202
5-09-30/
67. MP Materials, “MP Materials Announces Transformational Public-Private Partnership with the Department of Defense to Accelerate
U.S. Rare Earth Magnet Independence”, https://mpmaterials.com/news/mp-materials-announces-transformational-public-priva
te-partnership-with-the-department-of-defense-to-accelerate-u-s-rare-earth-magnet-independence/
68. Omanjana Goswami, “Chipping in: Critical minerals for semiconductor manufacturing in the U.S.”, https://sciencepolicyreview.
org/wp-content/uploads/securepdfs/2023/08/MITSPR-v4-191618004005.pdf
69. Ana Swanson and Meaghan Tobin, “China’s Rare Earth Restrictions Aim to Beat U.S. at Its Own Game”, The New York Times,
https://www.nytimes.com/2025/10/16/business/economy/china-rare-earths-supply-chain.html
70. Including lithium reserves, signiﬁcant deposits of rare earths, nickel, cobalt, and graphite.

an evolving ai supply chain
29
71. Australian Government, “Critical Minerals Strategy 2023–2030”, https://www.industry.gov.au/publications/critical-minerals-s
trategy-2023-2030
72. Australian Government, “Critical Minerals”, https://www.exportfinance.gov.au/criticalminerals
73. “The Future of U.S.-Australia Critical Minerals Cooperation”, Center for Strategic & International Studies (CSIS), https://www.csis.o
rg/analysis/future-us-australia-critical-minerals-cooperation
74. Melanie Burton, “US offers to buy stakes in Australian critical minerals companies”, Reuters, https://www.reuters.com/business/e
nergy/us-offers-buy-stakes-australian-critical-minerals-companies-2025-10-02/
75. Columbia Global Centers, “Journey Through Chile’s Lithium Landscape”, https://globalcenters.columbia.edu/news/journey-thr
ough-chiles-lithium-landscape
76. Daina Beth Solomon, “Exclusive: As Chile revs up lithium plans, Indigenous people demand more control”, Reuters, https:
//www.reuters.com/world/americas/chile-revs-up-lithium-plans-indigenous-people-demand-more-control-2025-04-07/
77. U.S. Geological Survey, “Mineral Commodity Summaries 2025”, https://www.usgs.gov/publications/mineral-commodity-summari
es-2025
78. Council on Foreign Relations, “China in Africa: March 2025”, https://www.cfr.org/article/china-africa-march-2025
79. Farrell Gregory and Paul J. Milas, “China in the Democratic Republic of the Congo: A New Dynamic in Critical Mineral Procure-
ment”, Army War College, https://ssi.armywarcollege.edu/SSI-Media/Recent-Publications/Article/3938204/china-in-the-d
emocratic-republic-of-the-congo-a-new-dynamic-in-critical-mineral/#end4
80. Goldman Sachs, “Will the $ 1 Trillion of Generative AI Investment Pay Off”, https://www.goldmansachs.com/insights/articles/wil
l-the-1-trillion-of-generative-ai-investment-pay-off
81. Goldman Sachs, “Gen AI: Too Much Spend Too Little Beneﬁt?”, https://www.goldmansachs.com/insights/top-of-mind/gen-ai-too
-much-spend-too-little-benefit
82. ASML, “ASML and Mistral AI Enter Strategic Partnership”, https://www.asml.com/en/news/press-releases/2025/asml-mistral-a
i-enter-strategic-partnership
83. NVIDIA, “OpenAI and NVIDIA Announce Strategic Partnership to Deploy 10GW of NVIDIA Systems”, NVIDIA Newsroom, https:
//nvidianews.nvidia.com/news/openai-and-nvidia-announce-strategic-partnership-to-deploy-10gw-of-nvidia-systems
84. OpenAI, “OpenAI–AMD Strategic Partnership”, https://openai.com/index/openai-amd-strategic-partnership/
