# BingX — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-BingX-25
> Timestamp: 2024-09-19T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.24)
> Target: BingX
> Amount (USD): $44,700,000
> Asset: Ethereum
> Vector: unknown
> References: BingX – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/BingX/BingX_report.html)

On 19 September 2024, the cryptocurrency exchange BingX experienced a significant security breach resulting in the theft of approximately $44.7 million USD. The attack targeted the exchange's infrastructure, exploiting vulnerabilities that allowed unauthorised access to user funds. The immediate financial impact was substantial, affecting both the exchange's liquidity and its users' assets.

The attack was executed through a sophisticated exploitation of BingX's infrastructure, potentially involving compromised private keys or vulnerabilities in smart contract implementations. The exact exploit mechanism remains under investigation, but initial analysis suggests a combination of access control failures and potential reentrancy attacks.

Stolen funds were rapidly moved from the initial exploit wallet through a series of layering transactions involving multiple blockchain networks and mixing services. The funds were eventually routed through known laundering infrastructure, including bridge hopping and mixer usage, before reaching various destination wallets.

The attack is suspected to be linked to the hacker group APT38, known for targeting financial institutions. This attribution is based on the use of similar tactics, techniques, and procedures (TTPs) observed in previous incidents attributed to this group.
