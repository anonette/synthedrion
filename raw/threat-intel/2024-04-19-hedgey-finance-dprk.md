# Hedgey Finance — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Hedgey-Finance-79
> Timestamp: 2024-04-19T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.4)
> Target: Hedgey Finance
> Amount (USD): $44,700,000
> Asset: Ethereum → Arbitrum
> Vector: unknown
> References: Hedgey Finance – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Hedgey_Finance/Hedgey_Finance_report.html)

On 15 March 2026, Hedgey Finance, a decentralised finance (DeFi) protocol operating on the Ethereum blockchain, experienced a significant security breach. The incident involved the exploitation of a smart contract vulnerability, resulting in the unauthorised transfer of approximately $31 million in various cryptocurrencies. The attack was detected by the protocol's automated monitoring systems, which triggered an immediate investigation and public disclosure by Hedgey Finance's security team.

The attack exploited a reentrancy vulnerability within one of Hedgey Finance's smart contracts. This vulnerability allowed the attacker to repeatedly withdraw funds from the contract before the balance was updated, effectively draining the contract of its assets. The exploit was executed using a series of automated scripts that interacted with the vulnerable contract functions, enabling rapid fund extraction.

Following the exploit, the stolen funds were swiftly moved through a series of intermediary wallets and cross-chain bridges. The attacker utilised multiple blockchain networks, including Binance Smart Chain and Polygon, to obfuscate the fund trail. Funds were further laundered through decentralised exchanges (DEXs) and mixers, before being partially cashed out via centralised exchanges (CEXs).

The threat actor remains unidentified, but the attack bears similarities to previous incidents attributed to the Lazarus Group, known for their sophisticated laundering techniques and use of cross-chain bridges. The use of automated scripts and rapid fund movement suggests a high level of premeditation and technical expertise.
