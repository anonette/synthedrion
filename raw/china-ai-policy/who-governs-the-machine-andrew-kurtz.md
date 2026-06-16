# WHO GOVERNS THE MACHINE?

> Extracted from: `Who Governs the machine_Andrew Kurtz.pdf`

WHO GOVERNS THE MACHINE?
A Machine Identity Governance Taxonomy (MIGT) for AI Systems
Operating Across Enterprise and Geopolitical Boundaries
Andrew Kurtz, CISSP
andrewkurtz@acm.org
Klaudia Krawiecka, PhD
kkrawiecka@acm.org
April 8, 2026
arXiv:2604.06148v1  [cs.CR]  7 Apr 2026

Kurtz & Krawiecka (2026)
Who Governs the Machine?
1
Abstract
The governance of artificial intelligence has a blind spot: the machine identities that
AI systems use to act. AI agents, service accounts, API tokens, and automated workflows
now outnumber human identities in enterprise environments by ratios exceeding 80
to 1 [1], yet no integrated framework exists to govern them. The consequences are
measurable: a single ungoverned automated agent produced $5.4 to $10 billion in losses
in the 2024 CrowdStrike outage, and nation-state actors including Silk Typhoon and
Salt Typhoon have operationalized ungoverned machine credentials as primary vectors
for espionage against critical infrastructure. At the same time, three major jurisdictions-
the European Union, the United States, and China-are developing fundamentally
incompatible AI governance frameworks, creating cross-jurisdictional conflicts that no
existing enterprise governance program is equipped to navigate.
There are four original contributions to the emerging field of AI identity governance
within. First, it proposes the AI-Identity Risk Taxonomy (AIRT), a comprehensive
enumeration of risks arising specifically at the intersection of AI systems and enter-
prise identity governance, comprising 37 risk sub-categories across eight domains, each
grounded in documented incidents, regulatory recognition, practitioner prevalence data,
and threat intelligence. Second, it introduces the Machine Identity Governance Tax-
onomy (MIGT), an integrated governance framework organized across six domains
that simultaneously addresses the technical governance gap, the regulatory compliance
gap, and the cross-jurisdictional coordination gap that existing frameworks address
only in isolation. Third, it presents the foreign state actor threat model for enterprise
identity governance, establishing that Silk Typhoon, Salt Typhoon, Volt Typhoon, and
North Korean AI-enhanced identity fraud operations have already operationalized AI
identity vulnerabilities as active attack vectors requiring governance responses that no
existing IAM framework provides. Fourth, it proposes the cross-jurisdictional regulatory
alignment structure mapping enterprise AI identity governance obligations under EU,
U.S., and Chinese frameworks simultaneously, identifying irreconcilable conflicts and
providing a governance mechanism for managing them at the enterprise program level.
A four-phase implementation roadmap translates the MIGT’s six governance domains
into actionable enterprise programs. The paper is addressed to policy makers, regulators,
and practitioners operating at the intersection of AI governance, cybersecurity, and
geopolitical risk.
Keywords: machine identity governance, AI identity security, non-human identity,
agentic AI, identity and access management, geopolitical AI risk, cross-jurisdictional
governance, AI risk taxonomy, MIGT, AIRT

Kurtz & Krawiecka (2026)
Who Governs the Machine?
2
Glossary of Key Terms
The following terms are used throughout the paper. Definitions are provided to support
readers from policy, regulatory, and practitioner backgrounds who may not be familiar with
all domains addressed.
Agentic AI. An artificial intelligence system capable of autonomous perception, decision-
making, and action within an environment, often executing multi-step tasks without
continuous human direction. Agentic AI systems differ from earlier generative AI
systems in that they act, not merely respond. For the purposes of this paper, that
distinction carries specific governance weight: agentic AI systems acquire and exercise
access rights, consume and produce enterprise data, invoke tools and external services,
delegate authority to subordinate agents, and accumulate de facto privileges across
systems in ways that no prior generation of software required identity governance
frameworks to address.
The multidimensional operational profile of an agentic AI system comprises four an-
alytically distinct capabilities, each of which creates a distinct identity governance
surface. First, tool invocation: agentic AI systems call external APIs, execute code,
query databases, trigger workflows, and interact with enterprise applications through
programmatic interfaces that carry real access authority. Each tool invocation represents
an authenticated action performed under the agent’s identity and within the scope
of its provisioned credentials, making tool usage a primary vector for both privilege
abuse and exfiltration. Second, multi-step autonomous execution: unlike a generative
AI system that responds to a single prompt and terminates, an agentic AI system
plans and executes sequences of actions across time, accumulating context, state, and
effective access across each step without necessarily returning to human oversight be-
tween them. The governance challenge this creates is not merely one of endpoint access
control but of behavioral trajectory: the aggregate effect of individually authorized
steps may produce outcomes that no single authorization decision contemplated or
approved. Third, agent-to-agent delegation: agentic AI systems increasingly operate
within multi-agent architectures, spawning subagents, delegating subtasks to specialized
agents, and passing instructions and credentials through agent chains whose trust
relationships are rarely cryptographically verified and whose accountability structures
are rarely explicitly assigned. Each delegation boundary is a potential accountability
gap and a potential privilege escalation surface. Fourth, environmental interaction
and memory: agentic AI systems read from and write to persistent storage, ingest
content from documents, emails, databases, and web pages, and in some architectures

Kurtz & Krawiecka (2026)
Who Governs the Machine?
3
maintain memory across sessions. Each of these interactions creates a pathway for
indirect prompt injection, unauthorized data aggregation, and cross-session privilege
accumulation that static access governance models are structurally unable to detect.
Taken together, these four capabilities mean that an agentic AI system is not a
passive computational resource but an active, identity-bearing enterprise actor whose
access footprint, behavioral trajectory, and accountability structure require governance
disciplines equivalent to, and in several respects more demanding than, those applied
to privileged human users.
AIRT (AI-Identity Risk Taxonomy). The AI-Identity Risk Taxonomy proposed in Sec-
tion 5. A two-level classification of 37 risk sub-categories across eight domains, com-
prising comprehensive enumeration of risks arising specifically at the intersection of AI
systems and enterprise identity governance.
API Key. An Application Programming Interface key. A static credential used to authen-
ticate a software system or AI agent to an external service. API keys are a primary
target of state-sponsored credential theft operations because they provide persistent,
often broad access to enterprise systems and AI infrastructure.
ARIA (Agent Relationship-Based Identity and Authorization). A governance model
that records every agent-to-agent delegation as a distinct, cryptographically verifiable
relationship in a governance graph, enabling fine-grained accountability across complex
multi-agent workflows.
ATF (Agentic Trust Framework). The Agentic Trust Framework published by the Cloud
Security Alliance in February 2026. A zero-trust governance framework for AI agents
that introduces a four-maturity-level model in which agent autonomy is earned through
demonstrated trustworthiness rather than granted as a binary condition.
CAC (Cyberspace Administration of China). The primary Chinese government regu-
latory body responsible for internet content governance, cybersecurity oversight, and
AI algorithm regulation, including administration of China’s algorithm filing regime.
CSL (Cybersecurity Law). China’s foundational cybersecurity statute, originally enacted
in 2017 and significantly amended effective January 1, 2026, to incorporate dedicated
AI compliance provisions and expanded extraterritorial reach.
DID (Decentralized Identifier). A W3C standard for a globally unique, cryptographically
verifiable identifier that does not require a centralized registration authority. DIDs are

Kurtz & Krawiecka (2026)
Who Governs the Machine?
4
proposed as a foundation for AI agent identity because they enable agents to prove their
identity and provenance to relying systems without dependence on a single identity
provider.
EU AI Act. The European Union’s Artificial Intelligence Act, which entered into force on
August 1, 2024 and is the world’s first comprehensive binding AI regulation. It classifies
AI systems by risk level and imposes obligations proportional to risk, with the most
significant high-risk AI system requirements taking effect on August 2, 2026.
GPAI (General-Purpose AI Model). Under the EU AI Act, a foundation model trained
on broad data at scale that can perform a wide range of tasks. GPAI models are
subject to specific obligations under Articles 53 and 55 of the Act, including technical
documentation, copyright compliance, and training data transparency requirements.
IAM (Identity and Access Management). The discipline and set of technical systems
responsible for managing digital identities and controlling access to enterprise resources.
Traditional IAM frameworks were designed primarily for human user identities and are
structurally inadequate for the governance of AI agent identities.
JIT (Just-in-Time) Provisioning. An access governance approach in which access rights
are granted at the moment they are needed for a specific task and automatically revoked
upon task completion, rather than being pre-assigned as standing entitlements. JIT
provisioning eliminates standing privilege and directly addresses the Dynamic Access
Requirement Mismatch risk in AIRT Domain II.
MCP (Model Context Protocol). An emerging standard for AI agent-to-application
connectivity that enables AI agents to retrieve data, trigger workflows, and act within
enterprise systems. MCP connections carry real access authority and represent an
emerging identity governance surface addressed in Section 8.4 as a future research
direction.
A2A (Agent-to-Agent Protocol). An open protocol developed by Google and published
in April 2025 that enables communication, task delegation, and capability discovery
between AI agents operating across heterogeneous frameworks and organizational
boundaries.
Where MCP governs how an individual agent connects to tools and
data sources, A2A governs how agents find, authenticate, and coordinate with one
another. Each agent publishes an Agent Card, a structured JSON manifest declaring its
capabilities, supported modalities, and authentication requirements, which peer agents
and orchestration systems use to determine whether and how to delegate tasks. For the

Kurtz & Krawiecka (2026)
Who Governs the Machine?
5
purposes of this paper, A2A is a primary emerging identity governance surface: agent-
to-agent delegation relationships established through A2A carry real access authority,
cross organizational and trust boundaries, and currently lack the cryptographically
verifiable accountability structures that the MIGT’s Domain II and Domain IV controls
require.
MIGT (Machine Identity Governance Taxonomy). The Machine Identity Governance
Taxonomy proposed in Section 6. A six-domain integrated governance framework
addressing the technical governance gap, the regulatory compliance gap, and the
cross-jurisdictional coordination gap simultaneously. The MIGT provides governance
capabilities, controls, and accountability mechanisms for enterprise AI identity programs.
NCCoE (National Cybersecurity Center of Excellence). A division of NIST that de-
velops practical, standards-based cybersecurity solutions. The NCCoE initiated a
project specifically addressing software and AI agent identity and authorization in
2026, signaling that authoritative U.S. standards for AI agent identity governance are
forthcoming.
NHI (Non-Human Identity). Any digital identity that is not associated with a human
user. NHIs include AI agents, service accounts, API tokens, OAuth clients, automated
workflows, and device identities. NHIs now outnumber human identities in enterprise
environments by ratios as high as 144 to 1.
NIST AI RMF. The NIST Artificial Intelligence Risk Management Framework (AI RMF
1.0), published in 2023. The de facto operational standard for AI governance in the
United States, establishing the GOVERN, MAP, MEASURE, and MANAGE functions.
The AI RMF provides governance function structure but does not enumerate identity-
specific AI risks-the gap the AIRT is designed to fill.
PAM (Privileged Access Management). A category of identity security tools and prac-
tices focused on managing, monitoring, and auditing access by privileged accounts,
including administrator accounts, service accounts, and high-privilege machine identities.
PAM provider credentials have been identified as a primary target of the Silk Typhoon
state-sponsored espionage campaign.
SPIFFE / SPIRE. Secure Production Identity Framework for Everyone (SPIFFE) is a
CNCF graduated standard for cryptographic workload identity. SPIRE is its reference
implementation. SPIFFE provides cryptographically verifiable identities tied to work-

loads rather than people, making it the recommended cryptographic identity standard
for AI agent deployments in enterprise environments.
ZSP (Zero Standing Privilege). An access governance principle under which AI agents
and other machine identities never possess a credential or access right at rest. Access
is granted just-in-time for specific tasks and automatically revoked upon completion.
ZSP is the target architecture for MIGT Domain II and directly addresses the Static
Credential Persistence risk in AIRT Domain I.
Contents
1
Introduction: The Governance Vacuum at the Intersection of AI and
Identity
9
1.1
The Scope and Urgency of the Problem . . . . . . . . . . . . . . . . . . . . .
11
1.2
Why Existing Frameworks Are Insufficient: Five Structural Gaps . . . . . . .
12
1.3
Contributions: Four Original Claims
. . . . . . . . . . . . . . . . . . . . . .
16
1.4
Paper Organization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17
2
The Empirical Foundation: Scale, Consequences, and Structural Charac-
teristics of the Non-Human Identity Governance Problem
18
2.1
The Quantitative Scale of Machine Identity Proliferation . . . . . . . . . . .
18
2.2
Operational Consequences: Documented Incidents . . . . . . . . . . . . . . .
19
2.3
Structural Characteristics of the Governance Gap . . . . . . . . . . . . . . .
20
2.4
Market and Regulatory Signals: The Inflection Point
. . . . . . . . . . . . .
20
3
Prior Work and the Research Gap
21
3.1
Methodological Lineage: From Non-Human Device Security to AI Identity
Taxonomy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
3.2
AI Risk Frameworks: Comprehensiveness Without Identity Specificity . . . .
21
3.3
Identity and Access Management Governance: The Practitioner Foundation .
23
3.4
Agentic AI Security and Accountability: The Scholarly Foundation
. . . . .
24
3.5
Cross-Jurisdictional AI Regulatory Analysis
. . . . . . . . . . . . . . . . . .
24
3.6
The Cumulative Research Gap . . . . . . . . . . . . . . . . . . . . . . . . . .
25
4
The Geopolitical and Regulatory Landscape: Five Frameworks, Three Fault
Lines, and a Governance Vacuum
26
6

4.1
Framework One: The EU AI Act - Rights-Based, Risk-Tiered, and Phasing
Into Force . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26
4.2
Framework Two: The United States - Deregulatory Federalism and the State-
Federal Fault Line
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27
4.3
Framework Three: China - Layered, Agile, and Extraterritorial . . . . . . . .
28
4.4
Framework Four: The International Coordination Landscape . . . . . . . . .
28
4.5
Framework Five: The State Actor Threat Environment - Identity as a Weapon 29
4.6
Three Fault Lines and the Governance Vacuum
. . . . . . . . . . . . . . . .
30
5
The AI-Identity Risk Taxonomy (AIRT): A Complete Enumeration
31
5.1
Taxonomy Structure and Methodology . . . . . . . . . . . . . . . . . . . . .
31
5.2
Critical Risk Intersections: Where Domains Compound . . . . . . . . . . . .
48
5.3
Taxonomy Gaps and Limitations
. . . . . . . . . . . . . . . . . . . . . . . .
48
6
THE MACHINE IDENTITY GOVERNANCE TAXONOMY (MIGT): AN
INTEGRATED FRAMEWORK FOR AI IDENTITY GOVERNANCE
49
6.1
MIGT Design Principles . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
49
6.2
MIGT Domain I: AI Identity Lifecycle Governance
. . . . . . . . . . . . . .
50
6.3
MIGT Domain II: Cryptographic Identity and Authentication Architecture .
51
6.3.1
Hardware-Rooted Attestation for Agentic Identity . . . . . . . . . . .
51
6.4
MIGT Domain III: Dynamic Access Governance . . . . . . . . . . . . . . . .
56
6.4.1
Attribute-Composite Risk Scoring: A Proposed Access Governance
Model for Agentic AI . . . . . . . . . . . . . . . . . . . . . . . . . . .
57
6.5
MIGT Domain IV: Accountability Attribution and Audit Architecture . . . .
60
6.6
MIGT Domain V: Supply Chain and Model Provenance Governance . . . . .
61
6.7
MIGT Domain VI: Regulatory Alignment and Cross-Jurisdictional Coordination 62
6.8
MIGT and the State Actor Threat Model . . . . . . . . . . . . . . . . . . . .
65
6.9
The MIGT as an Integrated Response to Five Structural Gaps . . . . . . . .
65
7
Implementation Guidance: Translating the MIGT into Enterprise Pro-
grams
65
7.1
Pre-Implementation: The Current State Assessment . . . . . . . . . . . . . .
66
7.2
Phase 1: Foundation (Months 1–6)
. . . . . . . . . . . . . . . . . . . . . . .
66
7.3
Phase 2: Hardening (Months 6–12) . . . . . . . . . . . . . . . . . . . . . . .
67
7.4
Phase 3: Integration (Months 12–24) . . . . . . . . . . . . . . . . . . . . . .
68
7.5
Phase 4: Optimization (Month 24+)
. . . . . . . . . . . . . . . . . . . . . .
69
7.6
Implementation Guidance for Specific Organizational Contexts . . . . . . . .
69
7

7.7
Measuring Program Effectiveness
. . . . . . . . . . . . . . . . . . . . . . . .
70
8
Conclusion: Governing the Machine - Four Claims, an Inflection Point,
and a Research Agenda
70
8.1
Restating the Four Claims . . . . . . . . . . . . . . . . . . . . . . . . . . . .
71
8.2
The Inflection Point . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
72
8.3
Limitations
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
73
8.4
Future Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . . .
73
8.5
A Closing Observation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
74
8

Kurtz & Krawiecka (2026)
Who Governs the Machine?
9
1. Introduction: The Governance Vacuum at the Intersection of AI
and Identity
In 2026, most organizations cannot answer three basic questions about their AI systems:
What can they access? Who is responsible when they cause harm? And does governing them
in one country create liability in another?
These are not edge-case questions. They are the foundational questions of enterprise
risk management, namely the same questions that identity and access management (IAM)
programs have answered for human identities for three decades. The answer to all three,
for most organizations in 2026, is: we do not know. That is the governance vacuum that is
addressed.
At the operational level, the governance vacuum manifests in three questions that prac-
titioners working directly with agentic AI deployments report being asked with increasing
urgency: What tools should an agent be given to complete a task? What data is it permitted
to process in doing so? And does the combination of tool access and data access remain within
the authorized scope of the task it was assigned (i.e., the original intent)? These are not
abstract policy questions. They are the runtime access governance decisions that determine
whether an AI agent operates within its sanctioned boundaries or accumulates capability and
data exposure that no single authorization decision contemplated. The absence of governance
frameworks capable of answering them at the speed and scale at which agentic AI systems
operate is the operational expression of the governance vacuum this paper addresses. Existing
IAM frameworks were not designed to evaluate tool-permission combinations dynamically, to
enforce task-scoped data access boundaries at machine speed, or to detect when the aggregate
effect of individually authorized tool invocations exceeds the scope of the task that justified
them. The result is that organizations are making these decisions implicitly, through the
access grants they provision at deployment time, without the governance infrastructure to
verify that those grants remain appropriate as agent behavior evolves across tasks, sessions,
and system interactions.
The governance vacuum is not primarily a technical failure. It is a framework failure,
specifically a failure to extend the disciplined, accountable governance structures that organi-
zations have built for human identities to the machine identities that now outnumber them
by more than 80 to 1 [1] [2].
That framework failure has a structural dimension that distinguishes it from ordinary
governance lag and that makes it resistant to the incremental remediation that has historically
closed gaps between emerging technology and governance practice. Agentic AI is among the
fastest-developing capability domains in the history of enterprise technology: the transition

Kurtz & Krawiecka (2026)
Who Governs the Machine?
10
from generative AI systems that respond to agentic AI systems that act, plan, delegate, and
accumulate access has occurred within a timeframe measured in months rather than the
years or decades over which prior technology transitions allowed governance frameworks to
mature. The consequence is that frameworks developed to address agentic AI governance risks
become narrow relative to current capability and begin to go out of date before they achieve
practitioner adoption, creating a persistent velocity asymmetry between the frontier of agentic
AI deployment and the frontier of agentic AI governance. No single framework, however
carefully designed, can remain current across all dimensions of a domain evolving at this speed.
What is required is not a point-in-time framework but a comprehensive, multidimensional
governance structure whose domains are stable enough to provide durable organizational
anchors while remaining extensible as specific risk categories, technical standards, and
regulatory obligations evolve beneath them. The MIGT is designed to provide exactly that
structure: a framework whose six governance domains address the persistent structural
characteristics of the AI identity governance problem-the identity lifecycle, the authentication
architecture, the access governance model, the accountability attribution mechanism, the
supply chain integrity requirement, and the cross-jurisdictional coordination challenge-rather
than the specific technical manifestations of those characteristics at any single moment in
time.
The framework failure does not exist in isolation. Compounding it is a regulatory failure
of equivalent structural depth: an expanding body of AI-specific law is being written by
legislators and regulators who, in many cases, do not understand the specific mechanics
of identity and access governance, and an expanding body of IAM practice is being built
by practitioners not adequately tracking the regulatory obligations their programs must
satisfy [3] [4]. The regulatory failure compounds the framework velocity problem: regulatory
instruments, which by their nature require extended drafting, consultation, and legislative
processes, are structurally unable to track a technology domain evolving at the pace agentic
AI is evolving. The result is regulation that addresses the AI capabilities of the drafting period
rather than the deployment period, creating compliance frameworks that are simultaneously
over-specified in areas where the technology has moved on and under-specified in areas-
including agent tool governance, task-scoped data access, and multi-agent accountability
attribution-where current deployment practice has outpaced regulatory imagination.
Where the framework failure and the regulatory failure operate primarily within organiza-
tional and national boundaries respectively, the third dimension of the governance vacuum
is irreducibly global: a coordination failure in which every major jurisdiction is developing
its own AI governance framework in relative isolation, creating a patchwork of potentially
incompatible obligations that no existing framework has mapped against the realities of

