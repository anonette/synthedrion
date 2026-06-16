# Comparative Global AI Regulation: Policy

> Extracted from: `Comparative Global AI Regulation - Policy Perspectives from the EU, China, and the US___Chun Witt Elkins___Kenyon and Oxford.pdf`

Comparative Global AI Regulation: Policy
Perspectives from the EU, China, and the US
Jon Chun1
Christian Schroeder de Witt2
Katherine Elkins1
1Kenyon College
2Oxford University
October 2024
1
Abstract
As a powerful and rapidly advancing dual-use technology, AI offers both
immense benefits and worrisome risks. In response, governing bodies around
the world are developing a range of regulatory AI laws and policies. This paper
compares three distinct approaches taken by the EU, China and the US. Within
the US, we explore AI regulation at both the federal and state level, with a fo-
cus on California’s pending Senate Bill 1047. Each regulatory system reflects
distinct cultural, political and economic perspectives. Each also highlights dif-
fering regional perspectives on regulatory risk-benefit tradeoffs, with divergent
judgments on the balance between safety versus innovation and cooperation
versus competition. Finally, differences between regulatory frameworks reflect
contrastive stances in regards to trust in centralized authority versus trust in a
more decentralized free market of self-interested stakeholders. Taken together,
these varied approaches to AI innovation and regulation influence each other,
the broader international community, and the future of AI regulation.
2
Introduction
Proposed in April 2021 and agreed upon by December, the EU Act was the
first major coordinated effort to regulate AI; it came into force in August 2024.
The Biden administration published its Blueprint for an AI Bill of Rights in
October 2022. It spoke to the need to protect citizen’s privacy and freedom
from algorithmic discrimination. The following month, on November 25th, sev-
eral Chinese government ministries jointly released regulations on AI-generated
deepfakes. The US Whitehouse Executive Order #14110 ”Safe, Secure, and
1
arXiv:2410.21279v1  [cs.CY]  5 Oct 2024

Trustworthy Development and Use of Artificial Intelligence” was issued in Oc-
tober 2023. In February 2024, California State Senator Scott Wiener introduced
what was arguably the strictest AI regulation with the ”SB-1047 Safe and Se-
cure Innovation for Frontier Artificial Intelligence Models Act”. After ten ma-
jor revisions across both the California Senate and Assembly, the bill passed on
September 3rd and now faces an uncertain future as it awaits Governor Newson’s
signature to become law.
Underlying these varied global efforts are common concerns over the ex-
pected social, economic, and geopolitical impacts of AI. The European Union
has taken a proactive stance with regard to social effects of AI, implement-
ing stringent regulations aimed at fostering competitiveness while prioritizing
ethical considerations, enhancing privacy protections, and mitigating poten-
tial harms. China has focused on aligning AI development with ”core socialist
values” while also addressing issues of transparency and workers’ rights. The
United States, meanwhile, has grappled with concerns about AI-generated dis-
information, election integrity, and the role of content recommendation systems
in social media, particularly in light of events such as the 2020 elections and the
rise of platforms like TikTok [Smit et al., 2022].
Beyond the societal effects, there is universal acknowledgement of the cen-
trality of AI to related technologies like advanced chips, energy production and
storage, 5G/6G telecommunications, satellites, and robotics. These illustrate
the importance of AI to national economics, competitiveness, and security. Some
argue that the EU’s stricter AI regulation may inadvertently stifle innovation,
deter investment, and weaken Europe’s position in the global AI and technology
race [Suominen, 2020]. The tension between regulatory safety and competitive-
ness is particularly evident in the dynamics between China and the US, with
both nations striving to balance innovation with responsible AI development [In-
formation Technology and Innovation Foundation (ITIF), 2024].
Still, there are efforts to transcend national policies and competitions to
develop a global harmonization of AI regulation.
AI automation threatens
widespread job displacement, exacerbates inequality and accelerates the need
to transition to a rapidly-evolving job market [The White House, 2024a]. In
September 2024, the United Nations’ AI Adivsory Body released a report high-
lighting key areas of concern that transcend national boundaries. These include
pervasive latent biases, emergence of surveillance states, and AI generated dis-
information [UN AI Advisory Body, 2024]. Additionally, serious legal, secu-
rity, and humanitarian issues–particularly related to autonomous weapons and
public security–underscore the importance of international cooperation. As AI
continues to evolve, the global community faces the complex task of developing
regulatory frameworks that can effectively address these multifaceted challenges
while fostering innovation and ensuring equitable benefits across nations.
2

3
AI Governance
This section describes the emerging AI regulatory frameworks in the EU,
China, and the US at both federal and state levels. In particular, it contrasts
the top-down, risk-based approach of the EU AI Act with the more market-
driven approach of the US. The latter emphasizes coordinating existing legal,
regulatory, and enforcement entities from the federal level down to states and
cities. In between is the Chinese approach, which has the appearance of cen-
tralized regulatory control, but in practice emphasizes decentralized innovation,
regional competition, and economic development at the local levels.
While the EU and China appear to have relatively stable AI regulatory
frameworks, there is a growing debate in the US about the future direction
of AI regulation. The Biden Executive Order #14110 on ”Safe, Secure, and
Transparent Development and Use of AI” coordinates over 100 specific tasks
both within and between over 50 federal entities in a decentralized way that
largely augments existing regulatory laws and agencies. However a number of
US Congressional committees, proposals, and influential public/corporate inter-
est groups are lobbying for a new AI regulatory structure that is more central-
ized, restrictive, and punitive than EO #14110. Some even promote centralized
registration of models, proofs of AI safety, and criminal penalties [LegiScan,
2024, Schumer, 2023].
4
The European Union
4.1
Overview
The 2024 EU AI Act is positioned as the world’s first comprehensive AI
law [European Union, 2024]. Just as prior European general purpose legisla-
tion, such as the 2016 General Data Protection Regulation (GDPR) [European
Union, 2016], the EU AI Act represents complex joint efforts and interests across
various EU bodies, including the European Commission, the European Parlia-
ment and the European Council, where the latter represents the Heads of State
of all EU member countries. Influence on the Act’s formation was also taken
publicly by national government officials, such as France’s premier Macron’s
overt lobbying for exemptions for open source AI providers such as Mistral [Ab-
boud and Espinoza, 2023], as well as, both publicly and covertly, by lobbying
and industry groups, including Big Tech [Perrigo, 2023], and German pro open-
source non-profit LAION [LAION, 2023].
Uniquely, the Act was first constructed within a product safety framework,
but then blended with a fundamental rights agenda at the behest of the Eu-
ropean Parliament and against pressure by the European Commission [The
Privacy Advisor Podcast, 2024]. This approach resulted in a unique and novel
blend of legislative frameworks, clearly setting the EU AI Act apart from prior
legislation building on established frameworks such as the GDPR. As Dragos
Tudorache, a member of the European Parliament from Romania and the chair
3

of the Special Committee on Artificial Intelligence in a Digital Age, remarked:
”Regulation isn’t just rules, it’s an opportunity to express our values [Tyrangiel,
2024].”
While constituting an innovative syncretism at heart, the Act does follow and
respect earlier European generalist regulatory initiatives, such as the GDPR,
and the 2012 Digital Markets Act [Parliament and of the European Union,
2022, DMA]. In fact, the EU started examining the compatibility of the GDPR
and AI as early as in 2020 [Sartor and Lagioia, 2020]. Nevertheless, the release
of ChatGPT in November 2022 and its rapid adoption by millions of consumers
worldwide caught European policymakers off-guard and led to significant ad-
justments to the Act’s handling of AI governance. On December 9th, 2023, the
Act was provisionally agreed between the European Parliament and the Eu-
ropean Council. During the 3-day round of negotiations, the Act’s scope was
tightened [Consilium, 2023]. It was clarified that the Act does not apply outside
of European law, does not infringe on the security competences of the member
states or so-entrusted entities, nor any military or defense applications. Impor-
tantly, it was clarified that the Act would not apply to sole purposes of research
and innovation, nor other non-professional use. Most importantly, the Act’s
traditional approach to AI systems risk classification was complemented by the
notion of general-purpose AI systems (GPAI) [European Union, 2024, Article
3(63)], resulting in a parallel governance track for such AI systems. Despite
open questions, the Act’s ambition to distinguish between GPAI and non-GPAI
systems, and GPAI systems of systemic risk, is similarly unique among AI reg-
ulations globally.
4.2
The Geopolitics of the Act
Besides regulating the EU single market, the Act is widely regarded as a
strategic effort by the European Commission to establish themselves as the lead-
ing AI rulemakers globally [Chatham House, 2024]. Just as after the adoption
of the GDPR in 2016 [European Union, 2016], it is speculated that companies
across the world will begin to prioritize compliance with European AI law out of
economic necessity, not through coercion [Almada and Radu, 2024]. In the case
of the GDPR, this form of “Brussels Effect” [Bradford, 2020] was complemented
by a “de jure” effect in which countries with a lack of their own regulatory ca-
pacity, such as many developing countries, incorporated EU laws instead. For
example, the Philippines incorporated the right to be forgotten into their Data
Privacy Act of 2012 [of the Philippines, 2012, Linklaters, 2024]. In a similar way,
it is speculated that the EU AI Act may similarly become the de-facto standard
for AI governance in much of the Western and developing world [Almada and
Radu, 2024].
One direct institutional consequence of the EU AI Act is the establishment of
a novel authority under the helm of the European Commission, namely the EU
AI Office. This new office will not only oversee AI regulation and AI systems’
compliance, provide a central pool of AI expertise to the EU’s member states,
but also provides a “strategic, coherent, and effective European approach on AI
4

