# Hope Finance — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Hope-Finance-80
> Timestamp: 2023-02-20T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.4)
> Target: Hope Finance
> Amount (USD): $1,860,000
> Asset: Ethereum → Arbitrum
> Vector: unknown
> References: Hope Finance – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Hope_Finance/Hope_Finance_report.html)

On 20 February 2023, Hope Finance, a decentralised finance (DeFi) protocol, experienced a significant security breach resulting in the theft of approximately $1,860,000. The attack targeted the protocol's smart contracts, exploiting a vulnerability that allowed the attacker to siphon funds from the platform. The immediate financial impact was substantial, affecting both the protocol's liquidity and its user base.

The attack was executed by exploiting a vulnerability in the smart contract's access control mechanisms. The attacker utilised a series of transactions to manipulate the contract's state, allowing unauthorised withdrawals. This involved a combination of reentrancy attacks and flash loan exploits, which are common in DeFi hacks. The specific functions abused and the tools used remain under investigation.

Post-exploit, the stolen funds were rapidly moved through a series of transactions involving multiple wallets and blockchain networks. The attacker employed bridge hopping and mixer services to obfuscate the fund trail. Key infrastructure used included Tornado Cash for mixing and various cross-chain bridges to move assets between networks.

The attack is suspected to be linked to the APT38 group, known for sophisticated cyber operations targeting financial institutions. This attribution is based on the use of similar TTPs and infrastructure overlaps with previous incidents attributed to APT38. The confidence level in this attribution is medium, pending further investigation.
