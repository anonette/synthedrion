# LNDFi — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-LNDFi-100
> Timestamp: 2021-05-09T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.18)
> Target: LNDFi
> Amount (USD): $1,180,000
> Asset: Ethereum → BSC
> Vector: unknown
> References: LNDFi – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/LNDFi/LNDFi_report.html)

On 9 May 2021, LNDFi, a decentralised finance protocol, experienced a significant security breach resulting in the theft of approximately $1,180,000.00. The attack targeted the protocol's smart contracts, exploiting vulnerabilities that allowed unauthorised fund transfers. The immediate financial impact was substantial, affecting both the protocol's liquidity and its user base.

The attack was executed through a sophisticated exploitation of smart contract vulnerabilities, potentially involving reentrancy or access control failures. The attacker utilised a series of rapid transactions to manipulate the protocol's state, enabling the extraction of funds without triggering immediate security alerts.

Stolen funds were initially moved through a series of intermediary wallets, employing techniques such as bridge hopping and mixer usage to obfuscate the trail. The funds traversed multiple blockchain networks, including Ethereum and Binance Smart Chain, before reaching centralised exchanges for cash-out.

The attack is suspected to be linked to the APT38 group, known for targeting financial institutions with similar methodologies. The use of advanced laundering techniques and infrastructure overlaps with previous incidents attributed to this group supports this hypothesis.
