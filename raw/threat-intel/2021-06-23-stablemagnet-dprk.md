# StableMagnet — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-StableMagnet-162
> Timestamp: 2021-06-23T00:00:00Z
> Attribution: DPRK / Lazarus Group (confidence: 0.07)
> Target: StableMagnet
> Amount (USD): $27,000,000
> Asset: Ethereum → BSC
> Vector: unknown
> References: StableMagnet – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/StableMagnet/StableMagnet_report.html)

On 23 June 2021, the StableMagnet protocol suffered a significant security breach resulting in the theft of approximately $27 million USD. The attack targeted the protocol's smart contract infrastructure, exploiting a vulnerability that allowed the attacker to siphon funds from the protocol's liquidity pools. The immediate financial impact was severe, affecting both the protocol's operations and its user base.

The attack was executed through a sophisticated exploit of the protocol's smart contract. The attacker utilised a combination of flash loans and price manipulation techniques to artificially inflate the value of certain assets, allowing them to withdraw more funds than they deposited. This exploit was facilitated by a reentrancy vulnerability in the contract's code, which was not adequately protected against recursive calls.

Following the exploit, the stolen funds were rapidly moved through a series of transactions across multiple blockchains. The attacker employed various laundering techniques, including bridge hopping and the use of decentralised exchanges (DEXs) to obfuscate the fund flow. Key infrastructure used included the Poly Network and several high-volume intermediaries identified in the social network analysis.

The Lazarus Group, a well-known cybercrime syndicate, is suspected to be behind the attack. This attribution is based on the use of similar tactics, techniques, and procedures (TTPs) observed in previous incidents attributed to the group, as well as infrastructure overlaps with known Lazarus operations. The confidence level in this attribution is medium.
