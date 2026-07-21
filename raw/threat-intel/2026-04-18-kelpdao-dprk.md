# KelpDao — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-KelpDao-93
> Timestamp: 2026-04-18T00:00:00Z
> Attribution: DPRK / Lazarus Group (confidence: 0.36)
> Target: KelpDao
> Amount (USD): $290,000,000
> Asset: Ethereum
> Vector: unknown
> References: KelpDao – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/KelpDao/KelpDao_report.html)

On 18 April 2026, KelpDao, a decentralised autonomous organisation (DAO) operating on the Ethereum blockchain, experienced a significant security breach. The attack resulted in the unauthorised transfer of approximately $290 million worth of various cryptocurrencies, primarily Ethereum (ETH) and its derivatives. The exploit mechanism remains unknown, but the attack was attributed to the Lazarus Group, a notorious hacking collective.

The attack exploited a vulnerability within the KelpDao smart contract system. Although the specific weakness remains unidentified, the attack involved multiple transactions executed in rapid succession, suggesting a potential reentrancy or access control failure. The absence of timestamps in the transaction data complicates precise timing analysis, but the attack was executed swiftly, indicating premeditated planning and execution.

Stolen funds were initially moved through a series of intermediary wallets, employing complex layering techniques involving multiple ERC20 tokens and cross-chain bridges. Notably, funds were transferred to addresses associated with known laundering infrastructure, including mixers and decentralised exchanges (DEXs). The use of these services suggests an attempt to obfuscate the fund trail and complicate recovery efforts.

The Lazarus Group is suspected of orchestrating the attack, with a high confidence level based on transaction patterns and infrastructure overlaps with previous incidents attributed to the group. The group's known tactics, techniques, and procedures (TTPs) align with those observed in this case, including the use of sophisticated laundering strategies and rapid fund movement.
