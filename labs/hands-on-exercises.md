# Hands-on Exercises

## Overview
Short, focused exercises that reinforce the concepts and tool usage from the course. Each exercise is designed to be completed in 30–90 minutes.

---

## Exercise A — Header Detective (30–45 minutes)
**Goal:** Find the true origin of a suspicious `.eml`.

**Steps**
1. Open `sample-header.eml` and extract full headers.
2. Read Received headers bottom-up and identify the earliest client IP and hostname.
3. Check SPF/DKIM/DMARC results and note alignment.
4. Lookup the earliest IP in `whois`/`dig` to find ASN and likely provider.

**Deliverable:** `exercise-A-answer.md` with origin IP, ASN, auth results, and a 3-line justification.

---

## Exercise B — Macro Static Triage (45–60 minutes)
**Goal:** Identify if a Word document contains suspicious macros and extract likely download URLs.

**Steps**
1. Use `olevba` to analyze `invoice.docm`.
2. Extract macro strings and search for suspicious functions (`CreateObject`, `Shell`, `powershell`).
3. If macros contain encoded blobs, decode common encodings (base64/hex) and search for URLs.

**Deliverable:** `exercise-B-iocs.md` with macros summary, suspected URLs, and recommended next steps.

---

## Exercise C — Link Expansion & Reputation (45–60 minutes)
**Goal:** Expand a shortened URL safely and determine if it is malicious.

**Steps**
1. Extract the shortened link from `link-sample.eml`.
2. Using an isolated VM or a safe HTTP client, perform a `HEAD` request following redirects and document each redirect step.
   - Example: `curl -I -L --max-redirs 10 'http://short.url/abc'`
3. Check the final domain's WHOIS and age, and run a reputation lookup through a local script or offline dataset.

**Deliverable:** `exercise-C-redirects.md` with full redirect chain, final landing page snapshot (HTML saved), and reputation notes.

---

## Exercise D — Build-a-YARA (60–90 minutes)
**Goal:** Write a YARA rule for a pattern observed in lab samples.

**Steps**
1. Analyze three malicious attachments and identify a common string or byte pattern.
2. Draft a YARA rule (with metadata, strings, and condition) that detects the pattern but minimizes false positives.
3. Test the rule against a small sample set (malicious + benign examples) and record results.

**Deliverable:** `exercise-D-yara.yar` and `exercise-D-results.md` with true/false positives counts.

---

## Exercise E — Executive Brief (30 minutes)
**Goal:** Convert technical findings into a one-page executive summary.

**Steps**
1. Take one lab incident and write a non-technical one-page brief including:
   - What happened (one paragraph)
   - Who was affected (one line)
   - Business impact (one paragraph)
   - Actions taken and recommended next steps (bullet list)

**Deliverable:** `exercise-E-executive.md`

---

## Hints & Safety
- Use copies of files for analysis and never alter originals.
- For any network activity, use an isolated environment with no link to production.
- If unsure about a step that might reach the internet, document the intended command and skip real execution.

## Optional: Instructor materials
- Provide sample `.eml` and attachments with varied techniques (macro, credential phishing link, BEC-style email).
- Provide a rubric for each exercise mapping expected outputs to grades.
