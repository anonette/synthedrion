# Balancer — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Balancer-19
> Timestamp: 2025-11-03T00:00:00Z
> Attribution: DPRK / Lazarus Group (confidence: 0.07)
> Target: Balancer
> Amount (USD): $128,000,000
> Asset: Ethereum
> Vector: unknown
> References: Balancer – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Balancer/Balancer_report.html)

On 3 November 2025, the Balancer protocol experienced a significant security breach resulting in the theft of approximately $128 million USD. The attack targeted the protocol's smart contracts, exploiting a vulnerability that allowed the attacker to siphon funds from the liquidity pools. The immediate financial impact was substantial, affecting both the protocol's operations and its users.

The attack was executed by exploiting a smart contract vulnerability, potentially involving reentrancy or flash loan attacks. The attacker manipulated the protocol's pricing mechanisms, allowing them to withdraw more funds than deposited. This type of attack often involves complex interactions with the protocol's smart contracts, leveraging weaknesses in access control or logic errors.

Stolen funds were rapidly moved through a series of transactions involving multiple wallets and blockchain networks. The attacker utilised various laundering techniques, including bridge hopping and mixer usage, to obfuscate the fund flow. Funds were eventually transferred to centralised exchanges for cash-out.

The attack is suspected to be linked to the Lazarus Group, a well-known cybercrime organisation with a history of targeting cryptocurrency platforms. This attribution is based on the use of similar tactics, techniques, and procedures (TTPs) observed in previous incidents attributed to this group.
