# Zunami Protocol II — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Zunami-Protocol---II-211
> Timestamp: 2025-05-14T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.4)
> Target: Zunami Protocol II
> Amount (USD): $500,000
> Asset: Ethereum
> Vector: unknown
> References: Zunami Protocol II – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Zunami_Protocol_-_II/Zunami_Protocol_-_II_report.html)

On 14 May 2025, the Zunami Protocol, a decentralised finance (DeFi) platform, was compromised, resulting in the unauthorised transfer of funds. The attack was executed by exploiting a vulnerability within the protocol, leading to a significant financial impact estimated at $500,000. The attack was attributed to the hacker group APT38, known for its sophisticated cyber operations.

The attack leveraged a vulnerability in the Zunami Protocol's smart contract, potentially involving reentrancy or access control failures. The precise exploit mechanism remains unknown, but the rapid sequence of transactions suggests a premeditated strategy exploiting a known weakness.

Stolen funds were initially moved from the exploit wallet (0x051370419b871f7c05dee8f7134401530832e250) to intermediary wallets, followed by layering through various transactions. The funds were then dispersed across multiple addresses, potentially using mixers and bridges to obfuscate the trail.

The attack is attributed to APT38, a group with a history of targeting financial institutions. This attribution is supported by the use of sophisticated laundering techniques and infrastructure overlaps with previous incidents linked to APT38.
