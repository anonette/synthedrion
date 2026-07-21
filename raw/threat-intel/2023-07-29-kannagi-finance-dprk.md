# Kannagi Finance — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Kannagi-Finance-92
> Timestamp: 2023-07-29T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.4)
> Target: Kannagi Finance
> Amount (USD): $2,100,000
> Asset: Ethereum
> Vector: unknown
> References: Kannagi Finance – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Kannagi_Finance/Kannagi_Finance_report.html)

On 29 July 2023, Kannagi Finance, a decentralised finance (DeFi) protocol, experienced a significant security breach resulting in the theft of approximately $2.1 million USD. The attack targeted the protocol's smart contracts, exploiting a vulnerability that allowed the attacker to siphon funds from the platform. The immediate financial impact was substantial, affecting both the protocol's liquidity and its user base.

The attack was executed through a sophisticated exploit of the protocol's smart contract infrastructure. The attacker utilised a reentrancy attack, a common vulnerability in smart contracts, which allowed them to repeatedly withdraw funds before the contract's state was updated. This exploit was facilitated by a series of rapid transactions that manipulated the contract's logic.

Following the exploit, the stolen funds were quickly moved through a series of transactions involving multiple wallets and blockchain networks. The attacker employed a combination of mixers and cross-chain bridges to obfuscate the fund flow, eventually directing the assets to centralised exchanges for cash-out. Key infrastructure used included Tornado Cash and various cross-chain bridges.

The attack is suspected to have been carried out by the cybercriminal group APT38, known for targeting financial institutions. This attribution is based on the use of similar tactics, techniques, and procedures (TTPs) observed in previous incidents linked to the group, including the use of specific laundering methods and infrastructure overlaps.
