# Merlin DEX — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Merlin-DEX-109
> Timestamp: 2023-04-25T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.18)
> Target: Merlin DEX
> Amount (USD): $1,820,000
> Asset: Ethereum
> Vector: unknown
> References: Merlin DEX – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Merlin_DEX/Merlin_DEX_report.html)

On 25 April 2023, Merlin DEX, a decentralised exchange operating on the Ethereum blockchain, experienced a significant security breach resulting in the theft of approximately $1,820,000.00 USD. The attack was executed by exploiting a vulnerability in the protocol's smart contract, leading to unauthorised fund transfers.

The attack leveraged a smart contract vulnerability, potentially involving reentrancy or access control failures. The attacker executed a series of transactions that manipulated the contract's state, allowing them to siphon funds without triggering security mechanisms. The exact exploit mechanism remains under investigation, but initial analysis suggests a sophisticated understanding of the protocol's architecture.

Post-exploit, the stolen funds were rapidly moved through a series of transactions involving multiple wallets and blockchain networks. The attacker utilised known laundering techniques such as bridge hopping and mixer usage to obfuscate the fund trail. Key infrastructure used includes Ethereum bridges and potential mixers, with final destinations suspected to be centralised exchanges for cash-out.

The attack is attributed to the hacker group APT38 with medium confidence. This assessment is based on the use of similar tactics, techniques, and procedures (TTPs) observed in previous incidents linked to the group, including sophisticated laundering methods and infrastructure overlaps.
