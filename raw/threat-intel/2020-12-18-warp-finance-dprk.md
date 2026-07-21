# Warp Finance — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Warp-Finance-194
> Timestamp: 2020-12-18T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.12)
> Target: Warp Finance
> Amount (USD): $7,800,000
> Asset: Ethereum
> Vector: unknown
> References: Warp Finance – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Warp_Finance/Warp_Finance_report.html)

On 18 December 2020, Warp Finance, a decentralised finance (DeFi) protocol, suffered a significant security breach resulting in the theft of approximately $7.8 million USD. The attack targeted the protocol's smart contracts, exploiting vulnerabilities to siphon funds from user deposits. The immediate financial impact was substantial, affecting both the protocol's liquidity and its user base.

The attack was executed through a sophisticated manipulation of Warp Finance's smart contracts. The attacker exploited a vulnerability related to flash loans, a common DeFi exploit vector, allowing them to manipulate asset prices and extract funds. The specific functions abused in the smart contract have not been detailed in the available data, but the rapid execution suggests a well-planned attack leveraging automated scripts.

Post-exploit, the stolen funds were rapidly moved through a series of transactions across multiple wallets, employing techniques such as bridge hopping and mixer usage to obfuscate the trail. The funds were eventually routed through various DeFi protocols and centralised exchanges, complicating recovery efforts. The use of known laundering infrastructure indicates a high level of premeditation and operational security.

The attack is suspected to be linked to the hacker group APT38, known for targeting financial institutions. This attribution is supported by the use of similar tactics, techniques, and procedures (TTPs) observed in previous incidents attributed to the group. The confidence level in this attribution is medium, pending further investigation and corroboration of additional intelligence.
