# 01 — Overview: Anatomy of a Phishing Email

## Objectives
- Understand the basic structure of an email (headers, body, MIME/attachments).
- Learn the delivery flow (MUA → MTA → MDA) and where attackers can intervene.
- Identify the key data sources used in email forensic analysis (raw source, headers, attachments, embedded links).

## Key Concepts
1. **Email components**
   - **Header**: From, To, Subject, Date, Message-ID, Received, Return-Path, Reply-To, DKIM-Signature, SPF/Authentication-Results, etc.
   - **Body**: plain text or HTML; may include embedded images, links, and tracking elements.
   - **MIME parts**: multipart/alternative, multipart/mixed, attachments, content-type, content-transfer-encoding.

2. **Delivery flow**
   - **MUA (Mail User Agent)**: end-user client (Outlook, Thunderbird, webmail UI).
   - **MTA (Mail Transfer Agent)**: SMTP servers that relay mail between networks (Postfix, Exim, Exchange).
   - **MDA (Mail Delivery Agent)**: final delivery into a mailbox (Dovecot, Exchange store).
   - Attacker control points: compromised MTA, abused open relay, forged headers, domain impersonation, use of compromised legitimate accounts.

3. **Data sources for analysis**
   - Raw `.eml` file (full headers + body).
   - Server logs (Postfix/Exim/Exchange), gateway logs, IDS/IPS logs.
   - Attachment files extracted and hashed; sandbox reports.
   - Web logs where clicked URLs redirected or landed.

## Quick Triage Checklist
- Extract full raw headers and body.
- Verify SPF/DKIM/DMARC results (from Authentication-Results header or check yourself).
- Inspect Received header chain for suspicious hops or IPs.
- Extract attachments and compute hashes (MD5/SHA1/SHA256).
- Resolve and inspect links (do not click directly—use trusted resolvers and safe browsing sandboxes).
- Run attachments through static scanners and sandbox if safe.

## Safety recommendations
- Always analyze suspected malicious content in isolated VMs or sandbox environments.
- Preserve evidence: keep original `.eml` and logs; record timestamps and metadata.
