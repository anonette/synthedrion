# TempleDAO — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-TempleDAO-177
> Timestamp: 2022-10-11T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.4)
> Target: TempleDAO
> Amount (USD): $2,300,000
> Asset: Ethereum
> Vector: unknown
> References: TempleDAO – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/TempleDAO/TempleDAO_report.html)

On 11 October 2022, TempleDAO, a decentralised finance protocol, suffered a significant security breach resulting in the theft of approximately $2.3 million USD. The attack targeted the protocol's smart contracts, exploiting vulnerabilities that allowed the attacker to siphon funds from the protocol's reserves.

The attacker exploited a vulnerability in the smart contract's access control mechanisms. This allowed unauthorised access to the protocol's funds, which were then transferred to an attacker-controlled wallet. The specific technical details of the exploit remain under investigation, but initial analysis suggests a failure in the contract's permission settings.

Stolen funds were initially moved through a series of rapid transactions across multiple wallets, employing techniques such as bridge hopping and mixer usage to obfuscate the trail. The funds were eventually routed through several decentralised exchanges and cross-chain bridges, complicating traceability.

The attack is suspected to be linked to the hacker group APT38, known for sophisticated cyber operations and previous incidents involving similar tactics. The use of advanced laundering techniques and infrastructure overlaps with known APT38 operations support this attribution.
