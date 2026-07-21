# Venus Protocol IV — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Venus-Protocol---IV-190
> Timestamp: 2026-03-15T00:00:00Z
> Attribution: DPRK / Lazarus Group (confidence: 0.07)
> Target: Venus Protocol IV
> Amount (USD): $3,700,000
> Asset: Ethereum → BSC
> Vector: unknown
> References: Venus Protocol IV – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Venus_Protocol___IV/Venus_Protocol___IV_report.html)

On 15 March 2026, Venus Protocol, a decentralised finance (DeFi) platform, experienced a significant security breach resulting in the theft of approximately $3.7 million USD. The attack targeted the protocol's smart contracts, exploiting vulnerabilities to siphon funds into attacker-controlled wallets. The incident was detected through abnormal transaction patterns and was publicly disclosed by the protocol's team shortly thereafter.

The attack was executed by exploiting a vulnerability in the protocol's smart contract code, potentially involving reentrancy or flash loan attacks. The attacker manipulated contract functions to withdraw funds without proper authorisation checks. The precise technical details of the exploit remain under investigation, but initial analysis suggests a sophisticated understanding of the protocol's architecture.

Stolen funds were rapidly moved through a series of transactions involving multiple wallets and blockchain networks. The attacker utilised known laundering techniques such as bridge hopping and mixer services to obfuscate the fund trail. Key infrastructure used included decentralised exchanges (DEXs) and cross-chain bridges, with funds eventually reaching centralised exchanges (CEXs) for potential cash-out.

The attack is suspected to be linked to the Lazarus Group, a well-known cybercrime syndicate with a history of targeting cryptocurrency platforms. This attribution is based on similarities in tactics, techniques, and procedures (TTPs) observed in previous incidents attributed to the group. The confidence level in this attribution is medium, pending further investigation.
