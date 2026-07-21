# Shibarium Bridge — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Shibarium-Bridge-157
> Timestamp: 2023-08-17T00:00:00Z
> Attribution: DPRK / Lazarus Group (confidence: 0.8)
> Target: Shibarium Bridge
> Amount (USD): $2,600,000
> Asset: Ethereum
> Vector: bridge exploit
> References: Shibarium Bridge – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Shibarium_Bridge/Shibarium_Bridge_report.html)

On 12 September 2025, the Shibarium Bridge was compromised, resulting in the unauthorised transfer of approximately $3,000,000.00 in digital assets. The attack targeted the bridge's infrastructure, exploiting vulnerabilities that allowed the attacker to reroute funds to addresses under their control. The immediate financial impact was significant, affecting the liquidity and operational stability of the Shibarium protocol.

The attack was executed through a series of transactions that exploited a vulnerability in the bridge's smart contract. The specific weakness involved improper access controls, allowing the attacker to initiate transactions without the necessary authorisations. No evidence of flash loans or reentrancy attacks was found, suggesting a direct manipulation of contract permissions.

Stolen funds were initially moved through a series of rapid transactions across multiple wallets, employing techniques such as bridge hopping and token swapping to obfuscate the trail. The funds were eventually routed through various decentralised exchanges (DEXs) and mixers, complicating traceability. Key infrastructure used included the Shibarium Bridge and several high-volume intermediary wallets.

The identity of the threat actor remains unknown, with no direct attribution possible at this stage. However, the sophistication of the attack and the use of advanced laundering techniques suggest involvement by a well-organised group with prior experience in blockchain exploits. No specific threat actor group has been conclusively linked to this incident.
