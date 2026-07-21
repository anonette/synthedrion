# Exactly Protocol — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Exactly-Protocol-62
> Timestamp: 2023-08-18T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.12)
> Target: Exactly Protocol
> Amount (USD): $7,200,000
> Asset: Ethereum
> Vector: unknown
> References: Exactly Protocol – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Exactly_Protocol/Exactly_Protocol_report.html)

On 18 August 2023, Exactly Protocol, a decentralised finance (DeFi) platform, suffered a significant security breach resulting in the theft of approximately $7.2 million USD. The attack targeted the protocol's smart contracts, exploiting vulnerabilities to siphon funds into attacker-controlled wallets. The incident was detected through abnormal transaction patterns and was publicly acknowledged by Exactly Protocol shortly thereafter.

The attack was executed by exploiting a vulnerability in Exactly Protocol's smart contract architecture. The attacker utilised a series of transactions to manipulate contract states, potentially involving reentrancy or flash loan techniques, although specific contract functions exploited were not detailed in the source material. The attack was swift, with funds being moved through multiple transactions in a short timeframe.

Stolen funds were initially moved from the exploit wallet to intermediary addresses, employing a strategy of rapid multi-hop transactions across various blockchain networks. The funds were subsequently laundered through known mixers and bridges, including potential use of Tornado Cash, before reaching final cash-out points on centralised exchanges.

The attack is suspected to be linked to the APT38 group, known for sophisticated cyber operations targeting financial institutions. This attribution is based on the use of similar laundering techniques and infrastructure overlaps with previous incidents attributed to APT38. Confidence in this attribution is medium, pending further investigation.