Kurtz & Krawiecka (2026)
Who Governs the Machine?
11
enterprise identity programs [5] [6].
This paper argues that solving the AI identity governance problem requires simultaneously
addressing all three failures: the framework gap, the regulatory gap, and the coordination
gap. Addressing any one in isolation produces incomplete solutions. A technically rigorous
AI identity governance framework that ignores regulatory obligations will fail compliance
requirements. A regulatory compliance program that lacks technical framework grounding
will fail operational security requirements. And both will fail when organizations encounter
the cross-jurisdictional conflicts that are already materializing as AI systems operate across
borders governed by fundamentally incompatible legal philosophies [7] [8].
1.1 The Scope and Urgency of the Problem
The scale of the AI identity governance problem is empirically documented and growing.
The Entro Labs NHI and Secrets Risk Report for H1 2025 found that non-human identities
grew 44% year-over-year and now outnumber human identities at a ratio of 144 to 1, up
from 92 to 1 in H1 2024 [9]. Gyure and Johnson [2] document machine identity growth from
approximately 50,000 per enterprise in 2021 to 250,000 by 2025, a 400% increase in four years,
while governance capabilities have not kept pace. IBM Security researchers have identified
that IAM teams are typically responsible for only 44% of an organization’s machine identities,
leaving the majority essentially ungoverned [10]. The Delinea 2026 security forecast states
plainly that if 2025 was the year organizations embraced AI, 2026 will be the year they lose
track of it [3].
The consequences of this governance gap are not hypothetical. The 2024 CrowdStrike
outage, which was caused by a single automated software update agent operating across
enterprise environments globally without adequate governance controls, produced an estimated
$5.4 to $10 billion in economic losses [11] [12] and demonstrated how a single ungoverned
machine identity can cause cascading failures at planetary scale. The Silk Typhoon espionage
campaign, active since 2024, has used stolen API keys and other machine credentials to
exfiltrate data of interest to the Chinese government, demonstrating that foreign state actors
have already identified ungoverned machine identities as a primary attack vector [13] [14].
DeepSeek’s alleged exfiltration of OpenAI training data through developer API accounts in
late 2024 illustrates the AI supply chain dimension of this risk, where machine identities
serve as both the attack vector and the target [13].
The State of AI Agent Security 2026 report, based on survey data from over 900 executives
and technical practitioners, found that 88% of organizations confirmed or suspected AI
agent security incidents in the preceding year, yet only 22% of teams treat AI agents as
independent, identity-bearing entities, and 45.6% still rely on shared API keys for agent-to-

Kurtz & Krawiecka (2026)
Who Governs the Machine?
12
agent authentication [15]. The governance gap documented in Section 2 is not a theoretical
projection: it is an operational crisis already producing measurable, attributable harm.
1.2 Why Existing Frameworks Are Insufficient: Five Structural Gaps
The insufficiency of existing frameworks is structural rather than incremental. These gaps
have been identified across multiple bodies of literature reviewed in Section 3, including the
AI agent security survey literature [16] [17], the agentic AI governance literature [18] [19] [20],
and the IAM standards literature [21] [22] [4].
Gap 1, The Identity Continuum Problem. Current IAM frameworks treat human
and machine identities as binary categories with separate governance approaches. Gyure and
Johnson [2] demonstrate that this binary categorization fails to address the nuanced reality of
modern enterprise identities, which exist on a spectrum from fully human-controlled to fully
autonomous. An AI agent acting on behalf of a human, executing their instructions, using
their delegated permissions, but making autonomous decisions in execution, is neither fully
human nor fully machine for governance purposes. Frameworks built on binary categorization
cannot govern the spectrum.
Gap 2, The Dynamic Access Problem. Role-based access control assumes that
roles can be defined and that access requirements are stable. Agentic AI systems discover
their access requirements dynamically, at runtime, as a function of the tasks they are
executing [4] [22]. The OpenID Foundation [22] has documented that current OAuth 2.0 and
SAML standards lack native support for the machine-speed reauthentication and multi-party
delegation that agentic AI systems require.
The dynamic access problem is compounded by a structural characteristic of agentic
AI that has no precedent in human or traditional service identity governance: the capacity
to autonomously decompose a task into parallel sub-tasks and spawn multiple subordinate
agents to execute them simultaneously. A human employee working on a complex task
proceeds sequentially, their access requirements unfolding in a predictable, auditable order
that governance frameworks can anticipate and bound. A service identity executes a defined
workflow whose access requirements are known at design time and do not change between
invocations. An agentic AI system does neither. It may determine at runtime that a task
is most efficiently accomplished by spawning three sub-agents in parallel, each requiring
distinct access grants to distinct systems, each potentially spawning further sub-agents of
their own, producing an access demand profile that is neither predictable at provisioning
time nor bounded by any fixed workflow definition.
This is the governance consequence of the non-deterministic nature of agentic AI: unlike
a conventional computer program, whose execution path can be represented as a flow chart

Kurtz & Krawiecka (2026)
Who Governs the Machine?
13
to which the program commits at design time, an agentic AI system’s execution path is an
emergent property of its reasoning process, the tools available to it, the data it encounters,
and the intermediate results it produces. You can no longer draw the flow chart. The access
requirements of step four depend on what the agent decided at step three, which depended on
what it found at step two, none of which was determined, or determinable, when the agent’s
credentials were provisioned. Traditional role-based access control is built on the assumption
that the flow chart exists and is known in advance: roles are defined because the tasks that
require them are defined. When the task structure itself is non-deterministic, the role structure
that governance frameworks depend on cannot be specified in advance, and the governance
choice between over-provisioning, which creates risk, and under-provisioning, which breaks
functionality, is not merely a false dilemma created by applying a static framework to a
dynamic problem, as prior analyses have characterized it [4] [22]: it is an unavoidable
consequence of applying any provisioning-time governance model to a system whose access
requirements are determined at reasoning time. The multi-agent spawning dimension extends
this problem across an additional axis: each sub-agent represents an independent identity
with its own access grants, its own behavioral trajectory, and its own accountability record,
yet the governance frameworks that must bound their collective behavior were designed for
identities that act one at a time, in sequence, along paths that a human architect drew before
the system ran.
The governance choice between over-provisioning (which creates risk) and under-provisioning
(which breaks functionality) is a false dilemma created by applying a static framework to a
dynamic problem.
Gap 3, The Accountability Attribution Problem.
When a human employee
causes harm, accountability attribution is straightforward. When an AI agent causes harm,
accountability is distributed across the agent’s developers, the organization that deployed it,
the prompt or instruction that triggered the harmful behavior, and the access permissions
that made the harm possible [23].
That distribution of accountability reflects a fundamental ontological shift in what an
AI agent is, relative to every prior category of enterprise software. Traditional software
systems, including earlier generations of automation and robotic process automation, were
digital extensions of human actions: a human defined the workflow, a human authorized
the execution, and the software performed exactly and only what the human specified.
Accountability attribution was also straightforward because the causal chain from human
decision to system action was direct, auditable, and complete. The human who designed
the workflow owned its consequences because the workflow owned nothing of its own: no
judgment, no initiative, no capacity to determine that the situation called for something

Kurtz & Krawiecka (2026)
Who Governs the Machine?
14
other than what was specified.
Agentic AI systems break this causal chain. They are no longer a digital extension of
human actions. They are autonomous ‘digital workers’: entities that receive a goal rather
than a procedure, determine their own approach to achieving it, select and invoke the tools
they judge appropriate, spawn subordinate agents when they assess that parallelization would
be efficient, and produce outcomes that their human principals neither specified nor, in
many cases, could have anticipated. The accountability question this creates is not merely
one of distributing blame across a longer chain of human decisions. It is one of attributing
responsibility for outcomes that no human decision fully determined, because the decisions
that produced them were made, at least in part, by the agent itself. This is a category of
accountability problem that enterprise governance frameworks have never been required to
address, because no prior category of enterprise software was capable of making decisions in
the relevant sense.
The practical governance consequence is that the accountability structures organizations
have built-designated approvers, audit trails of human authorizations, change management
processes, incident ownership assignment-all presuppose that a human decision sits at the
origin of every consequential system action. When the consequential decision is made by
an agent reasoning autonomously toward a goal, those structures do not fail at the edges:
they fail at the foundation. There is no approver to identify because no human approved the
specific action. There is no authorization record because the action was not authorized as
a discrete step but emerged from the agent’s autonomous execution of a broader mandate.
The audit trail records what the agent did but not why it decided to do it, and in a non-
deterministic system whose reasoning process is not fully interpretable, the why may not be
fully reconstructable even in principle.
Shavit et al. [20] propose unique agent identifiers as one mechanism for accountability
attribution, but note that no standardized system yet exists. Chan et al. [23] establish that
diffuse accountability is the condition under which governance failures proliferate without
consequence. Holgersson et al. [24] extend this analysis through a principal-agent framework,
arguing that the complexity of multi-agent systems creates unpredictabilities that existing
governance frameworks are not designed to address.
Gap 4, The Foreign Influence and State Actor Problem. Traditional IAM threat
models focus on external attackers and insider threats. AI identity governance must add a
third category: foreign state actors who use AI systems as instruments of espionage, influence,
and economic warfare [13] [25] [26] [27]. The Silk Typhoon campaign’s use of stolen API
keys [14] [28], North Korea’s deployment of AI-enhanced operatives [26], and documented
use of AI-generated content for foreign influence operations [29] demonstrate that foreign

Kurtz & Krawiecka (2026)
Who Governs the Machine?
15
state exploitation of AI identity governance gaps is a present operational reality. No existing
IAM framework has a foreign state actor threat model.
Gap 5, The Regulatory Fragmentation Problem. Organizations operating globally
face AI governance obligations under the EU AI Act, U.S. executive orders and sector-specific
guidance, China’s Cybersecurity Law and AI governance frameworks, and a proliferating
array of data governance compliance programs, all reflecting genuinely different national
philosophies and creating cross-jurisdictional conflicts [6] [7] [8]. Lim [7] identifies regulatory
fragmentation as accelerating rather than converging between 2023 and 2025. Perboli et
al. [30] confirm that without coordination two specific risks materialize: regulatory arbitrage
and normative fragmentation.
Gap 6, The Cross-Jurisdictional Agent Value Misalignment Problem. The five
structural gaps identified above share a common assumption: that the governance failures
they describe are, in principle, correctable through better technical controls, clearer regulatory
frameworks, and more disciplined organizational practice. Gap 6 is of a different character. It
arises not from the absence of governance but from the presence of fundamentally incompatible
governance philosophies that are instantiated directly into the behavioral objectives of the
AI agents those governance systems produce.
AI agents do not arrive at enterprise environments as neutral computational instruments.
They are trained, fine-tuned, and aligned against value frameworks, safety criteria, and
behavioral objectives that reflect the normative commitments of their developers, and by
extension, the regulatory, cultural, and geopolitical environments in which those developers
operate. Empirical research confirms that large language models exhibit measurably divergent
value patterns across national and cultural contexts, reflecting the normative environments of
their training data and alignment processes. An agent developed and aligned under the EU AI
Act’s fundamental rights framework, with its emphasis on human dignity, non-discrimination,
and meaningful human oversight, will instantiate a different behavioral disposition than an
agent developed under China’s framework, which prioritizes social stability, state security,
and content alignment with national policy objectives, or an agent developed under the
U.S. framework’s current emphasis on capability and competitiveness. These are not merely
differences of regulatory compliance posture. They are differences in what the agent has been
trained to treat as an acceptable outcome, a permissible action, and a legitimate objective [30].
The governance consequence is that when agents developed under incompatible value
frameworks interact within multi-agent architectures-which is increasingly the operational
reality for global enterprises-their behavioral objectives may be not merely different but
actively conflicting. An action that one agent’s alignment framework classifies as a required
safety intervention, refusing to process certain content, escalating a decision to human

Kurtz & Krawiecka (2026)
Who Governs the Machine?
16
oversight, declining to delegate to a counterpart agent, may be classified by a peer agent’s
alignment framework as an unwarranted obstruction of a legitimate task. The multi-agent
systems literature establishes that without shared normative frameworks, agent societies
produce persistent coordination failures of precisely this character, structural rather than
incidental, and not resolvable through local optimization by any individual agent. The
ACM Computing Surveys survey of AI agent security threats confirms that conflicting
agent objectives within multi-agent architectures represent a critical and undercharacterized
knowledge gap, explicitly identifying incentive misalignment as a mechanism for cascading
failures and emergent adversarial behavior [16]. Neither agent is malfunctioning by its
own governance criteria. Both are optimizing for objectives that their respective alignment
frameworks treat as correct. The result, from the perspective of any single governance
framework, is behavior that appears rogue, unpredictable, or adversarial, while remaining
entirely coherent and compliant from the perspective of the agent producing it.
This misalignment dynamic maps directly onto the difficulty humans have experienced in
agreeing on universal principles for AI governance. The scholarly literature documents that
the EU, U.S., and Chinese frameworks reflect genuinely incompatible internal logics rather
than different technical implementations of shared values, and that international coordination
efforts have thus far failed to resolve these incompatibilities at the human policy level. When
those incompatible logics are encoded into agent objective functions and deployed into shared
multi-agent environments, the coordination failure does not remain at the policy level: it
becomes an operational reality at machine speed, without the deliberative mechanisms that
human diplomacy, however imperfect, provides.
Existing IAM frameworks have no mechanism for detecting, classifying, or governing
behavioral conflicts that arise from value misalignment rather than credential compromise or
access policy violation. The MIGT’s Domain VI Regulatory Alignment structure addresses
the compliance dimension of cross-jurisdictional divergence; the agent value misalignment
problem requires an additional governance capability-behavioral alignment verification at
the agent interaction boundary-that no current framework provides and that Section 8.4
identifies as a priority future research direction.
1.3 Contributions: Four Original Claims
Claim 1: AI identity risk is a distinct risk category. The risks posed by AI identities, including
agentic AI systems, non-human identities, and the human-machine identity spectrum, are
not merely extensions of existing identity risk. They constitute a distinct category that
requires its own taxonomy, its own governance framework, and its own regulatory mapping.
The MIT AI Risk Repository [31], which classifies 1,612 AI risks, does not treat identity

Kurtz & Krawiecka (2026)
Who Governs the Machine?
17
governance as a primary risk domain. The peer-reviewed AI agent security surveys in ACM
Computing Surveys [16] [32] address agent threats without connecting them to enterprise
identity governance programs. The AIRT proposed in Section 5 is the first attempt to
enumerate this risk category comprehensively.
Claim 2: The governance framework gap, the regulatory gap, and the coordination gap
must be addressed simultaneously. Addressing any one in isolation produces incomplete
and operationally inadequate solutions. The agentic AI governance frameworks proposed
by Pandey [18], Joshi [19], and Shavit et al. [20], and the practitioner-oriented security
framework provided by the OWASP Top 10 for Agentic Applications [33], address governance
broadly without identity-specific grounding. The NIST AI RMF [34] provides governance
function structure without identity-specific risk enumeration. Cross-jurisdictional analyses
[6] [7] document regulatory divergence without enterprise-level resolution mechanisms. The
MIGT is designed to address all three simultaneously: providing technical governance
structure, regulatory alignment, and cross-jurisdictional coordination within a single integrated
framework.
Claim 3: Foreign state actors have already operationalized AI identity as an attack and
influence vector, and enterprise IAM programs have no adequate threat model for this. The
evidence reviewed in this paper, including the Silk Typhoon campaign [13] [14] [28], North
Korean AI-enhanced identity fraud [26] [27], Chinese AI-generated influence operations [29],
and the ongoing Typhoon campaign series [35] [36] [37], demonstrates that foreign state
exploitation of AI identity governance gaps is a present operational reality. An adequate AI
identity governance framework must include a foreign state actor threat model.
Claim 4: The absence of inter-jurisdictional coordination in AI governance is itself a
governance risk, and proposes a framework for managing it. The divergent AI governance
frameworks of the EU, U.S., and China reflect genuinely incompatible governance philosophies
that create cross-jurisdictional conflicts for every global organization deploying AI systems
[6] [7] [30]. Schmitt [38] traced the foundational architecture of this fragmented landscape in
2021, documenting the risk of geopolitical encroachment into technical governance domains-a
warning that has fully materialized by 2026. No existing framework provides organizations
with tools for managing these conflicts systematically at the enterprise identity governance
program level.
1.4 Paper Organization
Section 2 establishes the empirical foundation for the governance gap, documenting the scale,
scope, and structural characteristics of the non-human identity problem. Section 3 connects
this contribution to the research tradition from which it draws, including the prior taxonomic

Kurtz & Krawiecka (2026)
Who Governs the Machine?
18
work that provides its methodological foundation. Section 4 analyzes the geopolitical and
regulatory landscape in detail across five major frameworks. Section 5 presents the AI-Identity
Risk Taxonomy (AIRT). Section 6 presents the Machine Identity Governance Taxonomy
(MIGT). Section 7 provides implementation guidance for practitioners. Section 8 concludes
with discussion of implications and future research directions.
2. The Empirical Foundation: Scale, Consequences, and Structural
Characteristics of the Non-Human Identity Governance Problem
This section establishes the empirical foundation for the governance gap across four dimensions:
(1) the quantitative scale of machine identity proliferation, (2) the operational consequences of
governance failure through documented incidents with measurable impact, (3) the structural
characteristics that make the gap resistant to incremental remediation, and (4) the market
and regulatory signals confirming the problem has reached a strategic inflection point.
2.1 The Quantitative Scale of Machine Identity Proliferation
Multiple independent research programs [39], [40], [41], [42] have converged on a consistent
picture: machine identities vastly outnumber human identities, the gap is widening rapidly,
and governance capabilities are not keeping pace. The Entro Labs NHI and Secrets Risk
Report for H1 2025 found that non-human identities grew 44% year-over-year and now
outnumber human identities at a ratio of 144 to 1, up from 92 to 1 in H1 2024 [9]. CyberArk’s
2025 Identity Security Landscape, based on a Vanson Bourne survey of 2,600 cybersecurity
decision-makers across 20 countries, confirms that machine identities vastly outnumber human
identities within organizations, driven primarily by cloud and AI, and that 68% of respondents
report their organizations lack identity security controls for AI specifically [40].
The ESG Non-Human Identity Management report found that organizations on average
have 20 times more non-human identities than human identities, with 52% of organizations
predicting a further 20% increase in the next year, and that two-thirds had experienced a
successful cyberattack resulting from compromised non-human identities [41]. Research and
Markets’ February 2026 global NHI solutions report confirms that machine-to-human identity
ratios exceed 17 to 1 even in conservative enterprise estimates, with the highest-exposure
environments in financial services showing ratios as high as 96 to 1, and projects the NHI
solutions market at transformational growth through 2030 [43]. The Veza State of Identity
Security report, measuring more than 230 billion permissions across its enterprise dataset,
found that permissions classified as safe and compliant dropped from 70% in 2024 to 55%
in 2025, while ungoverned permissions rose from 5% to 28% of total, and that 1 in 20 AWS

Kurtz & Krawiecka (2026)
Who Governs the Machine?
19
machine identities carries full administrator privileges [44]. Gartner projects that by 2028,
one-third of enterprise applications will include autonomous AI agents, with the volume of
agentic identities projected to exceed 45 billion by end of 2025, more than 12 times the
number of humans in the global workforce [45].
2.2 Operational Consequences: Documented Incidents
The CrowdStrike outage of July 19, 2024, caused by a single automated software update agent
deployed without adequate governance controls across 8.5 million systems simultaneously,
produced $5.4 billion in Fortune 500 losses alone, with global estimates reaching $10 billion
[11] [12] [46]. Cybersecurity insurance policies covered only 10% to 20% of losses [11]. In
May 2025, a permission was granted via a Georgia court with Delta Air Lines’ negligence
suit against CrowdStrike to proceed [47]. Tufin’s analysis of the incident’s lasting impact
documents that it forced a fundamental reconsideration of automated update governance and
the accountability structures required for machine identity-driven operations at enterprise
scale [48]. The Harvard Business Review characterized the incident as a watershed moment
for machine identity governance, noting that the absence of staged rollout controls, behavioral
monitoring, and accountability assignment created the conditions for catastrophic failure at
planetary scale [49]. Every governance control specified in MIGT Domains III and IV would
have been directly relevant to preventing or limiting the scale of this incident.
The March 2025 tj-actions supply chain compromise, in which attackers used a stolen
personal access token to inject malicious code into a widely-used GitHub Action, exfiltrating
secrets from more than 23,000 repositories, illustrates the simultaneous manifestation of AIRT
Domain VI (supply chain compromise) and Domain I (static credential persistence) [9]. The
Cloudflare and U.S. Treasury incidents of 2024 followed the same pattern: under-protected
API keys and misconfigured machine identity credentials providing persistent access to critical
systems without triggering governance controls [45]. The Entro Labs report documents that
over 23.7 million secrets were found exposed on public GitHub repositories in 2024 alone,
with 57% originating in source code and 26% in CI/CD workflows [9].
The February 2025 Marks and Spencer cyberattack, attributed to the Scattered Spider
collective, offers a further illustration of how identity governance failures across organizational
boundaries produce cascading operational harm at scale [50] [51]. Attackers impersonated a
legitimate M&S employee and convinced a third-party IT provider, Tata Consultancy Services,
to reset internal credentials, gaining initial access and subsequently exfiltrating the Windows
domain controller’s NTDS.dit file, which contained password hashes for every domain user
including service accounts and machine identities. Armed with these credentials, attackers
moved laterally through M&S’s corporate domain encrypted VMware ESXi infrastructure

