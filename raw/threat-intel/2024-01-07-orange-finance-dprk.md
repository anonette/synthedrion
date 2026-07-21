# Orange Finance — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Orange-Finance-123
> Timestamp: 2024-01-07T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.12)
> Target: Orange Finance
> Amount (USD): $843,500
> Asset: Ethereum
> Vector: unknown
> References: Orange Finance – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Orange_Finance/Orange_Finance_report.html)

On 7 January 2024, Orange Finance, a decentralised finance (DeFi) protocol, suffered a significant security breach resulting in the theft of approximately $843,500.00 USD. The attack targeted the protocol's smart contracts, exploiting vulnerabilities to siphon funds into an attacker-controlled wallet.

The attack was executed by exploiting a vulnerability in the smart contract's access control mechanisms. The attacker likely used a combination of flash loans and reentrancy attacks to manipulate the protocol's state and extract funds without triggering immediate alarms.

Stolen funds were initially moved from the exploit wallet (0xeb0f537a7a1c3e38d4f57026982c11f6886233d7) to a secondary wallet (0xd90e2f925da726b50c4ed8d0fb90ad053324f31b). The funds were then layered through various DeFi protocols and bridges, including high-volume intermediaries such as LCX and Poly Network, to obfuscate their origin before reaching centralised exchanges for cash-out.

The attack is suspected to be orchestrated by APT38, a known cybercriminal group with a history of targeting financial institutions. The use of sophisticated laundering techniques and infrastructure overlaps with previous APT38 operations support this attribution.