AI system* or
GPAI model?
*(or tool, service,
process, component)
Provider
under EU law
Can the AI system be
directly used for
prohibited applications?
No deployment
within the EU
High-risk
applications?
open source?
Article 52: System
generates synthetic
audio, video, or text?
Watermark outputs.
Undergo the adequate
risk-specific process for
the provision of AI
systems
Article 52: System
directly interacts with
natural persons?
Ensure they are
informed.
Systemic Risk?
(according to the
FLOPS threshold)
GPAI model.
AI system.
Yes.
No.
Limited-risk applications?
Transparency obligations
set out by Article 52.
Engage with the AI
Office.
Document
the decision
process.
Provide adequate cyber
security, including
model evaluations and
adversarial testing.
No.
Yes.
For scientific
purposes only?
Obtain authorization from
rightsholders according to
Directive (EU) 2019/790
No responsibilities along
the AI value chain.
encouraged: model cards
/ data sheets
EU Commission
AI Office
Can designate a
GPAI model as
systemic risk.
Fine issued if
found incorrect.
Local Market
Surveillance
Authorities
Place on
the market.
High-risk systems
continuous, iterative
risk management
Trained on
copyrighted
data?
Provider is
SME?
Reduced
transparency
obligations.
No.
Yes.
No.
Yes.
Provide a sufficiently
detailed summary of the
training data content.
Can protect trade secrets and
confidential business information,
but needs to give copyright holders
and other parties with legitimate
interest the opportunity to exercise
and enforce their rights.
No.
Place on
the market.
Yes.
GPAI models of systemic risk
Continuous risk mitigation measures along
model’s lifecycle, and across AI value
chain. Report incidents to EU Commission.
Provide adequate cyber security protection
against malicious use.
To provide a template for the data
content summary which should be
simple and effective, and monitor.
Expert
Community
Monitor
deployments.
Consulting.
Respect wider
EU law.
Yes.
No.
No.
Yes.
Figure 1: Decision tree for providers of (GP)AI systems and GPAI models on
the way to the EU market.
at the international level” [European Commission, 2024]. A specialist position,
The Advisor for International Affairs, will represent the AI Office in “global
conversations on convergence toward common approaches” [EU AI Act, 2024].
The EU AI Office therefore is not only meant to consolidate the EU’s approach
to AI regulation within the European market, but will likely centrally support
the EU’s foreign policy ambitions in economic and trade negotiations.
4.3
Laws and Regulation
The Act is designed as an adaptive legislation, meaning that many details
are intentionally left vague to permit later adaptation as technology changes.
At its core lies a risk classification system that puts obligations mostly on the
developers (“providers”) of AI systems. Importantly, the Act not only applies
to systems that are placed on the market or put into service in the EU, but
also to AI systems whose output is used in the EU. The use of AI systems for
national security, research, or recreational purposes, as well as, more generally,
end-users of AI systems are excluded from regulation under the Act.
4.3.1
Systems and Models
The AI Act adopts the definition of AI system from the OECD’s AI Prin-
ciples, defining an AI system as “a machine-based system that is designed to
operate with varying levels of autonomy and that can, for explicit or implicit
objectives, generate outputs such as predictions, recommendations, or decisions
that influence physical or virtual environments” [OECD, 2019]. AI models, con-
versely, are mathematical algorithms or trained models that, in isolation, lack
additional components such as a user interface or hardware integration that
would allow them to be used as an AI system.
Among models, the Act further disambiguates between non-GPAI and
general-purpose AI (GPAI) models, with the latter defined as “an AI model,
5

including where such an AI model is trained with a large amount of data us-
ing self-supervision at scale, that displays significant generality and is capable
of competently performing a wide range of distinct tasks regardless of the way
the model is placed on the market and that can be integrated into a variety of
downstream systems or applications, except AI models that are used for research,
development or prototyping activities before they are placed on the market” [Eu-
ropean Union, 2024, Article 3(63)]. Where a GPAI model is integrated into an
AI system, the system is referred to as a GPAI system provided that the system
has the capability to serve a variety of purposes.
4.3.2
Roles
The Act fundamentally distinguishes between the roles of provider, deployer,
importer and distributor. Providers are those “placing on the market or putting
into service AI systems or placing on the market general-purpose AI models
in the Union” [European Union, 2024, Article 2], irrespectively of their loca-
tion.
They have pre-market obligations including an initial risk assessment,
risk-specific compliance, as well as risk-specific post-market obligations. De-
ployers are users of AI systems that are based on the EU and that don’t fall
within a small number of non-professional use cases. The Act furthermore dis-
tinguishes between AI models or systems provided or deployed from within the
EU, and those from outside.
4.4
Risks
At the core of the EU AI Act lies a risk classification system for AI systems
based on their possible “direct” use cases. In the case of GPAI systems, the
degree of “directness” is understood as the extent to which implemented safety
measures can prevent risk-relevant use by deployers. If local market surveillance
believe that a GPAI systems can be (or become) “directly” used for high-risk
activities the EU AI Office will carry out the corresponding compliance proce-
dures [European Union, 2024].
Prohibited use cases.
Integrating fundamental human rights into the prod-
uct safety framework, the Act defines a class of prohibited AI practices, such
as placing on the market AI systems that can be used for certain forms of
manipulation and exploitation, social scoring purposes, and certain biometric
identification purposes. Furthermore, the deployment of AI systems that leave
the user uninformed about their interaction with an AI system, emotion recog-
nition systems or biometric categorisation systems, or AI systems producing
deepfakes are all likewise prohibited [European Union, 2024, Article 5].
High-risk use.
The class of high risk systems constitutes the majority of risk-
related regulation [European Union, 2024, Article 6]. High-risk systems include
a wide variety of systems as defined in [European Union, 2024, Annex I-III],
6

Figure 2: The risk pyramid for AI systems (taken from [Madiega, 2024])
including systems meant to serve as safety systems for other AI systems. Ac-
cording to [European Union, 2024, Article 28(2a)], providers of high risk systems
are subject to compliance obligations, including the establishment of risk and
quality management systems, data governance, human oversight, cybersecurity
measures, postmarket monitoring, and maintenance of the required technical
documentation. Owing to the Act’s adaptive nature, it is expected that these
obligations will be further detailed in later, sector-specific regulation.
Limited risk.
Chatbots or AI systems that generate content or aid in
decision-making without any critical safety aspects or significance are deemed
of limited risk, although the Act only indirectly defines this class [European
Union, 2024, Recital 32a]. These systems are merely subject to transparency
obligations, including end-users of such systems must be informed that they are
interacting with AI.
Minimal risk.
AI systems that pose little to no risk to users’ rights, health, or
safety are left unregulated by the Act, although other obligations under EU law
still apply. These systems are sometimes referred to as minimal risk although
this term is not used in the Act.
Importantly, in the case of GPAI models, a special risk category is defined
for the standalone model even before having been integrated into an AI system.
GPAI models of systemic risk.
The Act imposes particular regulation on
providers of general-purpose AI models of systemic risk [European Union, 2024,
Article D], which it defines to be all models for which “the cumulative amount
of compute used for its training measured in floating point operations (FLOPs)
is greater than 1025” [European Union, 2024]. The limit of 1025 was reportedly
7

