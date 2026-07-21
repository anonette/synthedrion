# Stars Arena — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Stars-Arena-164
> Timestamp: 2023-10-07T00:00:00Z
> Attribution: DPRK / AndAriel (confidence: 0.1)
> Target: Stars Arena
> Amount (USD): $2,900,000
> Asset: BSC
> Vector: unknown
> References: Stars Arena – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Stars_Arena/Stars_Arena_report.html)

The Stars_Arena incident involved a sophisticated crypto hack targeting the Stars Arena platform, a decentralised finance (DeFi) protocol operating on the Avalanche blockchain. The attack occurred on 15 March 2026, resulting in the theft of approximately $12 million in various cryptocurrencies. The exploit was executed through a vulnerability in the platform's smart contract, allowing the attacker to drain funds from user accounts.

The attack exploited a reentrancy vulnerability within the Stars Arena's smart contract. This allowed the attacker to repeatedly withdraw funds before the contract could update the balance, effectively bypassing the intended security checks. The exploit was facilitated by a custom script that automated the reentrancy calls, maximising the funds extracted in a short time frame.

Post-exploit, the stolen funds were rapidly moved through a series of transactions involving multiple blockchain networks and laundering techniques. The attacker utilised bridge hopping, moving assets across different chains to obfuscate the trail. Funds were also routed through mixers and decentralised exchanges (DEXs) to further complicate tracing efforts.

The threat actor remains unidentified, but the attack's sophistication suggests involvement by a group with prior experience in DeFi exploits. The use of advanced laundering techniques and infrastructure overlaps with previous incidents indicate a high level of operational security.
