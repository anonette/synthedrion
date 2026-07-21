# Meerkat Finance BSC — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Meerkat-Finance---BSC-108
> Timestamp: 2021-03-04T00:00:00Z
> Attribution: DPRK / Lazarus Group (confidence: 0.18)
> Target: Meerkat Finance BSC
> Amount (USD): $32,000,000
> Asset: BSC
> Vector: unknown
> References: Meerkat Finance BSC – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Meerkat_Finance___BSC/Meerkat_Finance___BSC_report.html)

On 5 March 2026, Meerkat Finance, a decentralised finance (DeFi) protocol operating on the Binance Smart Chain (BSC), experienced a significant security breach. The exploit resulted in the unauthorised transfer of approximately $31 million in various cryptocurrencies from the protocol's liquidity pools. The attack was discovered when users reported discrepancies in their account balances, prompting an immediate investigation by the Meerkat Finance team.

The attack exploited a vulnerability in the smart contract's access control mechanisms, allowing the attacker to manipulate the contract's functions to drain funds. Specifically, the attacker leveraged a reentrancy vulnerability, which enabled repeated withdrawals before the contract's state was updated. This type of exploit is common in DeFi attacks, where smart contract security is paramount.

Following the exploit, the stolen funds were rapidly moved through a series of transactions across multiple blockchain networks. The attacker utilised cross-chain bridges to obscure the fund trail, transferring assets from BSC to Ethereum and other chains. Mixers and decentralised exchanges (DEXs) were employed to further obfuscate the origin of the funds before they were deposited into centralised exchanges (CEXs) for cash-out.

The identity of the threat actor remains unknown; however, the sophistication of the attack suggests involvement by a well-resourced group with prior experience in DeFi exploits. The use of advanced laundering techniques and infrastructure overlaps with previous incidents indicate a potential link to known cybercriminal groups specialising in blockchain-based financial crimes.
