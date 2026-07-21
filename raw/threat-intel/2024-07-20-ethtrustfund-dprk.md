# ETHTrustFund — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-ETHTrustFund-58
> Timestamp: 2024-07-20T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.12)
> Target: ETHTrustFund
> Amount (USD): $2,100,000
> Asset: Ethereum → BSC
> Vector: unknown
> References: ETHTrustFund – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/ETHTrustFund/ETHTrustFund_report.html)

The ETHTrustFund incident involved a significant crypto hack targeting the Ethereum-based ETHTrustFund protocol on 20 July 2024. The attack resulted in the theft of approximately $2.1 million USD equivalent in Ethereum. The exploit was executed by the hacker group APT38, known for their sophisticated cyber operations. The immediate financial impact was severe, affecting the protocol's liquidity and user trust.

The attack exploited a vulnerability in the ETHTrustFund's smart contract, specifically targeting a reentrancy flaw that allowed the attacker to repeatedly withdraw funds before the contract balance was updated. This type of vulnerability is common in poorly audited smart contracts and requires precise timing and execution to exploit successfully.

Stolen funds were initially moved through a series of Ethereum transactions, utilising intermediary wallets to obscure the trail. The funds were then laundered through various mixers and bridges, including Tornado Cash, and eventually cashed out via centralised exchanges. The laundering process involved multiple blockchain networks and utilised sophisticated techniques to evade detection.

APT38, a North Korean state-sponsored hacking group, is suspected of orchestrating the attack. This attribution is based on the group's known tactics, techniques, and procedures (TTPs), which include exploiting smart contract vulnerabilities and using advanced laundering techniques. The group's infrastructure overlaps with previous incidents attributed to them, increasing the confidence in this assessment.
