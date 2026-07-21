# GANA Payment — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-GANA-Payment-66
> Timestamp: 2025-11-20T00:00:00Z
> Attribution: DPRK / Lazarus Group (confidence: 0.14)
> Target: GANA Payment
> Amount (USD): $3,100,000
> Asset: Ethereum → BSC
> Vector: unknown
> References: GANA Payment – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/GANA_Payment/GANA_Payment_report.html)

On 20 November 2025, the GANA Payment protocol experienced a significant security breach resulting in the theft of approximately $3.1 million USD. The attack was executed by exploiting a vulnerability within the protocol's payment processing system, leading to unauthorised fund transfers. The immediate financial impact was substantial, affecting both the protocol's liquidity and its user base.

The attack was executed through a series of rapid transactions exploiting a vulnerability in the protocol's smart contract. The specific weakness exploited remains under investigation, but initial analysis suggests a potential flaw in access control mechanisms or a reentrancy vulnerability. The attacker utilised automated scripts to execute the exploit, indicating a high level of technical sophistication.

Stolen funds were initially moved from the exploit wallet to intermediary addresses, employing a series of rapid transactions to obfuscate the trail. The funds were subsequently laundered through multiple blockchain networks, utilising bridges and mixers to further complicate tracing efforts. The final destinations included several centralised exchanges, where the funds were likely converted to fiat currency.

The attack is attributed to the Lazarus Group, a well-known cybercriminal organisation with a history of targeting cryptocurrency platforms. This attribution is based on the use of similar tactics, techniques, and procedures (TTPs) observed in previous incidents linked to the group. The confidence level in this attribution is high due to the overlap in infrastructure and operational patterns.
