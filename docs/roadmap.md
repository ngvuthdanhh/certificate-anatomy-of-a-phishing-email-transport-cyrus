# Learning Roadmap

**Goal 1 (Weeks 0–2): Master the fundamentals**
- Understand SMTP, MTA, MDA, MUA and common email architectures.
- Learn how to read and interpret email headers and authentication (SPF/DKIM/DMARC).

**Goal 2 (Weeks 3–4): Analyze payloads and delivery**
- Understand MIME structure and common attachment formats (Office macros, PDF, archives).
- Learn evasion techniques (obfuscation, compression, nested archives) that attackers use to bypass filters.
- Tools to learn: ripmime, foremost, oletools, pefile, mailparser libraries.

**Goal 3 (Week 5): Build defensive controls**
- Secure mail servers (Postfix, Exim, Exchange) — hardening, rate-limits, greylisting.
- Deploy filtering and scanning stacks (SpamAssassin, Amavis, ClamAV) and implement DMARC policies.

**Goal 4 (Ongoing): Campaign analysis workflow**
- Establish a repeatable playbook:
  - Collection → Triage → Deep analysis → Mitigation → Reporting
- Maintain and tune detection rules and YARA signatures based on observed campaigns.

**Recommended reading & resources:** see `docs/references.md` and `extras/resources.md`.
