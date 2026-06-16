# Valerie J Parker, MSc-GH

> Extracted from: `AI Governance in Health Systems.pdf`

Valerie J Parker, MSc-GH
Duke-Margolis InsƟtute for Health Policy

Nicoleta J Economou, PhD
Duke Health

ChrisƟna Silcox, PhD
Duke-Margolis InsƟtute for Health Policy
White Paper
AI Governance in Health Systems
Aligning Innovation, Accountability, and Trust

Acknowledgements
The authors would like to thank several individuals for their contributions to this white paper. First, we are
deeply grateful to each member of the working group for their expert perspectives, open discussion, and
thoughtful feedback. We also thank the participants of our expert workshop (see Appendix A) for sharing
their expertise and experiences, as well as the multiple other health system representatives that held
individual informational calls with us. We also thank Rabail Baig of Duke Health for her work reviewing and
designing this paper. Any opinions expressed in this paper are solely those of the authors and do not
necessarily represent the views of policies of any other person or organization external to Duke-Margolis.
This work was funded by Duke AI Health.
Working Group
We are deeply grateful to each member of the working group for their expert perspecƟves, open
discussion, and thoughƞul feedback. Any opinions expressed in this paper are solely those of the authors
and do not necessarily represent the views or policies of any person or organizaƟon external to Duke-
Margolis.
Karen Habercoss
VP, Chief InformaƟon Security and Privacy Oﬃcer
The University of Chicago Medicine

Hailey Hildahl
Sr. Digital Product Manager
Mayo Clinic Plaƞorm

Nikesh Kotecha
Director, Head of Data Science
Stanford Healthcare

Mark Lifson
Director, AI Systems Engineering
Mayo Clinic Center for Digital Health

Michael Plesh
ExecuƟve Director of Technology
UNC Health

Anurang Revri
Vice President, Chief Enterprise Architect
Stanford Healthcare

Ram Rimal
Manager of Data Science and AI
UNC Health
Lauren Rost
Senior AI/ML Engineer
Mayo Clinic Center for Digital Health

Mathew D. Solomon
Assistant Director
Augmented Clinical Intelligence Program
Kaiser Permanente Northern California

David Vidal
Vice Chair, AI Enablement
Mayo Clinic Center for Digital Health

Ellen Woo
ExecuƟve Director
AI and Emerging Technologies
Kaiser Permanente

Daniel Yang
Vice President of AI and Emerging Technologies
Kaiser Permanente

3

Summary
Tools enabled by arƟﬁcial intelligence (AI) have the
potenƟal to transform paƟent outcomes and health
system operaƟons and are already having signiﬁcant
eﬀects. AI applicaƟons have facilitated faster triage and
diagnosis, enabled the anƟcipaƟon of paƟent outcomes
to create personalized treatment plans, and streamlined
clinical operaƟons, paƟent communicaƟon, and
resource allocaƟon. But while the integraƟon of AI tools
in healthcare systems oﬀers immense potenƟal, the use
of AI in such a sensiƟve and criƟcal sector also raises
signiﬁcant ethical, legal, and pracƟcal concerns.
A comprehensive governance system has mulƟple
advantages, including ensuring paƟent safety,
maintaining ethical standards, ensuring regulatory
compliance, fostering trust through transparency and
accountability, and managing privacy concerns and
other legal issues. But AI governance is a relaƟvely new
concept for health systems, many of which have
integrated only limited numbers of AI tools into their
workﬂows. To beter understand moƟvaƟons and
processes, the project team convened a working group
of six health systems located across the United States
who have established AI governance systems in the past
several years. The project team also conducted
individual interviews with other health systems to
understand their approaches. Although there are
important commonaliƟes in the components of
governance processes, there are diﬀerent ways to
accomplish these tasks. At the same Ɵme, we found that
this is a resource-intensive process across the board.
In the following secƟons, we will walk through the main
components of health system governance and explore
how diﬀerent health systems approach these
components, as well as discussing how health systems
can begin to set up their own governance systems. We
will also oﬀer recommendaƟons for policy makers,
health systems, and other stakeholders on how they can
standardize and simplify these processes to democraƟze
access to AI-enabled health tools and ensure the
availability of technical experƟse to help under-
resourced health systems realize the beneﬁts that AI
tools may provide.
AI Governance and Strategy
AI governance is the practice of reviewing, assessing,
and evaluating individual AI tools to ensure that they
can be used safely, responsibly, fairly, and effectively
with the health system’s patient population and in
compliance with applicable laws. When designing a
governance system, health systems should start with a
clear articulation of the principles and goals of
governance for that health system and identification of
stakeholders who should be involved in the
governance process. The benefits of a good
governance system include visibility into the AI tools
being used within the health system; predictability of
the information needed to review, implement, and
monitor an AI tool; transparency into the governance
process; standardization of the procedures for
evaluation, risk assessment, and risk mitigation; clear
lines of accountability; and centralized and
standardized documentation on each tool’s
assessment and testing.
It is important to separate the concepts of AI strategy
from AI governance. An AI strategy involves a
systematic consideration of how to prioritize the
assessment and implementation of AI tools within the
health system’s overall mission. What are the available
resources for IT implementation and worker training?
Does the health system want to prioritize certain types
of tools, such as system-wide operational efficiency
tools, population health management tools to assist in
accountable care programs, or specific clinical decision
support tools? While governance significantly benefits
from such a strategy having been clearly articulated by
health system executive leadership, governance
systems should not be responsible for establishing or
updating AI strategies. However, a health system’s AI
strategy should prioritize establishing an AI governance
process if one does not already exist.