reached as a middle ground between 1024 and 1026 demanded by two opposing
factions, the European Parliament, and the European Commission [European
Union, 2024, Chapter II(8)][The Privacy Advisor Podcast, 2024]. Providers of
GPAI need to register their model with the European Commission, and need
to adhere to a wide-ranging catalogue of safety and security criteria. Owing
to its adaptive nature, the Act purposefully leaves various technical criteria
related to systemic risk classifications open for later adjustment to account for
the unpredictability of technological progress.
4.5
Innovation and Open Source
The Act contains several measures intended to harness the economic and
societal benefits of open-source AI software [Eiras et al., 2024a,b].
The Act
defines free and open-source AI components to cover “the software and data,
including models and general-purpose AI models, tools, services or processes
of an AI system” and explicitly states that provision of such models on open
repositories should not seen as a form of monetization [European Union, 2024,
Recital 103].
The EU Act contains wide-ranging exemptions for providers of certain AI
systems provided under free and open source software licenses [European Union,
2024, Article 53-54]. To be exempt, the systems may not contain GPAI models
that fall within the systemic risk category, or otherwise exhibit unacceptable
behavior.
The Act distinguishes the above from providers of pre-trained AI
models that are made accessible to the public under a license that allows for
the access, usage, modification, and distribution of the model, and whose pa-
rameters, including the weights, the information on the model architecture, and
the information on model usage, are made publicly available. It is to be noted
that the term open source model is not used explicitly and the degree of le-
gal overlap with open source software is not immediately clear, and hence such
models might be referred to rather as open models. Open models are not ex-
empt from Article [European Union, 2024, C(1)(c)-(d)], as well as [European
Union, 2024, Article D] and [European Union, 2024, Article 28(2a)], the latter
governing third-party obligations “along the AI value chain of providers, distrib-
utors, importers, deployers or other third parties” [Sartor and Lagioia, 2020]
for high-risk AI systems.
Under any circumstances, providers of open GPAI model providers are re-
sponsible for transparency obligations according to [European Union, 2024, Ar-
ticle C(1)(c)-(d)]. These transparency requirements include respecting existing
Union copyright law [European Union, 2024, Article C(1)(c)] according to Arti-
cle 4(3) of the Digital Single Market Directive (EU) 2019/790 [European Union,
2019], and the need to make a “sufficiently detailed summary of the content used
for training of the general-purpose AI model” [European Union, 2024, Article
C(1)(d)]. The consequences of these transparency requirements for open GPAI
model providers have been examined in [Warso et al., 2024]. Importantly, Direc-
tive (EU) 2019/790 expands GDPR regulation to copyright owners who share
content online, meaning that key GDPR rights, such as the right to opt out [Eu-
8

ropean Union, 2016, GDPR Article 7] would require that copyright owners could
ask for their data to be removed from open GPAI model training data.
As a further measure to stimulate innovation, member states can establish
a regulatory sandbox, i.e. a controlled environment that facilitates the devel-
opment, testing and validation of innovative AI systems (for a limited period of
time) before they are put on the market [Madiega, 2024].
5
China
5.1
Overview
China’s approach to AI governance and regulation is a hybrid between the
centralized, top-down approach of the EU and the decentralized, free-market
of competing interests in the US. Like the EU, China emphasizes safety, indi-
vidual protections, and social harmony through top-down guidance, regulation,
and enforcement [Zhang, 2022]. Like the US, China also emphasizes bottom-up
innovation and economic development through a mix of decentralized provincial
control alongside very competitive local markets. This hybrid approach seeks to
optimize the benefits from both the EU and US models. The EU AI Act takes
a coherent, universal risk-based approach, but the abstract and ambiguous lan-
guage belies the hard work of grappling with real-world details in applying these
general rules to disparate, complex and highly situational cases. Conversely, a
fragmented, sector-specific approach like the US EO #14110 lacks coherent
high-level simplicity, but benefits from experienced domain experts translating
goals into more clear, immediate, and effective enforcement. China seeks to
benefit from the coherence of the EU AI Act and the practical benefits of the
US approach, which promotes innovation and economic competitiveness.
5.2
Laws and Regulations
China has advanced some of the first AI laws and regulations at the national
level, which are summarized in Table 2. Unlike the horizontal risk-based ap-
proach of the EU, China has favored the sector-specific US approach of laws
tailored to specific use-cases. These specific use-cases range from data privacy
(November 2021) to recommendation algorithms (March 2022) to generative AI
(January & August 2023). Despite appearances of centralized government con-
trol, Chinese AI regulations are the product of an iterative process involving di-
verse stakeholders that include mid-level bureaucrats, academics, corporations,
startups, and think tanks [Sheehan, 2024]. The central government relies upon
a pipeline of these experts to formulate, clarify, and interpret the details, while
local officials mainly concern themselves with ensuring goals and outcomes are
aligned with Chinese and socialist ideology [Zhang, 2022]. Both China’s State
Council and the Chinese Academy of Social Sciences have announced intentions
of working towards a more holistic National AI law, although the outcome is
uncertain [Webster et al., 2023].
9

Figure 3: Chinese AI Laws and Regulations
10

5.3
Registration
On paper, China has perhaps the most onerous AI regulation requirements
of the three regions considered. Table 3 lists the three major steps for deploy-
ing advanced AI models (for example, Baidu’s LLM ERNIE) in order to be
in compliance with regulatory laws (see Figure 4). These include model regis-
tration, rules for data management, and provisions for ongoing monitoring for
compliance. The registration process alone illustrates how strict central reg-
ulation can slow down innovation and economic growth. As of March 2024,
only 546 AI models have been registered, and just seventy are Large Language
Models [China Money Network, 2024]. This number is in stark contrast to the
countless commercial models, variants, and over 500,000 open-source LLMs on
Huggingface.co [Huggingface.co, 2024], which is banned in China [ChinaTalk,
2023].
5.4
Compliance and Industrial Policy
In 2015, China announced a national strategic plan and industrial policy
called “Made In China 2025” or MIC2025 integrated with their 13th (2016-2020)
and 14th (2021-2025) Five Year Plan [The State Council of the People’s Republic
of China, 2015].
MIC2025 directs strong government support for innovation
and high-end manufacturing to help make China a global leader in cutting-
edge technologies like AI by 2025 [Congressional Research Service, 2019]. Part
of this plan calls for supporting 10,000 “Little Giants,” the small and mid-
sized enterprises (SME) recognized as a key source of innovation [Global Times,
2021]. Although large “National Champions” like Baidu, Tencent, and Alibaba
are expected to fully comply with AI regulations because of their dominant
influence, the Little Giants are informally afforded leeway in order to avoid
heavy regulatory burdens that could stifle innovation [Zhang, 2024].
What this means from a practical standpoint is that despite such rigorous
guidelines, enforcement in China is relatively lax. Startups and SMEs fly under
the radar as long as they do not have a large public presence [Zhang, 2022].
This approach allows for the promotion of innovation, economic growth, and
international competitiveness [Yang, 2024].
China’s hybrid system of AI regulation and selective enforcement attempts
to combine the strengths of both the EU and the US approaches. While regu-
latory guidance is generally light, top-level enforcement usually comes into play
when destabilizing patterns arise. This reactive enforcement can cause transi-
tory market disruptions and lead to strict and sometimes surprisingly punitive
measures to reign in excesses and outcomes at odds with CCP values like “com-
mon prosperity” [Caixin Global, 2021]. This pattern of regulatory crackdown is
visible in other sectors from real estate[Bloomberg News, 2021] to education [In-
tresse, 2024]. Harsh penalties were levied by regulators between 2020-2022 to
try to control excessive inequality and check the rise of powerful tech (Alibaba)
and financial (Ant Group) corporations that could challenge government author-
ity [Chen and Liu, 2023]. Although deflating the real estate bubble significantly
11

Figure 4:
AI Model Compliance Steps in China
12

