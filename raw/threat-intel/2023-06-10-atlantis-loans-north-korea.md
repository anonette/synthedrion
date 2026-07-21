# Atlantis Loans — North Korea-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Atlantis-Loans-13
> Timestamp: 2023-06-10T00:00:00Z
> Attribution: North Korea / unknown group (confidence: unstated)
> Target: Atlantis Loans
> Amount (USD): $2,500,000
> Asset: Ethereum
> Vector: flash loan attack
> References: Atlantis Loans – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Atlantis_Loans/Atlantis_Loans_report.html)

On 10 June 2023, Atlantis Loans, a decentralised lending protocol, experienced a significant security breach resulting in the theft of approximately $2.5 million USD. The attack was executed through a series of flash loan transactions, exploiting vulnerabilities within the protocol's smart contracts. The immediate financial impact was substantial, affecting both the protocol's liquidity and its user base.

The attack leveraged a flash loan exploit, a common vulnerability in DeFi protocols, where the attacker borrowed a large amount of funds without collateral, manipulated the protocol's pricing mechanisms, and repaid the loan within a single transaction block. This exploit was facilitated by weaknesses in the protocol's smart contract logic, specifically in its price oracle and collateral valuation functions.

Stolen funds were initially moved through a series of rapid transactions across multiple wallets, employing techniques such as bridge hopping and mixer usage to obfuscate the trail. The funds were subsequently transferred through various blockchain networks, including Ethereum and Binance Smart Chain, before being deposited into centralised exchanges for cash-out.

The attack is suspected to be orchestrated by a sophisticated cybercriminal group with prior experience in DeFi exploits. The use of advanced laundering techniques and infrastructure overlaps with previous incidents suggest a high level of operational security and planning.
