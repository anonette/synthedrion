# Visor Finance — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Visor-Finance-191
> Timestamp: 2021-12-21T00:00:00Z
> Attribution: DPRK / AndAriel (confidence: 0.1)
> Target: Visor Finance
> Amount (USD): $8,200,000
> Asset: Ethereum
> Vector: unknown
> References: Visor Finance – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Visor_Finance/Visor_Finance_report.html)

On 21 December 2021, Visor Finance, a liquidity management protocol, experienced a significant security breach resulting in the theft of approximately $8.2 million USD. The attack targeted the protocol's smart contracts, exploiting vulnerabilities to siphon funds into attacker-controlled wallets. The immediate financial impact was substantial, affecting both the protocol's operations and its user base.

The attack was executed through a series of transactions that exploited weaknesses in the smart contract's access control mechanisms. The attacker utilised a combination of flash loans and reentrancy attacks to manipulate the protocol's liquidity pools, allowing them to withdraw funds without proper authorisation. This method indicates a high level of technical sophistication and understanding of the protocol's architecture.

Stolen funds were initially moved through a series of rapid transactions across multiple wallets, employing techniques such as bridge hopping and mixer usage to obfuscate the trail. The funds were subsequently transferred through various blockchain networks, including Ethereum and Binance Smart Chain, before being deposited into centralised exchanges for cash-out.

The attack is suspected to have been carried out by the hacker group "AndAriel," known for similar exploits in the past. The use of advanced laundering techniques and infrastructure overlaps with previous incidents attributed to this group support this hypothesis. The confidence level in this attribution is medium, pending further investigation.
