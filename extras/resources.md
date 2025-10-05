# Resources — Tools, Reading, Labs and Feeds

A curated list of tools, blogs, datasets, and practical resources for studying and defending against phishing.

---

## Tools & Utilities
- **Parsing & extraction**
  - `ripmime`, `munpack` — extract attachments from MIME.
  - Python `email` and `mailparser` — programmatic parsing of `.eml`.
- **Macro & OLE analysis**
  - `oletools` (olevba, olevba) — extract and analyze VBA macros.
  - `oledump.py` — inspect OLE streams.
- **PE and binary analysis**
  - `pefile`, `r2`/radare2, Ghidra — static analysis of PE files.
- **YARA & pattern matching**
  - `yara` — write signatures for observed indicators.
  - `ripgrep` — fast code and text searching.
- **Sandboxes & dynamic analysis**
  - Cuckoo Sandbox (open-source), Any.Run, Hybrid Analysis, VirusTotal (dynamic reports).
- **Network & URL analysis**
  - `curl`, `wget` (use in isolated env), `dig`, `whois`, `urlscan.io`, VirusTotal URL scan.
- **Threat sharing**
  - MISP — collaborative IOC sharing.
  - STIX/TAXII — structured threat exchange.

---

## Blogs, Vendor Research & Industry Reports
- Proofpoint Threat Research blog — phishing and email threat reports.
- Cofense Intelligence — phishing campaign analyses and datasets.
- Mandiant/FireEye blog — threat actor reports and case studies.
- APWG (Anti-Phishing Working Group) — annual phishing trends and data.
- US-CERT / national CERT blogs — advisories and incident reports.

---

## Recommended Papers & Standards
- RFC 5321 — SMTP.
- RFC 5322 — Internet Message Format.
- RFC 6376 — DKIM.
- RFC 7208 — SPF.
- RFC 7489 — DMARC.
- Academic papers: search for "phishing detection", "URL obfuscation", and "malicious document analysis" in IEEE/ACM libraries.

---

## Training & Hands-on Labs
- TryHackMe / Offensive Security labs with phishing / web exploitation modules.
- Open-source Cuckoo Sandbox setups for dynamic analysis labs.
- Build a local lab: mail server (Postfix), test MTA (OpenSMTPD), and a mail client VM for realistic flows (all isolated).

---

## Data Feeds & Reputations
- VirusTotal — file & URL scanning and historical data.
- URLhaus, PhishTank — phishing URL feeds.
- Passive DNS providers (SecurityTrails, CIRCL Passive DNS) for historical domain resolution.
- AbuseIPDB, Blocklists from Spamhaus for IP reputation.

---

## Books & Long-form Resources
- "Practical Malware Analysis" — for dynamic/static malware analysis techniques.
- "The Art of Memory Forensics" — useful for advanced incident investigations.
- Vendor whitepapers on email security (Proofpoint, Microsoft, Google, Cisco).

---

## Note on Responsible Use
- Use sandboxes and testing infrastructure ethically and legally.
- Do not submit sensitive private data to public services without authorization.
- When reusing vendor reports or graphs, always cite the original source and publication date.
