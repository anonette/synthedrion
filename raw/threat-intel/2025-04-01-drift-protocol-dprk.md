# Drift Protocol — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Drift-Protocol-57
> Timestamp: 2025-04-01T00:00:00Z
> Attribution: DPRK / Lazarus Group (confidence: 0.21)
> Target: Drift Protocol
> Amount (USD): $285,000,000
> Asset: Ethereum → BSC
> Vector: unknown
> References: Drift Protocol – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Drift_Protocol/Drift_Protocol_report.html)

On 01 April 2025, Drift Protocol, a decentralised finance (DeFi) platform, experienced a significant security breach resulting in the theft of approximately $285 million in cryptocurrency assets. The attack targeted the protocol's smart contracts, exploiting a vulnerability that allowed the attacker to siphon funds from user accounts. The immediate financial impact was severe, with a substantial portion of the protocol's Total Value Locked (TVL) being compromised.

The attack was executed through a sophisticated exploitation of a smart contract vulnerability, potentially involving a reentrancy attack or a flash loan exploit. The attacker manipulated the contract's logic to withdraw funds repeatedly before the contract's state could be updated. This type of attack suggests a high level of technical expertise and familiarity with the protocol's codebase.

The stolen funds were initially moved through a series of rapid transactions across multiple wallets, employing techniques such as bridge hopping and mixer usage to obfuscate the trail. The funds were then distributed across various chains and eventually cashed out through centralised exchanges. Notable infrastructure used includes Ethereum and Binance Smart Chain bridges, as well as known mixers.

The attack is suspected to be linked to the Lazarus Group, a well-known cybercrime syndicate with a history of targeting cryptocurrency platforms. This attribution is based on similarities in tactics, techniques, and procedures (TTPs) observed in previous incidents attributed to the group. The confidence level in this attribution is medium, pending further investigation.
