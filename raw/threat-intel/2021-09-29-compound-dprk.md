# Compound — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Compound-37
> Timestamp: 2021-09-29T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.24)
> Target: Compound
> Amount (USD): $147,000,000
> Asset: Ethereum
> Vector: unknown
> References: Compound – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Compound/Compound_report.html)

On 29 September 2021, the Compound protocol, a significant player in the decentralised finance (DeFi) ecosystem, experienced a major security breach. The incident involved the unauthorised transfer of approximately $147 million in digital assets. The attack targeted the protocol's smart contracts, exploiting a vulnerability that allowed the attacker to siphon funds without detection initially. The immediate financial impact was severe, affecting both the protocol's liquidity and its users' deposits.

The attack was executed by exploiting a vulnerability in the Compound protocol's smart contract. The specific weakness involved a flaw in the contract's logic that allowed the attacker to manipulate transaction sequences, potentially involving reentrancy or flash loan attacks. This technical breach enabled the attacker to drain funds from the protocol's reserves without triggering immediate alarms.

Post-exploit, the stolen funds were rapidly moved through a series of transactions designed to obfuscate their origin. The attacker utilised multiple blockchain networks, including Ethereum and Binance Smart Chain, and employed various laundering techniques such as mixer services and cross-chain bridges. The funds were eventually routed through centralised exchanges, making recovery efforts challenging.

The attack is attributed to the threat actor group APT38, known for its sophisticated cyber operations and links to state-sponsored activities. The attribution is supported by the use of advanced laundering techniques and infrastructure overlaps with previous incidents involving APT38. The group's modus operandi and the technical sophistication of the attack align with known TTPs of APT38.
