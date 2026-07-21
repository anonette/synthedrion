# Cream Finance — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Cream-Finance-41
> Timestamp: 2021-10-27T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.4)
> Target: Cream Finance
> Amount (USD): $130,000,000
> Asset: Ethereum
> Vector: unknown
> References: Cream Finance – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Cream_Finance/Cream_Finance_report.html)

On 27 October 2021, Cream Finance, a decentralised finance (DeFi) protocol, suffered a significant security breach resulting in the theft of approximately $130 million USD. The attack targeted Cream Finance's lending platform, exploiting vulnerabilities within its smart contracts. The immediate financial impact was substantial, affecting both the protocol's liquidity and its users' deposits.

The attack was executed through a sophisticated exploit involving a series of flash loans and reentrancy attacks. The attacker manipulated the protocol's price oracle and exploited a vulnerability in the smart contract's logic, allowing them to withdraw funds without proper collateralisation. This type of attack is indicative of a high level of technical expertise and understanding of DeFi protocols.

Following the exploit, the stolen funds were rapidly moved through a series of transactions involving multiple wallets and blockchain networks. The attacker utilised various laundering techniques, including bridge hopping and mixer services, to obfuscate the fund flow. Notably, funds were transferred across Ethereum and Binance Smart Chain, and through decentralised exchanges (DEXs) and mixers.

The attack is suspected to have been carried out by the North Korean hacker group APT38, known for targeting financial institutions. This attribution is based on the use of similar tactics, techniques, and procedures (TTPs) observed in previous incidents attributed to APT38, including the use of sophisticated laundering methods and infrastructure overlaps.
