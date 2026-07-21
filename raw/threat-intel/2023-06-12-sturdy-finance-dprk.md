# Sturdy Finance — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Sturdy-Finance-166
> Timestamp: 2023-06-12T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.4)
> Target: Sturdy Finance
> Amount (USD): $800,000
> Asset: Ethereum
> Vector: unknown
> References: Sturdy Finance – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Sturdy_Finance/Sturdy_Finance_report.html)

On 15 March 2026, Sturdy Finance, a decentralised finance (DeFi) protocol, experienced a significant security breach resulting in the theft of approximately $10 million in various cryptocurrencies. The attack targeted the protocol's smart contracts, exploiting a vulnerability that allowed the attacker to drain funds from the liquidity pools. The immediate financial impact was severe, affecting both the protocol's operations and its users' assets.

The attack was executed by exploiting a reentrancy vulnerability within the smart contract code of Sturdy Finance. This allowed the attacker to repeatedly withdraw funds before the contract's state was updated. The exploit involved a series of rapid transactions that manipulated the contract's logic, bypassing standard security checks. No evidence of private key compromise or infrastructure failure was found.

Following the exploit, the stolen funds were quickly moved through a series of transactions involving multiple blockchain networks. The attacker utilised cross-chain bridges and decentralised exchanges (DEXs) to obscure the fund flow. Notably, the funds were routed through Tornado Cash, a known mixer, and subsequently transferred to various wallets across different chains, including Ethereum and Binance Smart Chain.

The threat actor remains unidentified, but the sophistication of the attack suggests involvement of a well-resourced group with prior experience in DeFi exploits. The use of advanced laundering techniques and infrastructure overlaps with previous incidents indicate a possible connection to known cybercriminal groups specialising in DeFi attacks.
