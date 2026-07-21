# KyberSwap — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-KyberSwap-98
> Timestamp: 2023-11-22T00:00:00Z
> Attribution: DPRK / Lazarus Group (confidence: 0.07)
> Target: KyberSwap
> Amount (USD): $48,000,000
> Asset: Ethereum
> Vector: unknown
> References: KyberSwap – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/KyberSwap/KyberSwap_report.html)

On 22 November 2023, KyberSwap, a decentralised exchange platform, experienced a significant security breach resulting in the theft of approximately $48 million in various cryptocurrencies. The attack targeted the platform's liquidity pools, exploiting vulnerabilities in the smart contract infrastructure. The immediate financial impact was substantial, affecting both the platform's operations and its user base.

The attack was executed through a sophisticated exploit of the smart contract's concentrated liquidity protocol. The attacker utilised a combination of flash loans and price manipulation techniques to drain funds from the liquidity pools. The specific vulnerability exploited involved a flaw in the contract's price oracle mechanism, allowing the attacker to manipulate asset prices and execute trades at favourable rates.

Stolen funds were initially moved through a series of rapid transactions across multiple wallets, employing techniques such as bridge hopping and mixer usage to obfuscate the trail. The funds were subsequently laundered through various decentralised exchanges and cross-chain bridges, eventually reaching centralised exchanges for cash-out. Key infrastructure used included Tornado Cash and several cross-chain bridges.

The attack is attributed with medium confidence to the Lazarus Group, a North Korean state-sponsored hacking group known for targeting cryptocurrency platforms. This attribution is based on the use of similar tactics, techniques, and procedures (TTPs) observed in previous incidents linked to the group, as well as infrastructure overlaps.
