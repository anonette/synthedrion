# BNB Bridge — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-BNB-Bridge-16
> Timestamp: 2022-10-06T00:00:00Z
> Attribution: DPRK / Lazarus Group (confidence: 0.8)
> Target: BNB Bridge
> Amount (USD): $586,000,000
> Asset: Ethereum
> Vector: exchange compromise
> References: BNB Bridge – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/BNB_Bridge/BNB_Bridge_report.html)

On 6 October 2022, the BNB Bridge protocol suffered a significant security breach resulting in the theft of approximately $586 million USD. The attack targeted the BNB Bridge, a critical component in the Binance Smart Chain ecosystem, facilitating cross-chain transactions. The exploit was executed by the Lazarus Group, a well-known cybercriminal organisation.

The attack exploited a vulnerability in the BNB Bridge's smart contract, allowing the attacker to manipulate transaction data and siphon funds without detection. The specific weakness involved improper validation of cross-chain messages, which the attacker leveraged to initiate unauthorised transfers. The attack was executed using automated scripts to rapidly move funds through multiple transactions.

Stolen funds were initially moved from the exploit wallet to a series of intermediary wallets, employing complex layering techniques including bridge hopping and mixer usage. The funds traversed multiple blockchain networks, including Ethereum and Binance Smart Chain, before reaching centralised exchanges for cash-out.

The Lazarus Group is suspected with high confidence due to the use of known TTPs, including rapid fund movement and sophisticated laundering techniques. Historical data links the group to similar high-profile cryptocurrency thefts, reinforcing this attribution.
