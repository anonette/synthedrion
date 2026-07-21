# Wasabi Protocol — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Wasabi-Protocol-195
> Timestamp: 2026-04-30T00:00:00Z
> Attribution: DPRK / AndAriel (confidence: 0.1)
> Target: Wasabi Protocol
> Amount (USD): $5,900,000
> Asset: Ethereum
> Vector: unknown
> References: Wasabi Protocol – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Wasabi_Protocol/Wasabi_Protocol_report.html)

On 30 April 2026, the Wasabi Protocol, a decentralised finance (DeFi) platform, experienced a significant security breach resulting in the theft of approximately $5.9 million in various cryptocurrencies. The attack targeted the protocol's smart contracts, exploiting a vulnerability that allowed the attacker to siphon funds from user deposits. The immediate financial impact was severe, affecting both the protocol's liquidity and its user base.

The attack was executed by exploiting a vulnerability in the Wasabi Protocol's smart contract code. The attacker utilised a reentrancy attack, a common exploit in DeFi platforms, which allowed them to repeatedly withdraw funds before the contract's state was updated. This exploit was facilitated by a lack of proper access control and validation checks within the contract's functions.

Following the exploit, the stolen funds were rapidly moved through a series of transactions involving multiple intermediary wallets. The attacker employed various laundering techniques, including the use of decentralised exchanges (DEXs), cross-chain bridges, and mixers to obfuscate the fund flow. The funds were eventually distributed across several centralised exchanges (CEXs) for cash-out.

The threat actor is suspected to be the AndAriel group, known for previous DeFi exploits. This attribution is based on the use of similar Tactics, Techniques, and Procedures (TTPs) observed in past incidents, including the use of specific laundering patterns and infrastructure overlaps. The confidence level in this attribution is medium.
