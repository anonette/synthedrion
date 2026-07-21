# Penpie — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Penpie-128
> Timestamp: 2024-09-03T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.12)
> Target: Penpie
> Amount (USD): $27,000,000
> Asset: Ethereum → Arbitrum
> Vector: unknown
> References: Penpie – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Penpie/Penpie_report.html)

On 3 September 2024, the Penpie protocol experienced a significant security breach resulting in the theft of approximately $27 million USD. The attack targeted the protocol's smart contract infrastructure, exploiting vulnerabilities to siphon funds into attacker-controlled wallets. The immediate financial impact was severe, affecting the protocol's liquidity and user trust.

The attack was executed through a sophisticated exploit of the Penpie protocol's smart contracts. The attacker utilised a combination of flash loans and reentrancy attacks to manipulate the protocol's state and extract funds. This involved exploiting a known vulnerability in the contract's access control mechanisms, allowing unauthorised transactions to be executed.

Stolen funds were initially moved from the exploit wallet to intermediary wallets, employing a series of rapid transactions to obfuscate the trail. The funds were then laundered through multiple blockchain networks, utilising bridges and mixers to further complicate tracing efforts. Key infrastructure used included the Poly Network and various decentralised exchanges (DEXs).

The attack is suspected to have been carried out by the APT38 group, known for their sophisticated cyber operations and previous involvement in similar incidents. The use of advanced laundering techniques and infrastructure overlaps with past APT38 activities support this attribution.