4

Components of a Governance
System
Through our interviews and discussions, we found that
governance structures can vary signiﬁcantly while
remaining eﬀecƟve. It is important for health systems
to right-size their AI governance to their resources.
However, there were several commonaliƟes that
facilitated building eﬀecƟve governance processes.
OrganizaƟonal Alignment and Engagement
AI governance bodies should have an open line of
communicaƟon with leadership and decision-makers.
AI governance bodies must be empowered within their
organizaƟons to assess AI tools within their purview
and those decision-makers need to take
recommendaƟons seriously. This decision-making may
occur at the health system leadership level (C-suite) or
by individual business owners making ﬁnal purchase
and implementaƟon decisions. As menƟoned above,
Government Eﬀorts
Federal and State actions can incentivize responsible AI governance in multiple ways, and
there have already been steps in this direction. California Attorney General Rob Bonta began
to send letters to hospital CEOs in his state starting in September 2022, asking them to send a
list of all commercial decision-making tools in current use for clinical decision support,
population health management, operational optimization, or payment management. This list
was meant to include the purpose of the tool, any policies or training around the tool, and
contact information for the person(s) responsible for evaluating these tools for disparate
impact. Although many health systems had been thinking about how to govern AI health tools,
this state action made clear the need for a centralized inventory of such software tools and a
standardized evaluation system. Meanwhile, the National Institute of Standards and Measures
(NIST) was developing an AI Risk Management Framework to better manage risk during
development, review, and operationalization. Drafts of the Framework were published in
2022, and the final version was released in early 2023, with multiple companion tools released
over the rest of the 2023 and a Generative AI Risk Profile published in summer 2024. The
Office of Civil Rights at HHS also released a draft rule in 2022 and finalized the rule in May
2024 regarding Section 1557 of the Affordable Care Act, “which prohibits discrimination … in
covered health programs or activities.” Part of this new rule focuses on discrimination
resulting from the use of patient care decision support tools. Health systems must make a
“reasonable effort” to identify and mitigate the risk of discrimination or inequitable care
resulting from the use of these tools. The rule specifically notes that investigations will review
whether the health system has methods to review tools it adopts or uses, and whether the
tool is being used as intended. More recently, FDA Commissioner Robert Califf discussed the
need for health systems to “step up” governance of AI and remarked that “they’re going to
end up holding the bag on liability when these algorithms go wrong.”

5

