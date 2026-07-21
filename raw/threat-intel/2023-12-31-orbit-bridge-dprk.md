# Orbit Bridge — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Orbit-Bridge-124
> Timestamp: 2023-12-31T00:00:00Z
> Attribution: DPRK / Lazarus Group (confidence: 0.8)
> Target: Orbit Bridge
> Amount (USD): $81,500,000
> Asset: Ethereum
> Vector: bridge exploit
> References: Orbit Bridge – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Orbit_Bridge/Orbit_Bridge_report.html)

On 31 December 2023, the Orbit Bridge protocol was compromised, resulting in the theft of approximately $81.5 million USD. The attack targeted the bridge's infrastructure, exploiting vulnerabilities to siphon funds from the protocol's reserves. The immediate financial impact was significant, affecting both the protocol's liquidity and its users' assets.

The attack was executed by exploiting a vulnerability within the Orbit Bridge's smart contract infrastructure. The specific weakness involved a reentrancy attack, allowing the attacker to repeatedly withdraw funds before the contract's state was updated. This type of attack is often facilitated by inadequate access control mechanisms and improper handling of contract state changes.

Stolen funds were initially moved through a series of rapid transactions across multiple wallets, employing techniques such as bridge hopping and mixer usage to obfuscate the trail. The funds were laundered through various blockchain networks, including Ethereum and Binance Smart Chain, before reaching centralised exchanges for cash-out.

The attack is attributed to the Lazarus Group with high confidence. This attribution is based on the use of similar tactics, techniques, and procedures (TTPs) observed in previous incidents linked to this group, including infrastructure overlaps and transaction patterns.
