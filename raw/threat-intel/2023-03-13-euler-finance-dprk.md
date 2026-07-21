# Euler Finance — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Euler-Finance-61
> Timestamp: 2023-03-13T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.12)
> Target: Euler Finance
> Amount (USD): $197,000,000
> Asset: Ethereum
> Vector: unknown
> References: Euler Finance – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Euler_Finance/Euler_Finance_report.html)

On 13 March 2023, Euler Finance, a decentralised finance (DeFi) protocol, suffered a significant security breach resulting in the theft of approximately $197 million USD. The attack targeted the protocol's smart contracts, exploiting a vulnerability that allowed the attacker to drain funds from the platform. Euler Finance, known for its lending and borrowing services, operates primarily on the Ethereum blockchain.

The attack was executed through a sophisticated exploit involving a reentrancy attack on Euler Finance's smart contracts. The attacker manipulated the protocol's lending mechanism, allowing them to withdraw more funds than deposited. This was likely facilitated by a flaw in the contract's logic, potentially involving improper handling of state changes during contract execution.

Post-exploit, the stolen funds were rapidly moved through a series of transactions across multiple wallets. The attacker utilised various laundering techniques, including bridge hopping and mixer services, to obfuscate the fund trail. The funds were eventually distributed across several blockchain networks and exchanges, complicating recovery efforts.

The attack is suspected to be linked to the APT38 group, known for targeting financial institutions with advanced cyber capabilities. The use of sophisticated laundering techniques and infrastructure overlaps with previous incidents attributed to this group supports this hypothesis.
