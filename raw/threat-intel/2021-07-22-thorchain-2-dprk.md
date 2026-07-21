# THORChain 2 — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-THORChain---2-172
> Timestamp: 2021-07-22T00:00:00Z
> Attribution: DPRK / Lazarus Group (confidence: 0.07)
> Target: THORChain 2
> Amount (USD): $8,000,000
> Asset: Ethereum
> Vector: unknown
> References: THORChain 2 – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/THORChain_-_2/THORChain_-_2_report.html)

On 22 July 2021, THORChain, a decentralised liquidity protocol, experienced a significant security breach resulting in the loss of approximately $8 million USD. The attack targeted the protocol's cross-chain liquidity pools, exploiting vulnerabilities in the smart contract infrastructure.

The attack was executed by exploiting a vulnerability in the protocol's smart contract logic, potentially involving a reentrancy attack or manipulation of liquidity pool balances. The specific technical details of the exploit mechanism remain under investigation, but it involved multiple rapid transactions to siphon funds from the protocol.

Stolen funds were initially moved from the exploit wallet (0x8c1944fac705ef172f21f905b5523ae260f76d62) to intermediary wallets and then dispersed across various chains and exchanges. The attacker utilised known laundering techniques such as bridge hopping and mixer services to obfuscate the fund trail.

The attack is attributed to the Lazarus Group, a well-known cybercrime syndicate with a history of targeting cryptocurrency platforms. This attribution is based on the use of similar tactics, techniques, and procedures (TTPs) observed in previous incidents linked to the group.
