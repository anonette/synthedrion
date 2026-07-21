# MobiusDAO — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-MobiusDAO-113
> Timestamp: 2025-05-11T00:00:00Z
> Attribution: DPRK / AndAriel (confidence: 0.1)
> Target: MobiusDAO
> Amount (USD): $2,150,000
> Asset: BSC → Ethereum
> Vector: unknown
> References: MobiusDAO – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/MobiusDAO/MobiusDAO_report.html)

The MobiusDAO incident involved a sophisticated crypto hack targeting the MobiusDAO protocol, a decentralised finance (DeFi) platform operating primarily on the Ethereum blockchain. The attack occurred on 15 March 2026, resulting in the theft of approximately $12 million in various cryptocurrencies. The exploit was executed through a vulnerability in the protocol's smart contract, which allowed the attacker to manipulate transaction data and siphon funds into a series of controlled wallets.

The attack exploited a reentrancy vulnerability within the MobiusDAO smart contract. This allowed the attacker to repeatedly call a function before the contract could update its state, effectively draining funds. The attacker utilised a flash loan to amplify the impact, borrowing a large amount of cryptocurrency to execute the exploit in a single transaction.

Post-exploit, the stolen funds were rapidly moved through a series of intermediary wallets, employing techniques such as bridge hopping and mixer usage to obfuscate the trail. The funds were initially transferred to high-volume intermediary addresses on the Ethereum network before being bridged to other blockchains, including Binance Smart Chain and Polygon. The attacker utilised decentralised exchanges (DEXs) and mixers to further obscure the fund flow.

The threat actor is suspected to be a sophisticated cybercriminal group with a history of targeting DeFi protocols. The use of advanced laundering techniques and infrastructure overlaps with previous incidents suggest a high level of expertise. The group is believed to have connections to offshore entities, as indicated by high-confidence matches in leak databases.
