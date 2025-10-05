# 08 — OPSEC and Attribution: Operational Security and Tracing Attackers

## Objectives
- Understand OPSEC considerations during analysis and handling of malicious samples.
- Learn practical steps towards attribution and limitations of attribution.
- Know how to preserve evidence and collaborate with stakeholders.

## OPSEC while analyzing
- Use isolated analysis environments (segregated VMs, separate network).
- Avoid using personal or corporate credentials for sandbox or tool registration.
- Do not interact with live C2 infrastructure unnecessarily; prefer passive observation or controlled sinkholes.
- Use disposable accounts and ephemeral infrastructure for research activities that might require external connectivity.

## Evidence preservation
- Keep original `.eml` and raw file copies — never modify originals.
- Record hashes (MD5/SHA1/SHA256) and timestamps (UTC).
- Maintain chain-of-custody notes when handing evidence to incident response or legal teams.

## Attribution basics
- Gather technical indicators: IPs, domains, malware families, unique compile-time strings, infrastructure overlaps.
- Enrich IOCs with OSINT: WHOIS records, passive DNS, certificate transparency logs, hosting history, ASN ownership.
- Correlate TTPs with known threat actor profiles (use ATT&CK framework).
- Use caution: attackers use false flags (language artifacts, working hours, infrastructure staging) to mislead investigators.

## Limitations & pitfalls in attribution
- Shared infrastructure (bulletproof hosting, compromised servers) confuses origin-tracing.
- Use of open-source toolkits and commodity malware makes code reuse common across actor groups.
- False flags (deliberate artifacts) and third-party compromises create noisy signals.
- Attribution often requires multiple, corroborating data points and sometimes cooperation with hosting providers, registrars, or law enforcement.

## Practical steps for deeper investigation
- Query passive DNS databases to find historical domain/IP relationships.
- Check TLS certificate metadata and certificate chains for reuse patterns.
- Correlate times of activity and registrant details for patterns (timezones, language).
- If needed, engage ISPs, registrars, or law enforcement with formal requests to access server logs.

## Reporting & responsible disclosure
- Notify affected parties (hosting providers, targeted organizations) through proper channels.
- Use secure channels to share sensitive IOCs (e.g., MISP, STIX/TAXII feeds).
- When reporting to vendors or registrars, include reproducible details and timestamps.
