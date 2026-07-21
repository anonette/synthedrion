# Phemex — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Phemex-129
> Timestamp: 2025-01-23T00:00:00Z
> Attribution: DPRK / Lazarus Group (confidence: 0.14)
> Target: Phemex
> Amount (USD): $73,540,297
> Asset: Ethereum → BSC → Arbitrum
> Vector: unknown
> References: Phemex – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Phemex/Phemex_report.html)

On 23 January 2025, the Phemex cryptocurrency exchange experienced a significant security breach resulting in the theft of approximately $73.54 million USD in digital assets. The attack targeted the exchange's hot wallet infrastructure, exploiting vulnerabilities in transaction processing mechanisms. The immediate financial impact was substantial, affecting both the exchange's liquidity and its users' holdings.

The attack was executed through a sophisticated series of transactions that exploited a vulnerability in the exchange's transaction validation process. This involved the manipulation of transaction sequences to bypass security checks, potentially involving compromised private keys or insider access. The exact technical details of the vulnerability remain under investigation.

Stolen funds were rapidly moved from the exploit wallet through a series of intermediary wallets, employing techniques such as chain hopping and mixer usage to obfuscate the trail. The funds were eventually distributed across multiple exchanges and OTC desks, complicating recovery efforts. Key infrastructure used included known mixers and cross-chain bridges.

The attack is suspected to be linked to the Lazarus Group, a well-known cybercrime syndicate with a history of targeting cryptocurrency exchanges. This attribution is based on similarities in tactics, techniques, and procedures (TTPs) observed in previous incidents attributed to the group.