engaging with health system leadership also allows
governance to be integrated into an overall AI strategy.
We also found that governance teams were oŌen
mulƟdisciplinary to ensure that governance is a holisƟc
process.
IdenƟﬁcaƟon and RegistraƟon of AI Tools
While methods can vary, AI governance bodies must
have a system in place to idenƟfy AI tools under
consideraƟon for implementaƟon at their organizaƟon,
whether these tools are commercially available or were
developed internally. Once idenƟﬁed, AI governance
teams collect informaƟon on the AI tool that will be
used, potenƟally along with ﬁndings from the review
process below, to maintain an inventory of AI tools
assessed or implemented in the health system. This
inventory informaƟon may also modify the review
process based on the perceived risk of the tool.
Inventory processes also have the beneﬁt of
standardizing the type of informaƟon required for tool
assessment and seƫng appropriate expectaƟons on
informaƟon requirements when comparing potenƟal
tools to submit to the governance process. Some
health systems we spoke with were also performing or
considering a “look-back” process for registraƟon of
tools that had already been implemented before the
governance system was running.
Review and Assessment
The main funcƟon of AI governance is to evaluate AI
tools to be used in the health system. These review
processes vary by organizaƟon and may include
mulƟple domains spanning tool performance, privacy,
compliance, legal, paƟent safety (including bias
evaluaƟons), clinical integraƟon, IT integraƟon, and
others (Figure 1). AI governance teams may solicit
informaƟon about the product from the developer
directly or engage the internal champion for the tool to
supply the relevant informaƟon. For some tools,
validaƟon with internal data may also be done, either
retrospecƟvely or prospecƟvely. Typically, AI
governance groups convene to discuss relevant
Figure 1 - Potential areas of assessment in health system governance of AI tools. Health systems review and
assess AI tools in multiple domains. Review processes and domains vary by organization and organizations
may add or change components as their governance system process matures.

6

ﬁndings before issuing a recommendaƟon to relevant
decision makers within the organizaƟon. Diﬀerent
organizaƟons may limit the AI governance group to
issuing recommendaƟons on concerns or miƟgaƟon
suggesƟons, while other may have authority to make
implementaƟon or veto decisions.
Monitoring and Surveillance
Depending on the assessed risk of the AI tool, diﬀerent
types of monitoring may be required. Currently, this is
oŌen concentrated during pilot phases or immediately
post-implementaƟon. However, many people we spoke
with acknowledged that ongoing monitoring is needed
and are working to establish more standardized
surveillance processes, as well as methods for users to
communicate any concerns they may have or any
perceived performance changes over Ɵme. Some
systems require that every implemented tool have a
prespeciﬁed person who is responsible for monitoring
the use of the tool. Other systems have created a
schedule for governance-led audits of tools, which
allows tools that have been or become less useful than
expected to be updated or decommissioned.
Although this lisƟng of components may imply the
process is fairly linear, it is oŌen iteraƟve in pracƟce.
For instance, it is not unusual for the AI governance
commitee to gather addiƟonal informaƟon from the
developer throughout the process, should new
quesƟons or workﬂows be discovered. The new
informaƟon would inform the governance review and
assist commitee members in making a
recommendaƟon. Another example of this iteraƟve
process could be if the AI governance body issues a
recommendaƟon against implementaƟon of a tool due
to speciﬁc risks. Should the decision-makers decide the
tool is high priority, the AI governance body could be
tasked with coordinaƟng either with the developer or
internal process owner to develop miƟgaƟon measures
to address the idenƟﬁed risks to meet health system
needs and meet quality and ethical standards.
These AI governance components oŌen proceed
through mulƟple iteraƟve phases. For example, a tool
may go through an iniƟal assessment that results in a
pilot study being recommended. AŌerward, the AI
governance commitee may reassess the tool, applying
learnings from the pilot program, to determine a
recommendaƟon on a wider implementaƟon. Health
systems that are developing AI tools in-house will oŌen
have mulƟple iteraƟve review processes to move on to
the next phase of research and development. When
tools developed in-house are at the point of being
piloted or fully implemented, they are subject to
similar governance processes as commercial tools.
Tailoring an AI Governance
Approach

