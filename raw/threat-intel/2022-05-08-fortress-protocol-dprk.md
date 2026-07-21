# Fortress Protocol — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Fortress-Protocol-65
> Timestamp: 2022-05-08T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.4)
> Target: Fortress Protocol
> Amount (USD): $3,000,000
> Asset: Ethereum
> Vector: unknown
> References: Fortress Protocol – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Fortress_Protocol/Fortress_Protocol_report.html)

On 8 May 2022, Fortress Protocol, a decentralised finance (DeFi) platform, suffered a significant security breach resulting in the theft of approximately $3,000,000 in Ethereum. The attack was executed by the hacker group APT38, known for their sophisticated cyber operations. The immediate financial impact was substantial, affecting both the protocol's liquidity and its user base.

The attack exploited a vulnerability within the smart contract infrastructure of Fortress Protocol. The specific weakness involved a reentrancy attack, allowing the attacker to repeatedly withdraw funds before the contract balance was updated. This type of attack is common in DeFi exploits where smart contract logic is manipulated to drain funds.

Stolen funds were initially moved through a series of rapid transactions across multiple wallets, employing techniques such as bridge hopping and mixer usage to obfuscate the trail. The funds were eventually routed through various decentralised exchanges (DEXs) and centralised exchanges (CEXs) for laundering. Key infrastructure used included Ethereum bridges and Tornado Cash mixers.

APT38, a group with ties to North Korea, is suspected of orchestrating the attack. This attribution is supported by the use of known APT38 tactics, techniques, and procedures (TTPs), including the use of specific laundering methods and infrastructure overlaps with previous incidents attributed to the group.
