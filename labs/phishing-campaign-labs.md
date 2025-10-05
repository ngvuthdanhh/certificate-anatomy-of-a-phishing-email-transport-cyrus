# Phishing Campaign Labs

## Overview
This lab set guides students through the lifecycle of a phishing campaign analysis: collection, triage, enrichment, campaign linking, and reporting. All exercises must be run in isolated, offline or sandboxed environments — do **not** send real phishing emails or interact with live C2 infrastructure.

## Objectives
- Collect and normalize email artifacts from a sample campaign.
- Triage and classify samples (bulk vs targeted).
- Enrich indicators (domains, IPs, certificates, WHOIS, passive DNS).
- Build a campaign timeline linking messages, infrastructure and payloads.
- Produce a concise forensic report with IOCs and mitigations.

## Prerequisites
- Isolated lab VM(s) with no access to corporate network.
- Tools: `ripmime` / `munpack`, Python 3 with `mailparser` or `email` package, `jq`, `yara`, `whois`, `dig`, `curl`, `git`.
- Optional: access to sandbox services (VirusTotal/Hybrid/URLscan) via separate researcher account — use with care.

## Lab 1 — Collection & Normalization
1. Obtain a set of raw `.eml` files (simulated samples provided by instructor or created in a controlled testbed).
2. For each `.eml`, extract:
   - Full headers (save as `samplename.headers.txt`).
   - Body as `samplename.body.html` / `samplename.body.txt`.
   - Attachments saved in `attachments/samplename/`.
3. Compute and record hashes for each artifact (MD5, SHA1, SHA256).
   - Example: `sha256sum sample.eml > sample.hash.txt`

**Deliverable:** folder `collection/` containing `.eml`, headers, extracted attachments, and `collection-report.md` with a table of samples and hashes.

## Lab 2 — Triage & Classification
1. For each sample:
   - Read `Authentication-Results` and `Received` chain.
   - Note SPF/DKIM/DMARC results and any alignment issues.
2. Classify each email as `bulk/spam`, `targeted/spear-phish`, or `BEC-like` with reasons.
3. Create a short triage note per sample (1–2 paragraphs) including immediate indicators and risk level.

**Deliverable:** `triage/triage-notes.md` with per-sample classification.

## Lab 3 — Infrastructure Enrichment
1. Extract all domains and IPs found in:
   - Links (href values), embedded resources, attachment macro strings, Received headers.
2. For each domain/IP:
   - Run DNS lookup (`dig`), whois, and record ASN owner.
   - Optionally query passive DNS or URL scanning (do not submit real samples to public services without permission).
3. Create an enrichment table (CSV or markdown) with columns: indicator, type (domain/IP/hash), first seen in sample, ASN/owner, notes.

**Deliverable:** `enrichment/enrichment-table.csv` and `enrichment/notes.md`.

## Lab 4 — Campaign Linking & Timeline
1. Using timestamps from headers and enrichment data, construct a timeline of activity (first seen → last seen) for the campaign.
2. Link messages to common infrastructure (shared domains, same IP, similar macro code, same tracking IDs).
3. Plot a simple timeline (ASCII table or CSV for import into visualization tools).

**Deliverable:** `campaign/timeline.csv` and `campaign/links.md` explaining linkage rationale.

## Lab 5 — Reporting & Remediation Recommendations
1. Produce a forensic report (max 3 pages) containing:
   - Executive summary (1 paragraph)
   - Technical findings (IOCs, TTPs)
   - Timeline and linkage diagram
   - Recommended mitigations and detection rules (YARA prototypes, spam filter hints)
2. Optionally prepare a one-page briefing for non-technical stakeholders.

**Deliverable:** `report/forensic-report.pdf` (or `.md`) and `report/exec-summary.md`.

## Safety & Ethics
- Never send or forward samples to uninvolved third parties.
- Do not attempt to log into any credential harvesting pages; collect only HTML and static artifacts.
- When using public services for enrichment, avoid uploading PII or any sensitive corporate data.

## Grading / Assessment (suggested)
- Collection completeness & evidence handling (25%)
- Correct classification & triage rationale (20%)
- Quality of enrichment & linkage (25%)
- Clarity and usefulness of final report (30%)
