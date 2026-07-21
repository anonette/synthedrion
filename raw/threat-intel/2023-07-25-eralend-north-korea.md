# EraLend — North Korea-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-EraLend-60
> Timestamp: 2023-07-25T00:00:00Z
> Attribution: North Korea / unknown group (confidence: unstated)
> Target: EraLend
> Amount (USD): $3,400,000
> Asset: Ethereum
> Vector: unknown
> References: EraLend – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/EraLend/EraLend_report.html)

On 25 July 2023, EraLend, a decentralised finance (DeFi) protocol, experienced a significant security breach resulting in the theft of approximately $3.4 million USD. The attack targeted the protocol's smart contracts, exploiting vulnerabilities to siphon funds from user deposits. The immediate financial impact was substantial, affecting both the protocol's liquidity and its user base.

The attack was executed through a series of sophisticated transactions that exploited a vulnerability in EraLend's smart contract infrastructure. The specific weakness involved was likely related to improper access control or a reentrancy flaw, allowing the attacker to manipulate contract functions to drain funds. No specific smart contract functions or scripts have been identified in the source material.

Stolen funds were initially moved from the exploit wallet to several intermediary addresses, employing a strategy of rapid multi-hop transactions across different chains and using various DeFi protocols for layering. The attacker utilised known bridges and mixers to obfuscate the fund trail, eventually attempting to cash out through centralised exchanges.

The identity of the threat actor remains unknown, with no direct attribution possible from the available data. However, the use of sophisticated laundering techniques and infrastructure suggests a well-resourced and experienced group. No specific threat actor group has been conclusively linked to this incident.
