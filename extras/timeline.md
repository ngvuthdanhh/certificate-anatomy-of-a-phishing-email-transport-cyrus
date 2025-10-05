# Course Timeline — Suggested Schedule & Milestones

This timeline maps the syllabus to practical milestones and deliverables for a 6-week instructor-led course or a self-study plan.

---

## Week 0 — Preparation (Optional)
- Setup lab environment (isolated VMs, mail server testbed, sandbox).
- Install tools: `oletools`, `ripmime`, Python packages, YARA.
- Read `docs/index.md` and `docs/roadmap.md`.

## Week 1 — Foundations & Overview
- Finish `notes/01-overview.md`.
- Deliverable: Collect and submit one benign `.eml` example with annotated headers.

## Week 2 — Headers & Transport
- Finish `notes/02-email-headers.md` and `notes/03-smtp-transport.md`.
- Lab: extract and analyze three real-world headers; map Received chains and authentication results.
- Deliverable: short report describing how you traced the origin for one sample.

## Week 3 — MIME, Attachments, Spoofing
- Finish `notes/04-mime-and-attachments.md` and `notes/05-spoofing-and-phishing-techniques.md`.
- Lab: extract attachments, run static macro extraction on a sample.
- Deliverable: IOC list (hashes, suspicious strings) and remediation suggestions.

## Week 4 — Link & Payload Analysis
- Finish `notes/06-link-analysis.md` and `notes/07-malicious-attachment-analysis.md`.
- Lab: expand shortened URLs, follow redirect chains in sandbox, detonate one attachment safely.
- Deliverable: sandbox report summary and YARA rule prototype for observed patterns.

## Week 5 — OPSEC, Campaigns & Tools
- Finish `notes/08-opsec-and-attribution.md` and begin `notes/11-phishing-campaign-analysis.md` & `notes/12-analysis-tools.md`.
- Lab: perform passive DNS enrichment and build a small campaign timeline from sample IOCs.
- Deliverable: campaign timeline (who, what, how, when) and recommended detection rules.

## Week 6 — Defense, Legal & Reporting
- Complete remaining notes (`09`, `10`, `13`, `14`, `15`) and labs.
- Final assignment: end-to-end forensic analysis of one phishing campaign (raw `.eml` + attachments + links), mitigation playbook, and a one-page executive summary.
- Deliverable: final forensic report (technical appendix + mitigation checklist).

---

## Continuous Activities
- Maintain a living `extras/case-studies.md` with new campaigns and lessons.
- Keep YARA rules and detection signatures in a versioned folder.
- Regularly update `docs/references.md` with newly published vendor reports.

---

## Suggested assessment rubric (brief)
- **Technical accuracy (40%)** — header analysis, IOC extraction, sandbox evidence.
- **Process & OPSEC (20%)** — proper evidence handling and safe analysis.
- **Mitigation quality (20%)** — practical and prioritized controls.
- **Clarity & reporting (20%)** — readable report for technical and non-technical stakeholders.
