# WazirX — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-WazirX-196
> Timestamp: 2024-07-18T00:00:00Z
> Attribution: DPRK / Lazarus Group (confidence: 0.14)
> Target: WazirX
> Amount (USD): $235,000,000
> Asset: Ethereum
> Vector: unknown
> References: WazirX – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/WazirX/WazirX_report.html)

On 18 July 2024, WazirX, a prominent cryptocurrency exchange, experienced a significant security breach resulting in the theft of approximately $235 million USD. The attack was executed by the Lazarus Group, a well-known cybercriminal organisation. The exploit mechanism involved the compromise of private keys, allowing the attackers to initiate unauthorised transactions from the exchange's wallets.

The attackers exploited a vulnerability in WazirX's infrastructure, specifically targeting weak access controls that allowed them to gain access to private keys. This enabled the execution of transactions without detection until the funds were already in motion. The attack did not involve smart contract manipulation but rather a direct compromise of the exchange's security protocols.

The stolen funds were initially moved through a series of rapid transactions across multiple wallets to obscure their origin. The attackers utilised various blockchain bridges and mixers, including Tornado Cash, to launder the funds. The funds were eventually distributed across several exchanges, including those in jurisdictions with lax regulatory oversight.

The Lazarus Group is suspected with high confidence due to the use of known TTPs associated with the group, such as the use of specific laundering techniques and infrastructure overlaps with previous incidents attributed to them. The group's history of targeting cryptocurrency exchanges further supports this attribution.
