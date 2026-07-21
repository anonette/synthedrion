# Superfluid — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Superfluid-168
> Timestamp: 2022-02-08T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.12)
> Target: Superfluid
> Amount (USD): $8,700,000
> Asset: Ethereum
> Vector: unknown
> References: Superfluid – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Superfluid/Superfluid_report.html)

On 8 February 2022, the Superfluid protocol experienced a significant security breach resulting in the theft of approximately $8.7 million USD. The attack targeted the protocol's smart contracts, exploiting vulnerabilities to siphon funds into attacker-controlled wallets. The immediate financial impact was substantial, affecting both the protocol's operations and its user base.

The attack was executed by exploiting a vulnerability within the Superfluid smart contracts. The attacker utilised a series of rapid transactions to manipulate the protocol's internal accounting, effectively draining funds. The specific exploit mechanism involved a combination of reentrancy attacks and price manipulation, although the exact smart contract functions abused remain under investigation.

Stolen funds were initially moved from the exploit wallet to intermediary wallets through a series of rapid transactions. The attacker employed multiple blockchain bridges and mixers to obfuscate the fund flow, eventually directing the laundered assets to centralised exchanges for cash-out. Key infrastructure used included the Poly Network and various high-volume intermediaries.

The attack is suspected to be linked to the APT38 group, known for sophisticated cyber operations and financial crimes. This attribution is based on the use of similar TTPs and infrastructure overlaps with previous incidents attributed to APT38. The confidence level in this attribution is medium, pending further investigation.