Within the commonaliƟes discussed above, each
health care system we spoke with had tailored certain
aspects to establish an AI governance system that best
ﬁt the needs and resources of their organizaƟon
(Figure 2). One of the most interesƟng diﬀerences is
that some systems rolled their AI governance into the
exisƟng general governance around soŌware tools,
taking more of an educaƟonal approach to ensure
tradiƟonal governance enƟƟes were able to ask the
right quesƟons about AI tools, while other health
systems pulled AI tools into a fully separate governance
process. SƟll others took a hybrid approach, with some
of the review components integrated into pre-exisƟng
governance processes and other components being
considered separately. These approaches were not
consistent based on resource availability, although
health systems with fewer resources available for AI
governance may be more likely to rely on addiƟonal
training for exisƟng governance system parƟcipants.
OrganizaƟons diﬀered regarding whether a more
centralized or a federated approach was a beter ﬁt for
their health care system. Smaller health systems or
systems with less AI experƟse available generally took a
more centralized approach to assessments. Very large
systems’ approaches were more variable. While some
were centralized, others used a more federated
approach to allow for more ﬂexibility between
geographic sites or regions. In some cases, the tool
review and assessment were done by a more
centralized team who made detailed recommendaƟons
but the ulƟmate decision-making was federated. In
other cases, some aspects of review such as legal and

7

Decision-making Authority
A critical piece of governance design is identifying who has the ultimate decision-making authority on whether a
given AI tool will be implemented or decommissioned. This authority varied by organization. Some gave this
authority to the person who allocated budget funds for the AI tool, and the review process is meant to guide this decision.
Other health systems favored a more centralized decision process, where the review team or a larger governance group make
the final decision. Still other health systems placed some or all decision-making with executive leadership, who rely on
recommendations from the review process. This can ensure AI tool selection is consistent with the overall AI standards and
strategy.

Governance Committee Composition
Many AI governance committees are interdisciplinary, with members from disciplines such as IT, clinical care,
informatics, legal, privacy, ethics, compliance, human resources, patient engagement, DEI, and finance. Some have
relevant background in the AI, but others may need additional training on the implications of AI within their area of expertise.
Organizations that opt to integrate AI governance into their traditional governance for other technologies also provided
training on how to effectively assess AI tools. In these cases, adding a reviewer with AI technical expertise may be necessary.
Some health systems had small governance teams that consisted of one to three individuals. In these cases, assessments were
sometimes more focused on developer-reported performance, IT integration, privacy, and legal compliance, while local
performance was assessed through qualitative pilots or monitored in post-implementation reviews.

Including the Patient Voice
Many health systems want to include the patient voice in decisions on AI tools that may affect care. However, they
reported legal and logistical challenges in allowing individuals who are not health system employees to have
visibility into the full review process. Finding patients with the relevant expertise or providing adequate training on AI concepts
to allow for informed involvement is also difficult. In the meantime, some health systems have brought in ethics professionals
with expertise in patient opinions to help fill that perspective gap, while other health systems have consulted with pre-existing
patient committees as appropriate. As patients traditionally have not been involved in technology selection and
implementation, more work is needed on best practices in this space.
Governance Scope
AI is a broad term, and governance systems need to clarify the scope of tools within their purview. Some
organizaƟons focused on a range of AI tools, while others focused on machine-learning enabled tools only. Others
only reviewed enterprise tools. Some took a risk-based approach to diﬀerent types of AI. For example, an organizaƟon may only
require registraƟon for AI tools used for billing or business purposes but perform more in-depth reviews on AI tools that directly
aﬀect paƟent care. Others may have diﬀerent processes for tools that have been authorized by the FDA. Governance scope was
determined by several factors, including the resources available, and the scope may change as a governance system matures.

Tool IdenƟﬁcaƟon
Health systems must ensure they are aware when AI tools are being considered in order to bring them into the
governance process. There were a variety of strategies for this, including general informaƟonal campaigns, directed
conversaƟons with individuals involved in purchase decisions, and training with internal AI developers on how and when to
engage with the governance commitee. Some groups built in processes to “catch” tools within scope, oŌen in connecƟon with
IT and procurement oﬃces. There is not a perfect process and tools can slip through cracks at Ɵmes. It can also be diﬃcult to
idenƟfy when exisƟng tools are upgraded with AI-enabled soŌware opƟons and when already implemented AI tools have
signiﬁcant updates that may require addiƟonal governance acƟons.

Figure 2 - Tailoring a Governance Approach
Process-Focused Variations
People-Focused Variations

8

