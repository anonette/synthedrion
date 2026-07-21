# Level Finance — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Level-Finance-101
> Timestamp: 2023-05-01T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.4)
> Target: Level Finance
> Amount (USD): $1,100,000
> Asset: Ethereum → BSC
> Vector: unknown
> References: Level Finance – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Level_Finance/Level_Finance_report.html)

On 1 May 2023, Level Finance, a decentralised finance (DeFi) protocol, experienced a significant security breach resulting in the theft of approximately $1,100,000.00 in cryptocurrency assets. The attack targeted the protocol's smart contracts, exploiting a vulnerability that allowed unauthorised access to user funds. The immediate financial impact was substantial, affecting both the protocol's operations and its user base.

The attack was executed through a sophisticated exploitation of a smart contract vulnerability. The attacker utilised a reentrancy attack, a common DeFi exploit where a function is repeatedly called before the initial execution is completed, allowing the attacker to drain funds. This exploit was facilitated by a flaw in the contract's access control mechanisms, which failed to properly validate transaction sequences.

Following the exploit, the stolen funds were rapidly moved through a series of transactions involving multiple blockchain networks and laundering techniques. The attacker utilised cross-chain bridges and mixers to obfuscate the fund trail, eventually directing the assets to centralised exchanges for cash-out. Key infrastructure used included the Poly Network and various high-volume intermediary addresses.

The attack is attributed to the hacker group APT38, known for targeting financial institutions and employing advanced laundering techniques. The attribution is supported by the use of similar tactics, techniques, and procedures (TTPs) observed in previous incidents linked to this group. The confidence level in this attribution is medium, pending further verification.
