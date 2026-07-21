# RocketSwap — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-RocketSwap-148
> Timestamp: 2023-08-14T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.4)
> Target: RocketSwap
> Amount (USD): $869,000
> Asset: Ethereum
> Vector: unknown
> References: RocketSwap – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/RocketSwap/RocketSwap_report.html)

On 14 August 2023, RocketSwap, a decentralised finance (DeFi) protocol, experienced a significant security breach resulting in the theft of approximately $869,000. The attack targeted the protocol's smart contracts, exploiting a vulnerability that allowed the attacker to siphon funds from the liquidity pools. The immediate financial impact was substantial, affecting both the protocol's operations and its user base.

The attack was executed by exploiting a vulnerability in the smart contract's access control mechanisms. The attacker utilised a series of transactions to manipulate the contract's state, allowing unauthorised withdrawals. This involved the use of flash loans to inflate the pool's liquidity temporarily, followed by a reentrancy attack to drain funds.

Stolen funds were initially moved from the exploit wallet (0x96c0876f573e27636612cf306c9db072d2b13de8) through a series of intermediary wallets. The attacker employed multiple laundering techniques, including bridge hopping and mixer usage, to obfuscate the fund flow. Funds were eventually routed through various decentralised exchanges (DEXs) and centralised exchanges (CEXs) for cash-out.

The attack is attributed to the hacker group APT38, known for its sophisticated cyber operations and previous involvement in similar incidents. The use of advanced laundering techniques and infrastructure overlaps with past APT38 activities support this attribution.