privacy were centralized, but other aspects of review,
such as performance and clinical integraƟon, were
federated. SƟll other systems centralized governance of
enterprise soŌware but federated governance of
department-speciﬁc AI tools or centralized the
registraƟon process but federated the review and
monitoring processes. Many larger systems, even if
their processes were federated, menƟoned that they
were working to ensure open communicaƟon between
locaƟons to reduce or prevent repeƟƟon of work.
The project team also found interesƟng diﬀerences in
some of the logisƟcs of governance. However, all of the
health systems emphasized that they considered their
governance programs to be an evolving work in
progress and anƟcipated there could be changes in
processes and scope. For example, some governance
systems started with inventories and preliminary
evaluaƟons, but are now expanding to include aspects
of monitoring operaƟonal integraƟon and
performance. Other systems plan to expand the types
of tools that their governance will oversee over Ɵme.
Democratizing AI Across Health
Systems

Health care in the United States already has signiﬁcant
equity challenges. There is concern that AI tools could
worsen these inequiƟes either because the tools may
replicate and scale exisƟng biases in care if not
designed and tested carefully, or because the AI tools
are eﬀecƟve but only highly resourced health systems
can safely deploy the tools. If this happens, it will
greatly diminish the impact that AI could have,
especially in addressing persistent problems in
healthcare such as access issues and diagnosƟc
excellence.
We heard that government and health system
leadership cannot conƟnue to rely on volunteer eﬀorts
for sustainable governance of AI. Health systems are
concerned that they lack the resources to bring in staﬀ
or train exisƟng staﬀ, or to build the infrastructure
needed for eﬀecƟve and ethical governance.  There is a
criƟcal need for ways to scale and propagate internal AI
experƟse as well as templates and best pracƟces for
governance processes as health systems begin to
deploy these tools.
In the secƟons below, we will walk through some
recommendaƟons on how diﬀerent stakeholders can
help democraƟze safe and eﬃcient implementaƟon of
AI tools through eﬀecƟve governance.
Government AcƟons
Federal and state governments have mulƟple opƟons
to incenƟvize and to support eﬀecƟve governance of AI
tools in health. The OCR SecƟon 1557 rule described
earlier is one such example. The Oﬃce of the NaƟonal
Coordinator of Health InformaƟon Technology (ONC)
also released a ﬁnal rule on transparency requirements
for certain types of predicƟve decision support
intervenƟon tools. This later rule ensures that health
systems and users will have informaƟon about those
speciﬁc tools but also sets a baseline standard for what
informaƟon health systems should know about before
implemenƟng these types of care tools. Similarly, the
FDA recently put out guiding principles around
transparency for AI/ML devices that have signiﬁcant
overlap with ONC requirements.
At the state level, Colorado recently passed a law that
will require deployers of AI systems where outputs are
a “substanƟal factor” in decisions regarding the
provision, denial, cost, or terms of health care services
to implement a risk-management system, conduct
impact assessments, do annual reviews, and report any
discoveries of algorithmic discriminaƟon. Although the
speciﬁcs of these laws and rules can be debated, there
are clear opƟons for government bodies to incenƟvize
good governance. The government can also create
posiƟve incenƟves around governance such as safe
harbors for health system deployers that employ best
pracƟces to reduce some of the risk in deploying AI
tools, such as liability. For example, Colorado built an
aﬃrmaƟve defense into their law for deployers of AI
tools that could show that they had complied with
speciﬁc naƟonal or internaƟonal AI risk management
frameworks.
The government can also prioriƟze funding research to
simplify governance and make it more eﬃcient. This
may include creaƟng research funding prioriƟes around

9

