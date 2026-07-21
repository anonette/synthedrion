# Arbix Finance — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Arbix-Finance-10
> Timestamp: 2022-01-04T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.4)
> Target: Arbix Finance
> Amount (USD): $10,000,000
> Asset: Ethereum
> Vector: unknown
> References: Arbix Finance – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Arbix_Finance/Arbix_Finance_report.html)

On 4 January 2022, Arbix Finance, a decentralised finance (DeFi) protocol, suffered a significant security breach resulting in the theft of approximately $10 million USD. The attack targeted the protocol's smart contracts, exploiting vulnerabilities that allowed the attacker to siphon funds from the platform. The immediate financial impact was substantial, affecting both the protocol's liquidity and its user base.

The attack was executed by exploiting a vulnerability in the smart contract's access control mechanisms. The attacker utilised a series of transactions to manipulate the contract's state, allowing unauthorised withdrawals. This involved the use of flash loans to artificially inflate the protocol's liquidity, followed by a reentrancy attack to drain funds.

Stolen funds were initially moved through a series of rapid transactions across multiple wallets, employing techniques such as bridge hopping and mixer usage to obfuscate the trail. The funds were subsequently transferred through various blockchain networks, including Ethereum and Binance Smart Chain, before reaching centralised exchanges for cash-out.

The attack is suspected to have been carried out by the threat actor group APT38, known for its sophisticated cyber operations and previous involvement in similar incidents. The use of advanced laundering techniques and infrastructure overlaps with past APT38 activities support this attribution.
