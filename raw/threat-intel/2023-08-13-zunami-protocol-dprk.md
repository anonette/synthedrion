# Zunami Protocol — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Zunami-Protocol-210
> Timestamp: 2023-08-13T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.4)
> Target: Zunami Protocol
> Amount (USD): $2,100,000
> Asset: Ethereum
> Vector: unknown
> References: Zunami Protocol – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Zunami_Protocol/Zunami_Protocol_report.html)

On 14 May 2025, the Zunami Protocol, a decentralised finance (DeFi) platform, experienced a significant security breach resulting in the theft of approximately $500,000.00 USD. The attack targeted the protocol's smart contracts, exploiting vulnerabilities to siphon funds into attacker-controlled wallets.

The attack was executed through a series of rapid transactions exploiting a vulnerability in the protocol's smart contract logic. The specific weakness exploited involved improper access control mechanisms, allowing the attacker to manipulate transaction flows and extract funds without detection.

Stolen funds were initially moved from the exploit wallet (0x051370419b871f7c05dee8f7134401530832e250) to intermediary wallets, employing a series of rapid transactions to obfuscate the trail. The funds were subsequently layered through various DeFi platforms and mixers, including potential use of bridge hopping techniques to cross blockchain networks.

The attack is suspected to be orchestrated by the APT38 group, known for targeting financial institutions and employing sophisticated laundering techniques. The use of specific transaction patterns and infrastructure overlaps with previous incidents attributed to this group supports this hypothesis.
