# Poly Network — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Poly-Network-134
> Timestamp: 2021-08-10T00:00:00Z
> Attribution: DPRK / Lazarus Group (confidence: 0.14)
> Target: Poly Network
> Amount (USD): $611,000,000
> Asset: Ethereum
> Vector: bridge exploit
> References: Poly Network – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Poly_Network/Poly_Network_report.html)

On 10 August 2021, Poly Network, a cross-chain protocol, suffered a significant security breach resulting in the theft of approximately $611 million in various cryptocurrencies. The exploit targeted the protocol's smart contract infrastructure, allowing the attacker to transfer funds from Poly Network's wallets to addresses under their control.

The attack exploited a vulnerability in the smart contract's access control mechanism, allowing the attacker to bypass security checks and authorise transactions without proper validation. This involved manipulating the contract's logic to approve large transfers to the attacker's wallets.

Stolen funds were initially moved through a series of rapid transactions across multiple addresses, employing techniques such as bridge hopping and mixer usage to obfuscate the trail. The funds were distributed across various blockchains and eventually routed through centralised exchanges for cash-out.

The Lazarus Group, a North Korean state-sponsored hacking group, is suspected of orchestrating the attack. This attribution is based on the group's known tactics, techniques, and procedures (TTPs), including the use of similar laundering methods and infrastructure overlaps with previous incidents.