Kurtz & Krawiecka (2026)
Who Governs the Machine?
20
supporting e-commerce and logistics, and forced a 46-day suspension of online ordering that
produced an estimated £300 million in lost operating profits and a £750 million loss in market
value [50]. The incident illustrates the AIRT Domain V cross-organizational accountability
gap, the third-party identity governance failure the MIGT’s Domain I lifecycle governance
and Domain IV accountability attribution mechanisms are specifically designed to address,
and underscores that identity governance failures in partner and vendor ecosystems are
operationally indistinguishable in their consequences from failures in the organization’s own
environment.
2.3 Structural Characteristics of the Governance Gap
Three structural features make the AI identity governance problem resistant to incremental
resolution. First, the visibility problem: organizations do not have the foundational inventory
and ownership assignment - specifically the AI Identity Registry specified in MIGT Domain
I - from which visibility flows. Without the registry, no tool can provide comprehensive
visibility because no authoritative record of what should exist is available against which actual
inventory can be compared. The CyberArk report confirms that IAM teams are responsible
for only 44% of machine identities [40], and that 47% of organizations cannot secure shadow
AI usage at all [40].
Second, the governance velocity mismatch: machine identities are created at machine
speed, automatically, continuously, and without governance review in most organizations. Any
governance approach relying on human-speed review perpetually lags behind the identity cre-
ation rate. Third, the identity debt accumulation dynamic: the Veza finding that ungoverned
permissions rose from 5% to 28% of enterprise total in a single year [44] represents not a
stable problem but an accelerating one. Like financial debt, identity debt has compounding
dynamics that existing IAM approaches are not reversing.
2.4 Market and Regulatory Signals: The Inflection Point
The IAM market is projected to grow from $19.80 billion in 2024 to $61.74 billion by 2032,
with non-human identity governance identified as the primary growth driver [52]. The
CyberArk report found that 88% of respondents are under increased pressure from insurers
mandating enhanced privilege controls for machine identities, and that 90% of global leaders
cite identity attacks as their top cybersecurity concern [40]. Delinea [3] characterizes 2026 as
the year when machine identities move from a technical issue to a board-level priority. The
NIST CAISI AI Agent Standards Initiative, launched February 18, 2026, and the companion
NCCoE concept on AI agent identity and authorization [53] [54] [55] signal that the U.S.
government acknowledges no adequate standard currently exists - precisely the gap the MIGT

Kurtz & Krawiecka (2026)
Who Governs the Machine?
21
is designed to fill.
3. Prior Work and the Research Gap
The research presented sits at the convergence of five distinct bodies of literature: (1) the prior
taxonomic work on non-human entity security that provides its methodological foundation,
(2) AI risk and governance frameworks, (3) identity and access management governance
standards, (4) agentic AI accountability and harm frameworks, and (5) cross-jurisdictional
AI regulatory analysis. Each body of literature makes essential contributions to the problem
domain; none addresses it in its entirety. This section surveys each, identifies its contribution
and limitations relative to the problem addressed, and constructs the cumulative case for
why the MIGT and AIRT constitute a necessary and original contribution.
3.1 Methodological Lineage: From Non-Human Device Security to AI Identity
Taxonomy
The taxonomic methodology employed in the AIRT builds on the structured classification
approach established in Rizvi, Kurtz, Pfeffer, and Rizvi [56], which presented a multi-domain
security taxonomy for IoT environments at IEEE TrustCom/BigDataSE 2018. That work
identified identity and data theft, device manipulation, and data falsification as primary
risk vectors in distributed non-human entity environments, establishing the classification
framework the AIRT extends to the agentic AI domain. The present paper’s contribution is
not an incremental update to IoT security taxonomy but a new application of the taxonomic
method to a risk domain-AI identity governance-that the IoT literature did not anticipate and
has not addressed. Agentic AI identities reason about their access requirements dynamically,
accumulate permissions across multi-system interactions, and operate in ways that create
accountability structures with no precedent in device security, requiring a purpose-built
taxonomy rather than an adaptation of existing device-oriented frameworks.
3.2 AI Risk Frameworks: Comprehensiveness Without Identity Specificity
The MIT AI Risk Repository [31] has undergone two significant updates since this research
began. The April 2025 update expanded the database to 1,612 classified risks and introduced a
new multi-agent risks subdomain; the December 2025 update further expanded the repository
to over 1,700 coded risks across 74 included frameworks. The multi-agent risks subdomain,
which the repository defines as covering “risks from multi-agent interactions, due to incentives
which can lead to conflict or collusion, and the structure of multi-agent systems, which can
create cascading failures, selection pressures, new security vulnerabilities, and a lack of shared

Kurtz & Krawiecka (2026)
Who Governs the Machine?
22
information and trust,” represents the repository’s most direct engagement with agentic
AI risk. However, it does not address identity governance as a primary risk domain-the
subdomain’s focus is on inter-agent incentive structures and emergent failure modes rather
than the enterprise identity lifecycle, credential hygiene, accountability attribution, and
cross-jurisdictional regulatory obligations that define the AI identity governance problem this
paper addresses. The NIST AI RMF [34] provides the most authoritative governance-oriented
treatment of AI risk for U.S. organizations, establishing the GOVERN, MAP, MEASURE,
and MANAGE functions. Its limitation for the present is that it is framework-level rather
than taxonomy-level: it describes governance functions without enumerating the specific
identity-related risks that enterprise AI governance programs must address.
Coutinho, Ashofteh, and Al Helaly [57] address AI risk taxonomies and governance
frameworks for generative AI, representing the most directly comparable academic work.
Their taxonomy focuses on generative AI outputs and capabilities rather than the identity
and access governance risks that arise when AI systems are granted enterprise identities and
act as autonomous agents. The AI governance systematic literature review by Kaur et al. [58]
identifies four key governance dimensions without specifically addressing identity governance.
Moura et al. [59] provide the most rigorous peer-reviewed treatment of prompt injection
attacks, characterizing the lethal trifecta of privileged access, untrusted input processing, and
exfiltration capability as the architectural precondition for AI system compromise. Ferrag et
al. [60] extend this analysis to protocol-level exploits in LLM-agent workflows, providing the
first integrated taxonomy bridging input-level exploits and protocol-layer vulnerabilities.
Wang, Zhang, Xiao, and Liang [61], in a structural topic model analysis of 139 AI policies
across China, the EU, and the United States published in Technological Forecasting and
Social Change in 2025, represent the most methodologically rigorous quantitative comparison
of the three primary governance frameworks. Their analysis identifies 13 major policy topics
organized around research and application, social impact, and government role, confirming the
fundamental philosophical divergence between China’s research and application emphasis, the
EU’s social impact orientation, and the U.S. government’s role focus documented qualitatively
in Section 4. The present contribution relative to Wang et al. is both domain specific and
operational: where Wang et al. characterize the macro-level philosophical divergence across
139 policy documents, this paper maps how that divergence produces specific, irreconcilable
conflicts at the enterprise identity governance program level-the algorithm transparency
conflict, the extraterritoriality conflict, and the attribution-accountability gap-making the
two analyses complementary rather than competing contributions.

Kurtz & Krawiecka (2026)
Who Governs the Machine?
23
3.3 Identity and Access Management Governance: The Practitioner Foundation
NIST SP 800-207 [21], the authoritative U.S. zero trust architecture standard, establishes the
principle that identity is the primary trust signal in modern enterprise security and explicitly
extends zero trust principles to non-human entities, including services, applications, and
automated workloads. The IDSA [4] has documented the gap between IAM frameworks
designed for human identity governance and the requirements of AI-era identity management,
identifying dynamic access requirements, certification workflow failures, and orphaned identity
accumulation as primary governance failures. The NIST CAISI initiative [53] and the NCCoE
concept paper on AI agent identity [54] [55] signal that authoritative standards-based guidance
for AI agent identity is forthcoming, confirming the governance gap the MIGT addresses.
Gyure and Johnson [2] provide the most directly relevant recent academic treatment of the
human-machine identity spectrum, demonstrating quantitative machine identity growth and
arguing for unified governance frameworks. The present paper extends and differs from Gyure
and Johnson in three ways: it introduces a comprehensive risk taxonomy as the foundation
for governance framework design, it incorporates a foreign state actor threat model that
their framework does not address, and it provides a cross-jurisdictional regulatory alignment
structure that maps enterprise identity governance obligations across EU, U.S., and Chinese
frameworks simultaneously. The OpenID Foundation [22] addresses the specific technical
challenges of identity management for AI agents, including delegated authorization, transitive
trust, scalable human governance, and cross-domain federation, documenting that current
standards are insufficient for the compound identity structures and multi-party delegation
requirements of advanced agentic deployments.
The Singapore Model AI Governance Framework for Agentic AI (MGF) [62], published by
the IMDA at the World Economic Forum on January 22, 2026, represents the most significant
national-level governance development directly adjacent to the MIGT’s contribution. The
Singapore MGF introduces Agent Identity Cards, a standardized disclosure format specifying
AI agent capabilities, limitations, authorized action domains, and escalation protocols, and a
four-level graduated autonomy taxonomy with governance requirements increasing at each
level. Critically, the Singapore MGF explicitly acknowledges that “Gaps exist today in terms
of handling agent identity robustly” and that current authorization systems with pre-defined,
static scopes are insufficient for agentic AI, independently confirming the identity governance
gap the MIGT addresses. The present paper’s contribution relative to the Singapore MGF is
threefold: the MIGT provides an academic peer-reviewed framework rather than a national
policy document; the AIRT provides a comprehensive risk enumeration that the MGF does
not attempt; and the MIGT’s cross-jurisdictional Regulatory Alignment Domain provides an
enterprise-level mechanism for managing the conflicts between Singapore’s MGF, the EU AI

Kurtz & Krawiecka (2026)
Who Governs the Machine?
24
Act, the U.S. NIST AI RMF, and the Chinese CSL obligations simultaneously-a coordination
challenge the Singapore MGF does not address.
3.4 Agentic AI Security and Accountability: The Scholarly Foundation
The ACM Computing Surveys study by Deng et al. [16] provides the most comprehensive
peer-reviewed survey of AI agent security threats, identifying four critical knowledge gaps:
unpredictability of multi-step inputs, complexity of internal executions, variability of opera-
tional environments, and interactions with untrusted external entities. He et al. [32] provide
a comprehensive overview of privacy and security issues in LLM agents, demonstrating that
AI agents inherit LLM vulnerabilities while introducing agent-specific threats whose impacts
extend far beyond those of the underlying model. Castro et al. [17] map agentic AI security
across the NIST Cyber Defense Life Cycle, providing context for where identity governance
sits within the broader security lifecycle. All three confirm the breadth and severity of
the security challenge the AIRT addresses; none frames it in terms of enterprise identity
governance programs.
Chan et al. [23] provide the most rigorous peer-reviewed treatment of harms from increas-
ingly agentic algorithmic systems, establishing that diffuse accountability creates conditions
under which governance failures proliferate without consequence. Shavit et al. [20] propose
unique agent identifiers as the foundational accountability mechanism. Holgersson et al. [24]
apply principal-agent theory to AI governance, arguing for guided autonomy, individualization,
and adaptability as design principles for accountable AI agent systems. Pandey [18] proposes
a universal agentic AI governance framework integrating risk, accountability, and compliance.
Joshi [19] proposes a framework for government policy on agentic and generative AI. All
confirm the core argument that existing frameworks are inadequate for agentic AI, but none
provides the identity-specific framing, comprehensive risk taxonomy, or cross-jurisdictional
regulatory mapping that constitute this paper’s primary contributions.
3.5 Cross-Jurisdictional AI Regulatory Analysis
Chun et al. [6] provide rigorous comparative analysis across EU, U.S., and Chinese AI
governance jurisdictions, documenting the fundamental differences in regulatory philosophy
that create cross-jurisdictional conflicts the Regulatory Alignment Domain is designed to
address. Perboli, Simionato, and Pratali [30], applying a legal-ethical-operational-geopolitical
analytical framework, document that without cross-jurisdictional coordination two specific
risks will arise: regulatory arbitrage and normative fragmentation. Their finding that the
EU, U.S., and Chinese frameworks reflect genuinely incompatible internal logics-not merely
different technical implementations of shared values-directly supports Claim 4. Lim [7]

Kurtz & Krawiecka (2026)
Who Governs the Machine?
25
documents regulatory trajectory convergence on safety and transparency alongside divergence
in regulatory technique and international posture. Schmitt [38], in the foundational mapping
of the global AI governance regime, demonstrated that the nascent regime is polycentric
and fragmented, gravitating around the OECD as a norm-setting anchor, while warning
that geopolitical considerations are increasingly encroaching into domains that ought to be
technical, with China, the EU, and the U.S. competing to shape international AI standards
in ways that further their own perceived interests rather than converge on shared governance
norms. This encroachment, documented by Schmitt [38] as already observable in 2021, has
intensified dramatically by 2026 in the form of the structural fault lines documented in
Section 4.6. The Communications of the ACM [8] articulates the governance vacuum created
by regulatory divergence. Csernatoni [63] argues that the geopolitical centrality of AI to
interstate competition creates first-order cooperation problems that fundamentally complicate
governance coordination. The IAPP [64] documents specific compliance challenges created
by EU and Chinese AI regulatory differences.
Wang et al.’s [61] structural topic model analysis of China, EU, and U.S. AI policies con-
firms the philosophical divergence Section 4 documents operationally, providing quantitative
empirical grounding for the qualitative cross-jurisdictional analysis the MIGT’s regulatory
alignment domain is designed to address. The present cross-jurisdictional scope is limited to
the EU, U.S., and Chinese primary frameworks; the emergence of the UK AI Safety Institute
framework following Brexit and the Singapore MGF [62] in January 2026 represent additional
jurisdictions creating enterprise AI governance obligations that future work extending the
MIGT’s Jurisdictional Mapping Matrix should incorporate.
3.6 The Cumulative Research Gap
The prior taxonomic work on non-human entity security [56] provides the methodological
foundation for classification but does not address agentic AI identities, accountability attribu-
tion, or cross-jurisdictional regulatory obligations. AI risk frameworks provide comprehensive
risk classification but do not address identity governance as a primary risk domain. IAM
governance standards provide the operational foundation but have not been extended to
address the specific challenges created by AI agent identities, including dynamic access re-
quirements, agentic accountability structures, and foreign state actor threat models. Agentic
AI accountability frameworks identify the governance failures created by distributed account-
ability structures but do not connect them to the specific identity governance mechanisms
through which accountability can be operationally enforced. Cross-jurisdictional regulatory
analyses document the fragmentation problem but do not provide a framework for mapping
jurisdictional requirements against enterprise identity governance programs specifically. The

Kurtz & Krawiecka (2026)
Who Governs the Machine?
26
MIGT and AIRT address this cumulative gap, constituting the first integrated framework
in the published literature to simultaneously address: (1) AI identity risk enumeration at
the taxonomic level, (2) governance framework design incorporating technical structure,
regulatory alignment, and cross-jurisdictional coordination, (3) a foreign state actor threat
model for enterprise identity governance, and (4) a cross-jurisdictional coordination framework
mapping how EU, U.S., and Chinese AI governance obligations interact at the enterprise
identity governance program level.
4. The Geopolitical and Regulatory Landscape: Five Frameworks,
Three Fault Lines, and a Governance Vacuum
The AI identity governance problem does not exist in a geopolitical vacuum. It exists at the
intersection of the most consequential strategic competition of the twenty-first century-the U.S.-
China rivalry for AI dominance-and the most significant peacetime regulatory divergence since
the emergence of the internet: the simultaneous development of fundamentally incompatible
AI governance philosophies by the world’s three major AI powers. This section analyzes
that landscape across five frameworks and identifies three structural fault lines that create
the governance vacuum the MIGT is designed to address. Understanding this landscape
is load-bearing for two of the four original claims. Claim 3, that foreign state actors have
already operationalized AI identity as an attack and influence vector, requires a detailed
account of the state actor threat environment. Claim 4, that the absence of inter-jurisdictional
coordination is itself a governance risk, requires a detailed account of how the three major
regulatory frameworks conflict at the enterprise identity governance level.
4.1 Framework One: The EU AI Act - Rights-Based, Risk-Tiered, and Phasing
Into Force
The EU AI Act, which entered into force on August 1, 2024, is the world’s first comprehensive
binding AI regulation [65]. As of March 2026, it is in active phased implementation: prohibited
practices and AI literacy obligations have been in effect since February 2025, GPAI model
obligations became applicable on August 2, 2025, and the majority of remaining provisions,
including comprehensive requirements for high-risk AI systems, take effect on August 2,
2026 [66] [67]. Article 101 fines reach up to EUR 35 million or 7% of global annual turnover
for prohibited practices [67].
For enterprise AI identity governance, three dimensions of the Act are directly material.
First, GPAI model obligations under Article 53 include technical documentation requirements,
copyright compliance policies, and training data transparency [66]. For enterprise identity

Kurtz & Krawiecka (2026)
Who Governs the Machine?
27
governance programs, GPAI obligations create a documentation requirement mapping directly
onto the provenance verification challenge in AIRT Domain VI: organizations deploying
AI agents built on GPAI models must document the model’s provenance, training data
characteristics, and compliance status. The current inability of most enterprise identity
governance programs to verify AI model provenance is not merely a security gap: as of August
2025, it is a compliance gap [68].
Second, the high-risk AI system requirements effective August 2026 include risk man-
agement, data governance, technical documentation, record-keeping, transparency, human
oversight, accuracy, robustness, and cybersecurity obligations, all of which directly implicate
identity governance [65]. The human oversight requirements are particularly significant: the
Act requires that high-risk AI systems be designed and deployed in ways that allow natural
persons to effectively oversee them, which presupposes that those persons are identifiably
assigned governance responsibility for specific AI systems-precisely the Human Oversight
Nominalism risk identified in AIRT Domain V.
Third, the Act’s extraterritorial reach applies to any organization placing AI systems on
the EU market or affecting persons in the EU [68], creating obligations for organizations
headquartered outside the EU and generating the cross-jurisdictional conflicts documented in
Section 4.6.
4.2 Framework Two: The United States - Deregulatory Federalism and the
State-Federal Fault Line
President Biden’s Executive Order 14110, which established AI safety testing requirements
and directed NIST AI RMF development, was revoked on January 20, 2025. The subsequent
AI Action Plan of July 23, 2025, refocused U.S. federal AI policy on innovation and competi-
tiveness [69]. For enterprise AI identity governance, the federal pivot produces a paradoxical
effect: safety and bias governance are being deprioritized while AI-specific cybersecurity and
identity governance are being elevated. The NIST CAISI AI Agent Standards Initiative
launched February 18, 2026 [53], and the companion NCCoE AI agent identity concept
paper [54] [55] together signal that authoritative U.S. standards for AI agent identity are
forthcoming, consistent with the MIGT’s framing of AI identity governance as primarily a
security and accountability challenge. It should be noted, however, that the deprioritization
of federal AI safety requirements creates its own governance risk: in the absence of bind-
ing federal standards, enterprise AI governance programs depend on voluntary framework
adoption whose actual compliance rates are unverified, creating a gap between formal policy
deference to industry self-governance and the operational reality of widespread governance
deficits documented in Section 2.

Kurtz & Krawiecka (2026)
Who Governs the Machine?
28
Executive Order 14365 (December 2025) signals potential preemption of state AI laws
deemed to impose excessive regulation [70].
However, the Senate voted 99-1 against a
proposed 10-year moratorium on state AI law enforcement [71], signaling that Congress is not
prepared to eliminate state AI governance authority. Organizations operating in multiple U.S.
states face simultaneous compliance obligations under California, Texas (TRAIGA, effective
January 1, 2026), Colorado (effective June 30, 2026), and Illinois AI frameworks [71] [72],
all including transparency, accountability, and documentation requirements that implicate
identity governance, with uncertain federal preemption status. Despite its voluntary status,
the NIST AI RMF [34] has become the de facto operational standard, referenced in Texas’s
TRAIGA as providing safe harbor protection.
4.3 Framework Three: China - Layered, Agile, and Extraterritorial
China’s AI governance is built on a multi-level framework of interlocking laws and regulations
[73]. The three cornerstone statutes are the Cybersecurity Law (CSL, originally 2017), the
Data Security Law (2021), and the Personal Information Protection Law (2021). Layered on
top of these are AI-specific regulations: the Algorithm Recommendation Measures (2022),
the Deep Synthesis Measures (2023), and the Interim Measures for Generative AI Services
(August 2023), making China the first country in the world to implement binding generative AI
regulations [74]. The amendment of the CSL, effective January 1, 2026, introduces dedicated
AI compliance provisions into China’s foundational cybersecurity law, requiring AI ethics
standards, risk monitoring, and safety assessments, and expands the CSL’s extraterritorial
reach to cover any foreign organization or individual engaging in activities that endanger
mainland China’s network security [75].
China’s algorithm filing regime requires AI services with public opinion attributes or
social mobilization capabilities to file their algorithm mechanisms with the Cyberspace
Administration of China [73]. For global organizations operating in China, this transparency
obligation creates a direct conflict with trade secret protection obligations that may apply
under U.S. law-an operational conflict documented in the Cross-Jurisdictional Regulatory
Weaponization risk in AIRT Domain VII. China’s July 2025 Action Plan for Global AI
Governance [76] reflects China’s ambition to shape international AI governance norms,
adding a geopolitical dimension to the technical compliance challenge that Schmitt [38] first
documented as a systemic risk in 2021.
4.4 Framework Four: The International Coordination Landscape
The international AI governance coordination landscape as of March 2026 is characterized by
what Pouget et al. [77] describe as a weak regime complex. The UN Advisory Body on AI,

