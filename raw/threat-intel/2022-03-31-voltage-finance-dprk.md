# Voltage Finance — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Voltage-Finance-193
> Timestamp: 2022-03-31T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.4)
> Target: Voltage Finance
> Amount (USD): $4,000,000
> Asset: Ethereum
> Vector: unknown
> References: Voltage Finance – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Voltage_Finance/Voltage_Finance_report.html)

On 31 March 2022, Voltage Finance, a decentralised finance (DeFi) protocol operating on the Fuse Network, experienced a significant security breach resulting in the theft of approximately $4,000,000 USD. The attack was executed by the hacker group APT38, known for their sophisticated cyber operations. The immediate financial impact was substantial, affecting both the protocol's liquidity and its user base.

The attack exploited a vulnerability within the smart contract infrastructure of Voltage Finance. The specific weakness involved was likely related to improper access controls or a reentrancy flaw, allowing the attacker to manipulate transaction sequences and drain funds. The exact technical details of the exploit mechanism remain under investigation, but the rapid execution suggests premeditated planning and advanced technical capabilities.

Post-exploit, the stolen funds were swiftly moved through a series of transactions involving multiple intermediary wallets. The laundering process included the use of cross-chain bridges and decentralised exchanges (DEXs) to obscure the fund trail. Notably, the funds traversed through several high-volume intermediaries, including the BNB Bridge and SushiSwap, before reaching centralised exchanges (CEXs) for potential cash-out.

APT38, a group with ties to North Korean state-sponsored cyber activities, is suspected of orchestrating this attack. The attribution is supported by the group's known tactics, techniques, and procedures (TTPs), which include targeting financial institutions and employing sophisticated laundering strategies. The use of specific infrastructure and the timing of the attack align with previous APT38 operations.
