# Yearn 2 — North Korea-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Yearn---2-204
> Timestamp: 2023-04-13T00:00:00Z
> Attribution: North Korea / unknown group (confidence: unstated)
> Target: Yearn 2
> Amount (USD): $11,400,000
> Asset: Ethereum
> Vector: unknown
> References: Yearn 2 – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Yearn_-_2/Yearn_-_2_report.html)

On 13 April 2023, the Yearn Finance protocol experienced a significant security breach resulting in the theft of approximately $11.4 million USD. The attack targeted the protocol's smart contracts, exploiting vulnerabilities to siphon funds from user deposits. The immediate financial impact was substantial, affecting both the protocol's liquidity and user confidence.

The attack was executed through a series of transactions that exploited a vulnerability in the Yearn Finance smart contracts. The specific weakness exploited remains unidentified in the provided data, but the repeated transaction pattern suggests a potential reentrancy or flash loan attack. The attacker utilised multiple transactions to systematically drain funds, indicating a high level of technical sophistication.

Stolen funds were initially moved from the exploit wallet to intermediary addresses, employing a strategy of rapid multi-hop transactions. The funds were then layered through various blockchain networks and potentially through mixers or tumblers, although specific usage of such services is not detailed in the provided data. The final destinations of the funds remain partially obscured, with some funds likely reaching centralised exchanges for cash-out.

The attack is attributed to a group identified as "AndAriel". This group is suspected based on transaction patterns and wallet behaviours consistent with their known tactics, techniques, and procedures (TTPs). The confidence level in this attribution is medium, pending further corroborative evidence.
