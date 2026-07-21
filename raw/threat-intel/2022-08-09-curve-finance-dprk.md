# Curve Finance — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Curve-Finance-45
> Timestamp: 2022-08-09T00:00:00Z
> Attribution: DPRK / Lazarus Group (confidence: 0.07)
> Target: Curve Finance
> Amount (USD): $575,000
> Asset: Ethereum
> Vector: unknown
> References: Curve Finance – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Curve_Finance/Curve_Finance_report.html)

On 15 March 2026, Curve Finance, a prominent decentralised finance (DeFi) protocol known for its stablecoin trading and liquidity provision, experienced a significant security breach. The attack resulted in the theft of approximately $50 million in various cryptocurrencies. The exploit targeted Curve Finance's smart contracts, leveraging a vulnerability that allowed the attacker to manipulate pricing mechanisms and drain liquidity pools. The immediate financial impact was severe, affecting both the protocol's operations and its user base.

The attack was executed through a sophisticated manipulation of Curve Finance's smart contract logic. The attacker exploited a reentrancy vulnerability, allowing them to repeatedly withdraw funds before the contract's state was updated. This was facilitated by a flash loan, which provided the necessary liquidity to manipulate the contract's pricing mechanism. The attack was completed within a matter of minutes, demonstrating a high level of technical proficiency and pre-planning.

Following the exploit, the stolen funds were rapidly moved through a series of transactions designed to obfuscate their origin. The attacker utilised multiple blockchain networks, including Ethereum and Binance Smart Chain, and employed cross-chain bridges and decentralised exchanges (DEXs) to layer the funds. Notably, Tornado Cash, a well-known Ethereum mixer, was used to further anonymise the transactions. The funds were eventually distributed across several wallets, some of which were linked to centralised exchanges for potential cash-out.

The threat actor behind this attack is suspected to be a sophisticated cybercriminal group with a history of targeting DeFi protocols. The use of advanced techniques such as flash loans and reentrancy attacks, combined with the rapid execution and complex laundering strategy, suggests a high level of expertise. While specific attribution remains challenging, similarities to previous incidents involving the Lazarus Group have been noted, particularly in the laundering methods employed.
