# Beanstalk — DPRK-attributed incident

> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)
> Incident ID: CHA-Beanstalk-21
> Timestamp: 2022-04-17T00:00:00Z
> Attribution: DPRK / APT38 (confidence: 0.8)
> Target: Beanstalk
> Amount (USD): $182,000,000
> Asset: Ethereum
> Vector: unknown
> References: Beanstalk – Blockchain Forensics Intelligence Report (https://sandbox.hacksleuths.com/LLM_REPORTS/Beanstalk/Beanstalk_report.html)

On 17 April 2022, the Beanstalk protocol, a decentralised finance (DeFi) platform, suffered a significant exploit resulting in the theft of approximately $182 million USD. The attack targeted the protocol's governance mechanism, allowing the attacker to execute a flash loan attack that manipulated the governance process to drain funds from the protocol.

The attacker exploited a vulnerability in Beanstalk's governance system by using a flash loan to acquire a large amount of governance tokens temporarily. This allowed the attacker to pass a malicious proposal that transferred funds to an address under their control. The attack was executed swiftly, leveraging the decentralised nature of the protocol and the lack of immediate oversight in governance proposals.

Post-exploit, the stolen funds were rapidly moved through a series of transactions involving multiple wallets and blockchain networks. The attacker utilised various laundering techniques, including bridge hopping and mixer services, to obfuscate the fund trail. Key infrastructure used included the Ethereum and Binance Smart Chain networks, with funds eventually reaching centralised exchanges for cash-out.

The attack is attributed to the hacker group APT38, known for sophisticated cyber operations and financial thefts. The group's tactics, techniques, and procedures (TTPs) align with those observed in the Beanstalk exploit, including the use of advanced laundering strategies and infrastructure overlaps with previous incidents.
