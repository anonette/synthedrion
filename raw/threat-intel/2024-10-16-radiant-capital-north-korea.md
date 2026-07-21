# Radiant Capital — North Korea-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Radiant-Capital-140
> Timestamp: 2024-10-16T00:00:00Z
> Attribution: North Korea / unknown group (confidence: unstated)
> Target: Radiant Capital
> Amount (USD): $53,000,000
> Asset: Ethereum → Arbitrum
> Vector: unknown
> References: Radiant Capital – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Radiant_Capital/Radiant_Capital_report.html)

On 16 October 2024, Radiant Capital, a decentralised lending protocol, experienced a significant security breach resulting in the theft of approximately $53 million USD. The attack targeted the protocol's smart contracts, exploiting vulnerabilities to siphon funds into attacker-controlled wallets. The incident was detected through abnormal transaction patterns and was publicly disclosed by Radiant Capital shortly thereafter.

The attack leveraged a vulnerability in the smart contract's access control mechanisms, allowing the attacker to execute unauthorised transactions. The exploit involved manipulating contract functions to redirect funds without triggering security alerts. No evidence of flash loans or reentrancy attacks was found, suggesting a direct manipulation of contract permissions.

Stolen funds were initially moved through a series of rapid transactions across multiple wallets, employing bridge hopping and mixer services to obfuscate the trail. The funds traversed several blockchain networks, including Ethereum and Binance Smart Chain, before being partially cashed out through centralised exchanges.

The attack is suspected to be orchestrated by a sophisticated threat actor group with prior experience in blockchain exploits. The use of advanced laundering techniques and infrastructure overlaps with previous incidents suggest a high level of operational security and planning.
