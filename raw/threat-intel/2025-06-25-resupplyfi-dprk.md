# ResupplyFi — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-ResupplyFi-146
> Timestamp: 2025-06-25T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.35)
> Target: ResupplyFi
> Amount (USD): $9,800,000
> Asset: Ethereum
> Vector: unknown
> References: ResupplyFi – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/ResupplyFi/ResupplyFi_report.html)

On 25 June 2025, the decentralised finance (DeFi) protocol ResupplyFi experienced a significant security breach resulting in the theft of approximately $9.8 million USD. The attack was executed by exploiting a vulnerability within the protocol's smart contract infrastructure, leading to the unauthorised transfer of funds to an attacker-controlled wallet. The immediate financial impact was severe, affecting numerous users and stakeholders within the ResupplyFi ecosystem.

The attack leveraged a vulnerability in the ResupplyFi smart contract, potentially involving a reentrancy attack or a flash loan exploit. The attacker manipulated the contract's logic to siphon funds without triggering the usual security checks. This breach highlights a critical failure in the protocol's access control mechanisms, allowing the attacker to execute multiple transactions rapidly.

Post-exploit, the stolen funds were rapidly moved through a series of transactions involving multiple intermediary wallets. The attacker utilised various blockchain bridges and mixers to obfuscate the fund trail, eventually directing the assets to centralised exchanges for cash-out. Notably, the funds traversed through known laundering infrastructures, including bridge hopping and mixer usage.

The attack is attributed to the hacker group APT38, known for sophisticated cyber operations targeting financial institutions. The attribution is supported by the use of similar tactics, techniques, and procedures (TTPs) observed in previous incidents linked to this group. The confidence level in this attribution is medium, pending further verification.
