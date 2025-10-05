# 05 — Spoofing and Phishing Techniques: How Attacks Are Crafted

## Objectives
- Understand common spoofing methods and social-engineering techniques used in phishing.
- Recognize technical and human-oriented indicators of phishing.
- Learn simple countermeasures at technical and process levels.

## Spoofing techniques
- **Display-name spoofing:** Attacker chooses a display name that looks legitimate while the underlying email differs.
  - Example: `Bank Support <secure-update@attacker.com>`
- **Domain lookalike / homoglyphs:** Use visually similar characters or subdomains: `paypaI.com` (capital I), `secure.bank.example.com`.
- **Subdomain and path tricks:** Use long subdomains to appear legitimate: `bank-login.example.attacker.com`.
- **Friendly-from via compromised accounts:** Using a real (compromised) account to send phishing to contacts.
- **Reply-To manipulation:** Set reply-to to attacker-controlled address while From looks legit.
- **Email forwarding compromise:** Compromised forwarding rules can hide the true sender.

## Social-engineering lures
- **Credential phishing pages:** urgent message prompting users to sign in on fake login pages.
- **Invoice / payment scams:** fake invoices, overdue payments with attachment or link.
- **BEC (Business Email Compromise):** targeted requests for wire transfers or sensitive data, often using impersonation of executives.
- **Malicious attachments:** "invoice.zip" with an executable or macro-laden document.

## Psychological triggers commonly used
- Urgency / fear: "Your account will be suspended in 24 hours."
- Authority: "From CEO / Bank / IT."
- Curiosity: "Confidential — open immediately."
- Reciprocity / reward: "You have been rewarded — claim now."

## Indicators of phishing (technical + content)
- Mismatch between displayed sender and envelope sender.
- Poor grammar, unusual phrasing, generic greeting.
- Links with mismatched text vs actual URL on hover.
- Requests for sensitive data or credentials via email.
- Unexpected attachments or password-protected files with password in body.

## Defensive controls & mitigations
- Enforce DMARC with `p=quarantine` or `p=reject` when appropriate.
- Use anti-phishing solutions (link rewriting, click-time protection).
- Implement sender authentication and ensure internal users have MFA.
- Train users with phishing simulation and awareness programs.

## Triage guidance
- Treat any request for credentials or payment via email as suspicious until validated by alternative channel (phone call to known number, not data in email).
- For suspected BEC, escalate to security/finance policy and verify via an out-of-band channel.