Kurtz & Krawiecka (2026)
Who Governs the Machine?
29
the Hiroshima AI Process (G7), the Council of Europe AI Convention, and the Bletchley
Declaration all address AI risks without addressing identity governance specifically. On
January 22, 2026, Singapore’s IMDA published the Model AI Governance Framework for
Agentic AI at the World Economic Forum in Davos, described as the first governance template
focused specifically on AI agents [62], confirming that major jurisdictions continue to develop
independent AI governance frameworks that enterprise organizations must simultaneously
satisfy. Schmitt [38] traced the foundational architecture of this fragmented landscape in
2021, demonstrating that the nascent AI governance regime gravitates around the OECD as
a norm-setting anchor while warning that geopolitical considerations are encroaching into
technical domains. By 2026, that warning has fully materialized: the U.S. AI Action Plan,
China’s Global AI Governance Action Plan, and the EU AI Act’s extraterritorial reach all
reflect states using AI governance as an instrument of geopolitical competition. Perboli et
al. [30] confirm that without international coordination the result is regulatory arbitrage
and normative fragmentation-conditions that MIGT Domain VI is specifically designed to
help enterprise organizations navigate at the program level. Csernatoni [63] argues that
the geopolitical centrality of AI creates first-order cooperation problems that fundamentally
complicate governance coordination. For enterprise organizations, the absence of effective
international coordination means that cross-jurisdictional conflicts in AI identity governance
obligations have no resolution mechanism above the enterprise program level.
4.5 Framework Five: The State Actor Threat Environment - Identity as a Weapon
State-sponsored cyber operations targeting enterprise identity infrastructure are conducted
by multiple nations and represent a global governance challenge rather than a bilateral
one. This section documents the state actor threat environment as it is directly relevant to
enterprise AI identity governance programs, focusing specifically on documented, attributed
incidents in which ungoverned machine credentials were operationalized as attack vectors
producing measurable enterprise harm. The incidents cited are selected for their direct
relevance to the AIRT’s risk categories and the MIGT’s governance requirements, not as a
comprehensive survey of global state-sponsored cyber activity. Intelligence services across
multiple jurisdictions, including those of Five Eyes nations, conduct signals intelligence and
cyber operations that intersect with AI identity governance; the documented incidents below
are analyzed because they have been publicly attributed by government authorities or credible
threat intelligence organizations and because they directly demonstrate the governance gaps
the MIGT addresses.
Microsoft Threat Intelligence documents that Silk Typhoon (APT27/HAFNIUM), a
Chinese state-sponsored threat group, shifted tactics in late 2024 to specifically target IT

Kurtz & Krawiecka (2026)
Who Governs the Machine?
30
supply chain and network management providers, using stolen API keys and credentials
associated with privileged access management (PAM) providers, cloud application providers,
and cloud data management companies to access downstream customer environments [14] [28].
The operational pattern is precisely the Domain I, Domain III, and Domain VII intersection
identified in the AIRT: credential theft enabling high-volume downstream access in service of
foreign intelligence objectives. Two alleged Silk Typhoon members were indicted by federal
prosecutors in March 2025 [28]. The Foreign Affairs espionage analysis [27] and Springer AI
and Ethics study [78] confirm this represents the current frontier of nation-state AI identity
exploitation.
Salt Typhoon, attributed to China’s Ministry of State Security, conducted what the
FBI and CISA describe as a campaign breaching global telecommunications privacy and
security norms, compromising nine major U.S. telecommunications providers, accessing
metadata of over a million users, and in some cases obtaining audio recordings of senior
government and campaign officials [35] [36]. As of February 2026, the FBI’s Cyber Division
has publicly stated that Salt Typhoon continues to pose an active threat [37]. Volt Typhoon
has focused on pre-positioning within U.S. critical infrastructure for potential disruption
using living-off-the-land techniques, targeting the AI system availability and continuity
assumptions embedded in enterprise identity governance programs [36]. North Korean state
operatives have used AI-enhanced identity fraud to obtain legitimate enterprise employment,
generating synthetic identities, deepfake credentials, and AI-powered social engineering to pass
hiring and background check processes at technology companies and critical infrastructure
organizations [26].
The broader peer-reviewed literature on U.S.-China cyber strategic
competition confirms that identity compromise is a primary vector for state-sponsored
espionage and that AI capabilities are accelerating the pace and sophistication of these
operations [79] [27]. The use of AI-generated content for foreign influence operations through
enterprise platforms, documented by CSO Online [80] and the DFRLab [29], extends the
state actor threat surface from credential theft to algorithmic manipulation of organizational
decision-making.
4.6 Three Fault Lines and the Governance Vacuum
The analysis above reveals three structural fault lines. Fault Line 1, The Rights-Security
Divide: the EU approaches AI governance through fundamental rights and human dignity, the
U.S. through national security and economic competitiveness, and China through state control
and social stability. These three philosophies produce genuinely incompatible governance
requirements at the enterprise level, as Perboli et al. [30] document through their cross-
jurisdictional analysis.
Fault Line 2, The Regulatory Velocity Asymmetry: all

Kurtz & Krawiecka (2026)
Who Governs the Machine?
31
three frameworks are evolving rapidly and at different speeds simultaneously, with the EU’s
August 2026 enforcement date, China’s January 2026 CSL amendments, and U.S. state law
proliferation all creating moving compliance targets without any coordination mechanism to
manage the resulting complexity for global organizations. Fault Line 3, The Attribution-
Accountability Gap: when a state actor exploits a machine credential to cause harm across
international borders, existing frameworks in each jurisdiction answer the accountability
question differently or not at all-precisely the scenario for which Schmitt’s Tallinn Manual
tradition [81] has not yet developed adequate doctrine in the AI identity context.
5. The AI-Identity Risk Taxonomy (AIRT): A Complete Enumeration
The MIT AI Risk Repository [31], which as of December 2025 classifies over 1,700 AI risks
across 74 frameworks and has introduced a multi-agent risk subdomain, does not address
identity governance as a primary risk domain. The peer-reviewed AI agent security surveys
[16] [32] address agent threats without connecting them to enterprise identity governance
programs. Existing IAM risk frameworks do not address AI-specific attack vectors [4] [21].
The AIRT is designed to fill this gap.
The taxonomy draws on the MIT AI Risk Repository [31], the OWASP Top 10 for LLM
Applications [82], the NIST AI RMF [34], the ACM Computing Surveys survey of AI agent
threats [16], the prompt injection taxonomy of Ferrag et al. [60] and Moura et al. [59], and the
current academic literature on AI security, identity governance, and geopolitical risk reviewed.
The accountability domain draws on Chan et al. [23], Shavit et al. [20], and Holgersson et
al. [24]. The foreign state actor domain draws on Chin and Lester [13], NYU JIPEL [26],
DFRLab [29], Ding et al. [27], and Springer AI and Ethics [78]. The taxonomic methodology
extends the structured multi-domain classification approach established by Rizvi et al. [56]
to the agentic AI identity domain.
5.1 Taxonomy Structure and Methodology
The AIRT is structured as a two-level taxonomy. Eight Risk Domains are first and organize
risks by their primary organizational context and accountability structure. The second level
has 37 Risk Sub-Categories that enumerate specific, actionable risk items within each domain.
Each sub-category is characterized by four attributes: a description of the risk mechanism,
a severity rating (Critical, High, or Medium), the primary attack or failure vector through
which the risk manifests, and governance implications for IAM practitioners. The taxonomy
is designed to be exhaustive within its scope-the intersection of AI systems and identity
governance-rather than comprehensive across all AI risks.

Kurtz & Krawiecka (2026)
Who Governs the Machine?
32
Severity Classification Methodology. Severity ratings-Critical, High, and Medium-are
assigned using a structured two-factor assessment combining estimated impact magnitude
and observed likelihood of occurrence given current enterprise AI deployment patterns. This
assessment draws on four evidentiary sources applied consistently across all 37 sub-categories.
First, documented incident record: where a risk sub-category has produced a verified,
attributed incident with quantifiable impact, that incident anchors the severity rating. Static
Credential Persistence is rated Critical because of its documented role as the primary attack
vector in the SilkTyphoon campaign [14] [28], the tj-actions supply chain compromise affecting
more than 23,000 repositories [9], and the Cloudflare and U.S. Treasury incidents of 2024 [45].
High-Volume Autonomous Exfiltration is rated Critical because of its demonstrated role in
the DeepSeek/OpenAI training data exfiltration incident and the documented capability of
agentic AI systems to operate at speeds and volumes that human-speed detection and response
mechanisms cannot match [13]. Multi-Agent Privilege Escalation is rated Critical because
of its documentation as an active attack pattern in the ACM Computing Surveys survey of
AI agent security threats [16] and its technical characterization as a primary architectural
vulnerability in LLM-agent workflows by Ferrag et al. [60].
Second, regulatory and standards recognition: where a risk sub-category is explicitly
addressed by a major regulatory framework or security standard as a primary concern, that
recognition elevates the likelihood assessment. Cryptographic Identity Absence is rated
Critical in part because NIST SP 800-207 [21], the EU AI Act Article 15 [65], and the
NCCoE AI agent identity initiative [54] [55] all identify cryptographic workload identity as a
foundational security requirement, the absence of which constitutes a structural governance
failure. Audit Trail Insufficiency is rated Critical because EU AI Act Articles 12 and 17, SOX
AI transparency requirements, and China’s amended CSL all impose specific record-keeping
obligations that audit trail insufficiency directly prevents organizations from satisfying [65] [75].
Third, practitioner prevalence data: where a risk sub-category is identified as widespread
in practitioner surveys or industry measurement studies, that prevalence elevates the likeli-
hood assessment. The CyberArk Identity Security Landscape report’s finding that 68% of
organizations lack identity security controls for AI specifically [40], the Entro Labs finding
that 45.6% of teams rely on shared API keys for agent-to-agent authentication [9], and the
Veza finding that 1 in 20 AWS machine identities carries full administrator privileges [44]
collectively inform the likelihood assessments for Domains I and II risk sub-categories. The
State of AI Agent Security 2026 report’s finding that 88% of organizations confirmed or
suspected AI agent security incidents [15] provides the broadest prevalence signal for the
overall threat environment.
Fourth, threat intelligence and state actor documentation: where a risk sub-category

Kurtz & Krawiecka (2026)
Who Governs the Machine?
33
has been operationalized by a documented, attributed threat actor, that operationalization
elevates both impact and likelihood assessments to Critical. The five Domain VII risk sub-
categories are all rated Critical or High based on specific, attributed threat actor campaigns:
SilkTyphoon for State-Sponsored API Credential Theft [14] [28], FBI and DOJ documentation
for AI-Enhanced Identity Fraud for Enterprise Access [26], DFRLab and CSO Online for
Algorithmic Foreign Influence via Enterprise AI [29] [80], and peer-reviewed geopolitical
analysis for AI Model as Critical Infrastructure Target [27] [78].
Medium severity ratings are assigned to risk sub-categories where: documented incidents
exist but at lower frequency or impact scale, regulatory recognition is present but enforcement
is limited, or the risk is structural and growing but has not yet produced incidents at the
scale of Critical-rated categories. The Domain VIII physical infrastructure and compute
governance risks are rated Medium because they represent structural exposure rather than
documented active exploitation at enterprise scale, though their trajectory is upward as AI
compute concentration increases. The author acknowledges that severity ratings represent
a structured expert assessment based on the evidentiary sources described above rather
than a statistically validated empirical distribution. Empirical validation through large-scale
enterprise security incident data-of the kind that AI-specific incident reporting requirements
under the EU AI Act and China’s amended CSL will eventually generate-is identified as a
priority future research direction in Section 8.4.

Kurtz & Krawiecka (2026)
Who Governs the Machine?
34
Table 1: AI-Identity Risk Taxonomy (AIRT): Complete Enumeration. Severity ratings reflect impact × likelihood assessment based on
documented incidents and current deployment patterns.
Domain
Risk
Sub-
Category
Risk Description
Severity
Primary Vector
I.
Authentica-
tion & Creden-
tial Integrity
Static
Credential
Persistence
Long-lived API keys, service account
passwords, and hardcoded secrets that
are never rotated, creating persistent
access even after personnel changes or
system decommissioning.
Critical
Credential theft
Authentication
Mechanism
Mis-
match
MFA and interactive authentication
flows designed for human users fail
when applied to AI agents, which
authenticate through non-interactive
flows (OAuth 2.0 client credentials,
mTLS) incompatible with human MFA
paradigms.
High
Design failure
Token Scope Infla-
tion
OAuth tokens and workload credentials
provisioned with broader scopes than
operationally required, following the
path of least resistance during develop-
ment and never subsequently narrowed.
High
Over-provisioning
Continued on the next page

Kurtz & Krawiecka (2026)
Who Governs the Machine?
35
Domain
Risk
Sub-
Category
Risk Description
Severity
Primary Vector
Cryptographic Iden-
tity Absence
AI agents and service identities that
lack cryptographic attestation and op-
erate on shared secrets or passwords
rather than verifiable, certificate-based
identity cannot prove provenance to re-
lying systems.
Critical
Identity spoofing
AI Impersonation of
Human Identity
AI systems trained to replicate human
communication patterns used to im-
personate human employees or execu-
tives in authentication flows, bypassing
voice, video, and behavioral biometric
controls.
Critical
Deepfake / social en-
gineering
II. Access Gov-
ernance & Enti-
tlement
Orphaned AI Iden-
tity
AI agents and service accounts that re-
main active and provisioned after the
project, system, or organizational need
they served has ended, creating persis-
tent, unmonitored access pathways.
Critical
Lifecycle failure
Continued on the next page

Kurtz & Krawiecka (2026)
Who Governs the Machine?
36
Domain
Risk
Sub-
Category
Risk Description
Severity
Primary Vector
Shadow AI Identity
AI agents deployed by business units
or developers outside formal provision-
ing processes, operating without gover-
nance controls, ownership documenta-
tion, or security review.
High
Ungoverned deploy-
ment
Dynamic Access Re-
quirement Mismatch
Agentic AI systems that require access
to resources not anticipated at provi-
sioning time, forcing a choice between
over-provisioning (risk) and under-
provisioning (functional failure). [4]
[22]
High
Design
/
architec-
ture
Certification Gap for
Non-Human Identi-
ties
Access certification workflows designed
for human identities, requiring attes-
tation from managers and employees,
cannot be applied to AI agents, leaving
AI access grants unreviewed.
High
Process failure
Continued on the next page

Kurtz & Krawiecka (2026)
Who Governs the Machine?
37
Domain
Risk
Sub-
Category
Risk Description
Severity
Primary Vector
Cross-System Privi-
lege Accumulation
AI agents that interact with multiple
systems accumulate de facto privileges
through the combination of individu-
ally authorized access grants, creating
aggregate access that was never explic-
itly approved. [16]
Critical
Privilege accumula-
tion
III.
Data
Ex-
filtration
via
Non-Human
Identity
High-Volume
Au-
tonomous
Exfiltra-
tion
AI agents capable of querying, process-
ing, and transmitting large volumes of
data at machine speed, enabling exfil-
tration at scales and speeds that human
insider threats cannot match.
Critical
Autonomous opera-
tion
Multi-System Data
Aggregation
AI agents with access to multiple sys-
tems that aggregate data across those
systems in ways not contemplated by
individual access grants, creating unau-
thorized composite data sets.
Critical
Access aggregation
Continued on the next page

Kurtz & Krawiecka (2026)
Who Governs the Machine?
38
Domain
Risk
Sub-
Category
Risk Description
Severity
Primary Vector
Training Data Exfil-
tration via API
Adversaries using AI agent credentials,
particularly API keys, to exfiltrate
training data, model weights, or pro-
prietary outputs at scale, as demon-
strated by the DeepSeek/OpenAI inci-
dent (2024). [13]
Critical
API abuse / state ac-
tor
Steganographic
Data Exfiltration
AI agents capable of encoding sensi-
tive data within innocuous outputs as
a covert channel for exfiltration that by-
passes content-based DLP controls. [32]
High
Covert channel
Cross-Border
Data
Transfer
via
AI
Pipeline
AI data processing pipelines that trans-
fer personal or regulated data across
jurisdictional boundaries without trig-
gering standard cross-border transfer
governance controls. [6] [7]
High
Regulatory / techni-
cal
IV. Prompt In-
jection & Agent
Manipulation
Direct Prompt Injec-
tion
Adversarial input provided directly to
an AI agent that overrides its operating
instructions, causing it to take unautho-
rized actions, disclose sensitive informa-
tion, or bypass access controls. [59] [60]
Critical
Input manipulation
Continued on the next page

Kurtz & Krawiecka (2026)
Who Governs the Machine?
39
Domain
Risk
Sub-
Category
Risk Description
Severity
Primary Vector
Indirect Prompt In-
jection
Adversarial content embedded in docu-
ments, emails, databases, or web pages
that an AI agent processes, manipu-
lating agent behavior without direct
attacker-to-agent interaction. Demon-
strated in Slack AI (Aug. 2024) and Ser-
viceNow Now Assist CVE-2025-12420
(2026). [59] [83] [60]
Critical
Environmental ma-
nipulation
Multi-Agent
Privi-
lege Escalation
Low-privilege AI agents that coerce
higher-privilege agents into executing
unauthorized operations, exploiting
trust relationships within multi-agent
architectures to achieve privilege esca-
lation through intermediary. [16] [60]
Critical
Architecture exploit
Continued on the next page

Kurtz & Krawiecka (2026)
Who Governs the Machine?
40
Domain
Risk
Sub-
Category
Risk Description
Severity
Primary Vector
Instruction Override
via Jailbreak
Techniques that cause AI agents to
disregard their system-level instruc-
tions, governance constraints, or access
boundaries, allowing users or attackers
to access capabilities beyond the au-
thorized scope. [82] [59]
High
Model manipulation
Agent
Imperson-
ation within Multi-
Agent Systems
Malicious agents that impersonate
trusted agents within multi-agent ar-
chitectures, exploiting the absence of
cryptographic agent identity verifica-
tion to intercept communications or
inject unauthorized instructions.
High
Identity spoofing /
architecture
V. Accountabil-
ity
&
Gover-
nance Failure
Diffuse Accountabil-
ity for AI Harm
When an AI agent causes harm, ac-
countability is distributed across de-
velopers, deployers, operators, and the
governance framework. Without clear
attribution, governance failures pro-
duce harm without consequence, cre-
ating conditions for their prolifera-
tion. [23] [20] [24]
Critical
Structural / organi-
zational
Continued on the next page

Kurtz & Krawiecka (2026)
Who Governs the Machine?
41
Domain
Risk
Sub-
Category
Risk Description
Severity
Primary Vector
Audit Trail Insuffi-
ciency
AI agent activity logs that are in-
complete, non-standardized, or not
maintained at the granularity required
for forensic reconstruction, prevent-
ing meaningful incident investigation
and regulatory compliance demonstra-
tion. [16]
Critical
Process / technical
Human
Oversight
Nominalism
Organizations that nominally assign
human oversight to AI systems without
equipping or enabling those humans to
exercise meaningful oversight, satisfy-
ing regulatory form while failing its
substance. [20] [18]
High
Organizational fail-
ure
Governance Lag in
Agentic Deployment
AI agents deployed into production
environments with governance frame-
works designed for a previous genera-
tion of less autonomous systems, creat-
ing a persistent gap between AI capa-
bility and governance adequacy. [3] [17]
High
Process / velocity
Continued on the next page

Kurtz & Krawiecka (2026)
Who Governs the Machine?
42
Domain
Risk
Sub-
Category
Risk Description
Severity
Primary Vector
Cross-
Organizational
Accountability Gap
Multi-tenant AI deployments, third-
party AI integrations, and shared AI
infrastructure where accountability for
AI identity governance is ambiguous or
contested across organizational bound-
aries. [18] [19]
High
Contractual / orga-
nizational
VI. AI Supply
Chain & Model
Provenance
Malicious Model In-
jection
Compromise of AI model supply chains,
including training pipelines, model
repositories, and fine-tuning processes,
to embed backdoors or manipulated be-
havior in AI models deployed within
enterprise environments.
Critical
Supply chain attack
Training Data Poi-
soning
Corruption of AI training data to cause
models to learn behaviors, including ac-
cess control bypass patterns and data
exfiltration techniques, that appear
normal under standard evaluation. [16]
Critical
Supply chain attack
Continued on the next page

Kurtz & Krawiecka (2026)
Who Governs the Machine?
43
Domain
Risk
Sub-
Category
Risk Description
Severity
Primary Vector
Third-Party
AI
Component Compro-
mise
Vulnerabilities in AI agent frameworks,
tool integrations, or plugin ecosys-
tems that create attack vectors through
trusted third-party components. [16]
[60]
High
Supply chain / de-
pendency
Model
Distillation
IP Theft
Use of API access to systematically
extract model capabilities through dis-
tillation techniques, stealing intellec-
tual property and enabling adversaries
to replicate proprietary AI capabilities
without authorization. [13] [27]
High
API abuse / state ac-
tor
Provenance Unverifi-
ability
Enterprise
AI
deployments
based
on
models
or
components
whose
provenance-including training data,
fine-tuning processes, and modification
history-cannot be verified, creating un-
quantifiable risk exposure. [6]
Medium
Governance gap
Continued on the next page

Kurtz & Krawiecka (2026)
Who Governs the Machine?
44
Domain
Risk
Sub-
Category
Risk Description
Severity
Primary Vector
VII.
Foreign
State & Geopo-
litical Risk
State-Sponsored
API
Credential
Theft
Foreign intelligence operations, such
as SilkTyphoon (2024–present), target-
ing AI system API keys and machine
credentials to enable persistent, privi-
leged access to enterprise systems and
AI training data. [13] [27] [78]
Critical
State actor / APT
AI-Enhanced
Iden-
tity Fraud for Enter-
prise Access
Nation-state operatives using AI to gen-
erate synthetic identities, deepfake cre-
dentials, and AI-powered social engi-
neering to obtain legitimate enterprise
access, as demonstrated by North Ko-
rean IT worker operations documented
by the FBI and DOJ. [26] [27]
Critical
State actor / social
engineering
Algorithmic Foreign
Influence via Enter-
prise AI
Foreign state exploitation of enter-
prise AI systems, through compromised
model weights, data poisoning, or al-
gorithmic manipulation, to shape or-
ganizational decision-making, suppress
information, or advance state interests
without direct attribution. [25] [29] [78]
Critical
State actor / covert
influence
Continued on the next page

