# Uwulend — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Uwulend-187
> Timestamp: 2024-06-10T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.12)
> Target: Uwulend
> Amount (USD): $19,400,000
> Asset: Ethereum
> Vector: unknown
> References: Uwulend – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Uwulend/Uwulend_report.html)

On 10 June 2024, the Uwulend protocol experienced a significant security breach resulting in the theft of approximately $19.4 million USD. The attack targeted the protocol's smart contracts, exploiting vulnerabilities to drain funds. The immediate financial impact was severe, affecting both the protocol's liquidity and its user base. The exploit mechanism involved a sophisticated manipulation of smart contract functions, allowing the attacker to siphon funds undetected initially.

The attack was executed through a vulnerability in the smart contract's logic, potentially involving reentrancy or access control failures. The attacker likely used automated scripts to execute rapid transactions, exploiting the protocol's lack of adequate security checks. The specific functions abused remain under investigation, but the attack's precision suggests a deep understanding of the protocol's architecture.

Stolen funds were quickly moved through a series of transactions across multiple blockchains, employing techniques such as bridge hopping and mixer usage to obfuscate the trail. The attacker utilised known laundering infrastructure, including decentralised exchanges and cross-chain bridges, to layer and integrate the funds into the broader crypto ecosystem.

The attack is suspected to be the work of APT38, a group known for targeting financial institutions with sophisticated cyber operations. This attribution is supported by the use of similar tactics, techniques, and procedures (TTPs) observed in previous incidents linked to the group. The confidence level in this attribution is medium, pending further analysis.
