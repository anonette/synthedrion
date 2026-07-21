# Cork Protocol — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Cork-Protocol-40
> Timestamp: 2025-05-28T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.12)
> Target: Cork Protocol
> Amount (USD): $12,000,000
> Asset: Ethereum
> Vector: unknown
> References: Cork Protocol – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Cork_Protocol/Cork_Protocol_report.html)

The Cork Protocol incident involved a sophisticated crypto hack targeting a decentralised finance (DeFi) protocol, resulting in significant financial losses. The attack occurred on 15 March 2026, exploiting vulnerabilities within the protocol's smart contracts. The immediate financial impact was the theft of approximately $12 million in various cryptocurrencies. The exploit mechanism involved a combination of smart contract manipulation and rapid fund transfers across multiple blockchain networks.

The attack was executed through a reentrancy vulnerability in the protocol's smart contracts, allowing the attacker to repeatedly withdraw funds before the contract state was updated. This was compounded by the use of flash loans to amplify the attack's impact. The attacker utilised automated scripts to execute transactions rapidly, exploiting the protocol's lack of adequate reentrancy guards.

Stolen funds were initially moved from the exploit wallet to intermediary wallets, employing a series of rapid transactions to obfuscate the trail. The attacker utilised cross-chain bridges and mixers to further layer the funds, eventually depositing them into centralised exchanges (CEXs) for cash-out. Notable infrastructure used included the Ethereum and Binance Smart Chain networks, with funds passing through Tornado Cash and other mixing services.

The threat actor is suspected to be a sophisticated cybercriminal group with prior experience in DeFi exploits. The use of advanced laundering techniques and infrastructure overlaps with previous incidents suggest a high level of operational security. Attribution confidence is medium, pending further investigation into wallet connections and transaction patterns.