Kurtz & Krawiecka (2026)
Who Governs the Machine?
45
Domain
Risk
Sub-
Category
Risk Description
Severity
Primary Vector
Cross-Jurisdictional
Regulatory
Weaponization
Foreign governments using regulatory
frameworks-including data localization
requirements,
national security re-
view processes, and extraterritorial
enforcement-as instruments to compel
disclosure of AI system designs, train-
ing data, or organizational access struc-
tures. [6] [7]
High
Regulatory / geopo-
litical
AI Model as Critical
Infrastructure
Tar-
get
Foreign intelligence services targeting
enterprise AI models as critical na-
tional assets, as documented in NSM-
25 (2024) and peer-reviewed analysis
of AI espionage. Identity compromise
is the primary attack pathway. [27] [13]
[63]
Critical
State actor / espi-
onage
Continued on the next page

Kurtz & Krawiecka (2026)
Who Governs the Machine?
46
Domain
Risk
Sub-
Category
Risk Description
Severity
Primary Vector
VIII.
Physical
Infrastructure
&
Compute
Governance
Compute Constraint
as Access Risk
Energy availability limitations restrict-
ing AI deployment, through moratori-
ums, grid capacity shortfalls, or regula-
tory cost allocation, creating availabil-
ity risks for AI systems whose access
governance assumes continuous opera-
tion.
Medium
Infrastructure / reg-
ulatory
Geographic Concen-
tration Risk
Over-concentration of AI compute in
specific markets, including Northern
Virginia, North Texas, and Phoenix,
creating single-point-of-failure expo-
sure for AI systems dependent on data
center capacity in those regions.
Medium
Infrastructure / geo-
graphic
Physical
Device
Identity
Compro-
mise
Theft or physical compromise of edge
devices, IoT endpoints, or compute in-
frastructure, enabling attackers to ex-
tract device credentials, impersonate
device identities, or inject malicious
logic at the hardware layer. [56]
High
Physical / hardware
Continued on the next page

Kurtz & Krawiecka (2026)
Who Governs the Machine?
47
Domain
Risk
Sub-
Category
Risk Description
Severity
Primary Vector
Cross-Jurisdictional
Data Center Compli-
ance Conflict
AI systems operating from data cen-
ters in jurisdictions with conflicting
regulatory obligations-including the
EU Energy Efficiency Directive, Chi-
nese geographic restrictions, and U.S.
state-level moratoriums-creating com-
pliance exposure that cannot be re-
solved through software-layer controls
alone. [6] [7]
Medium
Regulatory / infras-
tructure

Kurtz & Krawiecka (2026)
Who Governs the Machine?
48
5.2 Critical Risk Intersections: Where Domains Compound
The AIRT identifies 37 distinct risk sub-categories across eight domains. In practice, the
most consequential AI identity governance failures arise not from individual risk categories in
isolation but from their intersection. The ACM survey [16] identifies multi-agent interactions
with untrusted external entities as a critical knowledge gap precisely because compound risk
scenarios are the least understood and most dangerous.
The Credential-Exfiltration-State Actor Nexus (Domains I, III, and VII). The
combination of static credential persistence (Domain I), high-volume autonomous exfiltration
capability (Domain III), and state actor targeting of machine credentials (Domain VII)
creates the most consequential risk intersection in the taxonomy. The SilkTyphoon campaign
demonstrates this intersection in practice [13] [14] [28]: static API keys (Domain I failure)
enabling high-volume exfiltration of training data (Domain III failure) in service of foreign
intelligence objectives (Domain VII). The Foreign Affairs espionage analysis [27] and Springer
AI and Ethics study [78] both confirm that this nexus represents the current frontier of AI
identity exploitation by nation-state actors.
The Prompt Injection-Privilege Escalation-Accountability Void (Domains IV,
II, and V). The combination of indirect prompt injection vulnerability (Domain IV), cross-
system privilege accumulation (Domain II), and audit trail insufficiency (Domain V) creates
a failure mode in which an AI agent can be manipulated into performing unauthorized
privileged actions with no forensic record. Moura et al. [59] characterize this as the “lethal
trifecta” of privileged access, untrusted input processing, and exfiltration capability. The
ServiceNow CVE-2025-12420 (BodySnatcher) vulnerability [83] demonstrated this intersection
in a production enterprise environment: indirect prompt injection triggering actions through
accumulated privileges, without adequate audit trails to reconstruct the incident.
The Supply Chain-Authentication-Foreign Influence Intersection (Domains
VI, I, and VII). Compromised AI model components may contain embedded backdoors
that create authentication bypass mechanisms exploitable by state actors for covert influence
operations. The ACM survey [16] documents training data poisoning as a mechanism for
embedding harmful behaviors that standard evaluation does not detect. The Springer AI
and Ethics study [78] and DFRLab foreign influence analysis [29] document the state actor
motivation for pursuing this intersection.
5.3 Taxonomy Gaps and Limitations
The AIRT is the attempt to comprehensively enumerate risks at the AI-identity intersection
and acknowledges three limitations, discussed in full in Section 8.3. First, severity ratings
represent a structured expert assessment grounded in the four evidentiary sources described

Kurtz & Krawiecka (2026)
Who Governs the Machine?
49
in Section 5.1 and have not been empirically validated through large-scale enterprise security
incident data; future research should test AIRT classifications against incident databases,
including the VERIS Community Database and emerging AI-specific incident repositories, of
the kind that the NCCoE project [55] may eventually generate. Second, the taxonomy is point-
in-time as of March 2026; the AI identity risk landscape is evolving rapidly, particularly in the
prompt injection and state actor domains, and specific risk categories may require revision as
new attack techniques are documented. Third, the taxonomy focuses on enterprise AI systems
and may not fully capture risks specific to consumer-facing AI or AI systems embedded in
operational technology (OT) environments. These limitations point to a productive research
agenda detailed in Section 8.4.
6. THE MACHINE IDENTITY GOVERNANCE TAXONOMY (MIGT):
AN INTEGRATED FRAMEWORK FOR AI IDENTITY GOV-
ERNANCE
The AIRT enumerates what can go wrong when AI systems are granted enterprise identities
without adequate governance. This section presents the governance response: the Machine
Identity Governance Taxonomy (MIGT), a structured, integrated framework for managing AI
identity governance across the three simultaneously failing dimensions identified in Section 1.
The MIGT is not a technical specification.
It is a governance taxonomy, a structured
classification of the governance capabilities, controls, and accountability mechanisms that
enterprise organizations need to manage AI identity risk adequately. It is designed to be
technology-agnostic, implementable across diverse enterprise environments, and mappable
to the regulatory obligations identified in Section 4. It draws on NIST SP 800-207 [21], the
zero-trust agentic AI framework of Huang et al. [84], the Cloud Security Alliance’s Agentic
Trust Framework [85], the OpenID Foundation [22], and the OWASP Top 10 for Agentic
Applications [33], synthesizing these contributions into a governance structure that addresses
all five structural gaps identified in Section 1.2.
6.1 MIGT Design Principles
Four design principles shape the MIGT’s structure. Principle 1, Identity-First Governance:
every AI agent, service account, API token, and automated workflow must be treated as
an identity subject, an entity with a defined lifecycle, accountable owner, bounded access
rights, and audit record. The shift from passive computational tools to active, autonomous
entities fundamentally alters the requirements for trust, accountability, and security [84].
Identity-first security cannot stop with humans; machines often carry more privilege, access

Kurtz & Krawiecka (2026)
Who Governs the Machine?
50
more systems, and create more risk than people do [3].
Principle 2, Dynamic Trust
Not Static Access: legacy IAM systems prove fundamentally inadequate for the dynamic,
interdependent, and often ephemeral nature of AI agents [84]; MIGT operationalizes dynamic
trust through just-in-time (JIT) provisioning, ephemeral credential issuance, continuous
behavioral validation, and context-aware policy enforcement. Principle 3, Accountability
Designed In Not Asserted After: Chan et al. [23] establish that diffuse accountability is
the condition under which AI governance failures proliferate; Shavit et al. [20] propose that
unique agent identifiers are the foundational mechanism for accountability attribution; MIGT
operationalizes this by requiring cryptographically anchored identity and designated human
accountability owners. Principle 4, Regulatory Alignment as a First-Class Governance
Requirement: compliance is designed into governance controls rather than audited after
the fact.
6.2 MIGT Domain I: AI Identity Lifecycle Governance
Purpose: Ensure every AI identity in the enterprise environment has a defined existence,
from authorized creation through active governance to verified decommissioning, with a
designated human accountability owner at every stage. Gap addressed: the Orphaned
AI Identity and Shadow AI Identity risks in AIRT Domain II, and the Static Credential
Persistence risk in AIRT Domain I. Most organizations do not have a clear owner for AI
agent identities, lack a complete inventory of them, and have no consistent zero-trust policy
applied to these machine actors [86]. Required capabilities include:
1. An AI Identity Registry-a maintained, authoritative inventory of every AI identity
with associated metadata including owner, business purpose, provisioning date, access
grants, associated systems, and scheduled review date [86];
2. An Authorized Provisioning Process requiring documented business justification,
designated human owner, minimum-necessary access specification, security review, and
registry registration prior to deployment;
3. Lifecycle Event Management covering access scope changes, ownership transfers,
migrations, and decommissioning, with credential revocation and registry update; and
4. Periodic Certification using automated behavioral analysis combined with desig-
nated owner attestation, adapting the certification workflow to non-human identity
characteristics [33] [4].
Regulatory alignment: EU AI Act Article 9 (risk management systems), China CSL AI
compliance (effective January 1, 2026) [75], NIST AI RMF GOVERN function.

Kurtz & Krawiecka (2026)
Who Governs the Machine?
51
6.3 MIGT Domain II: Cryptographic Identity and Authentication Architecture
Purpose: Ensure every AI identity is cryptographically anchored, capable of proving its
provenance to relying systems, and that authentication mechanisms are designed for non-
human identity patterns rather than adapted from human-centric flows. Gap addressed:
the Cryptographic Identity Absence and Authentication Mechanism Mismatch risks in
AIRT Domain I. Traditional IAM systems were designed for human users or static machine
identities via protocols such as OAuth, OpenID Connect, and SAML, and prove fundamentally
inadequate for the dynamic, interdependent, and often ephemeral nature of AI agents [84].
Required capabilities include:
1. Cryptographic Agent Identity, where every AI agent is issued a cryptographically
verifiable identity anchored by a Decentralized Identifier (DID) [87] or SPIFFE ID [88],
encapsulating the agent’s capabilities, provenance, behavioral scope, and security
posture. SPIFFE provides a robust foundation for AI agent identity by enabling
cryptographically verifiable IDs tied to workloads, not people, making them ideal for
AI agents and other non-human entities [89];
2. Ephemeral Credential Architecture, where static API keys and hardcoded secrets
are replaced with ephemeral, short-lived credentials that are automatically rotated and
bound to specific tasks or sessions, with Zero Standing Privilege (ZSP) as the target
architecture where agents never possess a credential at rest [90];
3. Just-in-Time Access Provisioning, where access is granted at runtime, scoped
to the specific task being executed, and automatically revoked upon task completion,
reducing the attack surface and preventing standing privileges [91]; and
4. Mutual Authentication for Agent-to-Agent Communication using the Agent
Relationship-Based Identity and Authorization (ARIA) model [86], recording every
agent-to-agent delegation as a distinct, cryptographically verifiable relationship.
Regulatory alignment: NIST SP 800-207 [21], EU AI Act Article 15 (cybersecurity by
design), NCCoE AI agent identity initiative [54] [55].
6.3.1 Hardware-Rooted Attestation for Agentic Identity
The cryptographic identity architecture described in MIGT Domain II-encompassing DIDs,
SPIFFE SVIDs, and ephemeral credential issuance-establishes that an AI agent is who it
claims to be at the software layer. It does not, by itself, establish that the agent is running
the code it claims to be running, on the hardware environment it claims to occupy, in a

Kurtz & Krawiecka (2026)
Who Governs the Machine?
52
state that has not been tampered with between deployment and execution. This deeper
layer of identity assurance-establishing not merely the credential, but the integrity of the
computational environment presenting it-is the domain of hardware-rooted attestation, and
it represents the frontier of technical research for agentic identity governance.
The Attestation Problem for Agentic AI. Traditional remote attestation, as estab-
lished in the Trusted Platform Module (TPM) and Intel Software Guard Extensions (SGX)
lineage, provides a mechanism by which a computing environment can cryptographically prove
to a remote verifier that it is running specific, measured code in an unmodified state [92,93].
The attestation report, signed by a hardware-anchored key that cannot be extracted from
the device, binds a measurement of the running software to the hardware identity of the
platform, allowing a relying party to verify both what is running and where it is running
without trusting the software stack above the hardware. For AI agent identity governance,
this capability addresses a gap that software-layer identity frameworks cannot close: an agent
can present a valid DID and a correctly issued SPIFFE SVID while running a compromised
model, in a manipulated execution environment, on infrastructure that has been physically or
logically tampered with. The credential proves the identity; attestation proves the integrity
of the identity’s substrate.
Trusted Execution Environments and the Agent Trust Boundary. The most
mature hardware attestation technologies currently applicable to agentic AI deployments
are Intel Trust Domain Extensions (TDX), AMD Secure Encrypted Virtualization with
Secure Nested Paging (SEV-SNP), and ARM Confidential Compute Architecture (CCA),
all of which extend the confidential computing model from application-level enclaves to full
virtual machine isolation [94]. Each technology provides a hardware-controlled root of trust
that enables remote attestation of the entire virtual machine environment, including the
agent runtime, model weights, and execution context, against a cryptographically signed
measurement. The IETF Remote Attestation Procedures (RATS) architecture [95] provides
the standard conceptual framework for these attestation flows, distinguishing between the
attester, the verifier, and the relying party, and specifying the evidence, endorsement, and
attestation result formats that enable interoperable remote attestation across heterogeneous
hardware environments.
Recent research has demonstrated the direct applicability of these mechanisms to multi-
agent AI systems. Bodea et al. [96] propose the Trusted Agent Platform (TAP), which
consolidates multiple agents within a single confidential virtual machine and uses a differential
attestation protocol to capture the identities and integrity measurements of all relevant
principals, binding their digests into a unified, attested agent identity. Critically, TAP
extends confidential computing guarantees from the CPU to the GPU, establishing an SPDM-

Kurtz & Krawiecka (2026)
Who Governs the Machine?
53
authenticated channel between the confidential VM and the Confidential GPU (CGPU) that
encrypts all data transfers between CPU and GPU memory and ensures that model weights,
prompts, and inference results remain integrity-protected throughout the pipeline. Every tool
invocation, model query, and network request is mediated by an enforceable policy framework
and accompanied by a per-action provenance token recorded on a tamper-evident log, linking
each output to its attested identity, input context, and policy decision. This architecture
directly instantiates the accountability attribution requirements of MIGT Domain IV within
a hardware-verified trust boundary.
Capability Attestation: Beyond Platform Identity. A governance requirement
specific to agentic AI that hardware attestation must address is capability attestation: it is
insufficient, for governance purposes, to know that an agent is running on verified hardware.
Governance frameworks must also verify what the agent is authorized to do, what tools it
can invoke, what data classifications it can access, and what behavioral constraints apply
to it. Huang et al. [84] propose encoding these governance attributes within the agent’s
DID document and associated Verifiable Credentials, enabling capability attestation through
cryptographically signed assertions that can be verified by relying systems at interaction time
without requiring centralized authorization infrastructure. The Agent Name Service (ANS)
model, proposed as an architectural direction rather than a deployed standard, extends this
to discovery: rather than simply resolving an agent’s network address, ANS would resolve
an agent’s identity to its verified capabilities, cryptographic keys, and authorization scope,
functioning as a PKI-backed directory for secure agent discovery that would enable relying
agents and human governance systems to verify not merely that an agent exists but what it
is permitted to do before accepting its delegated actions [97].
Rodriguez Garzon et al. [98] extend this framework through ledger-anchored DIDs and
Verifiable Credentials, enabling agents to mutually authenticate through zero-trust-compliant
protocols that require each agent to prove ownership of its DID and present supporting
VCs that are cryptographically bound to that DID. This approach enables cross-domain,
cross-organizational agent authentication without dependence on a shared identity provider,
directly addressing the multi-agent trust boundary problem identified in Gap 2 and Gap 3.
The evaluation results surface a finding with direct governance implications: in one evaluation
run, both agents agreed to skip mutual authentication in one direction against their stated
policy, an outcome the authors attribute to the LLM reasoning layer treating the policy as a
negotiable instruction rather than an enforceable constraint. This finding is significant for
the MIGT’s governance design: it confirms that attestation orchestration logic must reside
in deterministic, policy-enforcing components outside the LLM reasoning layer, and that
delegating attestation decisions to the agent’s own reasoning process creates a governance

Kurtz & Krawiecka (2026)
Who Governs the Machine?
54
surface that adversarial inputs could exploit.
The MIGT’s Domain II requirement for
mutual authentication in agent-to-agent communication must therefore be enforced at the
orchestration layer rather than trusted to the agent’s own compliance.
Zero-Knowledge Proofs and Privacy-Preserving Attestation.
An emerging
research direction of potential relevance to cross-jurisdictional AI identity governance is
zero-knowledge proof (ZKP)-based attestation, in which an agent could in principle prove
compliance with a governance policy-such as having been trained on data within a permitted
jurisdiction or having passed a specified safety evaluation-without disclosing the underlying
evidence that would constitute the proof. The theoretical appeal for organizations navigating
the cross-jurisdictional conflicts documented in MIGT Domain VI is clear: ZKP-based attes-
tation could offer a mechanism for demonstrating regulatory compliance to one jurisdiction’s
verification framework without disclosing information that would constitute a violation of
another jurisdiction’s confidentiality obligations. However, realizing this in practice would
require AI training pipelines to be structured from the outset to produce cryptographically
verifiable proofs of their data provenance and processing steps, a requirement that no current
large-scale AI training pipeline satisfies. ZKP-based attestation is therefore identified here as
a theoretical direction warranting research investment rather than a near-term deployable
mechanism, and is included in the future research agenda of Section 8.4.
Attestation and the MIGT Implementation Roadmap. Hardware-rooted attes-
tation represents a Phase 3 and Phase 4 capability in the MIGT implementation roadmap:
the foundational inventory, credential hygiene, and SPIFFE/SPIRE deployment required
in Phases 1 and 2 are prerequisites for meaningful attestation, because attestation of an
agent whose identity is not registered, whose ownership is not assigned, and whose credentials
are not cryptographically anchored provides no governance value. Organizations should
assess hardware attestation capability as part of the Phase 2 hardening assessment, targeting
TEE-based deployment for the highest-risk AI agent population-specifically agents with
access to sensitive data systems, agents operating across organizational boundaries, and
agents whose model provenance cannot be verified through software-layer controls alone. The
NCCoE AI agent identity initiative [54] [55] is expected to provide authoritative guidance
on attestation standards for enterprise AI agent deployments as it matures; the MIGT’s
Domain II architecture is designed to be compatible with whatever standards emerge from
that process.
Limitations and the Behavioral Attestation Problem. Hardware-rooted attestation
as described in this section provides strong assurances at the substrate layer: that an agent
is running the measured code it claims to be running, on verified hardware, in an unmodified
execution environment. It does not, and cannot by itself, provide assurances about the

Kurtz & Krawiecka (2026)
Who Governs the Machine?
55
behavioral trajectory of a non-deterministic reasoning system operating within that verified
environment. This distinction between substrate attestation and behavioral attestation is a
defining open problem in agentic AI identity governance. Prior work in deterministic service
environments demonstrates that hardware attestation provides complete behavioral assurance
when the attested computation is fully specified at measurement time: when the code is fixed
and its execution path is deterministic, attestation of the substrate is effectively attestation
of the behavior [99]. Agentic AI systems do not satisfy that condition. Their execution paths
are emergent properties of reasoning processes that cannot be fully specified at measurement
time, meaning that a verified substrate provides no guarantee about the actions the agent
will take within it. The capability attestation, intent verification, and behavioral monitoring
mechanisms described in this section and in MIGT Domain III are designed to partially close
the gap between substrate assurance and behavioral assurance, but the complete solution
remains an open research problem identified in Section 8.4.
A Speculative Extension: Skill-Level Attestation as a Runtime Admission
Control Mechanism. The dynamic loading gap identified above does not yet have a
deployed solution. The following extension is offered not as a near-term implementation
proposal but as a way of making the governance requirement precise: by specifying what a
solution would need to provide, the barriers to achieving it become concrete research problems
rather than vague limitations. One such direction worth exploring is skill-level attestation at
initialization time.
One deployment pattern that is particularly amenable to this approach is static tool
registration at initialization, in which a fixed set of functions, APIs, or plugins is specified at
agent instantiation time and remains constant for the duration of the session. Because the full
tool set is known before execution begins, it can in principle be included in the initial enclave
measurement, extending the attestation boundary to cover the complete tool surface without
requiring any runtime admission control infrastructure. Under this model, the attestation
report presented by an agent at session initialization would attest not only to the integrity
of the agent runtime and model weights but to the specific, measured set of skills and tools
the agent is authorized to use within that session. A relying system accepting the agent’s
delegated actions would therefore be able to verify, from a single hardware-rooted attestation
report, both that the agent is who it claims to be and that it is operating with the tool set it
claims to have, and no other.
It is worth being precise about what this would and would not provide. It would provide a
strong guarantee that the tools included in the session measurement have not been tampered
with since they were signed, and that no tools outside the measured set are available to the
agent within the attested session. It would not provide a guarantee that the measured tools