governance best pracƟces, maturity models, and
infrastructure to make monitoring for performance
draŌ and bias and general surveillance more eﬃcient.
Government could also fund development of open-
source tools such as inventory systems and tesƟng
tools to make the governance process less
burdensome. A recent journal perspecƟve suggested
that the government could help build a registry of AI
tools similar to ClinicalTrials.gov that would also have a
federated component linking to health system
assessments of that tool. A system like this could also
provide HHS a central locaƟon for users and paƟents to
report safety concerns about AI tools, which is a task
required in the 2023 ExecuƟve Order on AI. Finally, the
government could consider establishing and funding
Health AI Technical Centers of Excellence to provide
training modules for staﬃng governance teams and act
as an expert resource for under-resourced health
systems, as well as general workforce development
around AI literacy.
Developer AcƟons
Developers are a signiﬁcant source of AI experƟse.
Although they cannot be considered imparƟal, they do
have an interest in increasing trust in AI tools and
ensuring that they are being implemented and used
correctly. The project team spoke with several
commercial developers of tools and heard concerns
that many health systems are not asking enough
quesƟons about their products. Developers and health
systems should be working together to create
standardized checklists of informaƟon for diﬀerent
types of AI tools, to set appropriate expectaƟons and
increase transparency. This would also allow
developers to create a standard informaƟon disclosure
form that could be shared with governance teams that
could reduce the amount of back-and-forth
communicaƟon between developers and governance
teams, increasing governance eﬃciencies. Health
systems that the project team spoke with frequently
menƟoned that transparency around health system
data movement and how that data is used is especially
important to them.
Developers should also work to foster collaboraƟon
and trust with health systems. Aligning on expectaƟons
early and improving understanding of health system
legal compliance requirements would be helpful. One
example of this involved product updates. Health
systems felt there were oŌen signiﬁcant mismatches
on what consƟtutes a “substanƟal change” that would
require more acƟve alerts to health systems to allow
for governance review. This was oŌen around data
security and privacy, but also when a product that
previously did not use AI/ML in its soŌware was
updated to include AI/ML components.
Developers can also create tools to facilitate local
governance. One company recently announced that
they would provide kits to simplify local tuning and
tesƟng of their products. This aligns with the previously
menƟoned FDA transparency principles staƟng that it
would be helpful for developers to provide informaƟon
on “how to conduct local site-speciﬁc acceptance
tesƟng or validaƟon” and “plans for ongoing
performance monitoring.” Another company we spoke
with described tools that would be able to automate
monitoring for performance driŌ.
Health System AcƟons
Health system leaders should prioriƟze AI governance
now and seek learning from early adopters, assessing
what is the right-sized approach for their speciﬁc
circumstances. However, health systems that have
already built governance systems or have signiﬁcant
experƟse in AI (such as academic health systems) also
have a role in democraƟzing AI across seƫngs. These
systems should share documentaƟon on how their
governance systems work, including tools such as
registraƟon/informaƟon intake forms and surveillance
procedures, and consider partnering with other health
systems, especially those with fewer resources. At the
same Ɵme, all health systems need to work to diﬀuse
knowledge about AI and responsible AI
implementaƟon throughout their workforce.
To accomplish both tasks, health systems can create
peer-to-peer learning spaces to educate, share and
support each other implemenƟng best pracƟces in AI
governance. For example, the ECHO InsƟtute New
Mexico Hub is starƟng a community of pracƟce for
providers around implemenƟng AI in medicine. A
recent pilot project called the PracƟce Network also

10

just launched, where parƟcipants will receive “access
to one-on-one guidance, expert consultaƟon, peer
learning community, educaƟonal materials, and other
resources” from more experienced health systems
partners to increase equitable use of AI in healthcare.
Health systems with less AI experƟse have found that
working with more local or smaller AI developers can
be helpful in building a more trusƟng relaƟonship and
allow the developer to beter understand and then
design toward the needs of a speciﬁc health system.
Other Stakeholder AcƟons
Other stakeholders also have important roles. EnƟƟes
such as clinical socieƟes, public-private partnerships,
and standards groups should focus on creaƟng
guidance in this space. Examples include the NaƟonal
Academies’ AI Code of Conduct and the CoaliƟon for
Health AI’s Assurance Guides. We also expect that third
parƟes will enter this space to help provide assurance
reviews and provide contracted governance services or
commercial governance soŌware tools. One early
example is Dandelion Health, which provides a free
validaƟon service for certain types of health AI tools
through a grant from the Gordon and Bety Moore
FoundaƟon. Outsourcing some of these tasks to
reusable validaƟon plaƞorms could create eﬃciencies
of scale and reduce overall costs.
Medical, nursing, and other clinical professional
schools and training programs also should develop
curricula on best pracƟces in assessment and using AI
tools while clinical socieƟes and other organizaƟons
should establish conƟnuing educaƟon courses on
responsible governance and use of AI.
Conclusion
AI tools present an extraordinary opportunity to
transform health care, but establishing a robust AI
governance framework is essenƟal to ensure that these
tools are deployed safely, ethically, and in compliance
with regulatory standards. Governance systems not
only protect paƟent safety and foster trust; they also
facilitate innovaƟon by providing clear guidelines and
processes for assessing and implemenƟng AI
technologies. The diverse strategies employed by
diﬀerent health systems highlight the conƟnued need
for ﬂexibility in governance approaches, factoring in
health systems’ speciﬁc consideraƟons around
resources and processes. However, the number of
commonaliƟes found when exploring the diﬀerent
governance processes suggests that health systems
should make use of published frameworks and
guidance as they create their own processes.
Work is also needed to ensure that the safe and
eﬀecƟve use of AI tools can be democraƟzed across all
health systems. Widespread implementaƟon of AI
governance in healthcare hinges on addressing key
challenges such as funding, staﬃng, and training. This
will involve targeted acƟons among government,
developers, health systems and other stakeholders.
Ensuring that AI tools can be safely used in all health
systems will be a challenging and ongoing task but
must be accomplished if health AI is to fulfill its
potential to improve health outcomes, reduce costs,
enhance the clinical experience for both patients and
providers, and advance health equity.

