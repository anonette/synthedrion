# Popsicle Finance — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Popsicle-Finance-136
> Timestamp: 2021-08-03T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.4)
> Target: Popsicle Finance
> Amount (USD): $20,000,000
> Asset: Ethereum
> Vector: unknown
> References: Popsicle Finance – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Popsicle_Finance/Popsicle_Finance_report.html)

On 3 August 2021, Popsicle Finance, a decentralised finance (DeFi) protocol, experienced a significant security breach resulting in the theft of approximately $20 million USD. The attack targeted the protocol's liquidity pools, exploiting vulnerabilities in the smart contract code. The immediate financial impact was severe, affecting both the protocol's operations and its user base.

The attack was executed by exploiting a vulnerability in the smart contract's logic, potentially involving a reentrancy attack or a flash loan exploit. The attacker manipulated the contract's state to withdraw funds without proper authorisation. The specific functions abused and the exact technical details of the exploit remain under investigation.

Stolen funds were rapidly moved through a series of transactions across multiple blockchain networks. The attacker utilised various DeFi protocols, bridges, and mixers to obfuscate the fund flow. Key infrastructure used included Ethereum-based mixers and cross-chain bridges, facilitating the movement of assets to less traceable environments.

The attack is suspected to be linked to the APT38 group, known for sophisticated cyber operations targeting financial institutions. This attribution is based on the use of similar TTPs and infrastructure overlaps with previous incidents attributed to APT38.