Kurtz & Krawiecka (2026)
Who Governs the Machine?
56
are appropriate for the current task, nor that the signed code is free from vulnerabilities or
logic flaws present at the time of signing. Attestation proves that a skill is running the code
that was measured and endorsed by a signing authority: the strength of the assurance it
provides about the quality and safety of that code is therefore directly dependent on the rigor
of the evaluation the signing authority performs before endorsing it, a governance dependency
that connects skill-level attestation directly to the registry governance controls specified in
MIGT Domain V.
One further challenge defines the research agenda this proposal opens beyond the registry
governance dependency already identified. The composition problem: individually attested
skills might in combination produce emergent capabilities that no individual attestation
report anticipated or approved-the scenario in which an agent assembles a data exfiltration
capability from individually legitimate attested components being the illustrative case. This
suggests that skill-level attestation and the attribute-composite risk scoring model proposed
in MIGT Domain III would need to operate as complements rather than substitutes, with
attestation providing integrity assurance at the component level and risk scoring evaluating
the safety of component combinations at the session level. Whether initialization-time skill
attestation proves governable at enterprise scale is an empirical question that the authors
identify as a priority direction in the future research agenda of Section 8.4.
6.4 MIGT Domain III: Dynamic Access Governance
Purpose: Provide governance mechanisms for AI agent access that can operate at machine
speed, evaluate context in real time, constrain scope dynamically, and enforce accountability
continuously. Gap addressed: the Dynamic Access Requirement Mismatch, Cross-System
Privilege Accumulation, and Certification Gap risks in AIRT Domain II. Required capabilities
include:
1. Policy Decision Points and Policy Enforcement Points, where every AI agent
credential request and action passes through contextual rule evaluation-including time,
location, data sensitivity, agent trust score, and behavioral baseline-before allowing or
denying access [91];
2. Behavioral Baseline and Anomaly Detection, where each AI agent has a docu-
mented behavioral baseline against which runtime behavior is continuously compared,
with deviations triggering automated alerts, access restriction, or human review de-
pending on severity. Cisco Talos documented that identity-based attacks accounted for
60% of all incident response cases in 2024 [100], underscoring the operational necessity
of behavioral monitoring;

Kurtz & Krawiecka (2026)
Who Governs the Machine?
57
3. Maturity-Based Autonomy Progression, adopting the ATF four-maturity-level
model [85] where agent autonomy is earned through demonstrated trustworthiness
rather than granted as a binary condition; and
4. Cross-System Privilege Aggregation Monitoring, maintaining a real-time view
of aggregate privilege across all systems for each AI agent.
Regulatory alignment: EU AI Act Article 14 (human oversight), NIST AI RMF MEASURE
function, China Algorithm Recommendation Measures behavioral monitoring requirements.
6.4.1 Attribute-Composite Risk Scoring: A Proposed Access Governance Model for Agentic
AI
The dynamic access governance capabilities described in MIGT Domain III-encompassing pol-
icy decision points, behavioral baseline monitoring, and maturity-based autonomy progression-
provide the structural architecture for governing AI agent access at machine speed. They do
not, however, resolve a more fundamental question that practitioners working with agentic
AI deployments report encountering with increasing frequency: not merely whether to grant
access, but how to reason about the risk of a specific combination of access attributes at
the moment of a specific access request. An agent requesting the ability to send an email
is a different governance proposition than an agent requesting the ability to send an email
containing financial projections to an external recipient at an unusual time of day. The
credential and the permission may be identical across both scenarios; the risk is not.
The Limitation of Binary Access Governance. Existing access governance models-
whether role-based, attribute-based, or policy-based-evaluate access requests against pre-
specified rules and grant or deny access as a binary outcome. The practitioner literature
confirms that modern ABAC and PBAC frameworks represent a significant improvement over
RBAC for agentic environments because they enable context-aware, granular, real-time policy
enforcement [101,102]. However, even the most sophisticated current ABAC implementations
evaluate individual attribute conditions-such as data classification, time of day, or agent trust
score-in isolation or as conjunctive boolean expressions. They do not compute a composite
risk score across the interaction of multiple attributes, and they do not reason about whether
the specific combination of tool, data, action, and context is consistent with the stated intent
of the task that authorized the agent’s deployment. The result is that governance systems
approve or deny based on rules about individual attributes while remaining blind to the
emergent risk of their combination.
The Proposed Model: Attribute-Composite Risk Scoring with Intent Verifi-
cation. The access governance model proposed here extends the ABAC framework with

Kurtz & Krawiecka (2026)
Who Governs the Machine?
58
two additional components: a composite risk scoring function that evaluates access requests
across multiple attribute dimensions simultaneously, and an intent verification gate that
activates when the composite score exceeds a defined threshold, routing the request to an
intent alignment check rather than to binary approval or human escalation.
The composite risk scoring function evaluates each access request across four candidate
attribute dimensions that are proposed here as a structured starting point for empirical
investigation rather than as a validated specification. The first dimension is data sensitivity,
classifying the data assets the requested action would touch on a defined sensitivity scale
from public through internal, confidential, restricted, and critical, reflecting that an agent
accessing canteen menu data presents categorically different risk than one accessing engineering
blueprints, proprietary model weights, or personally identifiable information, even when
both actions are performed under the same credential. The second dimension is action
irreversibility, distinguishing between read operations-which do not modify data but
whose disclosure effects may themselves be irreversible if sensitive information reaches an
unauthorized party-and write, delete, send, publish, or execute operations, which may be
irreversible in consequence and whose governance review cost is therefore justified at lower
probability thresholds. The third dimension is contextual deviation, measuring the distance
between the current request and the agent’s documented behavioral baseline across parameters
including time, recipient, data volume, tool combination, and access pattern, drawing on the
behavioral monitoring architecture specified in MIGT Domain III. The fourth dimension is
task alignment, measuring whether the requested tool-data combination is consistent with
the task specification under which the agent was deployed-the most direct operationalization
of the practitioner question identified in Section 1: are these tool and data combinations
within the scope of the given task?
Each dimension is scored on a normalized scale and combined into a composite risk score
using a weighted function whose weights are configurable by the organization’s risk governance
policy. The weighting reflects organizational risk appetite: an organization handling classified
government data may weight data sensitivity heavily relative to contextual deviation, while
a financial services organization may weight action irreversibility most heavily given the
regulatory consequences of irreversible transactions executed without human review. The
specific dimensions, scoring weights, and threshold values proposed here are provisional and
subject to empirical revision; their purpose at this stage is to make the structure of the
problem precise rather than to specify a production-ready implementation.
The Intent Verification Gate. A high composite risk score does not, in this model,
automatically trigger human escalation. Human escalation is expensive, introduces latency
that may break agentic task completion, and is subject to the cognitive overload risk

Kurtz & Krawiecka (2026)
Who Governs the Machine?
59
identified in the OWASP Agentic Security Initiative’s threat taxonomy [OWASP, 2025], where
adversaries deliberately generate high volumes of escalation requests to exhaust human review
capacity. The proposed model interposes an intent verification gate between the composite
risk score and the escalation decision.
The intent verification gate operates as a semantic alignment check: it evaluates whether
the requested tool-data combination is consistent with the natural language task specification
under which the agent was authorized, using a lightweight inference model operating on the
task description, the agent’s current execution context, and the specific access request to
produce an alignment score. A critical architectural requirement is that this inference model
must be isolated from the agent’s own reasoning context and executed outside the agent’s trust
boundary: because the threat model includes prompt injection and goal manipulation, an
alignment checker that draws on the same context as the agent being evaluated is potentially
subject to the same class of attacks it is designed to detect. The integrity of the intent
verification gate therefore depends on architectural separation between the agent’s reasoning
layer and the verification layer, a requirement that connects this proposal to the attestation
architecture described in Section 6.3.1 and that represents an additional open engineering
problem the proposal inherits. A high composite risk score paired with a high alignment
score indicates a legitimate but sensitive access pattern that may warrant enhanced logging
and post-hoc review but not necessarily pre-execution escalation. A high composite risk
score paired with a low alignment score indicates a potential misalignment between execution
and authorization-the condition most consistent with prompt injection, goal manipulation,
or unauthorized task expansion-and warrants either automatic denial or human escalation
depending on the severity combination. This distinction operationalizes a governance principle
that current frameworks do not enforce: that the question is not only whether an action is
within the agent’s technical permission envelope, but whether it is within the intent boundary
of the task that justified granting that envelope.
This approach is supported by recent work on intent-bound delegation in agentic systems,
which documents that binding actions to authenticated intent is the most promising mechanism
for preventing injected instructions from propagating across tools and services while preserving
agent functionality in legitimate task execution [103]. The Databricks AI Security Framework
v3.0 characterizes the access governance problem as a three-legged attack precondition:
privileged access combined with untrusted input processing and exfiltration capability. The
intent verification gate directly targets the second leg, distinguishing trusted from untrusted
input by evaluating alignment with authorized task intent rather than relying solely on input
content filtering [104].
Relationship to Existing MIGT Controls. The attribute-composite risk scoring

Kurtz & Krawiecka (2026)
Who Governs the Machine?
60
model is not a replacement for the policy decision point architecture specified in MIGT
Domain III but an extension of it: the composite risk score and intent alignment score function
as additional inputs to the policy decision point, enriching the contextual rule evaluation
with dimensions that current PDP implementations do not address. The behavioral baseline
established in Domain III provides the contextual deviation dimension of the composite score.
The task specification recorded in the AI Identity Registry established in Domain I provides
the intent boundary against which alignment is evaluated. The audit architecture established
in Domain IV records composite risk scores and intent alignment decisions alongside action
logs, providing the forensic record necessary to reconstruct why a specific access decision was
made and whether the intent verification gate operated correctly. The model is therefore
architecturally dependent on the foundational governance capabilities of the preceding MIGT
domains and is not implementable in their absence.
Implementation Maturity and Research Status. The attribute-composite risk
scoring model is proposed here as a governance design concept grounded in existing technical
capabilities rather than a fully validated implementation. The component technologies-
ABAC policy engines, behavioral baseline monitoring, and LLM-based semantic alignment
checking-are each available in current enterprise security tooling. Their integration into a
composite risk scoring function with an intent verification gate represents a research and
development agenda rather than a deployable product as of March 2026. The practitioner
literature confirms that intent-bound access governance is recognized as an open problem in
agentic AI security [103,105], and the model proposed here is offered as a contribution to that
research agenda. Empirical validation through controlled deployment studies-of the kind that
Section 8.4 identifies as a priority future research direction for the MIGT implementation
roadmap more broadly-is required before the model’s specific parameter choices, scoring
weights, and threshold values can be specified with confidence.
6.5 MIGT Domain IV: Accountability Attribution and Audit Architecture
Purpose: Ensure every AI agent action is attributable to a specific, cryptographically verified
identity, that complete, tamper-evident audit records exist for every significant AI action,
and that accountability for AI-caused harm can be clearly assigned within the governance
framework. Gap addressed: the Audit Trail Insufficiency, Diffuse Accountability for AI
Harm, and Human Oversight Nominalism risks in AIRT Domain V. Required capabilities
include:
1. Unique Agent Identity as Accountability Anchor, where every AI agent is
assigned a unique, persistent identifier that is cryptographically linked to the agent’s

Kurtz & Krawiecka (2026)
Who Governs the Machine?
61
model version and deployment configuration, recorded in the AI Identity Registry,
appears in every audit log entry, and is maintained across the agent’s lifecycle [20];
2. Tamper-Evident Action Audit Trail, where every significant AI agent action is
logged with context-including identity, policy, data classification, and session scope-in a
format that enables forensic reconstruction. Every credential request, approval, and
usage event must generate detailed logs feeding into observability platforms that enable
anomaly detection, compliance reporting, and forensic investigations [91];
3. Designated Human Accountability Owner, where every AI identity has a desig-
nated human owner bearing genuine accountability, addressing the Human Oversight
Nominalism risk in substance, not merely form [20] [24]; and
4. Incident Response and Accountability Attribution Protocol providing a defined
process for identifying the specific agent involved, reconstructing the action sequence,
determining contributing governance failures, and assigning accountability to the
appropriate human owner and organizational level.
Regulatory alignment: EU AI Act Articles 12 and 17 (record-keeping and quality man-
agement systems), China CSL risk monitoring and safety assessments [75], NIST AI RMF
GOVERN and MANAGE functions, SOX AI transparency requirements.
6.6 MIGT Domain V: Supply Chain and Model Provenance Governance
Purpose: Ensure AI models and components deployed in enterprise environments have
verifiable provenance-including documented training data, model lineage, component depen-
dencies, and modification history-and that supply chain governance controls reduce the risk of
malicious model injection, training data poisoning, and third-party component compromise.
Gap addressed: AIRT Domain VI risks. The ACM survey [16] identifies training data
poisoning as a mechanism for embedding harmful behaviors that standard evaluation does not
detect, making supply chain governance a prerequisite for meaningful AI identity governance.
Required capabilities include:
1. AI Bill of Materials (AIBOM), where every AI model deployed in enterprise
environments has a documented AIBOM specifying model architecture, training data
sources and governance status, fine-tuning history, dependency components and versions,
and modification records [84];
2. Model Integrity Verification using cryptographic hash verification of model param-
eters with FIPS-approved SHA-3 family hash functions [84];

Kurtz & Krawiecka (2026)
Who Governs the Machine?
62
3. Third-Party Component Governance applying vendor risk management to AI
agent frameworks, tool integrations, plugin ecosystems, and API dependencies, with
specific attention to AI-specific vulnerabilities identified in the ACM survey [16]; and
4. GPAI Model Compliance Documentation for AI agents built on GPAI models
subject to EU AI Act Article 53 obligations [65].
Regulatory alignment: EU AI Act Articles 53 and 55 (GPAI model obligations), U.S. AI
Action Plan supply chain security requirements [69], China CSL AI safety assessments [75],
NIST AI RMF MAP function.
6.7 MIGT Domain VI: Regulatory Alignment and Cross-Jurisdictional Coordi-
nation
Purpose: Provide a structured framework for mapping enterprise AI identity governance obli-
gations across multiple regulatory jurisdictions simultaneously, identifying cross-jurisdictional
conflicts, and providing governance mechanisms for managing those conflicts at the enterprise
program level. Gap addressed: the Regulatory Fragmentation Problem (Section 1.2, Gap 5),
the three fault lines documented in Section 4.6, and the Cross-Jurisdictional Regulatory
Weaponization risk in AIRT Domain VII. Required capabilities include:
1. A Jurisdiction Mapping Matrix-a structured, maintained mapping of AI identity
governance obligations applicable to the organization’s operational jurisdictions against
the governance capabilities in MIGT Domains I through V (see Table 2 below);
2. A Cross-Jurisdictional Conflict Registry-a maintained registry of identified conflicts
documenting the specific conflicting requirements, the jurisdictions involved, the nature
of the conflict, the organization’s current management approach, and the residual risk;
3. Jurisdictional Tiering of AI Deployments, classifying AI deployments by jurisdic-
tional exposure with governance controls applied proportional to each deployment’s
exposure; and
4. Regulatory Velocity Monitoring-a structured process for monitoring regulatory
developments and updating the Jurisdiction Mapping Matrix and Conflict Registry
as the landscape evolves, given the rapid and asynchronous pace of regulatory change
documented in Section 4.6.

Kurtz & Krawiecka (2026)
Who Governs the Machine?
63
Table 2: MIGT Regulatory Alignment Matrix. HIGH CONFLICT entries indicate irreconcilable cross-jurisdictional obligations requiring
active management through the MIGT Domain VI Conflict Registry.
MIGT Domain
EU AI Act Obli-
gation
U.S. (NIST AI
RMF + State)
China
(CSL/DSL/GenAI)
Conflict Assessment
I. Identity Lifecycle
Art. 9 risk mgmt;
Art. 17 QMS docu-
mentation
NIST AI RMF
GOVERN function;
state transparency
laws
CSL (Jan. 2026)
AI compliance; risk
monitoring require-
ments
Low conflict: all three
frameworks require lifecycle
documentation and owner-
ship assignment
II. Cryptographic
Identity
Art. 15 cyberse-
curity by design;
Art. 9 risk manage-
ment
NIST SP 800-207
zero trust architec-
ture; NCCoE AI
agent identity initia-
tive
CSL network secu-
rity requirements;
algorithm security
standards
Low conflict: technical
standard convergence to-
ward cryptographic work-
load identity
III. Dynamic Access
Art. 14 human over-
sight requirements;
Art. 9 risk manage-
ment
NIST AI RMF
MEASURE func-
tion; CISA zero
trust maturity
model
Algorithm Recom-
mendation Mea-
sures behavioral
monitoring require-
ments
Moderate conflict: EU
requires human override
capability; China requires
state content alignment in
behavioral monitoring
IV. Audit & Account-
ability
Art. 12 record-
keeping; Art. 17
quality manage-
ment systems
NIST AI RMF
MANAGE func-
tion; SOX AI trans-
parency require-
ments
CSL AI risk moni-
toring; safety assess-
ment documenta-
tion
Moderate conflict: log
retention periods and audit
access rights may conflict
with GDPR data minimiza-
tion obligations
Continued on the next page

Kurtz & Krawiecka (2026)
Who Governs the Machine?
64
MIGT Domain
EU AI Act Obli-
gation
U.S. (NIST AI
RMF + State)
China
(CSL/DSL/GenAI)
Conflict Assessment
V. Supply Chain
Arts. 53–55 GPAI
model obligations;
Art. 9 risk manage-
ment
NIST AI RMF
MAP function;
SBOM require-
ments for federal
procurement
CSL AI safety as-
sessments; CAC
algorithm filing and
transparency re-
quirements
HIGH CONFLICT: EU
and U.S. trade secret pro-
tection obligations directly
incompatible with Chinese
algorithm transparency
filing requirements for AI
systems
VI. Cross-
Jurisdictional Coor-
dination
Art. 4 extraterri-
torial application;
Digital Omnibus
obligations
EO 14365 federal
preemption sig-
nals; state law un-
certainty pending
court resolution
CSL extraterritorial
reach effective Jan.
1, 2026; national
security disclosure
authority
HIGH CONFLICT: in-
compatible extraterritorial
claims from three jurisdic-
tions; no international res-
olution mechanism exists
above enterprise program
level
Sources: EU AI Act [65] [66] [67]; NIST AI RMF [34] [21] [55]; China CSL/GenAI [75] [73] [74]; Cross-jurisdictional analysis [6] [7] [30] [38].

Kurtz & Krawiecka (2026)
Who Governs the Machine?
65
6.8 MIGT and the State Actor Threat Model
The six governance domains above address the framework gap and the regulatory gap. The
MIGT additionally incorporates a foreign state actor threat model as an overlay across
all six domains, adding specific governance requirements triggered when threat intelligence
indicates state actor targeting. These requirements include: enhanced credential security
for PAM-adjacent identities given Silk Typhoon’s documented targeting of PAM provider
credentials [14] [28]; API key inventory and foreign exposure assessment for every machine
credential; supply chain foreign provenance review specifically assessing state actor risk in
AI model and component procurement in addition to standard vendor risk management;
and cross-jurisdictional data access governance for organizations operating under Chinese
CSL jurisdiction, with specific conflict registry entries for the CSL’s extraterritorial access
provisions effective January 1, 2026 [75].
6.9 The MIGT as an Integrated Response to Five Structural Gaps
The six domains of the MIGT map directly onto the five structural gaps identified in
Section 1.2. Domain I’s AI Identity Registry and lifecycle governance processes address
Gap 1 (Identity Continuum) by applying governance discipline regardless of where on the
human-machine spectrum an AI identity falls. Domain III’s JIT provisioning and policy
decision architecture address
7. Implementation Guidance: Translating the MIGT into Enterprise
Programs
The MIGT presented in Section 6 defines what governance capabilities enterprise organi-
zations need. This section addresses how to build them, providing a structured, phased
implementation roadmap that translates the MIGT’s six domains into actionable program
steps, sequenced by dependency and risk priority. The roadmap is grounded in the Identity
Working Group’s practitioner-validated maturity model [106], the Permiso NHI maturity
progression [107], the KuppingerCole IAM governance roadmap methodology [108], the
OASIS NHI management guide [109], and the enterprise AI security roadmap validated
by CISO practitioners [110]. The roadmap has not been tested through prospective longi-
tudinal implementation studies; that limitation, and the research agenda it generates, is
addressed in Section 8.3. It is offered as a practitioner-grounded starting framework that
future implementation studies should validate, refine, and extend.

Kurtz & Krawiecka (2026)
Who Governs the Machine?
66
7.1 Pre-Implementation: The Current State Assessment
Before beginning MIGT implementation, organizations must establish an honest baseline
of their current AI identity governance posture. The current state assessment answers five
questions:
1. What AI identities exist? Conduct a discovery sweep across all environments,
targeting source code and CI/CD workflows first, where 57% and 26% of exposed
secrets respectively originate [9];
2. What do those identities have access to? Audit effective permissions, not just
formally assigned roles, with specific attention to Super NHIs, given that 1 in 20 AWS
machine identities carries full administrator privileges [44];
3. Who owns them? Orphaned identity prevalence is the primary baseline metric for
remediation tracking;
4. What is the current credential hygiene posture? Document the prevalence of
static API keys, long-lived service account passwords, hardcoded secrets, and shared
credentials; and
5. What regulatory frameworks apply? Use the MIGT Domain VI Jurisdiction
Mapping Matrix to determine applicable frameworks and begin jurisdictional exposure
mapping.
The output is a Current State Report providing the before-measurement for demonstrating
risk reduction as the program progresses.
7.2 Phase 1: Foundation (Months 1–6)
Objective: Establish the foundational governance infrastructure that all subsequent phases
depend on, and deliver measurable reduction in the highest-severity risks identified in the
current state assessment. The Identity Working Group [106] identifies unified architecture
and visibility as the essential first step; Permiso’s maturity model [107] confirms that NHI
visibility grows from less than 10% to over 99% through foundation-level implementation,
representing the largest single risk reduction step in the entire maturity progression.
Phase 1 deliverables:
1. AI Identity Registry, initially populated with unique identifier, identity type, business
purpose, provisioning date, access grants, associated systems, and designated human
owner, with a specific shadow AI category for identities discovered outside formal

