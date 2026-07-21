# Lodestar Finance — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Lodestar-Finance-103
> Timestamp: 2022-12-10T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.4)
> Target: Lodestar Finance
> Amount (USD): $6,500,000
> Asset: Ethereum
> Vector: unknown
> References: Lodestar Finance – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Lodestar_Finance/Lodestar_Finance_report.html)

On 10 December 2022, Lodestar Finance, a decentralised finance (DeFi) protocol, experienced a significant security breach resulting in the theft of approximately $6.5 million USD. The attack targeted the protocol's smart contracts, exploiting vulnerabilities to siphon funds into attacker-controlled wallets.

The attack was executed by exploiting a vulnerability in the Lodestar Finance smart contracts, potentially involving reentrancy or access control failures. The attacker utilised a series of transactions to manipulate the protocol's state, allowing unauthorised fund transfers. Specific smart contract functions and technical details of the exploit remain under investigation.

Stolen funds were initially moved from the exploit wallet to intermediary wallets, employing a series of rapid transactions across multiple chains and bridges. The attacker utilised known laundering techniques, including bridge hopping and mixer usage, to obfuscate the fund flow. Key infrastructure involved included the use of high-volume intermediaries and potential centralised exchanges for cash-out.

The attack is suspected to be linked to the APT38 group, known for targeting financial institutions and employing sophisticated laundering techniques. The use of specific laundering patterns and infrastructure overlaps with previous APT38 activities supports this attribution at a medium confidence level.