About Duke Health. Duke Health is commited to advancing health and
transforming lives through clinical care, medical educaƟon, and innovaƟve
research. Duke Health’s comprehensive network of hospitals, outpaƟent
clinics, and specialty centers, serving diverse populaƟons across NC and
beyond. Its mission emphasizes training the next generaƟon of healthcare
leaders and advancing cuƫng-edge research in areas such as precision
medicine, AI-driven healthcare, and populaƟon health. Duke Health is a
commited to equity, innovaƟon, and conƟnuous improvement, ensuring
that care is not only safe and eﬀecƟve but also equitable and responsive to
the needs of all paƟents. Through collaboraƟve eﬀorts across its academic
and clinical arms, Duke Health remains at the forefront of addressing the
most complex healthcare challenges, fostering a healthier future for
individuals and communiƟes worldwide.

About Duke-Margolis. The Robert J. Margolis, MD, InsƟtute for Health
Policy at Duke University is directed by Mark McClellan, MD, PhD, and
brings together experƟse from the Washington, DC, policy community, Duke
University, and Duke Health to address the most pressing issues in health
policy. The mission of Duke-Margolis is to improve health, health equity and
the value of health care through pracƟcal, innovaƟve, and evidence-based
policy soluƟons. Duke-Margolis catalyzes Duke University’s leading
capabiliƟes, including interdisciplinary academic research and capacity for
educaƟon and engagement, to inform policymaking and implementaƟon for
beter health and health care. For more informaƟon, visit
healthpolicy.duke.edu.

11

Appendix A: Expert Workshop Participant List
Health System Governance of AI Tools
Virtual Expert Workshop | June 6, 2024

Laura Adams
NaƟonal Academy of Medicine
Brian Anderson
CoaliƟon for Health AI
Allie DeLonay
SAS
Nicoleta J Economou
Duke Health
Tom Ferrone
Tempus AI
James Gaston
Parkland Health & Hospital System
Mallory Gibreal
Bryan Health
Karen Habercross
University of Chicago
Marianne Hamilton Lopez
Duke-Margolis InsƟtute for Health Policy
James Leo
MemorialCare Health System
Bret Moran
Parkland Health & Hospital System
Zachary Lipton
Abridge
Valerie Parker
Duke-Margolis InsƟtute for Health Policy
Anurang Revri
Stanford Healthcare
Ram Rimal
University of North Carolina Chapel Hill
Brian Scarpelli
Connected Health IniƟaƟve
ChrisƟna Silcox
Duke-Margolis InsƟtute for Health Policy
Jennifer Stoll
OCHIN, Inc.
ChrisƟne Swisher
Oracle Health
Sylvia Trujillo
OCHIN, Inc.
David Vidal
Mayo Clinic
Celena Wheeler
Oracle Health
Ellen Woo
Kaiser Permanente
Daniel Yang
Kaiser Permanente
