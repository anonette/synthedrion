# Grim Finance — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Grim-Finance-73
> Timestamp: 2021-12-18T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.4)
> Target: Grim Finance
> Amount (USD): $30,000,000
> Asset: Ethereum
> Vector: unknown
> References: Grim Finance – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Grim_Finance/Grim_Finance_report.html)

On 18 December 2021, Grim Finance, a decentralised finance (DeFi) protocol, suffered a significant security breach resulting in the theft of approximately $30 million USD. The attack targeted the protocol's smart contracts, exploiting vulnerabilities to siphon funds from user deposits. The immediate financial impact was severe, affecting the protocol's liquidity and user trust.

The attack was executed through a vulnerability in Grim Finance's smart contract architecture, specifically exploiting a reentrancy flaw. This allowed the attacker to repeatedly withdraw funds before the contract's balance was updated. The exploit involved sophisticated scripting to automate the attack sequence, indicating a high level of technical proficiency.

Stolen funds were initially moved through a series of rapid transactions across multiple wallets, employing techniques such as bridge hopping and mixer usage to obfuscate the trail. The funds were subsequently laundered through various DeFi protocols and centralised exchanges, including the use of high-volume intermediaries identified in the social network analysis.

The attack is suspected to be linked to the APT38 group, known for targeting financial institutions with similar tactics. The use of advanced laundering techniques and infrastructure overlaps with previous incidents attributed to this group support this hypothesis.
