# Harmony Horizon Bridge — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Harmony-Bridge-78
> Timestamp: 2022-06-23T00:00:00Z
> Attribution: DPRK / Lazarus Group (confidence: 0.8)
> Target: Harmony Horizon Bridge
> Amount (USD): $100,000,000
> Asset: Ethereum
> Vector: bridge exploit
> References: Harmony Bridge – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Harmony_Bridge/Harmony_Bridge_report.html)

On 23 June 2022, the Harmony Bridge, a cross-chain bridge facilitating asset transfers between different blockchain networks, was exploited, resulting in the theft of approximately $100 million USD. The exploit targeted the bridge's infrastructure, allowing the attacker to siphon funds from the protocol. The immediate financial impact was significant, affecting the bridge's liquidity and user trust.

The attack was executed by exploiting a vulnerability in the bridge's smart contract, potentially involving a private key compromise or a flaw in the access control mechanisms. The attacker utilised a series of transactions to drain funds, leveraging the bridge's functionality to transfer assets across chains without proper authorisation checks.

Stolen funds were initially moved from the exploit wallet to intermediary wallets, employing a series of rapid transactions to obfuscate the trail. The attacker utilised multiple blockchain networks and bridges, including known mixers, to layer the funds and evade detection. The funds were eventually directed towards centralised exchanges for cash-out.

The Lazarus Group, a North Korean state-sponsored hacking group, is suspected of orchestrating the attack. This attribution is based on the group's known tactics, techniques, and procedures (TTPs), including the use of similar infrastructure and laundering methods in previous incidents.
