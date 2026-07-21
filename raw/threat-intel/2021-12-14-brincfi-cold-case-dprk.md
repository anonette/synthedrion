# BrincFi Cold Case — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-BrincFi---Cold-Case-29
> Timestamp: 2021-12-14T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.29)
> Target: BrincFi Cold Case
> Amount (USD): $1,100,000
> Asset: Ethereum
> Vector: unknown
> References: BrincFi Cold Case – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/BrincFi_-_Cold_Case/BrincFi_-_Cold_Case_report.html)

On 14 December 2021, the BrincFi protocol experienced a significant security breach resulting in the theft of approximately $1,100,000.00. The attack targeted the protocol's smart contract infrastructure, exploiting a vulnerability that allowed the attacker to siphon funds from the protocol's reserves.

The attack was executed by exploiting a vulnerability in the smart contract's logic, potentially involving a reentrancy attack or an access control failure. The attacker utilised a series of transactions to manipulate the contract's state, allowing unauthorised withdrawals.

Stolen funds were initially moved from the exploit wallet to intermediary wallets, employing a series of rapid transactions to obfuscate the trail. The attacker utilised known laundering techniques, including bridge hopping and mixer usage, to further obscure the fund flow. Funds were eventually moved to centralised exchanges for cash-out.

The attack is attributed to the hacker group APT38 with a medium level of confidence. This attribution is based on the use of similar tactics, techniques, and procedures (TTPs) observed in previous incidents linked to the group, including infrastructure overlaps and transaction patterns.