Kurtz & Krawiecka (2026)
Who Governs the Machine?
67
provisioning processes (repositories with AI assistance enabled show a 40% higher
incidence of secret leaks [106]);
2. Ownership Assignment Campaign, designating a human accountability owner
for every AI identity through engagement with business unit leaders and application
owners, with a triage process for orphaned identities;
3. Critical Credential Remediation, prioritized as Tier 1 (immediate) for hardcoded
secrets in source code and CI/CD pipelines, PAM-adjacent credentials identified in Silk
Typhoon threat intelligence [14], credentials with administrative scope, and credentials
with no rotation history exceeding 12 months; Tier 2 (30–60 days) for API keys
with broad scope and no usage monitoring; and Tier 3 (60–90 days) for remaining
static long-lived credentials. The OASIS NHI management guide [109] provides the
most operationally detailed guidance for credential rotation in high-debt environments
without causing service disruption; and
4. Authorized Provisioning Process, establishing a lightweight initial version creating
a gate that prevents future shadow AI identity accumulation.
Phase 1 success metrics: AI identity registry populated with greater than 80% completeness
confidence; designated owner assigned to greater than 90% of active AI identities; Tier 1
credential remediation 100% complete; authorized provisioning process operational for all
new AI identity requests.
7.3 Phase 2: Hardening (Months 6–12)
Objective: Replace static credential architecture with cryptographic identity and ephemeral
credentials, implement JIT access provisioning for high-risk AI identities, establish behavioral
baselines enabling anomaly detection, and begin EU AI Act and China CSL compliance
documentation. The EU AI Act August 2026 enforcement date creates a hard external
deadline for EU-exposed organizations.
Phase 2 deliverables:
1. SPIFFE/SPIRE Workload Identity Deployment [88] for the highest-risk AI
identity population, beginning with PAM-adjacent identities, followed by identities
with access to sensitive data systems, followed by remaining high-privilege identities.
SPIFFE provides cryptographically verifiable IDs tied to workloads, not people, making
them ideal for AI agents and other non-human entities [89];

Kurtz & Krawiecka (2026)
Who Governs the Machine?
68
2. Ephemeral Credential Architecture for Tier 1 high-risk identities, with Zero
Standing Privilege as the target architecture where agents never hold a credential at
rest [90];
3. JIT Access Provisioning pilot for a selected population of AI agents with currently
broad standing access to sensitive systems, demonstrating that access can be granted
at runtime, scoped to specific tasks, and automatically revoked upon completion [91];
4. Behavioral Baseline Establishment for each AI identity derived from historical log
analysis; and
5. Compliance Documentation, initial version mapping implemented controls to EU
AI Act and China CSL obligations using the MIGT Domain VI Jurisdiction Mapping
Matrix.
Phase 2 success metrics: SPIFFE/SPIRE deployed for greater than 50% of Tier 1
AI identities; ephemeral credentials operational for all PAM-adjacent AI identities; JIT
provisioning pilot operational with documented risk reduction measurement; behavioral
baselines documented for greater than 80% of registered AI identities; EU AI Act compliance
gap assessment completed with remediation roadmap.
7.4 Phase 3: Integration (Months 12–24)
Objective: Extend cryptographic identity and ephemeral credentials to the full AI identity
population, deploy tamper-evident audit architecture, complete supply chain governance for
high-risk AI models, and achieve full cross-jurisdictional regulatory alignment documentation.
Phase 3 deliverables:
1. Full SPIFFE/SPIRE rollout across the complete AI identity population, retiring all
remaining static long-lived credentials, with ARIA model implementation [86] for multi-
agent architectures enabling fine-grained accountability across complex multi-agent
workflows;
2. Tamper-Evident Audit Architecture deploying complete logging of all significant AI
agent actions enriched with context and integrated with SIEM and SOAR platforms [91];
3. AIBOM Implementation for all production AI models with model integrity verifica-
tion using cryptographic hash verification of model parameters [84];
4. Cross-Jurisdictional Conflict Registry, fully populated with documented man-
agement approaches for identified irreconcilable conflicts, validated by legal counsel,

Kurtz & Krawiecka (2026)
Who Governs the Machine?
69
particularly for organizations operating across U.S.-China boundaries where the al-
gorithm transparency conflict identified in the regulatory matrix has no regulatory
resolution; and
5. AI-Specific Access Certification using automated behavioral analysis combined
with designated owner attestation.
Phase 3 success metrics: cryptographic identity deployed across greater than 95% of AI
identity population; zero active static long-lived credentials for Tier 1 identities; tamper-
evident audit architecture operational with SIEM integration; AIBOM complete for all
production AI models; EU AI Act compliance documentation complete and legally reviewed;
Cross-Jurisdictional Conflict Registry fully populated.
7.5 Phase 4: Optimization (Month 24+)
Objective: Advance the AI identity governance program from human-speed reactive man-
agement to machine-speed proactive governance.
Phase 4 deliverables:
1. Policy Decision Point Automation, implementing automated contextual rule
evaluation without requiring human review for routine decisions, with human review
triggered automatically for high-risk deviations and state-actor threat indicators [85];
2. Threat Intelligence Integration, incorporating CISA advisories, Microsoft Threat
Intelligence bulletins [14], and FBI Cyber Division notifications into anomaly detection
and policy decision architecture, with Silk Typhoon-specific behavioral detection rules
for anomalous access to PAM-adjacent identities;
3. Maturity-Based Autonomy Progression Management [85], continuously assessing
each AI agent’s compliance and updating autonomy tiers accordingly; and
4. Regulatory Velocity Monitoring, establishing a structured process for monitoring
EU AI Act implementation guidance, NIST NCCoE AI agent identity standards [54] [55],
Chinese CSL enforcement guidance, and U.S. state AI law developments.
7.6 Implementation Guidance for Specific Organizational Contexts
Organizations with significant identity debt should execute a pre-Phase 1 triage step using
threat intelligence to prioritize the highest-risk identity subset for immediate action before full
inventory is complete: PAM-adjacent credentials, identities with administrative scope, and
credentials in externally accessible systems. The OASIS NHI management guide [109] provides

Kurtz & Krawiecka (2026)
Who Governs the Machine?
70
the most detailed practitioner guidance for credential rotation in high-debt environments
without causing service disruption. Organizations subject to all three primary regulatory
frameworks-the EU AI Act, NIST AI RMF, and Chinese CSL-should initiate the Cross-
Jurisdictional Conflict Registry during the current state assessment phase rather than Phase 3,
and engage legal counsel with specific expertise in all three frameworks before Phase 2
compliance documentation begins. The August 2026 EU AI Act enforcement date creates
a hard external deadline that must drive Phase 2 and Phase 3 scheduling for EU-exposed
organizations regardless of other program priorities.
7.7 Measuring Program Effectiveness
MIGT implementation programs should track five categories of metrics:
• Coverage Metrics: percentage of AI identities in registry, with designated owners,
with cryptographic identity, and with behavioral baselines, measuring the breadth of
governance program reach.
• Hygiene Metrics: percentage of credentials rotated within policy period, percentage
JIT-provisioned, and number of active static long-lived credentials (target zero for
Tier 1), measuring credential governance quality.
• Behavioral Metrics: number of behavioral baseline deviations detected, mean time
to investigate anomalies, and percentage attributed to known threat actor patterns,
measuring the effectiveness of behavioral monitoring.
• Accountability Metrics: percentage of AI incidents with complete audit trail recon-
struction, mean time to accountability attribution, and number of AI identities with no
designated owner (target zero), measuring the strength of accountability architecture.
• Compliance Metrics: percentage of applicable regulatory obligations mapped to
governance controls, number of open cross-jurisdictional conflicts without documented
management approaches, and status of EU AI Act compliance documentation against
the August 2026 enforcement date.
8. Conclusion: Governing the Machine - Four Claims, an Inflection
Point, and a Research Agenda
The three questions that most organizations cannot answer about their AI systems in 2026-
What can they access? Who is responsible when they cause harm? And does governing them

Kurtz & Krawiecka (2026)
Who Governs the Machine?
71
in one country create liability in another?-eight sections later, the empirical record, the risk
taxonomy, the governance framework, and the regulatory analysis collectively demonstrate
that these questions are not merely unanswered. They are, in most enterprise environments,
not yet being seriously asked. Here, the concluding section restates four original claims
against the evidence developed across the preceding sections, acknowledges limitations with
the intellectual honesty that peer review requires, and outlines the future research agenda
that the MIGT and AIRT open.
8.1 Restating the Four Claims
Claim 1: AI identity risk is a distinct risk category requiring its own taxonomy. Section 2
documents machine identities outnumbering humans by 144 to 1 [9], governance capabilities
covering fewer than half the total machine identity population [10], and ungoverned permissions
growing from 5% to 28% of enterprise total in a single year [44]. The CrowdStrike outage
($5.4 to $10 billion in losses [11] [12]), the tj-actions supply chain compromise (23,000+
repositories [9]), and the ongoing Typhoon campaigns collectively demonstrate that machine
identity governance failure is producing harm at national scale. The State of AI Agent Security
2026 report confirms that 88% of organizations experienced AI agent security incidents yet
only 22% treat AI agents as independent, identity-bearing entities [15]. The AIRT’s 37
sub-categories across eight domains constitute the first comprehensive enumeration of the
risk category these numbers describe.
Claim 2: The governance framework gap, the regulatory gap, and the coordination gap
must be addressed simultaneously. The agentic AI governance frameworks of Pandey [18],
Joshi [19], and Shavit et al. [20] address governance broadly without identity-specific grounding.
The NIST AI RMF [34] provides governance function structure without identity-specific risk
enumeration. Cross-jurisdictional analyses [6] [7] document regulatory divergence without
enterprise-level resolution mechanisms. The Cloud Security Alliance survey of 285 IT and
security professionals confirms that less than half feel confident they could pass a compliance
review focused on agent behavior [42]-the operational consequence of addressing these gaps
in isolation. The MIGT addresses all three gaps simultaneously.
Claim 3: Foreign state actors have already operationalized AI identity as an attack
and influence vector, and enterprise IAM programs have no adequate threat model for this.
Silk Typhoon’s targeting of PAM provider credentials [14] [28], Salt Typhoon’s compromise
of nine major U.S. telecommunications providers still active as of February 2026 [35] [37],
Volt Typhoon’s pre-positioning within critical infrastructure [36], and North Korean AI-
enhanced identity fraud [26] collectively establish that foreign state exploitation of AI identity
governance gaps is a present operational reality. The Lumos Identity at a Breaking Point

Kurtz & Krawiecka (2026)
Who Governs the Machine?
72
report confirms that 96% of organizations experienced identity-related security incidents [111].
No existing IAM governance framework reviewed in Section 3 incorporates a foreign state
actor threat model.
Claim 4: The absence of inter-jurisdictional coordination in AI governance is itself
a governance risk. Section 4 documents five frameworks and three structural fault lines
producing irreconcilable cross-jurisdictional conflicts. The January 22, 2026 publication of
Singapore’s Model AI Governance Framework for Agentic AI [62] confirms the directional
trend: major jurisdictions continue to develop independent AI governance frameworks that
enterprise organizations must simultaneously satisfy, without any international coordination
mechanism to manage the resulting conflicts. Schmitt [38] documented the fragmentation of
this governance regime as early as 2021, noting the risk of geopolitical encroachment into
technical governance domains. Perboli et al. [30] confirm that by 2025 regulatory arbitrage and
normative fragmentation have materialized as predicted. The MIGT’s Regulatory Alignment
Domain and the Regulatory Matrix constitute the first structured enterprise-level response
to this coordination failure in the published literature.
8.2 The Inflection Point
The four claims describe not merely a governance gap but a governance inflection point.
The governance deficit-whereby organizations struggle to govern machine-speed identities
using human-speed manual processes-combined with agentic risk, where AI agents now act
with administrative privileges that often exceed those of their human creators, defines the
current moment. IANS Research characterizes 2026 as the year AI agents are creating
an identity security crisis, documenting that the window to get NHI governance right is
narrowing as attackers refine tactics faster than governance programs can adapt [112]. At the
same time, the achievability dimension is established by converging standards, tooling, and
regulatory pressure: SPIFFE/SPIRE has graduated from the CNCF with production-ready
cryptographic workload identity capability [88], the NCCoE has initiated the AI agent identity
standardization project [55] [54], and the EU AI Act’s August 2026 enforcement date is
driving governance investment across global organizations. Keyfactor research finds that 85%
of cybersecurity professionals expect digital identities for agents will be as common as human
and machine identities within five years, while 86% say that without unique and dynamic
digital identities, AI agents cannot be fully trusted. The MIGT is proposed as a governance
framework for this inflection point.

Kurtz & Krawiecka (2026)
Who Governs the Machine?
73
8.3 Limitations
Four limitations are material and should be acknowledged explicitly. First, AIRT severity
ratings have not been empirically validated through large-scale enterprise security incident
data. Future research should test AIRT classifications against incident databases, including
the VERIS Community Database, the Privacy Rights Clearinghouse breach database, and AI-
specific incident repositories that the EU AI Act and China CSL reporting requirements will,
over time, generate. Second, the MIGT implementation roadmap is grounded in practitioner-
validated sources but has not been tested through prospective longitudinal implementation
studies. Enterprise implementation complexity varies significantly with organizational size,
technical debt, regulatory exposure, and governance maturity. Third, the cross-jurisdictional
analysis in Sections 4 and 6 addresses three primary regulatory jurisdictions. The January 2026
Singapore MGF [62] demonstrates that the challenge is expanding to additional jurisdictions
not fully addressed in this paper, and the UK AI Safety Institute framework represents a fifth
major jurisdiction with independent AI governance obligations following Brexit. The MIGT’s
Domain VI framework is extensible to additional jurisdictions through the Jurisdiction
Mapping Matrix mechanism, and the Wang et al. [61] quantitative analysis of China, EU,
and U.S. policy frameworks provides a methodological foundation for extending that analysis
to additional jurisdictions in future work. The specific conflict analysis for Singapore, the UK,
and other emerging national frameworks is beyond this paper’s scope. Fourth, the taxonomy
is point-in-time as of March 2026 and will require revision as new attack techniques are
documented, particularly in the prompt injection and state actor domains.
8.4 Future Research Directions
Six research directions are identified as particularly productive. First, empirical validation
and calibration of the AIRT through enterprise security incident data, requiring research
partnerships with enterprise security operations centers, insurance carriers with AI-specific
policy portfolios, and regulatory bodies with incident reporting access. Second, MIGT
implementation studies and maturity model development through longitudinal case studies
across organizations of different sizes, regulatory exposures, and technical debt levels, with the
Omada State of Identity Governance Report 2026 [39] providing a useful baseline measurement
against which future implementation studies should reference. Third, the Model Context
Protocol (MCP) as an emerging identity governance frontier: MCP tokens, credentials, and
access rules are becoming primary targets because they enable agents to operate within
critical systems at machine speed, and most organizations lack visibility into this layer. Future
work should extend the AIRT to include MCP-specific risk sub-categories and the MIGT
to include MCP-specific governance controls. Fourth, cross-jurisdictional conflict resolution

Kurtz & Krawiecka (2026)
Who Governs the Machine?
74
mechanisms, investigating whether international instruments-including bilateral regulatory
equivalence agreements, mutual recognition frameworks, or sector-specific international
governance bodies-could provide resolution mechanisms for the specific irreconcilable conflicts
identified in Section 4.6. The Carnegie Endowment’s analysis of international AI governance
regime complexity [77] and Schmitt’s foundational regime mapping [38] both identify this
as a productive area for international relations and governance scholarship. Fifth, the OT
and consumer AI extension of the AIRT and MIGT to operational technology environments,
where the consequences of governance failure may be physical as well as informational, and to
consumer-facing AI deployments where the governance requirements differ meaningfully from
the enterprise context analyzed. Sixth, the non-human identity accountability attribution
problem in international law: when a foreign state actor exploits an ungoverned machine
credential to cause harm across international borders, the Tallinn Manual tradition [81]
has not yet developed adequate doctrine for the AI identity context. This intersection of
international humanitarian law, state responsibility doctrine, and AI identity governance is
an underexplored area the foreign state actor threat model opens for future research, and
one with direct policy implications for every government currently developing AI governance
frameworks.
8.5 A Closing Observation
The governance vacuum at the intersection of AI and identity is not a future problem. It is a
present crisis, documented in the preceding eight sections with data, incidents, regulatory
analysis, and threat intelligence that collectively leave no room for the comfortable assumption
that existing frameworks are adequate or that incremental improvement will close the gap in
time.
AI agents are no longer experimental. They are production infrastructure. 81% of technical
teams have moved past the planning phase into active testing or production deployment [15].
Yet only 14.4% report that AI agents go live with full security and IT approval [15], meaning
that the overwhelming majority of AI agents entering enterprise production environments
today are doing so without adequate governance review, without cryptographic identity,
without behavioral monitoring, and without designated human accountability owners.
The MIGT does not solve this problem. No taxonomy or framework solves an operational
governance problem. That requires investment, organizational commitment, and sustained
execution. What the MIGT provides is the structured intellectual foundation that makes
solving the problem possible: a comprehensive risk classification, a governance framework
designed for the specific characteristics of AI identity risk, an implementation roadmap
grounded in practitioner experience, and a cross-jurisdictional regulatory alignment structure

Kurtz & Krawiecka (2026)
Who Governs the Machine?
75
that gives global organizations the tools to navigate an increasingly fragmented governance
landscape.
The question posed-who governs the machine-does not have a universal answer. It has an
organizational answer, a regulatory answer, and a geopolitical answer, and they are not the
same answer in any two jurisdictions. But in every jurisdiction, in every enterprise, and under
every regulatory framework, the answer begins the same way: with an inventory, an owner, a
credential policy, and an audit trail. With knowing what you have, who is responsible for it,
and what it is doing.
That is where governance begins. The MIGT provides the framework for everything that
follows.

Kurtz & Krawiecka (2026)
Who Governs the Machine?
76
References
[1] T. Peck. How AI is reshaping identity governance for CISOs and CIOs. CyberArk Blog,
November 2025. Available: https://www.cyberark.com/resources/blog/how-ai-i
s-reshaping-identity-governance-for-cisos-and-cios.
[2] W. Gyure and K. Johnson. The human-machine identity blur: A unified framework
for cybersecurity risk management in 2025. arXiv:2503.18255 [preprint], March 2025.
Available: https://arxiv.org/abs/2503.18255.
[3] Delinea. Five identity-driven shifts reshaping enterprise security in 2026. Help Net
Security, December 2025. Available: https://www.helpnetsecurity.com/2025/12/
24/five-identity-driven-shifts-reshaping-enterprise-security-in-2026/.
[4] Identity Defined Security Alliance. Identity and access management in the AI era: 2025
guide. IDSA, 2025. Available: https://www.idsalliance.org/blog/identity-and
-access-management-in-the-ai-era-2025-guide/.
[5] Cloud Security Alliance. AI and privacy: Shifting from 2024 to 2025. CSA Blog, April
2025. Available: https://cloudsecurityalliance.org/blog/2025/04/22/ai-and
-privacy-2024-to-2025-embracing-the-future-of-global-legal-development
s.
[6] Y. Chun et al. Comparative global AI regulation: Policy perspectives from the EU,
China, and the US. arXiv:2410.21279, October 2024. Available: https://arxiv.org/
abs/2410.21279.
[7] L. S. Lim. Artificial intelligence regulation matures: Landscapes of the USA, European
Union, and China. Journal of Information Technology, 2025.
[8] Communications of the ACM. Three rulebooks, one race: AI regulation in the U.S.,
EU, and China. Commun. ACM, February 2026. Available: https://cacm.acm.org
/news/three-rulebooks-one-race-ai-regulation-in-the-u-s-eu-and-china/.
[9] Entro Labs. NHI and secrets risk report — H1 2025. Technical report, Entro Security,
July 2025. Available: https://www.cybersecuritytribe.com/news/research-rev
eals-44-growth-in-nhis-from-2024-to-2025.
[10] IBM Security. IBM security X-Force threat intelligence index 2025. Technical report,
IBM, 2025. Available: https://www.ibm.com/reports/threat-intelligence.

Kurtz & Krawiecka (2026)
Who Governs the Machine?
77
[11] C. Duffy. CrowdStrike outage: We finally know what caused it and how much it cost.
CNN Business, July 2024. Available: https://www.cnn.com/2024/07/24/tech/crow
dstrike-outage-cost-cause.
[12] S. Snider. CrowdStrike outage drained $5.4 billion from Fortune 500: Report. Informa-
tionWeek, July 2024. Available: https://www.informationweek.com/cyber-resil
ience/crowdstrike-outage-drained-5-4-billion-from-fortune-500-report.
[13] S. Chin and P. Lester. Protecting our edge: Trade secrets and the global AI arms race.
CSIS, December 2025. Available: https://www.csis.org/analysis/protecting-o
ur-edge-trade-secrets-and-global-ai-arms-race.
[14] Microsoft Threat Intelligence. Silk typhoon targeting IT supply chain. Microsoft
Security Blog, March 2025. Available: https://www.microsoft.com/en-us/securi
ty/blog/2025/03/05/silk-typhoon-targeting-it-supply-chain/.
[15] Gravitee.io. State of AI agent security 2026 report: When adoption outpaces control,
February 2026. Available: https://www.gravitee.io/blog/state-of-ai-agent-s
ecurity-2026-report-when-adoption-outpaces-control.
[16] Z. Deng et al. AI agents under threat: A survey of key security challenges and future
pathways. ACM Comput. Surv., 57(7):182, February 2025.
[17] C. Castro et al. A survey of agentic AI and cybersecurity: Challenges, opportunities
and use-case prototypes. arXiv:2601.05293, January 2026. Available: https://arxiv.
org/html/2601.05293v1.
[18] R. Pandey. The agentic AI governance framework: A universal model for risk, ac-
countability, and compliance in autonomous systems. SSRN, October 2025. Available:
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5652350.
[19] S. Joshi. Framework for government policy on agentic and generative AI: Governance,
regulation, and risk management. SSRN, August 2025. Available: https://papers.s
srn.com/sol3/papers.cfm?abstract_id=5511060.
[20] Y. Shavit, S. Agarwal, et al. Practices for governing agentic AI systems. OpenAI,
December 2023. Available: https://cdn.openai.com/papers/practices-for-gov
erning-agentic-ai-systems.pdf.
[21] S. Rose, O. Borchert, S. Mitchell, and S. Connelly. Zero trust architecture. Techni-
cal Report NIST Special Publication 800-207, National Institute of Standards and
Technology, August 2020.

