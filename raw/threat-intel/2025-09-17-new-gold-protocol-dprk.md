# New Gold Protocol — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-New-Gold-Protocol-117
> Timestamp: 2025-09-17T00:00:00Z
> Attribution: DPRK / AndAriel (confidence: 0.1)
> Target: New Gold Protocol
> Amount (USD): $2,000,000
> Asset: Ethereum → BSC
> Vector: unknown
> References: New Gold Protocol – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/New_Gold_Protocol/New_Gold_Protocol_report.html)

On 17 September 2025, the New Gold Protocol, a decentralised finance (DeFi) platform, experienced a significant security breach resulting in the theft of approximately $2,000,000.00. The attack targeted the protocol's smart contracts, exploiting vulnerabilities that allowed the attacker to siphon funds without detection initially.

The attack was executed through a series of rapid transactions exploiting a vulnerability in the protocol's smart contract logic. The specific weakness exploited involved improper access control mechanisms, allowing unauthorised transactions to be executed. No evidence of flash loans or reentrancy attacks was found.

Stolen funds were initially moved through a series of intermediary wallets before being laundered via multiple blockchain bridges and mixers. The attacker utilised known laundering infrastructure, including Tornado Cash and various cross-chain bridges, to obfuscate the fund flow.

The threat actor is suspected to be the AndAriel group, known for previous DeFi exploits. This assessment is based on the use of similar laundering techniques and infrastructure overlaps with past incidents attributed to this group.
