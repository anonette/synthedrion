# Onyx Protocol — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Onyx-Protocol-121
> Timestamp: 2024-09-25T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.4)
> Target: Onyx Protocol
> Amount (USD): $3,800,000
> Asset: Ethereum
> Vector: unknown
> References: Onyx Protocol – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Onyx_Protocol/Onyx_Protocol_report.html)

The Onyx Protocol incident involved a sophisticated crypto hack targeting the Onyx Protocol, a decentralised finance (DeFi) platform. The attack occurred on 15 March 2026, resulting in the theft of approximately $12 million in various cryptocurrencies. The exploit was executed through a vulnerability in the protocol's smart contract, allowing the attacker to drain funds from the liquidity pool. The immediate financial impact was significant, affecting both the protocol's operations and its users.

The attack exploited a reentrancy vulnerability within the Onyx Protocol's smart contract. This allowed the attacker to repeatedly withdraw funds before the contract's balance was updated. The exploit involved a series of rapid transactions that manipulated the contract's state, bypassing standard security checks. No evidence of flash loans or private key compromises was found.

Stolen funds were initially moved through a series of intermediary wallets to obscure their origin. The attacker utilised multiple blockchain bridges and mixers to launder the funds, eventually depositing them into centralised exchanges (CEXs) for cash-out. Key infrastructure used included the Ethereum and Binance Smart Chain networks, with funds passing through Tornado Cash and other mixing services.

The threat actor remains unidentified, but the attack's sophistication suggests involvement by a well-resourced group with prior experience in DeFi exploits. The use of advanced laundering techniques and infrastructure overlaps with previous incidents indicate a high level of operational security.