reduced household wealth tied to property speculation, the IMF shows China
leads the world’s largest economies with a 5.2% GDP growth [International
Monetary Fund, 2024]. Some of this success is attributed to China’s strategic
industrial policy with its flexible regulatory framework.
6
United States
6.1
Overview
On October 30, 2023 US President Biden signed an executive order (EO
#14110) on the ”Safe,Secure,and Trustworthy Development and Use of Artificial
Intelligence” [The White House, 2023b]. This act moved beyond the voluntary
commitments secured in July 2023 [The White House, 2023a] and the October
2022 AI Bill of Rights [The White House, 2022]. EO #14110 represents the
most comprehensive form of AI regulation in the United States to that date.
It directly delegates AI responsibilities to over 50 existing federal regulatory
agencies and other bodies with over 100 specific tasks designed to:
• Build out the capacity to address emerging concerns around AI
• Integrate AI into agency operations
• Enhance coordination between agencies on AI-related matters
On August 28, 2024 the California Assembly passed SB 1047, the Safe and
Secure Innovation for Frontier AI Models Act. Unlike the federal Presidental
Executive Order, this state law focused on creating a regulatory framework to
test, register, and audit models that could present a danger to public safety.
This AI regulation targets models with substantial investment in pretraining
and fine-tuning above given thresholds of $100M/1026 flops and $10M/1025
flops respectively.
6.2
Laws and Regulations
AI regulation in the US represents somewhat of a departure from the more
typical US approach to regulation. In the US, the legislative branch typically
passes laws that form the framework for regulation, which are then enforced by
the executive branch, primarily under the oversight of various federal agencies.
For example, the US Congress passes laws that define specific industries or ac-
tivities along with broad goals such as advancing scientific research [National
Science Foundation, 2024], promoting fair markets [Security and Exchange Com-
mission, 2024], and safeguarding the environment [Environmental Protection
Agency, 2024] (see NSF, SEC and EPA mission statements and goals). At times,
multiple agencies will be tasked with regulating different aspects of the same
broad goal. For example, the Federal Trade Commission (FTC), the Consumer
Product Safety Commission (CPSC), and the Consumer Financial Protection
Bureau (CFPB) specialize in different aspects of consumer protection and safety.
13

US States and municipalities have also added regulations in areas they feel are
inadequately addressed by federal regulations.
This approach is in keeping with historical norms. The philosophical dis-
trust of centralized power is reflected in the very design of the American system
of checks and balances between branches of government. A decentralized US
approach is also a way to reduce bureaucratic layers, more directly empower
domain experts, and balance power between competing narrow, self-interested
parties. These include powerful voting blocks, special interests, and a $46 bil-
lion state and federal lobbying industry [Massoglia, 2024]. For these reasons,
commercial applications of technology within the US have traditionally been
regulated through various mechanisms including legislative action, executive
orders, agency rulemaking, industry self-regulation, international agreements,
and private self-regulation.
To remain competitive in rapidly changing world markets, US tech com-
panies often pursue self-regulation as a strategy for tackling privacy, digital
advertising, content moderation, and cybersecurity [Cusumano et al., 2021, Mi-
now and Minow, 2023]. We see a similar approach taken in the Biden-Harris
approach to securing voluntary commitments by leading AI companies to man-
age the risks posed by AI [The White House, 2023b]. Furthermore, interna-
tional agreements or regulations are sometimes adopted by US companies to
do business abroad, as in the case for EU’s GDPR [European Union, 2016] and
China’s Cybersecurity Law [National People’s Congress of the People’s Republic
of China, 2016]. The regulatory process often combines these approaches, with
laws providing the foundation for agency regulations involving public input and
expert consultation as technologies and circumstances evolve.
The rapid pace of AI innovation and the immense potential impact of AI,
coupled with the lack of technical expertise in government, has reversed the
normal sequence for enacting regulation that begins with the U.S. Congress.
EO #14110 is a case where the executive branch is initiating many AI-related
policies–from research to regulation–partly due to its ability to more quickly
respond in a coherent and comprehensive manner The White House [2023b].
Although somewhat exceptional for the US process of lawmaking, White House
Presidential executive orders more closely match the top-down, centralized or-
ganization of the European Commission in Brussels and the CCP in Beijing.
In spite of this similarity to the E.U. and China, aspects of the order nonethe-
less reflect the distinct US approach that can be characterized as “bottom-up”
and distributed rather than “top-down” and centralized.
In contrast to the
more centralized, top-down approach to AI regulation prioritizing safety (EU)
and social stability (China), the United States takes a more distributed, multi-
stakeholder approach to AI regulation that mirrors its earlier approaches to
regulating new technologies.
While universal directives on AI are provided by the centralized political
bodies of the CCP and to a lesser extent, the European Commission, a wide
range of guidelines, initiatives, laws, and other policies including trade related
to AI are distributed between various US federal branches and agencies and
even states [Perkins and Coie, 2024].
EO #14110 organizes this distributed
14

regulatory system with specific objectives and deadlines delegated to various
federal agencies directly from the executive branch.
Meanwhile, the US legislative branch is considering dozens of individual
bills [GovTrack.us, 2024]. Thune’s 2023 AI Research, Innovation and Account-
ability Act would create enforceable accountability and transparency for high-
risk systems. The REAL Political Advertisements Act [Klobuchar, 2023] aims to
limit the use of Generative AI in campaigns, The Stop Spying Bosses Act [Casey,
2023] aims to limit the use of AI by employers to surveil employees, and the No
FAKES Act [Coons et al., 2023] aims to protect visual and voice likenesses of
individuals. Two notable, ambitious, and more restrictive plans have been in-
troduced by Senator Schumer in the form of his SAFE initiative [Schumer, 2023]
and the Blumenthal-Hawley Framework [Office of Senator Richard Blumenthal,
2024]. At this time, however, none have been passed. Meanwhile, individual
US states and municipalities have passed laws and are debating more exten-
sive regulation regarding AI [International Association of Privacy Professionals,
2024]. In 2023 more than 40 bills were proposed, and Texas and Connecticut
adopted statutes focused on preventing discrimination [White and Case, 2024].
In the 2024 legislative session, at least forty states, Puerto Rico, The Virgin
Islands and Washington D.C. have introduced AI bills and six states, Puerto
Rico, the Virgin Islands have adopted resolutions or passed legislation [National
Conference of State Legislatures, 2023]. While Article VI of the US Constitu-
tion affirms the supremacy of federal law over state law, California is home to
many of the largest AI corporations, and other industries (e.g. auto emission
levels) have often complied with Calfornia’s stricter standards.
6.3
White House Executive Order 14110
Since 2016 and over three different Presidential administrations, a number of
executive orders related to AI have been issued. The Biden White House’s Oc-
tober 2023 “Executive Order on the Safe, Secure, and Trustworthy Development
and Use of Artificial Intelligence” is the most comprehensive to date [The White
House, 2023b]. It directs over fifty federal agencies to take over one hundred
specific actions addressing eight core policy areas listed in Figure 5 including:
safety and security, innovation and competition, worker support, bias and civil
rights, consumer protection, privacy, federal use of AI, and international lead-
ership [The White House, 2024b]. The eight policy areas are ranked by the
aggregate number of requirements and federal entities assigned to each area.
These arguably provide a loose sense of priorities in each policy area from the
most relevant (federal use, safety/security, and innovation/competition) to the
least (worker support). EO #14110 implements many guidelines in the 2022 AI
Bill of Rights to ensure the responsible design and use of artificial intelligence
with regards to civil rights and privacy in areas such as hiring, healthcare, and
surveillance [The White House, 2022].
EO #14110 also addresses many of the core concerns highlighted in the EU
AI Act. It does so, however, with several key differences [Congressional Research
Service, 2024]. While the EU AI Act establishes a new regulatory agency, the EU
15

Figure 5: Executive Order #14110 on the Safe, Secure, and Trustworth Devel-
opment and Use of AI (* see Appendix A for agency acronyms)
AI Office, which coordinates with member states, industry and civil society, the
current US strategy relies upon augmenting the extensive network of existing
US federal agencies with pre-existing specialized domain expertise.
The US
approach can be seen to emphasize extending expansive regulatory and legal
frameworks from the ground up where infrastructure already exists, in contrast
to creating a new centralized regulatory framework.
Because the US approach involves over fifty federal agencies, it is also much
more extensive in implementation details than the EU. It directly addresses
broader issues like unemployment, education, research, and consumer protec-
tion.
Finally, and again in contrast to the EU AI Act, this US strategy is
arguably more immediately actionable given the over one hundred specific ob-
jectives.
Many deadlines are delegated to federal agencies to be completed
within 180 to 270 days. These agencies are already specialized across a broad
spectrum of existing federal government responsibilities that are being disrupted
by AI. As of this writing, both the White House 180-day and 270-day deadlines
have been met [The White House, 2024c,d].
Enforcement is another major area of difference between the EU and the US.
The EU AI Acts’ risk model is premised upon prevention. General guidelines,
specific penalties, and centralized regulation prohibit activities unless explicitly
permitted. In contrast, the current US risk model is permissive. It promotes
innovation through competition, encourages decentralized self-regulation, and
16

relies upon an extensive network of existing laws and regulations against abu-
sive, illegal, and negligent practices. These networks of existing laws range over
a wide spectrum, extending from specific consumer protection laws to evolv-
ing intellectual property laws [Walters and Wiseman, 2022]. This permissive
approach follows the American tradition of tech sector self-regulation with its
notable success in sectors like online advertising (DAA, NAI), cybersecurity
(NIST, CISA), biotechnology (IGSC, IASB), nanotechnology (ISO, NanoRisk),
and cloud computing (CSA).
Within this permissive structure, and in response to the White House EO
14110, the National Institute of Standards and Technology [NIST, 2024a] es-
tablished the US AI Safety Institute in January of 2024. Housed within the
larger Department of Commerce, NIST was originally established to facilitate
U.S. industrial competitiveness. The US AI Safety Institute has members from
academia, industry, and nonprofits. This partnership mirrors the kind of decen-
tralized and voluntary approach discussed earlier. The US AI Safety Institute’s
initial task forces focus on safety, evaluation, measurement, and risk manage-
ment. Their work follows upon the initial Risk Management Framework pub-
lished in April 2024 [NIST, 2024b]. On July 12 2024 representatives from the
US AI Safety Institute and the European AI Office met in Washington, D.C.
and announced plans for further cooperation and collaboration [NIST, 2024c].
6.4
California SB 1047
The California Senate Bill 1047 (SB 1047: Safe and Secure Innovation for
Frontier AI Models Act), introduced in February 2024 by Senator Scott Wiener,
attempts to minimize potential negative societal impacts of AI in the face of
rapid progress [LegiScan, 2024]. The bill emerged in response to growing con-
cerns about the unique threats posed by powerful AI systems [GDPR Local,
2024]. It would affect nearly every leading AI company either based in Silicon
Valley or doing business with California, the 5th largest economy in the world.
SB 1047 aims to establish a comprehensive AI regulatory framework in Cali-
fornia that is more narrowly focused on ’frontier models’ as defined by potential
risks and computational resources [Anstey and Breslin, 2024]. The bill has gar-
nered support from a diverse coalition of politicians and stakeholders including
AI researchers, unions, and some technology companies advocating for respon-
sible AI development [The Hill, 2024, Lovely, 2024, The Verge, 2024]. It has
also faced opposition from politicians, industry groups, some AI researchers,
and open-source advocates who worry about overly stringent regulations. Crit-
Figure 6: Action Timeline for SB 1047
17

ics fear the bill could stifle innovation, favor a handful of tech giants, and put
California at a competitive disadvantage [Nunez, 2024, Abbott, 2024, Chilson
and Stout, 2024, Abboud and Espinoza, 2023]. However, opinions are roughly
split within traditional interest groups including large corporations, leading re-
searchers, and politicians across both parties, leaving the future of SB 1047
somewhat uncertain.
Ongoing debates surrounding the bill’s potential impact on US competi-
tiveness, AI research and development continue. Uncertainties around costs,
definition of key terms, and the feasibility of implementing requirements raise
more immediate concerns. Much debate centers on the balance between fos-
tering innovation and implementing safeguards [Foley and Lardner LLP, 2024,
Morgan Lewis, 2024]. One of the most controversial aspects of SB 1047 is its
requirement for developers to implement a full shutdown capability for covered
AI models [Neontri, 2024]. Concerns have been raised over potential disrup-
tions to critical infrastructure and services that may rely on these systems, a
demonstration of the complex interdependencies and deep integration of AI with
various sectors of the economy and society [LegiScan, 2024].
Since its introduction, SB 1047 has undergone several revisions in response
to feedback from various stakeholders. Notable changes include narrowing the
scope of pre-harm enforcement and potential liabilities based on site-specific
plans. Controversial elements like the frontier model division, know your cus-
tomer requirements, and uniform pricing were removed. Ambiguities in defini-
tions like ”covered models” were clarified to more precisely target high-impact
AI systems. The scope of the required safety and security protocols were de-
fined, and the timeline for compliance was adjusted to give companies more time
to adapt to the new regulations [LegiScan, 2024]. These amendments demon-
strate the iterative nature of the legislative process, particularly when dealing
with rapidly-evolving technologies like AI and the conflicting interests of di-
verse stakeholders. As other jurisdictions both within the United States and
internationally grapple with similar issues, the outcome of California’s legisla-
tive efforts may have far-reaching impacts for the future of AI regulation and
development [Foley and Lardner LLP, 2024].
Unlike the EU AI Act, which adopts a comprehensive, risk-based approach to
AI regulation across various sectors and applications, SB 1047 appears to focus
more narrowly on high-impact AI systems, particularly those trained using sub-
stantial computational resources [cmswire2024, euronews2024]. This targeted
approach may reflect a philosophy that prioritizes regulating the most powerful
and potentially influential AI models that have the greatest far-reaching societal
impacts.
While the EU AI Act offers a degree of flexibility in implementation, al-
lowing for tailored requirements for specific high-risk AI applications [Gracias,
2024], it is unclear whether SB 1047 adopts a similar approach. In contrast, the
federal U.S. approach to AI regulation, which may influence SB 1047, typically
involves adapting existing laws and regulatory frameworks to address AI-specific
challenges. The special focus on the computational resources used to train fron-
tier AI models suggest a unique regulatory philosophy in which the technical
18

potential of AI systems emerges as the key factor in determining regulatory
requirements.
As shown in Figure 6, SB 1047’s timeline for implementation and compli-
ance, the bill is structured around specific milestones: immediate actions, ac-
tions required by January 1, 2026, actions required by January 1, 2027, and
ongoing actions [smdailyjournal]. While detailed information about the specific
requirements associated with each time frame is not available, this phased ap-
proach suggests a recognition of the need for a gradual implementation process,
allowing stakeholders time to adapt to new regulatory requirements.
6.4.1
Immediate Actions
Figure 7 outlines a series of immediate actions that developers of covered AI
models must undertake if SB 1047 is signed into law. These actions are designed
to establish a framework for the responsible development, risk management, and
public safety around the deployment of high-impact AI systems.
At the core of SB 1047’s immediate requirements is the establishment of ad-
ministrative, technical, and physical measures to prevent unauthorized access
and misuse of covered models, with particular focus on defending against ad-
vanced persistent threats and sophisticated actors. However, the bill’s specific
cybersecurity requirements are not explicitly detailed.
Another key immediate action is the development of a safety and secu-
rity protocol. This written document outlines procedures for managing risks
throughout the model’s lifecycle, including testing procedures to assess poten-
tial harm. Again, exact details of this protocol are not provided.
19

Figure 7: Immediate actions required according to CA SB 1047
6.4.2
Actions by January 2026
SB 1047 outlines a series of actions that developers of covered AI models must
undertake by January 1, 2026, as illustrated in Figure 8. A key requirement
is the implementation of annual third-party audits. Starting January 1, 2026,
developers must engage independent auditors to assess their compliance with the
bill’s requirements. These audits, conducted according to regulations issued by
the Government Operations Agency, require detailed reports evaluating internal
controls and any instances of noncompliance. Developers are required to retain
unredacted versions of these audit reports and provide access to the Attorney
General upon request.
In line with the bill’s commitment to transparency,
redacted versions of these reports must be published, with redactions limited to
protecting sensitive information.
SB 1047 also mandates that developers submit annual compliance statements
to the Attorney General.
These statements, signed by the chief technology
officer or a senior corporate officer, must include assessments of potential critical
harms and verification of compliance with the bill’s requirements. The bill also
introduces a 72-hour reporting requirement for any AI safety incidents affecting
covered models.
Furthermore, SB 1047 establishes a consortium within the Government Op-
erations Agency tasked with developing a framework for ”CalCompute,” a public
cloud computing cluster. This initiative, culminating in a report to be sub-
mitted to the Legislature by January 1, 2026, demonstrates a commitment to
creating public infrastructure for AI development and research. These actions,
20

Figure 8: Actions required by Jan 1st, 2026 according to CA SB 1047
taken together, demonstrate the desire to create a more robust, transparent,
and accountable ecosystem for AI development and deployment.
6.4.3
Actions by January 2027
SB 1047 also outlines a series of actions to be implemented by January 1,
2027, as illustrated in Figure 9. These actions are designed to establish a robust
regulatory framework and governance structure for high-impact AI systems in
California.
Actions include the establishment of the Board of Frontier Models within
the Government Operations Agency.
As shown in Figure 9, the board will
consist of nine members with expertise in AI, safety, and related fields. Their
primary responsibility will be to approve regulations and guidance, ensuring
that the regulatory framework remains informed by the latest developments in
AI technology and safety considerations.
By January 1, 2027, and annually thereafter, the Government Operations
Agency is mandated to issue a set of regulations subject to approval by the
Board of Frontier Models. These regulations serve three functions. First, they
update the definition of ”covered model,” adjusting thresholds to reflect techno-
logical advancements and emerging risks. Second, they establish comprehensive
auditing requirements, defining standards and best practices for the third-party
audits introduced in the previous phase. Finally, they provide guidance on pre-
venting critical harm and offer recommendations to developers on risk mitigation
strategies.
21

Figure 9: Actions required by Jan 1st, 2027 according to CA SB 1047
22

6.4.4
Ongoing Actions
Finally, SB 1047 outlines a comprehensive set of ongoing actions that de-
velopers and operators of high-impact AI systems must undertake to ensure
continued compliance and safety, as illustrated in Figure 10. First and fore-
most, developers are required to engage in annual re-evaluations and updates of
their safety and security protocols. This process ensures that protocols remain
current and responsive to changes in model capabilities and industry best prac-
tices. Complementing this internal review, the bill mandates the continuation
of annual third-party audits.
Figure 10 highlights the ongoing obligation for developers to report AI safety
incidents within 72 hours of discovery. The bill also requires adherence to up-
dated regulations issued by the Government Operations Agency: developers
must remain compliant with the latest standards and definitions.
Of particular note is that SB 1047 introduces important protections for
whistleblowers, prohibiting retaliation against employees who report non-
compliance or risks. The bill also outlines specific responsibilities for operators
of computing clusters. These include policies to assess customers’ use of com-
pute resources with a focus on those using resources sufficient to train covered
models, along with a capability to enact full shutdowns if necessary.
23

Figure 10: Ongoing Actions required according to CA SB 1047
6.4.5
Enforcement
SB 1047 establishes an enforcement mechanism to ensure compliance with
its provisions. It is designed to provide the necessary authority and tools to
address violations and protect the public interest.
The Attorney General is
granted significant authority in enforcing SB 1047 and is empowered to bring
civil actions against entities that violate the bill’s provisions. This authority
extends to halting non-compliant activities and seeking a range of remedies,
including civil penalties and damages where appropriate.
The penalty structure is designed to be proportionate and impactful. Civil
penalties are calculated based on the cost of compute used to train the model
in question. This approach ensures that penalties are commensurate with the
scale and potential impact of the AI system involved.
Additionally, the bill
provides for specific penalties for particular violations such as misrepresentation
by auditors.
Protections and remedies are also established for whistleblowers. Employees
who face retaliation for reporting non-compliance are granted the right to seek
injunctive relief. These protections are cumulative with other laws, ensuring
safeguards for individuals who come forward with concerns.
6.4.6
Veto and After Effects
On September 29th 2024, Governor Newsom vetoed SB 1047 [Newsom,
2024b] because he opposed standards solely based on model size and com-
putational resources.
Instead, he said it was necessary to consider whether
24

AI systems would be deployed in high-risk environments and involve critical
decision-making. As an alternative, Newsom will consult with AI experts to
develop more targeted guardrails for AI deployment and work with the legis-
lature on more empirically-based regulation.
Despite the veto, SB 1047 has
significantly impacted the AI regulation debate by:
• Highlighting the need for proactive safety measures and accountability in
AI development.
• Sparking discussions on the appropriate metrics for regulating AI, such as
computational resources versus actual risks and impacts.
• Raising awareness about potential catastrophic risks associated with ad-
vanced AI systems.
• Demonstrating the challenges of balancing innovation with safety con-
cerns.
• Encouraging industry stakeholders, startups, investors, and open-source
developers to seriously consider AI safety and governance in their strategic
planning.
The bill and subsequent veto have also revealed tensions between state-
level and national approaches to AI regulation, as well as unlikely divisions and
alliances within academia, industry, and government (see Appendix A). Many
argue that a federal framework would be the more effective place to address AI
regulation. Nonetheless, the debate over California SB 1047 will undoubtedly
influence future regulatory efforts at both state and federal levels and could lead
to more nuanced and effective AI regulation. Indeed, Governor Newsom has
signed 17 AI-related bills in the month before his SB 1047 veto and established
new initiatives with the CA legislature and AI experts to establish workable
guardrails and empirical, science-based trajectory analysis of frontier models
[Newsom, 2024a].
The bill and subsequent veto have also revealed tensions between state-
level and national approaches to AI regulation, as well as unlikely divisions
and alliances within academia, industry, and government (see Appendix A).
Many argue that a federal framework would be more effective to address AI
regulation. Nonetheless, the debate over California SB 1047 will likely influence
future regulatory efforts at both state and federal levels. Governor Newsom
signed an impressive 17 AI-related bills prior to his SB 1047 veto. Immediately
after his veto, Newsom launched initiatives with the legislature and AI experts to
develop workable AI guardrails. These initiatives also aim to create empirically-
based predictions of future frontier model capabilities likely to target specific
high-risk AI applications.
25

7
Conclusion
The EU, China, and the US are each evolving distinct regulatory systems
that vary in approach and emphasis. The EU AI Act proposes a coherent, uni-
versal, risk-based regulatory framework with strict and well-defined penalties.
It is criticized, however, for stifling innovation, using ambiguous language, and
not anticipating expected challenges in implementation across heterogeneous use
cases. The Chinese approach to AI regulation synthesizes the US approach of
use-case specific laws with general guidelines translated into a centralized and
comprehensive registration, testing, and monitoring framework. At the same
time, innovation and economic growth is directly and indirectly supported by
initiatives like investment in thousands of ‘Little Dragons’ alongside relatively
lax enforcement for SMEs. This hybrid approach has led to a variety of surpris-
ing technological breakthroughs and economic successes, but it risks criticism
of capriciousness given that regulations are not uniformly applied or enforced.
The Biden White House Executive Order on “Safe, Secure, and Trustworthy
Development and Use of Artificial Intelligence” is the most organized plan in
the US. It delegates over one hundred specific tasks to over fifty federal agencies
in order to build out AI expertise and oversight according to specific domain
expertise. The decentralized US approach also involves smaller regulatory initia-
tives by the US Congress, individual states like California, and even cities. This
reflects the US market-driven approach acknowledging competing stakeholders.
The approach has come under criticism, however, for relying too heavily on
self-regulation and for being susceptible to flaws like regulatory capture. In re-
sponse, California, home to most of the leading AI companies, introduced what
is arguably the most stringent regulation. After ten major revisions, Governor
Newsom vetoed the bill.
Growing trade tensions and geopolitical competition between the US and
China are bolstering arguments for AI regulation policies favoring faster inno-
vation and technological independence aligned with industrial policy. The US,
with China following suite, has increased tariffs, coordinated international ex-
port bans, and imposed sanctions on strategic technologies like EVs, advanced
chips, and semiconductor manufacturing equipment.
These geopolitical ten-
sions mean that the regulatory landscape will continue to evolve as countries
re-evaluate their stance towards risk alongside their desire to remain at the
forefront of AI development.
8
Contributions
• Jon Chun: The United States and China
• Christian Schroeder de Witt: The European Union
• Katherine Elkins: The United States
Each author has reviewed each other’s section and takes responsibility for the
content of their own.
26

References
A. Abbott.
Coalition letter opposing california sb 1047, jun 2024.
URL
https://laweconcenter.org/resources/coalition-letter-opposing-
california-sb-1047/. Accessed: 2024-09-17.
L. Abboud and J. Espinoza.
EU’s new AI Act risks hampering innovation,
warns Emmanuel Macron. Financial Times, Dec. 2023. URL https://www.
ft.com/content/9339d104-7b0c-42b8-9316-72226dd4e4c0.
M. Almada and A. Radu.
The Brussels Side-Effect:
How the AI Act
Can Reduce the Global Reach of EU Policy.
German Law Journal,
pages 1–18, Feb. 2024.
ISSN 2071-8322.
doi:
10.1017/glj.2023.108.
URL
https://www.cambridge.org/core/journals/german-law-
journal/article/brussels-sideeffect-how-the-ai-act-can-reduce-
the-global-reach-of-eu-policy/032C72AEC537EBB6AE96C0FD90387E3E.
S. M. Anstey and M. J. Breslin. Proposed california ai law sb 1047 – an overview
for developers, 2024. URL https://ktslaw.com/en/insights/alert/2024/
9/{468C5A1A-3410-4E0F-892F-83EA3602EF61}?pdf=1. Accessed: 2024-09-
16.
Bloomberg News. In its latest crackdown, china intensifies focus on real estate.
Aljazeera.com, July 2021.
URL https://www.aljazeera.com/economy/
2021/7/28/in-its-latest-crackdown-china-intensifies-focus-on-
real-estate. Accessed: May 2, 2024.
A. Bradford. The Brussels Effect: How the European Union Rules the World.
Faculty Books, Mar. 2020. doi: https://doi.org/10.1093/oso/9780190088583.
001.0001. URL https://scholarship.law.columbia.edu/books/232.
Caixin Global. Full text: Xi jinping’s speech on boosting common prosperity.
Caixin Global, October 2021. URL https://www.caixinglobal.com/2021-
10-19/full-text-xi-jinpings-speech-on-boosting-common-
prosperity-101788302.html. Accessed: May 2, 2024.
R. P. Casey. Stop spying bosses act, 2023. URL https://www.congress.gov/
bill/118th-congress/senate-bill/262/text.
Chatham
House.
The
EU’s
new
AI
Act
could
have
global
impact
|
Chatham
House
–
International
Affairs
Think
Tank,
Mar.
2024.
URL https://www.chathamhouse.org/2024/03/eus-new-ai-act-could-
have-global-impact.
L. Y. Chen and L. Liu.
China ends tech crackdown with fines on tencent,
ant group. Bloomberg.com, July 2023. URL https://www.envoy.cirrus.
bloomberg.com/news/articles/2023-07-07/china-ends-probe-of-
jack-ma-backed-ant-with-984-million-fine?srnd=premium.
Accessed:
May 2, 2024.
27

N. Chilson and K. Stout.
Coalition letter opposing california sb 1047, jun
2024. URL https://laweconcenter.org/resources/coalition-letter-
opposing-california-sb-1047/. Accessed: 2024-06-20.
China Money Network.
Chinese tech giants dominate ai algorithms with
a focus on industry-specific applications.
China Money Network, March
2024. URL https://www.chinamoneynetwork.com/2024/03/07/chinese-
tech-giants-dominate-ai-algorithms-with-a-focus-on-industry-
specific-applications. Accessed: May 2, 2024.
ChinaTalk. Hugging face blocked! ’self-castrating’ china’s ml development +
jordan at apec. ChinaTalk, October 2023. URL https://www.chinatalk.
media/p/hugging-face-blocked-self-castrating.
Accessed:
May 2,
2024.
cmswire2024. Is california’s sb-1047 the future of ai regulation?, 2024. URL
https://www.cmswire.com/digital-experience/is-california-sb-
1047-the-future-of-ai-regulation/. Accessed: 2024-09-18.
Congressional Research Service. The made in china 2025 initiative: Economic
implications for the united states, April 2019. URL https://crsreports.
congress.gov/product/pdf/IF/IF10964/4. Accessed: May 2, 2024.
Congressional Research Service. Highlights of the 2023 executive order on arti-
ficial intelligence for congress, 2024. URL https://crsreports.congress.
gov/product/pdf/R/R47843/8. Accessed: May 2, 2024.
Consilium.
Artificial
intelligence
act:
Council
and
Parliament
strike
a deal on the first rules for AI in the world,
2023.
URL https:
//www.consilium.europa.eu/en/press/press-releases/2023/12/09/
artificial-intelligence-act-council-and-parliament-strike-a-
deal-on-the-first-worldwide-rules-for-ai/.
C. Coons, M. Blackburn, A. Klobuchar, and T. Tillis.
No fakes act,
2023.
URL https://www.coons.senate.gov/imo/media/doc/no_fakes_
act_one_pager.pdf.
M. A. Cusumano,
A. Gawer,
and D. B. Yoffie.
Social media com-
panies should self-regulate. now.
Harvard Business Review,
January
2021. URL https://hbr.org/2021/01/social-media-companies-should-
self-regulate-now.
F. Eiras, A. Petrov, B. Vidgen, C. S. de Witt, F. Pizzati, K. Elkins,
S. Mukhopadhyay, A. Bibi, B. Csaba, F. Steibel, F. Barez, G. Smith,
G. Guadagni, J. Chun, J. Cabot, J. M. Imperial, J. A. Nolazco-Flores, L. Lan-
day, M. Jackson, P. R¨ottger, P. H. S. Torr, T. Darrell, Y. S. Lee, and J. Foer-
ster. Near to Mid-term Risks and Opportunities of Open-Source Generative
AI, May 2024a. URL http://arxiv.org/abs/2404.17047. arXiv:2404.17047
[cs].
28

F. Eiras,
A. Petrov,
B. Vidgen,
C. Schroeder,
F. Pizzati,
K. Elkins,
S. Mukhopadhyay, A. Bibi, A. Purewal, C. Botos, F. Steibel, F. Keshtkar,
F. Barez, G. Smith, G. Guadagni, J. Chun, J. Cabot, J. Imperial, J. A.
Nolazco, L. Landay, M. Jackson, P. H. S. Torr, T. Darrell, Y. Lee, and J. Fo-
erster. Risks and Opportunities of Open-Source Generative AI, May 2024b.
URL http://arxiv.org/abs/2405.08597.
Environmental Protection Agency. About page, our mission and what we do,
2024. URL https://www.epa.gov/aboutepa/our-mission-and-what-we-
do. Accessed: July 16, 2024.
EU AI Act. Why work at the EU AI Office? | EU Artificial Intelligence Act,
2024. URL https://artificialintelligenceact.eu/why-work-at-the-
eu-ai-office/.
euronews2024. A big win for the eu - how california’s ai legislation compares to
the eu ai act, 2024. URL https://www.euronews.com/next/2024/09/11/a-
big-win-for-the-eu-how-californias-ai-legislation-compares-to-
the-eu-ai-act. Accessed: 2024-09-18.
European Commission. European AI Office | Shaping Europe’s digital future,
2024. URL https://digital-strategy.ec.europa.eu/en/policies/ai-
office.
European Union. Regulation (eu) 2016/679 of the european parliament and of
the council of 27 april 2016 on the protection of natural persons with regard
to the processing of personal data and on the free movement of such data
(general data protection regulation), article 7, 2016.
URL https://eur-
lex.europa.eu/eli/reg/2016/679/oj. Accessed: 2024-09-08.
European Union. Directive (eu) 2019/790 of the european parliament and of the
council of 17 april 2019 on copyright and related rights in the digital single
market and amending directives 96/9/ec and 2001/29/ec, 2019. URL https:
//eur-lex.europa.eu/eli/dir/2019/790/oj. Accessed: 2024-09-08.
European Union. Regulation (eu) 2024/123 of the european parliament and of
the council of 21 may 2024 laying down harmonised rules on artificial intelli-
gence (artificial intelligence act), 2024. URL https://eur-lex.europa.eu/
legal-content/EN/TXT/?uri=CELEX:52021PC0206. Accessed: 2024-09-08.
Foley and Lardner LLP.
California dreamin’:
Sb 1047 and ai innovation,
2024.
URL https://www.foley.com/insights/publications/2024/07/
california-dreamin-sb-1047-ai-innovation/. Accessed: 2024-09-16.
GDPR Local.
California’s senate bill 1047:
Key takeaways on california’s
ai safety bill, 2024. URL https://gdprlocal.com/californias-senate-
bill-1047-key-takeaways-on-californias-ai-safety-bill/. Accessed:
2024-09-16.
29

Global Times. China to develop 10,000 ’little giants’ in push for advanced man-
ufacturing. GlobalTimes.cn, July 2021. URL https://www.globaltimes.
cn/page/202107/1227877.shtml. Accessed: May 2, 2024.
GovTrack.us. Govtrack.us, 2024. URL https://www.govtrack.us/. Accessed:
16 Sept. 2024.
S. Gracias. Comparing eu ai act to proposed ai-related legislation in the us.
University of Chicago Business Law Review, 2024.
Huggingface.co. Models, May 2024. URL https://huggingface.co/models.
Accessed: May 2, 2024.
Information Technology and Innovation Foundation (ITIF). How innovative is
china in ai? ITIF, 2024. URL https://itif.org/publications/2024/08/
26/how-innovative-is-china-in-ai/. Accessed: 2024-09-23.
International Association of Privacy Professionals. Us state ai governance leg-
islation tracker, 2024.
URL https://iapp.org/resources/article/us-
state-ai-governance-legislation-tracker/. Accessed: 16 Sept. 2024.
International Monetary Fund.
World economic outlook:
April 2024, April
2024. URL https://meetings.imf.org/en/IMF/Home/Publications/WEO/
Issues/2024/04/16/world-economic-outlook-april-2024.
Accessed:
May 2, 2024.
G.
Intresse.
China’s
new
draft
regulations
for
after-school
tutor-
ing.
China-Briefing.com, February 2024.
URL https://www.china-
briefing.com/news/china-after-school-tutoring-new-draft-
regulations-key-points/. Accessed: May 2, 2024.
A. Klobuchar.
Real political advertisements act, 2023.
URL https://www.
congress.gov/bill/118th-congress/senate-bill/1596/text.
LAION. A Call to Protect Open-Source AI in Europe | LAION, 2023. URL
https://laion.ai/notes/letter-to-the-eu-parliament.
LegiScan. California senate bill 1047: Safe and secure innovation for frontier
Artificial Intelligence models act, 2024. URL https://legiscan.com/CA/
text/SB1047/2023. Accessed: May 1, 2024.
Linklaters.
Data
Protected
Philippines|
Insights
|
Linklaters,
2024.
URL https://www.linklaters.com/en/insights/data-protected/data-
protected---philippines.
G. Lovely. Sag-aftra and women’s groups urge gavin newsom to sign ai safety bill,
sep 2024.
URL https://www.theverge.com/2024/9/11/24242142/sag-
aftra-ai-now-gavin-newsom-safety-sb-1047-letters. Accessed: 2024-
09-18.
30

T. Madiega. Artificial intelligence act, 2024. URL https://www.europarl.
europa.eu/RegData/etudes/BRIE/2021/698792/EPRS_BRI(2021)698792_
EN.pdf.
A. Massoglia.
State and federal lobbying spending tops $46 billion after
federal lobbying spending broke records in 2023.
OpenSecrets.com, Jan-
uary 2024.
URL https://www.opensecrets.org/news/2024/01/state-
and-federal-lobbying-spending-tops-46-billion-after-federal-
lobbying-spending-broke-records-in-2023.
M. Minow and N. Minow.
Social media companies should pursue serious
self-supervision— soon: Response to professors douek and kadri. Harvard
Law Review, June 2023. URL https://harvardlawreview.org/forum/vol-
136/social-media-companies-should-pursue-serious-self-
supervision-soon-response-to-professors-douek-and-kadri/.
Morgan
Lewis.
California’s
sb
1047
would
impose
new
safety
re-
quirements
for
developers
of
large-scale
ai
models,
2024.
URL
https://www.morganlewis.com/pubs/2024/08/californias-sb-1047-
would-impose-new-safety-requirements-for-developers-of-large-
scale-ai-models. Accessed: 2024-09-16.
National
Conference
of
State
Legislatures.
Ai
2024
legislation,
June
2023.
URL
https://www.ncsl.org/technology-and-communication/
artificial-intelligence-2024-legislation. Accessed: July 12, 2024.
National People’s Congress of the People’s Republic of China. Cybersecurity
law of the people’s republic of china, November 2016. URL https://www.
cac.gov.cn/2016-11/07/c_1119867116.htm. Adopted at the 24th Meeting
of the Standing Committee of the Twelfth National People’s Congress of the
People’s Republic of China.
National Science Foundation. About, 2024. URL https://new.nsf.gov/about.
Accessed: July 16, 2024.
Neontri. California senate bill 1047, 2024. URL https://neontri.com/blog/
california-senate-bill-1047/. Accessed: 2024-09-16.
G. Newsom.
Office of the governor,
2024a.
URL https://www.gov.
ca.gov/2024/09/29/governor-newsom-announces-new-initiatives-
to-advance-safe-and-responsible-ai-protect-californians/#:
~:text=What%20you%20need%20to%20know:%20Governor%20Newsom%
20announced%20that%20the. Accessed: 2024-09-23.
G. Newsom.
Office of the governor, 2024b.
URL https://www.gov.ca.
gov/wp-content/uploads/2024/09/SB-1047-Veto-Message.pdf#:~:
text=I%20am%20returning%20Senate%20Bill%201047%20without%20my%
20signature.%20This. Accessed: 2024-09-23.
31

NIST. About, 2024a. URL https://www.nist.gov/about-nist. Accessed:
July 16, 2024.
NIST. Ai risk management framework, 2024b. URL https://www.nist.gov/
itl/ai-risk-management-framework. Accessed: July 16, 2024.
NIST. Ai safety institute and european ai office hold technical dialogue, July
2024c.
URL
https://www.nist.gov/news-events/news/2024/07/us-
ai-safety-institute-and-european-ai-office-hold-technical-
dialogue. Accessed: July 16, 2024.
M.
Nunez.
Ai
safety
showdown:
Yann
lecun
slams
california’s
sb
1047
as
geoffrey
hinton
backs
new
regulations,
sep
2024.
URL
https://venturebeat.com/ai/ai-safety-showdown-yann-lecun-slams-
californias-sb-1047-as-geoffrey-hinton-backs-new-regulations/.
Accessed: 2024-09-18.
OECD. OECD Principles on AI, 2019. URL https://www.oecd.org/going-
digital/ai/principles/. Accessed: 2024-09-08.
R. of the Philippines. Republic act no. 10173: Data privacy act of 2012. https:
//www.privacy.gov.ph/data-privacy-act/, 2012. Enacted on August 15,
2012.
Office
of
Senator
Richard
Blumenthal.
Blumenthal
&
hawley
an-
nounce bipartisan framework on artificial intelligence legislation, April
2024.
URL
https://www.blumenthal.senate.gov/newsroom/press/
release/blumenthal-and-hawley-announce-bipartisan-framework-on-
artificial-intelligence-legislation. Accessed: May 2, 2024.
E. Parliament and C. of the European Union. Regulation (eu) 2022/1925 of the
european parliament and of the council of 14 september 2022 on contestable
and fair markets in the digital sector (digital markets act). https://eur-
lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R1925, 2022.
Official Journal of the European Union, L 265/1, 12 October 2022.
Perkins and Coie. States begin to regulate ai in the absence of regulation, May
2024.
URL https://www.perkinscoie.com/en/news-insights/states-
begin-to-regulate-ai-in-absence-of-federal-legislation.html. Ac-
cessed: July 16, 2024.
B. Perrigo.
Exclusive:
OpenAI Lobbied E.U. to Water Down AI Regula-
tion, June 2023. URL https://time.com/6288245/openai-eu-lobbying-
ai-act/.
G. Sartor and F. Lagioia. The impact of the general data protection regulation
(gdpr) on artificial intelligence. Study PE 641.530, European Parliamentary
Research Service (EPRS), 2020. URL https://www.europarl.europa.eu/
32

RegData/etudes/STUD/2020/641530/EPRS_STU(2020)641530_EN.pdf. Sci-
entific Foresight Unit (STOA), Panel for the Future of Science and Technol-
ogy.
C. Schumer. Sen. chuck schumer launches safe innovation in the ai age at csis,
June 2023. URL https://www.csis.org/analysis/sen-chuck-schumer-
launches-safe-innovation-ai-age-csis. Accessed: May 1, 2024.
Security and Exchange Commission. About and mission, 2024. URL https:
//www.sec.gov/about/mission. Accessed: July 16, 2024.
M. Sheehan.
Tracing the roots of china’s ai regulations.
Carnegie
Endowment
for
International
Peace,
February
2024.
URL
https:
//carnegieendowment.org/2024/02/27/tracing-roots-of-china-s-
ai-regulations-pub-91815. Accessed: May 2, 2024.
smdailyjournal.
Deep
dive
into
sb-1047,
2024.
URL
https:
//www.smdailyjournal.com/opinion/columnists/deep-dive-into-sb-
1047/article_fb548bf2-278c-11ef-8307-a72b52b6e079.html. Accessed:
2024-09-16.
S. Smit et al.
Addressing the european technology gap.
McKinsey &
Company,
2022.
URL
https://www.mckinsey.com/capabilities/
strategy-and-corporate-finance/our-insights/securing-europes-
competitiveness-addressing-its-technology-gap.
Accessed: 2024-09-
22.
K.
Suominen.
On
the
rise:
Europe’s
competition
policy
challenges
to
technology
companies.
Center
for
Strategic
and
International
Studies
(CSIS),
2020.
URL
https://www.csis.org/analysis/rise-
europes-competition-policy-challenges-technology-companies.
Ac-
cessed: 2024-09-22.
The Hill.
Ai employees support california ai bill.
The Hill,
2024.
URL https://thehill.com/policy/technology/4869225-ai-employees-
support-california-ai-bill/. Accessed: 2024-01-15.
The Privacy Advisor Podcast.
The Privacy Advisor Podcast:
Inside
the EU AI Act negotiations:
A discussion with Laura Caroli, 2024.
URL https://privacyadvisorpodcast.libsyn.com/inside-the-eu-ai-
act-negotiations-a-discussion-with-laura-caroli.
The State Council of the People’s Republic of China. Made in china 2025, 2015.
URL https://english.www.gov.cn/2016special/madeinchina2025/. Ac-
cessed: May 2, 2024.
The Verge.
California’s sb-1047 ai industry regulation faces backlash, 2024.
URL
https://www.theverge.com/2024/9/11/24226251/california-sb-
1047-ai-industry-regulation-backlash. Accessed: 2024-09-16.
33

The White House. Blueprint for an ai bill of rights, October 2022. URL https:
//www.whitehouse.gov/ostp/ai-bill-of-rights/. Accessed: 2024-05-02.
The White House. Fact sheet: Biden-harris administration secures voluntary
commitments from leading artificial intelligence companies to manage
the risks posed by ai,
July 2023a.
URL https://www.whitehouse.
gov/briefing-room/statements-releases/2023/07/21/fact-sheet-
biden-harris-administration-secures-voluntary-commitments-from-
leading-artificial-intelligence-companies-to-manage-the-risks-
posed-by-ai/. Accessed: 2024-05-02.
The White House.
Executive order on the safe, secure, and trustwor-
thy
development
and
use
of
artificial
intelligence,
October
2023b.
URL
https://www.whitehouse.gov/briefing-room/presidential-
actions/2023/10/30/executive-order-on-the-safe-secure-and-
trustworthy-development-and-use-of-artificial-intelligence/.
Accessed: 2024-09-25.
The White House. Potential labor market impacts of artificial intelligence: An
empirical analysis, July 2024a.
URL https://www.whitehouse.gov/wp-
content/uploads/2024/07/Potential-Labor-Market-Impacts-of-
Artificial-Intelligence-An-Empirical-Analysis-July-2024.pdf.
Accessed: 2024-09-25.
The White House. Administration actions on ai, March 2024b. URL https:
//ai.gov/actions/. Accessed: 2024-09-25.
The White House.
Biden-harris administration announces key ai actions
180 days following president biden’s landmark executive order,
April
2024c.
URL https://www.whitehouse.gov/briefing-room/statements-
releases/2024/04/29/biden-harris-administration-announces-
key-ai-actions-180-days-following-president-bidens-landmark-
executive-order/. Accessed: 2024-05-02.
The White House.
Fact sheet: Biden-harris administration announces new
ai actions and receives additional major voluntary commitment on ai, July
2024d. URL https://www.whitehouse.gov/briefing-room/statements-
releases/2024/07/26/fact-sheet-biden-harris-administration-
announces-new-ai-actions-and-receives-additional-major-
voluntary-commitment-on-ai/. Accessed: 2024-09-25.
J. Tyrangiel.
Opinion | I found the smartest politician on AI. It’s
no one you’d expect.
Washington Post,
Mar. 2024.
ISSN 0190-
8286. URL https://www.washingtonpost.com/opinions/2024/03/20/ai-
europe-regulation-leading/.
UN AI Advisory Body.
Governing ai for humanity,
September 2024.
URL https://www.un.org/sites/un2.un.org/files/governing_ai_for_
humanity_final_report_en.pdf. Accessed: 2024-09-18.
34

D. Walters and H. J. Wiseman.
Self-regulation in the cradle: The role of
standards in emerging industries.
SSRN Electronic Journal, 2022.
doi:
10.2139/ssrn.4226081.
Z. Warso, M. Gahntz, and P. Keller.
Sufficiently detailed?
a proposal for
implementing the ai act’s training data transparency requirement for gpai,
June 2024. URL https://openfuture.eu/wp-content/uploads/2024/06/
240618AIAtransparency_template_requirements-2.pdf.
This report is
published under the terms of the Creative Commons Attribution License.
G. Webster, J. Zhou, M. Shi, H. Dorwart, J. Costigan, and Q. Chen.
Forum:
Analyzing
an
expert
proposal
for
china’s
artificial
intelli-
gence
law.
DigiChina,
Stanford
University,
August
2023.
URL
https://digichina.stanford.edu/work/forum-analyzing-an-expert-
proposal-for-chinas-artificial-intelligence-law/.
Accessed: May
2, 2024.
White and Case.
Ai watch global regulatory tracker us, 2024.
URL
https://www.whitecase.com/insight-our-thinking/ai-watch-global-
regulatory-tracker-united-states. Accessed: 2024-09-25.
Z. Yang.
Why the chinese government is sparing ai from harsh reg-
ulations—for
now.
MIT
Technology
Review,
April
2024.
URL
https://www.technologyreview.com/2024/04/09/1091004/china-tech-
regulation-harsh-zhang/. Accessed: May 2, 2024.
A. Zhang. High Wire: How China Regulates Big Tech and Governs Its Economy.
Oxford University Press, 2022.
A. H. Zhang. How china regulates big tech and governs ai, March 2024. URL
https://www.youtube.com/watch?v=NS1DGd2IXDs. Philip K.H. Wong Cen-
tre for Chinese Law [Video]. YouTube. Accessed: May 2, 2024.
35

Appendix A: Sample of Diverse Supporters and
Opponents of California SB 1047
Side
Category
Name
Description
Pro
Politician
Sen.
Anthony
Wiener
https://tinyurl.com/4ub8u7ha
Pro
Academics
Yoshua
Bengio,
Geoffrey Hinton,
Lawrence Lessig,
Stuart Russell
https://safesecureai.org/
experts
Pro
Academic
Dan Hendrycks
https://tinyurl.com/ytn7vcfr
Pro
AI Researchers
Call to Lead
https://calltolead.org/
Pro
AI Non-Profit
Center
for
AI
Safety
https://www.safe.ai/work/
statement-on-ai-risk
Pro
AI
Frontier
Corp
OpenAI
https://tinyurl.com/2s42ndr5
Pro
AI
Frontier
Corp
Anthropic
https://tinyurl.com/yth2k2hn
Pro
Hollywood
Actors
and
Unions
https://tinyurl.com/4ad85wzu
Pro
Entrepreneur
Elon Musk
https://x.com/elonmusk/
status/1828205685386936567
Con
Politician
Sen.
Nancy
Pelosi
https://tinyurl.com/y25yrre9
Con
Politician
Rep. Ro Khanna
https://tinyurl.com/3sz3jwns
Con
Politician
SF Mayor Lon-
don Breed
https://tinyurl.com/3664wwua
Con
Academic
Yan LeCun
https://x.com/ylecun/status/
1807552057466909156
Con
Academic
Fei-Fei Li
https://tinyurl.com/4b9uzctb
Con
Academics
CalTech
https://tinyurl.com/2xf6xcw5
Con
AI
Frontier
Corp
Meta
https://tinyurl.com/y2sus9xp
Con
AI
Frontier
Corp
Google
https://tinyurl.com/adseybwp
Con
AI Non-Profit
The AI Alliance
https://thealliance.ai/core-
projects/sb1047
Con
Thought Lead-
ers
Investors,
En-
trepeneurs
and
Academics
https://tinyurl.com/26h9f397
Table 1: Split among leading voices on California SB 1047 does not
follow traditional dividing lines
36
