# Wormhole — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Wormhole-202
> Timestamp: 2022-02-02T00:00:00Z
> Attribution: DPRK / Lazarus Group (confidence: 0.8)
> Target: Wormhole
> Amount (USD): $326,000,000
> Asset: Ethereum
> Vector: bridge exploit
> References: Wormhole – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Wormhole/Wormhole_report.html)

The Wormhole incident involved a significant crypto hack targeting a blockchain bridge protocol, resulting in the theft of approximately $326 million USD. The attack occurred on 2 February 2022, exploiting vulnerabilities within the protocol's smart contract infrastructure. The immediate financial impact was severe, affecting the protocol's liquidity and user trust.

The attack was executed by exploiting a vulnerability in the bridge's smart contract, allowing the attacker to mint wrapped tokens without the necessary collateral. This exploit was facilitated by a failure in the contract's validation logic, which did not adequately verify the authenticity of the minting requests.

Stolen funds were rapidly moved through a series of transactions involving multiple blockchain networks and laundering techniques. The attacker utilised bridge hopping, mixer services, and decentralised exchanges (DEXs) to obfuscate the fund flow. Key infrastructure included the use of the Ethereum and Binance Smart Chain networks, with funds eventually reaching centralised exchanges for cash-out.

The Lazarus Group, a North Korean state-sponsored hacking group, is suspected of orchestrating the attack. This attribution is supported by the group's known tactics, techniques, and procedures (TTPs), which align with the methods used in this incident, including the use of sophisticated laundering techniques and infrastructure overlaps with previous attacks.
