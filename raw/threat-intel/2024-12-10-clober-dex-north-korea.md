# Clober Dex — North Korea-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Clober-Dex-34
> Timestamp: 2024-12-10T00:00:00Z
> Attribution: North Korea / unknown group (confidence: unstated)
> Target: Clober Dex
> Amount (USD): $500,000
> Asset: Ethereum
> Vector: unknown
> References: Clober Dex – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Clober_Dex/Clober_Dex_report.html)

On 10 December 2024, Clober Dex, a decentralised exchange operating on multiple blockchain networks, experienced a significant security breach. The incident resulted in the unauthorised transfer of approximately $500,000 in digital assets. The exploit was detected through abnormal transaction patterns and was publicly disclosed by Clober Dex within hours of the breach.

The attack exploited a vulnerability in Clober Dex's smart contract infrastructure, specifically targeting a reentrancy flaw that allowed the attacker to repeatedly withdraw funds without updating the balance. This vulnerability was exploited using a series of rapid transactions, leveraging automated scripts to maximise the extraction of funds.

Stolen funds were initially moved through a series of intermediary wallets, employing techniques such as bridge hopping and mixer usage to obfuscate the trail. The funds were subsequently transferred across multiple blockchain networks and eventually cashed out through centralised exchanges. Key infrastructure used included known mixers and cross-chain bridges.

The attack is suspected to be the work of a sophisticated threat actor group with a history of targeting decentralised finance platforms. The use of advanced laundering techniques and infrastructure overlaps with previous incidents suggest a high level of operational security and experience.
