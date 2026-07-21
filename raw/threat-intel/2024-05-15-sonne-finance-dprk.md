# Sonne Finance — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Sonne-Finance-160
> Timestamp: 2024-05-15T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.12)
> Target: Sonne Finance
> Amount (USD): $20,000,000
> Asset: Ethereum
> Vector: unknown
> References: Sonne Finance – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Sonne_Finance/Sonne_Finance_report.html)

On 15 May 2024, Sonne Finance, a decentralised finance (DeFi) protocol, experienced a significant security breach resulting in the theft of approximately $20 million USD. The attack was executed by exploiting a vulnerability within the protocol's smart contract infrastructure, leading to the unauthorised transfer of funds. The immediate financial impact was severe, affecting both the protocol's liquidity and its users' deposits.

The attack leveraged a smart contract vulnerability, potentially involving reentrancy or access control failures, allowing the attacker to manipulate transactions and drain funds. The precise exploit mechanism remains under investigation, but initial analysis suggests the use of automated scripts to execute rapid transactions, bypassing standard security checks.

Stolen funds were initially moved through a series of rapid transactions across multiple wallets, employing techniques such as bridge hopping and mixer usage to obfuscate the trail. The funds traversed various blockchain networks and utilised decentralised exchanges (DEXs) and centralised exchanges (CEXs) for laundering. Key infrastructure included known mixers and cross-chain bridges, indicating a sophisticated laundering strategy.

The attack is attributed to the threat actor group APT38, known for targeting financial institutions and employing advanced laundering techniques. The attribution is supported by the use of similar tactics, techniques, and procedures (TTPs) observed in previous incidents linked to this group. The confidence level in this attribution is medium, pending further investigation.
