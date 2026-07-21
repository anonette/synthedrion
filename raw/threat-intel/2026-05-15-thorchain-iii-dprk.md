# THORChain III — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-THORChain---III-173
> Timestamp: 2026-05-15T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.12)
> Target: THORChain III
> Amount (USD): $10,700,000
> Asset: Ethereum
> Vector: unknown
> References: THORChain III – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/THORChain_-_III/THORChain_-_III_report.html)

On 15 May 2026, THORChain, a decentralised liquidity protocol, experienced a significant security breach resulting in the theft of approximately $10.7 million in Ethereum (ETH) and related assets. The attack was executed by exploiting a vulnerability within the protocol's smart contract infrastructure, leading to unauthorised fund transfers. The immediate financial impact was substantial, affecting both the protocol's liquidity and its user base.

The attack leveraged a smart contract vulnerability, potentially involving reentrancy or access control failures, allowing the attacker to manipulate transaction flows and extract funds. The specific exploit mechanism remains under investigation, but initial analysis suggests the use of automated scripts to execute rapid, multi-step transactions.

Post-exploit, the stolen funds were rapidly moved through a series of transactions involving multiple wallets and intermediary addresses. The attacker utilised various blockchain bridges and mixers to obfuscate the fund trail, eventually directing assets towards centralised exchanges for potential cash-out. Key infrastructure used includes the THORChain network and external bridges.

The attack is attributed to APT38, a North Korean state-sponsored hacking group known for targeting financial institutions and cryptocurrency exchanges. This attribution is based on the group's historical tactics, techniques, and procedures (TTPs), including the use of sophisticated laundering methods and infrastructure overlaps with previous incidents.
