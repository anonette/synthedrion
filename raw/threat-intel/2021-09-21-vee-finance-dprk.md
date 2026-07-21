# Vee Finance — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Vee-Finance-188
> Timestamp: 2021-09-21T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.4)
> Target: Vee Finance
> Amount (USD): $34,000,000
> Asset: Ethereum
> Vector: unknown
> References: Vee Finance – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Vee_Finance/Vee_Finance_report.html)

On 21 September 2021, Vee Finance, a decentralised finance (DeFi) protocol, experienced a significant security breach resulting in the theft of approximately $34 million USD. The attack targeted the protocol's smart contracts, exploiting vulnerabilities to siphon funds from user deposits. The immediate financial impact was severe, affecting the protocol's liquidity and user trust.

The attack was executed by exploiting a vulnerability within Vee Finance's smart contract infrastructure. The specific weakness involved was likely related to improper access control or a reentrancy flaw, allowing the attacker to manipulate contract functions to withdraw funds illicitly. The technical execution involved a series of rapid transactions designed to obfuscate the exploit's origin.

Post-exploit, the stolen funds were quickly moved through a series of transactions involving multiple blockchain networks and laundering techniques. The attacker utilised bridges and mixers to obscure the fund trail, eventually directing the assets to centralised exchanges for cash-out. Notable infrastructure used included TornadoCash and RSwap.net, indicating a sophisticated laundering strategy.

The attack is suspected to be linked to the APT38 group, known for targeting financial institutions. This attribution is based on the use of similar tactics, techniques, and procedures (TTPs) observed in previous incidents attributed to this group. The confidence level in this attribution is medium, pending further investigation.