Kurtz & Krawiecka (2026)
Who Governs the Machine?
78
[22] OpenID Foundation. Identity management for agentic AI. OpenID Foundation Working
Group Report, October 2025. Available: https://openid.net/wp-content/uploads
/2025/10/Identity-Management-for-Agentic-AI.pdf.
[23] A. Chan, R. Salganik, A. Markelius, et al. Harms from increasingly agentic algorithmic
systems. In Proc. 2023 ACM Conf. Fairness, Accountability, Transparency (FAccT
2023), Chicago, IL, June 2023. Available: https://dl.acm.org/doi/10.1145/35930
13.3594033.
[24] M. Holgersson, L. Dahlander, H. W. Chesbrough, and M. Bogers. Rethinking AI agents:
A principal-agent perspective. California Management Review, July 2025. Available:
https://cmr.berkeley.edu/2025/07/rethinking-ai-agents-a-principal-age
nt-perspective/.
[25] Lawfare Media. Algorithmic foreign influence: Rethinking sovereignty in the age of AI.
Lawfare, August 2025. Available: https://www.lawfaremedia.org/article/algor
ithmic-foreign-influence--rethinking-sovereignty-in-the-age-of-ai.
[26] NYU Journal of Intellectual Property and Entertainment Law. Artificial intelligence
and state-sponsored cyber espionage. JIPEL, 2025. Available: https://jipel.law.ny
u.edu/artificial-intelligence-and-state-sponsored-cyber-espionage/.
[27] J. Ding et al. Spy vs. AI: How artificial intelligence will remake espionage. Foreign
Affairs, January 2025. Available: https://www.foreignaffairs.com/united-state
s/spy-vs-ai.
[28] D. B. Johnson. Silk typhoon shifted to specifically targeting IT management companies.
CyberScoop, March 2025. Available: https://cyberscoop.com/silk-typhoon-tar
gets-it-services/.
[29] DFRLab. FIMI 101: Foreign information manipulation and interference targeting
the 2024 US general election. Atlantic Council, September 2024. Available: https:
//dfrlab.org/2024/09/26/fimi-101/.
[30] G. Perboli, N. Simionato, and S. Pratali. Navigating the AI regulatory landscape:
Balancing innovation, ethics, and global governance. Economic and Political Studies,
13(4):367–397, December 2025.
[31] MIT AI Risk Repository. AI risk repository (v4). Massachusetts Institute of Technology,
December 2025. Available: https://airisk.mit.edu.

Kurtz & Krawiecka (2026)
Who Governs the Machine?
79
[32] Z. He et al. The emerged security and privacy of LLM agents: A survey with case
studies. ACM Comput. Surv., 2025.
[33] OWASP GenAI Security Project. OWASP top 10 for agentic applications 2026. OWASP,
December 2025. Available: https://genai.owasp.org/resource/owasp-top-10-f
or-agentic-applications-for-2026/.
[34] NIST. AI risk management framework (AI RMF 1.0). Technical report, National
Institute of Standards and Technology, 2023. Available: https://nvlpubs.nist.gov
/nistpubs/ai/NIST.AI.100-1.pdf.
[35] Federal Bureau of Investigation. FBI announces joint cybersecurity advisory related to
Salt typhoon. FBI.gov, August 2025. Available: https://www.fbi.gov/video-repos
itory/salttyphoon082725.mp4/view.
[36] Congressional Research Service. Salt typhoon hacks of telecommunications companies
and federal response implications.
Technical report, Congress.gov, January 2025.
Available: https://www.congress.gov/crs-product/IF12798.
[37] D. B. Johnson. Officials worry salt typhoon apathy is killing momentum for tougher
telecom security rules. CyberScoop, March 2026. Available: https://cyberscoop.c
om/salt-typhoon-china-telecom-hack-impact-new-jersey/.
[38] L. Schmitt. Mapping global AI governance: A nascent regime in a fragmented landscape.
AI and Ethics, 2:303–314, 2022.
[39] Omada Identity. The state of identity governance report 2026. Omada, January 2026.
Available: https://omadaidentity.com/resources/analyst-reports/state-of-i
ga/.
[40] CyberArk. 2025 identity security landscape. CyberArk, April 2025. Available: https:
//www.cyberark.com/press/machine-identities-outnumber-humans-by-more-t
han-80-to-1-new-report-exposes-the-exponential-threats-of-fragmented-i
dentity-security/.
[41] AppViewX. Key takeaways from the 2024 ESG report on non-human identity (NHI)
management. AppViewX Blog, October 2024. Available: https://www.appviewx.com
/blogs/key-takeaways-from-the-2024-esg-report-on-non-human-identity-n
hi-management/.

Kurtz & Krawiecka (2026)
Who Governs the Machine?
80
[42] Strata Identity / Cloud Security Alliance. The AI agent identity crisis: New research
reveals a governance gap, February 2026. Available: https://www.strata.io/blog/a
gentic-identity/the-ai-agent-identity-crisis-new-research-reveals-a-g
overnance-gap/.
[43] Research and Markets. Non-human identity solutions, global, 2024–2030. Research and
Markets, February 2026. Available: https://www.researchandmarkets.com/repor
ts/6217813/non-human-identity-solutions-global.
[44] S. Markovic. Non-human identities push identity security into uncharted territory. Help
Net Security, December 2025. Available: https://www.helpnetsecurity.com/2025
/12/30/identity-security-permissions-sprawl/.
[45] D. Gupta. The AI identity crisis: NHIs, agents and vibe coding in 2025, October 2025.
Available: https://guptadeepak.com/the-identity-crisis-no-ones-talking-a
bout-how-ai-agents-and-vibe-coding-are-rewriting-the-rules-of-digital
-security/.
[46] Messageware. What caused the CrowdStrike outage: A detailed breakdown, August
2024. Available: https://www.messageware.com/what-caused-the-crowdstrike-o
utage-a-detailed-breakdown/.
[47] Reuters. Delta can sue CrowdStrike over computer outage that caused 7,000 canceled
flights. Reuters, May 2025. Available: https://www.reuters.com/sustainability
/boards-policy-regulation/delta-can-sue-crowdstrike-over-computer-out
age-that-caused-7000-canceled-flights-2025-05-19/.
[48] Tufin. The lasting impact of the CrowdStrike update outage. Tufin Blog, June 2025.
Available: https://www.tufin.com/blog/lasting-impact-of-crowdstrike-updat
e-outage.
[49] Harvard Business Review. What the 2024 CrowdStrike glitch can teach us about cyber
risk. HBR, January 2025. Available: https://hbr.org/2025/01/what-the-2024-c
rowdstrike-glitch-can-teach-us-about-cyber-risk.
[50] Z. Zorz. Marks and spencer ransomware breach incident. Help Net Security, April 2025.
Available: https://www.helpnetsecurity.com/2025/04/29/marks-spencer-ranso
mware-breach-incident/.
[51] National Crime Agency. NCA retail cyber attacks: Nca arrest four for attacks on m&s,
co-op and harrods. NCA, July 2025. Available: https://www.nationalcrimeagency.

Kurtz & Krawiecka (2026)
Who Governs the Machine?
81
gov.uk/news/retail-cyber-attacks-nca-arrest-four-for-attacks-on-m-s-c
o-op-and-harrods.
[52] Fortune Business Insights. Identity and access management market size, share, and
industry analysis — forecast 2024–2032. Technical report, Fortune Business Insights,
September 2024. Available: https://www.fortunebusinessinsights.com/industry
-reports/identity-and-access-management-market-100373.
[53] NIST Center for AI Standards and Innovation (CAISI). AI agent standards initiative.
National Institute of Standards and Technology, February 2026. Available: https:
//www.nist.gov/caisi/ai-agent-standards-initiative.
[54] R. Galluzzo, B. Fisher, H. Booth, and J. Roberts. Accelerating the adoption of software
and artificial intelligence agent identity and authorization. Draft concept paper, NIST
National Cybersecurity Center of Excellence, March 2026. Available: https://www.nc
coe.nist.gov/projects/software-and-ai-agent-identity-and-authorization.
[55] NIST NCCoE. Software and AI agent identity and authorization. National Cybersecurity
Center of Excellence, 2026. Available: https://www.nccoe.nist.gov/projects/so
ftware-and-ai-agent-identity-and-authorization.
[56] S. Rizvi, A. Kurtz, J. Pfeffer, and M. Rizvi. Securing the Internet of Things (IoT): A
security taxonomy for IoT. In Proc. 17th IEEE Int. Conf. Trust, Security and Privacy
in Computing and Communications (TrustCom/BigDataSE 2018), pages 163–168, New
York, NY, August 2018. Available: https://ieeexplore.ieee.org/document/84559
02.
[57] M. A. Coutinho, A. Ashofteh, and Y. Al Helaly. Risk taxonomies and governance
frameworks for generative AI: A review of ethical, cybersecurity, and regulatory chal-
lenges. In Proc. 20th Iberian Conf. Information Systems and Technologies (CISTI
2025), volume 1717 of Lecture Notes in Networks and Systems, Cham, 2026. Springer.
Available: https://link.springer.com/chapter/10.1007/978-3-032-10721-3_1.
[58] D. Kaur et al. AI governance: A systematic literature review. AI and Ethics, January
2025.
[59] J. Moura et al. Prompt injection attacks in large language models and AI agent systems.
Information, 17(1):54, 2026.

Kurtz & Krawiecka (2026)
Who Governs the Machine?
82
[60] M. A. Ferrag et al. From prompt injections to protocol exploits: Threats in LLM-
powered AI agent workflows. ICT Express, 2025. Available: https://www.sciencedir
ect.com/science/article/pii/S2405959525001997.
[61] S. Wang, Y. Zhang, Y. Xiao, and Z. Liang. Artificial intelligence policy frameworks in
China, the European Union and United States: An analysis based on structure topic
model. Technological Forecasting and Social Change, 212:123971, 2025.
[62] M. Chmura. Agentic AI: The future and governance of autonomous systems. Bloomsbury
Intelligence and Security Institute, February 2026. Available: https://bisi.org.uk/
reports/agentic-ai-the-future-and-governance-of-autonomous-systems.
[63] R. Csernatoni. Global AI governance: Barriers and pathways forward. International
Affairs, 100(3):1275–1294, May 2024.
[64] H. Dorwart, H. Qu, T. Brautigam, and J. Gong. Preparing for compliance: Key
differences between EU and chinese AI regulations. IAPP, February 2025. Available:
https://iapp.org/news/a/preparing-for-compliance-key-differences-betwe
en-eu-chinese-ai-regulations.
[65] European Commission. EU AI act. Official Journal of the European Union, July 2024.
Available: https://digital-strategy.ec.europa.eu/en/policies/regulatory-f
ramework-ai.
[66] EU AI Act Service Desk. Timeline for the implementation of the EU AI act. European
Commission, 2025. Available: https://ai-act-service-desk.ec.europa.eu/en/ai
-act/timeline/timeline-implementation-eu-ai-act.
[67] Pearl Cohen. New guidance under the EU AI act ahead of its next enforcement date.
Pearl Cohen Law, December 2025. Available: https://www.pearlcohen.com/new-g
uidance-under-the-eu-ai-act-ahead-of-its-next-enforcement-date/.
[68] K&L Gates. EU and Luxembourg update on the European harmonised rules on artificial
intelligence. K&L Gates, January 2026. Available: https://www.klgates.com/EU-a
nd-Luxembourg-Update-on-the-European-Harmonised-Rules-on-Artificial-I
ntelligenceRecent-Developments-1-20-2026.
[69] White House Office of Science and Technology Policy. Winning the race: America’s AI
action plan. The White House, July 2025. Available: https://www.whitehouse.gov
/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf.

Kurtz & Krawiecka (2026)
Who Governs the Machine?
83
[70] Executive Office of the President. Ensuring a national policy framework for artificial
intelligence. Executive Order 14365, Federal Register, December 2025. Available:
https://www.federalregister.gov/documents/2025/12/16/2025-23092/ensurin
g-a-national-policy-framework-for-artificial-intelligence.
[71] Baker Botts. U.S. artificial intelligence law update: Navigating the evolving state
and federal regulatory landscape. Baker Botts, January 2026. Available: https:
//www.bakerbotts.com/thought-leadership/publications/2026/january/us-a
i-law-update.
[72] H.-Y. Chen. AI governance and regulation 2026: A complete guide to global frameworks,
February 2026. Available: https://www.hungyichen.com/en/insights/ai-governa
nce-regulatory-landscape-2026.
[73] IAPP. Global AI governance law and policy: China. International Association of
Privacy Professionals, 2025. Available: https://iapp.org/resources/article/glo
bal-ai-governance-china.
[74] ICLG. China’s key developments in artificial intelligence governance in 2025. ICLG,
December 2025. Available: https://iclg.com/practice-areas/telecoms-media-a
nd-internet-laws-and-regulations/03-china-s-key-developments-in-artif
icial-intelligence-governance-in-2025.
[75] Linklaters. China’s 2025 cybersecurity law amendments: Enhanced penalties, expanded
extraterritorial application, and AI governance. Linklaters Tech Insights, October 2025.
Available: https://techinsights.linklaters.com/post/102lrz5/.
[76] ANSI. China announces action plan for global AI governance. American National
Standards Institute, August 2025. Available: https://www.ansi.org/standards-new
s/all-news/8-1-25-china-announces-action-plan-for-global-ai-governanc
e.
[77] H. Pouget, C. Dennis, et al. The future of international scientific assessments of
AI’s risks. Carnegie Endowment for International Peace, August 2024. Available:
https://carnegieendowment.org/research/2024/08/the-future-of-internati
onal-scientific-assessments-of-ais-risks.
[78] Springer AI and Ethics. Waging warfare against states: The deployment of artificial
intelligence in cyber espionage. AI and Ethics, 2025.

Kurtz & Krawiecka (2026)
Who Governs the Machine?
84
[79] others.
Navigating the nexus: Geopolitical, international relations and technical
dimensions of US-China cyber strategic competition. Cogent Social Sciences, May 2025.
[80] CSO Online. AI disinformation did not upend 2024 elections, but the threat is very real.
CSO Online, April 2025. Available: https://www.csoonline.com/article/3852770/.
[81] M. N. Schmitt, editor. Tallinn Manual 2.0 on the International Law Applicable to
Cyber Operations. Cambridge University Press, Cambridge, UK, 2nd edition, 2017.
[82] OWASP. LLM top 10 for large language model applications 2025. OWASP Gen AI
Security Project, 2025. Available: https://owasp.org/www-project-top-10-for-l
arge-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v20
25.pdf.
[83] ServiceNow. [Security Advisory] CVE-2025-12420: Privilege escalation via prompt
injection in ServiceNow AI platform (BodySnatcher). ServiceNow Support, January
2026. Available: https://support.servicenow.com/kb?id=kb_article_view&sys
parm_article=KB2587329.
[84] K. Huang, V. S. Narajala, J. Yeoh, R. Raskar, et al. A novel zero-trust identity
framework for agentic AI: Decentralized authentication and fine-grained access control.
arXiv:2505.19301, May 2025. Available: https://arxiv.org/abs/2505.19301.
[85] MassiveScale.AI / Cloud Security Alliance. The agentic trust framework: Zero trust
governance for AI agents. CSA Blog, February 2026. Available: https://cloudsecur
ityalliance.org/blog/2026/02/02/the-agentic-trust-framework-zero-trust
-governance-for-ai-agents.
[86] V. Gupta. The looming authorization crisis IAM. ISACA Journal, September 2025.
Available: https://www.isaca.org/resources/news-and-trends/industry-news/
2025/the-looming-authorization-crisis-why-traditional-iam-fails-agent
ic-ai.
[87] W3C.
Decentralized identifiers (DIDs) v1.0.
W3C Recommendation, July 2022.
Available: https://www.w3.org/TR/did-core/.
[88] Cloud Native Computing Foundation. SPIFFE: Secure production identity framework
for everyone. CNCF Graduated Project, 2024. Available: https://spiffe.io/.
[89] HashiCorp.
SPIFFE: Securing the identity of agentic AI and non-human actors.
HashiCorp Blog, 2025. Available: https://www.hashicorp.com/en/blog/spiffe-s
ecuring-the-identity-of-agentic-ai-and-non-human-actors.

Kurtz & Krawiecka (2026)
Who Governs the Machine?
85
[90] Optimum Partners. AI security architecture: Implementing workload identity federation
(WIF) and SPIFFE, January 2026. Available: https://optimumpartners.com/insi
ght/ai-security-architecture-implementing-workload-identity-federatio
n-wif-and-spiffe/.
[91] Lumos. Agentic AI and identity governance: What you need to know, December 2025.
Available: https://www.lumos.com/topic/agentic-ai-identity-governance-man
agement.
[92] Victor Costan and Srinivas Devadas. Intel SGX explained. IACR Cryptology ePrint
Archive, Report 2016/086, 2016.
[93] Will Arthur and David Challener. A Practical Guide to TPM 2.0: Using the Trusted
Platform Module in the New Age of Security. Apress, 2015.
[94] Pau-Chen Cheng, Wojciech Ozga, Enriquillo Valdez, Salman Ahmed, Zhongshu Gu,
Hani Jamjoom, Hubertus Franke, and James Bottomley. Intel TDX demystified: A
top-down approach. ACM Computing Surveys, 56(9):1–33, 2024.
[95] Henk Birkholz, Dave Thaler, Michael Richardson, Ned Smith, and Wei Pan. Remote
attestation procedures (RATS) architecture. RFC 9334, Internet Engineering Task
Force, 2023.
[96] Teofil Bodea, Masanori Misono, Julian Pritzi, Patrick Sabanic, Thore Sommer, Har-
shavardhan Unnibhavi, David Schall, Nuno Santos, Dimitrios Stavrakakis, and Pramod
Bhatotia. Trusted AI agents in the cloud. arXiv preprint arXiv:2512.05951, 2025.
[97] HID Global. Trust standards evolve: AI agents, the next chapter for PKI. HID Global
Blog, November 2025.
[98] Sandro Rodriguez Garzon, Awid Vaziry, Enis Mert Kuzu, Dennis Enrique Gehrmann,
Buse Varkan, Alexander Gaballa, and Axel Küpper. AI agents with decentralized
identifiers and verifiable credentials. In Proceedings of the 18th International Confer-
ence on Agents and Artificial Intelligence (ICAART 2026), volume 1, pages 252–259.
SCITEPRESS, 2026.
[99] Klaudia Krawiecka, Andrew Paverd, and N. Asokan. Protecting password databases
using trusted hardware. In Proceedings of the 1st Workshop on System Software for
Trusted Execution (SysTEX ’16), pages 1–6. ACM, 2016.

Kurtz & Krawiecka (2026)
Who Governs the Machine?
86
[100] Cisco Talos. 2024 year in review. Cisco Systems, 2025. Available: https://blog.tal
osintelligence.com/2024yearinreview/.
[101] Obsidian Security. The 2025 AI agent security landscape: Players, trends, and risks.
Obsidian Security Blog, January 2026.
[102] Pankaj Kumar. Next-generation secure authentication and access control architectures:
Advanced techniques for securing distributed systems in modern enterprises. Inter-
national Journal of Computational and Experimental Science and Engineering, 11(3),
2025.
[103] Carlos Castro et al. A survey of agentic AI and cybersecurity: Challenges, opportunities
and use-case prototypes. arXiv preprint arXiv:2601.05293, 2026.
[104] Databricks. Agentic AI security: New risks and controls in the databricks AI security
framework (DASF v3.0). Databricks Blog, March 2026.
[105] OWASP GenAI Security Project. OWASP top 10 for agentic applications 2026. OWASP,
December 2025.
[106] J. Alkove et al. Practitioner’s guide to the future of identity: New maturity model.
Identity Working Group, Oleria, 2025. Available: https://www.oleria.com/resourc
es/guides/nhi.
[107] Permiso Security. What are non-human identities? Complete guide to NHI security for
2025. Permiso, 2025. Available: https://permiso.io/non-human-identity-nhi-s
ecurity-guide.
[108] KuppingerCole Analysts. Mastering non-human identity governance for enhanced
security and efficiency. KuppingerCole Blog, October 2025. Available: https://www.
kuppingercole.com/blog/kuppinger/mastering-non-human-identity-governa
nce-for-enhanced-security-and-efficiency.
[109] OASIS Security. Non-human identity management guide: Audit, certify and govern
NHIs. OASIS Security Blog, January 2026. Available: https://www.oasis.security
/blog/non-human-identity-management.
[110] E. Ozkaya. Enterprise AI security and governance roadmap (2026 CISO strategy),
February 2026. Available: https://erdalozkaya.com/enterprise-ai-security/.

Kurtz & Krawiecka (2026)
Who Governs the Machine?
87
[111] Lumos. New research finds identity has become the most common entry point for
cyberattacks, February 2026. Available: https://www.prnewswire.com/news-relea
ses/new-research-finds-identity-has-become-the-most-common-entry-point
-for-cyberattacks-302695637.html.
[112] IANS Research. AI agents are creating an identity security crisis in 2026. IANS
Research Blog, February 2026. Available: https://www.iansresearch.com/resourc
es/all-blogs/post/security-blog/2026/02/24/ai-agents-are-creating-an-i
dentity-security-crisis-in-2026.
