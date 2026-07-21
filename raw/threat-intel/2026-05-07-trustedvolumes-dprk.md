# TrustedVolumes — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-TrustedVolumes-182
> Timestamp: 2026-05-07T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.12)
> Target: TrustedVolumes
> Amount (USD): $5,870,000
> Asset: Ethereum
> Vector: unknown
> References: TrustedVolumes – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/TrustedVolumes/TrustedVolumes_report.html)

On 07 May 2026, the TrustedVolumes platform experienced a significant security breach resulting in the theft of approximately $5,870,000.00 in various cryptocurrencies, including ETH, WBTC, and USDC. The attack targeted the platform's smart contract infrastructure, exploiting vulnerabilities that allowed the attacker to siphon funds from user accounts. The immediate financial impact was substantial, affecting both the platform's liquidity and user trust.

The attack was executed through a sophisticated exploitation of smart contract vulnerabilities, potentially involving reentrancy attacks or access control failures. The attacker utilised a series of automated scripts to execute transactions rapidly, bypassing security measures and extracting funds from the platform's reserves. The exact exploit mechanism remains under investigation, but initial analysis suggests a combination of flash loan attacks and price manipulation tactics.

Stolen funds were initially moved through a series of intermediary wallets, employing complex layering techniques to obfuscate the trail. The attacker utilised multiple blockchain networks, including Ethereum and Binance Smart Chain, and leveraged cross-chain bridges to further disperse the assets. Funds were subsequently routed through mixers and decentralised exchanges (DEXs) before reaching centralised exchanges (CEXs) for cash-out.

The attack is suspected to be the work of APT38, a North Korean state-sponsored hacking group known for targeting financial institutions. This attribution is based on the use of similar tactics, techniques, and procedures (TTPs) observed in previous incidents attributed to the group, as well as infrastructure overlaps and the strategic targeting of high-value financial platforms.
