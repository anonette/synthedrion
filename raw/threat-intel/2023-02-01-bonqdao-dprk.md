# BonqDAO — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-BonqDAO-28
> Timestamp: 2023-02-01T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.4)
> Target: BonqDAO
> Amount (USD): $120,000,000
> Asset: Ethereum → Polygon
> Vector: unknown
> References: BonqDAO – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/BonqDAO/BonqDAO_report.html)

On 1 February 2023, BonqDAO, a decentralised finance protocol, experienced a significant security breach resulting in the theft of approximately $120 million in digital assets. The attack targeted the protocol's smart contracts, exploiting a vulnerability that allowed the attacker to manipulate token prices and drain funds. The immediate financial impact was severe, affecting both the protocol's liquidity and its user base.

The attack was executed by exploiting a vulnerability in the BonqDAO smart contract, specifically through price manipulation techniques. The attacker utilised a flash loan to artificially inflate the price of certain tokens, allowing them to withdraw more funds than they deposited. This exploit was facilitated by a lack of proper input validation and insufficient checks within the smart contract code.

Stolen funds were initially moved from the exploit wallet to several intermediary wallets, employing a series of rapid transactions to obfuscate the trail. The attacker utilised multiple blockchain bridges and mixers, including Tornado Cash, to launder the funds across different chains. Ultimately, the funds were distributed to various exchanges for cash-out.

The attack is suspected to be linked to the APT38 group, known for its sophisticated cyber operations and previous involvement in similar incidents. The use of advanced laundering techniques and infrastructure overlaps with past APT38 activities support this attribution.
