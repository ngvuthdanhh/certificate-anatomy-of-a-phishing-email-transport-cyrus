# Case Studies — Real-world Phishing Campaigns and Lessons

This file collects short, actionable analyses of notable phishing campaigns. Each case focuses on delivery, TTPs, detection gaps, and defensive lessons.

---

## Case Study 1 — Credential Harvesting via Brand Impersonation (Retail/Payments)
**Summary:** Campaign impersonated a major payment provider using near-identical domains and HTML login pages. Emails used urgent language ("Your account is suspended") and link shorteners to hide final landing page.

**TTPs**
- Display-name spoofing + lookalike domains (IDN/homoglyph).
- URL shorteners and multi-stage redirects through compromised websites.
- HTML pages that mirrored the legitimate login page with form POST to attacker-controlled endpoint.

**Detection gaps exploited**
- Recipient trust in brand and urgency cues.
- Gateway allowed redirects and did not detonate pages in a sandbox at click-time.
- Domain registration was recent and privacy-protected, but no proactive DMARC enforcement.

**Mitigations**
- Enforce DMARC (p=quarantine/reject) for critical domains.
- Deploy click-time protection (rewriting + sandbox visit) and URL reputation checks.
- User training focusing on link-hover checks and out-of-band verification for account issues.

**Lessons**
- Even polished pages can be malicious; always validate domain, not just page appearance.
- Click-time protections are highly effective for credential-harvesting campaigns.

---

## Case Study 2 — Business Email Compromise (BEC) Targeting Finance
**Summary:** Targeted spear-phishing toward finance teams using compromised vendor accounts and context-aware content (invoice numbers, PO references). Attackers used subtle display-name impersonation of a CFO and requested an urgent wire transfer.

**TTPs**
- Reconnaissance (social media, public docs) to harvest vendor names and contacts.
- Compromised vendor mailbox used to send trustworthy-looking invoices.
- Use of business language, correct invoice formatting, and valid-looking sender addresses.

**Detection gaps exploited**
- Reliance on sender reputation and presence of valid SPF/DKIM when vendor was legitimately compromised.
- Lack of process controls for validating high-value transfers (no multi-person approval).

**Mitigations**
- Implement strict financial controls: multi-factor approval for transfers above thresholds.
- Out-of-band verification for any change in payment details (call verified number).
- Monitor for unusual forwarding rules or automation set on vendor mailboxes.

**Lessons**
- BEC is a process and controls problem as much as a technical one.
- Assume compromise is possible even for known vendors; verify critical requests.

---

## Case Study 3 — Malware Delivery via Macro-enabled Documents
**Summary:** Large-scale phishing with ZIP attachments containing macro-enabled Word documents. Macros used simple obfuscation to run PowerShell commands that downloaded payloads from cloud storage.

**TTPs**
- Password-protected ZIP with password in the email body to bypass some email scanners.
- Obfuscated VBA that launched `powershell.exe` with encoded commands.
- Hosting payloads on reputable cloud infrastructure (e.g., AWS S3, Azure) to blend in.

**Detection gaps exploited**
- Gateway allowed password-protected archives to pass through.
- Static scanners failed to detect obfuscation patterns; dynamic sandboxing was not applied pre-delivery.
- Users were accustomed to receiving ZIP attachments and opened them.

**Mitigations**
- Block or quarantine password-protected archives by default; require manual review.
- Use macro-blocking policies at endpoint and require explicit admin approval for macro execution.
- Enable attachment detonation in sandbox with network sinkholing for known bad domains.

**Lessons**
- Attackers increasingly use legitimate services for hosting — reputation alone is insufficient.
- Combine gateway sandboxing, endpoint controls, and user awareness for layered defense.

---

## How to add new case studies
- Include: summary, timeline of attack, TTPs, exploited detection gaps, mitigations, lessons learned.
- Cite sources (vendor reports, CERTs, academic papers) and include publish dates.
