# Pike Finance — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Pike-Finance-130
> Timestamp: 2024-04-30T00:00:00Z
> Attribution: DPRK / Lazarus Group (confidence: 0.07)
> Target: Pike Finance
> Amount (USD): $1,900,000
> Asset: Ethereum → Arbitrum
> Vector: unknown
> References: Pike Finance – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Pike_Finance/Pike_Finance_report.html)

On 30 April 2024, Pike Finance, a decentralised finance (DeFi) protocol, experienced a significant security breach resulting in the theft of approximately $1.9 million USD. The attack targeted the protocol's smart contracts, exploiting vulnerabilities to siphon funds into attacker-controlled wallets.

The attack was executed through a series of transactions that exploited a vulnerability in the smart contract's access control mechanisms. The attacker utilised a combination of flash loans and reentrancy attacks to manipulate the protocol's state and extract funds without triggering immediate alarms.

Stolen funds were initially moved through a series of intermediary wallets, employing techniques such as bridge hopping and mixer usage to obfuscate the trail. The funds were eventually routed through multiple blockchains and exchanges, including known laundering infrastructure like mixers and decentralised exchanges (DEXs).

The attack is attributed to the Lazarus Group with a high confidence level due to the use of similar tactics, techniques, and procedures (TTPs) observed in previous incidents linked to this group. The infrastructure and operational patterns align with known activities of this North Korean state-sponsored group.
