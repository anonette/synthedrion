# GriffinAI — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-GriffinAI-72
> Timestamp: 2025-09-24T00:00:00Z
> Attribution: DPRK / Lazarus Group (confidence: 0.21)
> Target: GriffinAI
> Amount (USD): $3,000,000
> Asset: BSC → Ethereum
> Vector: unknown
> References: GriffinAI – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/GriffinAI/GriffinAI_report.html)

On 24 September 2025, GriffinAI, a blockchain-based protocol, experienced a significant security breach resulting in the theft of approximately $3,000,000 USD equivalent in various cryptocurrencies. The attack was executed by exploiting a vulnerability within the protocol's smart contract infrastructure, leading to unauthorised fund transfers. The immediate financial impact was substantial, affecting both the protocol's operations and its user base.

The attack leveraged a smart contract vulnerability, potentially involving reentrancy or access control failures, allowing the attacker to execute multiple transactions that drained funds from the protocol. The specific functions exploited remain under investigation, but the rapid sequence of transactions suggests a well-planned attack using automated scripts.

Stolen funds were quickly moved through a series of transactions involving multiple wallets, bridges, and exchanges. The attacker utilised bridge hopping and mixer services to obfuscate the fund trail, eventually attempting to cash out through centralised exchanges. Key infrastructure used included known laundering services and cross-chain bridges.

The attack is suspected to be linked to the Lazarus Group, a known cybercriminal organisation with a history of targeting blockchain platforms. This attribution is supported by similarities in tactics, techniques, and procedures (TTPs) observed in previous incidents attributed to the group.
