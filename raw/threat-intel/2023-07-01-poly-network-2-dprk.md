# Poly Network 2 — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Poly-Network---2-135
> Timestamp: 2023-07-01T00:00:00Z
> Attribution: DPRK / Lazarus Group (confidence: 0.14)
> Target: Poly Network 2
> Amount (USD): $611,000,000
> Asset: Ethereum
> Vector: bridge exploit
> References: Poly Network 2 – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Poly_Network_-_2/Poly_Network_-_2_report.html)

The Poly Network incident, designated as Poly_Network_-_2, involved a significant breach where approximately $611 million was illicitly transferred from the Poly Network protocol. The attack was executed on 10 August 2021, targeting the cross-chain interoperability protocol, which facilitates asset transfers across different blockchains. The immediate financial impact was substantial, affecting numerous users and the protocol's operations.

The attack exploited a vulnerability in the Poly Network's smart contract system, specifically targeting the bridge mechanism that manages cross-chain transactions. The attacker manipulated the contract's logic to authorise large transfers without proper validation. This breach highlights potential weaknesses in access control and transaction validation within smart contracts.

Stolen funds were initially moved from the exploit wallet to a series of intermediary wallets, employing complex layering techniques including bridge hopping and mixing services. The funds traversed multiple chains and utilised decentralised exchanges (DEXs) to obfuscate the trail. The primary laundering strategy involved the use of known mixers and cross-chain bridges to disperse the assets.

The Lazarus Group, a North Korean state-sponsored hacking group, is suspected of orchestrating the attack. This attribution is based on the group's known tactics, techniques, and procedures (TTPs), which align with the observed attack patterns and infrastructure used. The group's historical involvement in similar high-profile cryptocurrency heists further supports this hypothesis.
