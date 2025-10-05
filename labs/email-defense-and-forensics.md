# Email Defense & Forensics Lab

## Overview
This lab focuses on building detection, filtering, and forensic controls for email systems. Students will configure (or simulate configuration) of common defenses, write simple detection rules, and practice forensic triage on provided incidents.

## Objectives
- Configure basic mail-gateway defenses (SPF, DKIM, DMARC, SpamAssassin rules).
- Create simple detection signatures (YARA for attachments, header heuristics).
- Perform forensic analysis of an incident and recommend technical mitigations.

## Prerequisites
- Test mail server (Postfix or simulated config files) in isolated environment, or sample config snippets if not deploying.
- Tools: SpamAssassin, Amavis (or simulated rule engine), OpenSSL, `opendkim`, `opendmarc` (optional), `yara`.
- Sample malicious `.eml` and attachment files for analysis.

## Lab 1 — Authentication Enforcement (Config exercise)
1. Inspect domain DNS records for sample domains (use `dig TXT domain`).
2. Draft recommended DNS records for:
   - SPF (example: `v=spf1 mx ip4:203.0.113.0/24 -all`)
   - DKIM (generate keypair, show sample TXT record for selector `mail._domainkey`)
   - DMARC (`_dmarc` TXT with policy and reporting URIs)
3. If you have a lab Postfix instance, configure MTA to:
   - Check SPF (using `postfix-policyd-spf-python` or similar).
   - Verify DKIM signatures (with `opendkim`).
   - Apply DMARC policy actions via `opendmarc` or external policy engine.

**Deliverable:** `auth-config/` folder with sample DNS txt records and Postfix/opendkim snippet.

## Lab 2 — Gateway Filtering Rules
1. Review sample malicious attachments and create:
   - SpamAssassin rules targeting suspicious header patterns and subject lines.
   - Amavis policy snippet to quarantine password-protected archives.
2. Test rules on sample `.eml` and show scoring output from SpamAssassin.

**Deliverable:** `gateway-rules/spamassassin.cf` and `gateway-rules/amavis.conf` examples + test logs.

## Lab 3 — YARA & Attachment Detection
1. Write 2 YARA rules:
   - Rule A: detect obfuscated VBA macro containing `Base64` + `powershell` string pattern.
   - Rule B: detect PE with suspicious import (e.g., `URLDownloadToFile` or `WinExec`).
2. Run YARA against attachments and report matches with file hashes.

**Deliverable:** `yara/` containing `vba-obf.yar` and `pe-sus.yar` and `yara-report.md`.

## Lab 4 — Forensic Incident Walkthrough
1. You are given an incident archive (`incident-package.zip`) containing:
   - `sample.eml`, attachments, logs from mail gateway.
2. Steps:
   - Verify integrity (hashes).
   - Reconstruct message flow using Received headers and gateway logs.
   - Extract IOCs (domains, IPs, hashes) and check enrichment table (ASN/whois).
   - Propose short remediation plan: blocklists, mailflow rules, endpoint actions, user notifications.

**Deliverable:** `incident/forensic-walkthrough.md` with chronology, conclusion, and remediation checklist.

## Safety & Notes
- Do not enable any rule in production without testing.
- Use a simulated environment or config review process for changes to mail servers.

## Assessment (suggested)
- Correctness of DNS/Auth recommendations (25%)
- Effectiveness of filtering rules (25%)
- YARA rule quality and test coverage (20%)
- Forensic walkthrough clarity and mitigation plan (30%)
