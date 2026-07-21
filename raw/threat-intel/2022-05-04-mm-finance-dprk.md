# MM Finance — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-MM-Finance-106
> Timestamp: 2022-05-04T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.4)
> Target: MM Finance
> Amount (USD): $2,000,000
> Asset: Ethereum
> Vector: unknown
> References: MM Finance – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/MM_Finance/MM_Finance_report.html)

On 4 May 2022, MM Finance, a decentralised finance (DeFi) protocol, experienced a significant security breach resulting in the theft of approximately $2,000,000.00. The attack targeted the protocol's smart contracts, exploiting vulnerabilities that allowed unauthorised fund transfers. The immediate financial impact was substantial, affecting both the protocol's liquidity and its user base.

The attack was executed through a series of transactions that exploited a vulnerability in the smart contract's access control mechanisms. The attacker utilised a combination of flash loans and reentrancy attacks to manipulate the protocol's state and siphon funds. The specific functions abused and the technical details of the exploit remain under investigation.

Stolen funds were initially moved from the exploit wallet to intermediary addresses before being laundered through various DeFi protocols and cross-chain bridges. The attacker utilised known mixers and tumblers to obfuscate the fund trail, eventually cashing out through centralised exchanges (CEXs).

The attack is suspected to be linked to the APT38 group, known for its sophisticated cyber operations targeting financial institutions. The use of advanced laundering techniques and infrastructure overlaps with previous incidents attributed to this group support this hypothesis.
