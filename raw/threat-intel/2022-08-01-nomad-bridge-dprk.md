# Nomad Bridge — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Nomad-Bridge-119
> Timestamp: 2022-08-01T00:00:00Z
> Attribution: DPRK / Lazarus Group (confidence: 0.8)
> Target: Nomad Bridge
> Amount (USD): $190,000,000
> Asset: Ethereum
> Vector: bridge exploit
> References: Nomad Bridge – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Nomad_Bridge/Nomad_Bridge_report.html)

On 1 August 2022, the Nomad Bridge, a cross-chain protocol facilitating asset transfers between different blockchain networks, was exploited. The attack resulted in the theft of approximately $190 million USD in digital assets. The exploit targeted a vulnerability within the bridge's smart contract, allowing unauthorised withdrawals. The immediate financial impact was significant, affecting numerous users and stakeholders reliant on the bridge for cross-chain transactions.

The attack exploited a vulnerability in the Nomad Bridge's smart contract, specifically related to improper validation of transaction inputs. This allowed the attacker to repeatedly withdraw funds without proper authorisation. The exploit was executed using a series of transactions that manipulated the bridge's state, bypassing security checks and enabling the extraction of funds.

The stolen funds were initially moved from the exploit wallet to a series of intermediary wallets. These funds were then laundered through various mixers and cross-chain bridges, including Tornado Cash and other decentralised exchanges, to obfuscate their origin. The laundering process involved multiple blockchain networks, making tracing efforts complex and resource-intensive.

The Lazarus Group, a North Korean state-sponsored hacking group, is suspected of orchestrating the attack. This attribution is based on the group's known tactics, techniques, and procedures (TTPs), which align with the observed attack patterns and laundering methods. The group's previous involvement in similar high-profile cryptocurrency heists further supports this hypothesis.
