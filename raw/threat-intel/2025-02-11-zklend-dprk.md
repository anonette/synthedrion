# zkLend — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-zkLend-213
> Timestamp: 2025-02-11T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.41)
> Target: zkLend
> Amount (USD): $9,570,000
> Asset: Ethereum
> Vector: unknown
> References: zkLend – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/zkLend/zkLend_report.html)

On 11 February 2025, zkLend, a decentralised finance protocol, experienced a significant security breach resulting in the theft of approximately $9,570,000. The attack was executed by exploiting a vulnerability within the protocol's smart contract infrastructure, leading to unauthorised fund transfers. The immediate financial impact was substantial, affecting both the protocol's liquidity and its user base.

The attack leveraged a smart contract vulnerability, potentially involving reentrancy or access control failures, allowing the attacker to manipulate transaction flows and extract funds. The precise exploit mechanism remains under investigation, but initial analysis suggests the use of automated scripts to execute rapid transactions.

Stolen funds were initially moved through a series of rapid transactions across multiple wallets, employing techniques such as bridge hopping and mixer usage to obfuscate the trail. The funds traversed various blockchain networks and utilised decentralised exchanges (DEXs) and centralised exchanges (CEXs) for laundering.

The attack is attributed to the hacker group APT38, known for its sophisticated cyber operations and previous involvement in similar incidents. The attribution is supported by transaction patterns and infrastructure overlaps with past attacks linked to APT38.
