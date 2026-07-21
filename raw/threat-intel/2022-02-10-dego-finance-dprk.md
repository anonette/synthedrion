# Dego Finance — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Dego-Finance-50
> Timestamp: 2022-02-10T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.4)
> Target: Dego Finance
> Amount (USD): $10,000,000
> Asset: Ethereum
> Vector: unknown
> References: Dego Finance – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Dego_Finance/Dego_Finance_report.html)

On 10 February 2022, Dego Finance, a decentralised finance (DeFi) protocol, experienced a significant security breach resulting in the theft of approximately $10,000,000. The attack targeted the protocol's smart contracts, exploiting vulnerabilities that allowed unauthorised access to user funds. The immediate financial impact was substantial, affecting both the protocol's liquidity and its user base.

The attack was executed through a combination of smart contract vulnerabilities and potentially compromised private keys. The attacker utilised a series of transactions to manipulate the protocol's functions, enabling the extraction of funds without triggering immediate security alerts. The specific exploit mechanism involved manipulating transaction sequences to bypass security checks.

Stolen funds were initially moved from the exploit wallet through a series of intermediary wallets, employing techniques such as bridge hopping and mixer usage to obfuscate the trail. The funds were subsequently transferred across multiple blockchain networks, including Ethereum and Binance Smart Chain, before reaching centralised exchanges for cash-out.

The attack is suspected to have been orchestrated by the cybercriminal group APT38, known for targeting financial institutions. This attribution is based on the use of similar tactics, techniques, and procedures (TTPs) observed in previous incidents linked to the group. The confidence level in this attribution is medium, pending further investigation.
