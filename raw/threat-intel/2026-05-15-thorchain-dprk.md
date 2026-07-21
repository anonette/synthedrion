# THORChain — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-THORChain-171
> Timestamp: 2026-05-15T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.12)
> Target: THORChain
> Amount (USD): $10,700,000
> Asset: Ethereum
> Vector: unknown
> References: THORChain – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/THORChain/THORChain_report.html)

On 22 July 2021, THORChain, a decentralised liquidity protocol, suffered a significant security breach resulting in the theft of approximately $8,000,000. The attack targeted the protocol's smart contracts, exploiting a vulnerability that allowed the attacker to manipulate transaction data and siphon funds. The immediate financial impact was substantial, affecting the protocol's liquidity and user trust.

The attacker exploited a vulnerability in THORChain's smart contract logic, potentially involving a reentrancy attack or manipulation of price oracles. This allowed the attacker to execute multiple transactions that drained funds from the protocol. The specific technical details of the exploit remain under investigation, but it is suspected that the attacker used sophisticated scripts to automate the process.

Stolen funds were initially moved from the exploit wallet to several intermediary wallets. The attacker utilised multiple blockchain networks and bridges, including Ethereum and Binance Smart Chain, to obscure the fund trail. Mixers and decentralised exchanges were employed to further launder the funds, eventually reaching centralised exchanges for cash-out.

The attack is suspected to be linked to the Lazarus Group, a North Korean state-sponsored hacking group known for targeting cryptocurrency platforms. This attribution is based on the use of similar tactics, techniques, and procedures (TTPs) observed in previous incidents attributed to the group, as well as infrastructure overlaps.
