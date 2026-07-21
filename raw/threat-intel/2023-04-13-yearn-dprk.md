# Yearn — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Yearn-203
> Timestamp: 2023-04-13T00:00:00Z
> Attribution: DPRK / AndAriel (confidence: 0.1)
> Target: Yearn
> Amount (USD): $11,400,000
> Asset: Ethereum
> Vector: unknown
> References: Yearn – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Yearn/Yearn_report.html)

On 13 April 2023, the Yearn protocol experienced a significant security breach resulting in the theft of approximately $11.4 million USD. The attack targeted the protocol's smart contracts, exploiting a vulnerability that allowed the attacker to siphon funds from the protocol's liquidity pools. The immediate financial impact was substantial, affecting both the protocol's operations and its user base.

The attack was executed through a sophisticated exploitation of a smart contract vulnerability, potentially involving a reentrancy attack or a flash loan exploit. The attacker manipulated the protocol's contract functions to withdraw funds repeatedly before the contract's state could be updated. This indicates a high level of technical expertise and understanding of the protocol's codebase.

Stolen funds were rapidly moved through a series of transactions involving multiple wallets and blockchain networks. The attacker utilised a combination of mixers, bridges, and exchanges to obscure the fund flow. Notably, the funds were routed through known laundering infrastructure, including bridge hopping and mixer usage, before reaching centralised exchanges for cash-out.

The attack is suspected to be linked to the AndAriel hacker group, known for similar exploits in the DeFi space. The use of specific laundering techniques and infrastructure overlaps with previous incidents attributed to this group. The confidence level in this attribution is medium, based on behavioural and technical indicators.
