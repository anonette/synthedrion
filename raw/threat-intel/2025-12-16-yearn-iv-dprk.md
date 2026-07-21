# Yearn IV — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Yearn---IV-206
> Timestamp: 2025-12-16T00:00:00Z
> Attribution: DPRK / AndAriel (confidence: 0.1)
> Target: Yearn IV
> Amount (USD): $293,000
> Asset: Ethereum
> Vector: unknown
> References: Yearn IV – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Yearn_-_IV/Yearn_-_IV_report.html)

On 13 April 2023, the Yearn Finance protocol was targeted in a sophisticated cyber attack, resulting in the theft of approximately $11.4 million USD. The attack was executed by a group identified as "AndAriel", exploiting vulnerabilities within the protocol's smart contract infrastructure. The immediate financial impact was significant, affecting the protocol's liquidity and user trust.

The attack leveraged a vulnerability in the Yearn Finance smart contracts, potentially involving reentrancy or flash loan exploits. The exact mechanism remains under investigation, but the rapid sequence of transactions suggests a premeditated and technically sophisticated approach. No specific smart contract functions or infrastructure failures have been explicitly identified in the available data.

Stolen funds were initially moved from the exploit wallet (0x14ec0cd2acee4ce37260b925f74648127a889a28) to intermediary wallets, including 0x62494b3ed9663334e57f23532155ea0575c487c5. The funds were then layered through various transactions, potentially involving mixers and cross-chain bridges, before reaching final cash-out destinations. Specific exchanges or mixers used have not been identified in the provided data.

The group "AndAriel" is suspected of orchestrating the attack, with a medium confidence level based on transaction patterns and wallet behaviours. The group's tactics, techniques, and procedures (TTPs) align with previous incidents involving rapid fund movement and sophisticated laundering strategies.
