# DeFiLabs — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-DeFiLabs-49
> Timestamp: 2023-07-27T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.18)
> Target: DeFiLabs
> Amount (USD): $1,600,000
> Asset: Ethereum → BSC
> Vector: unknown
> References: DeFiLabs – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/DeFiLabs/DeFiLabs_report.html)

On 27 July 2023, DeFiLabs, a decentralised finance platform, experienced a significant security breach resulting in the theft of approximately $1,600,000.00 USD. The attack was executed by exploiting a vulnerability within the platform's smart contract infrastructure, leading to unauthorised fund transfers. The immediate financial impact was substantial, affecting both the platform's liquidity and its user base.

The attack leveraged a smart contract vulnerability, potentially involving reentrancy or access control failures. The attacker utilised a series of rapid transactions to drain funds from the platform. The exact exploit mechanism remains under investigation, but initial analysis suggests the use of automated scripts to execute the attack efficiently.

Stolen funds were initially moved through a series of intermediary wallets before being laundered via multiple blockchain networks. The attacker employed bridge hopping and mixer services to obfuscate the fund trail, eventually attempting to cash out through centralised exchanges. Key infrastructure used included known mixers and cross-chain bridges.

The attack is suspected to be linked to the APT38 group, known for targeting financial institutions. This attribution is based on the use of similar tactics, techniques, and procedures (TTPs) observed in previous incidents attributed to this group. The confidence level in this attribution is medium, pending further investigation.
