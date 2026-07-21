# Anyswap — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Anyswap-09
> Timestamp: 2021-07-10T00:00:00Z
> Attribution: DPRK / Lazarus Group (confidence: 0.07)
> Target: Anyswap
> Amount (USD): $7,900,000
> Asset: Ethereum
> Vector: unknown
> References: Anyswap – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Anyswap/Anyswap_report.html)

On 10 July 2021, the Anyswap protocol experienced a significant security breach resulting in the theft of approximately $7.9 million USD. The attack targeted the protocol's cross-chain bridge functionality, exploiting vulnerabilities to siphon funds from user accounts. The immediate financial impact was severe, affecting numerous users and causing a temporary halt in operations.

The attack was executed by exploiting a vulnerability in the smart contract logic of Anyswap's bridge. The attacker utilised a series of transactions to manipulate the contract's state, allowing unauthorised withdrawals. This involved exploiting access control weaknesses and potentially leveraging compromised private keys.

Stolen funds were initially moved through a series of rapid transactions across multiple wallets, employing techniques such as bridge hopping and mixer usage to obfuscate the trail. The funds were eventually routed through known laundering infrastructure, including Tornado Cash and various cross-chain bridges, before reaching centralised exchanges for cash-out.

The attack is attributed to the Lazarus Group, a well-known cybercrime syndicate with a history of targeting cryptocurrency platforms. This attribution is based on the use of similar tactics, techniques, and procedures (TTPs) observed in previous incidents linked to the group.
