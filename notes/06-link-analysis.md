# 06 — Link Analysis: Investigating URLs and Redirect Chains

## Objectives
- Understand methods to safely analyze links found in messages.
- Identify techniques attackers use to obfuscate malicious destinations.
- Use lookup tools and heuristics to triage suspicious URLs.

## Common link obfuscation techniques
- **URL shorteners**: hide final destination (bit.ly, t.co). Expand to reveal final target.
- **Redirection chains**: multiple redirects through analytics or compromised sites before landing on payload.
- **IDN homograph attacks**: internationalized domain names that visually mimic legitimate domains.
- **URL encoding / obfuscation**: long query strings, base64-encoded parameters, or hex-encoded segments.
- **Use of legitimate hosting/CDN**: attackers host payload on legitimate services (GitHub Pages, AWS S3, Google Drive).

## Safe analysis workflow
1. **Do not click links directly** in a non-isolated environment.
2. **Extract the URL** from raw source or HTML, including `href` values.
3. **Expand shortened links** using trusted expanders or via `curl -I` / `HEAD` requests from an isolated environment.
4. **Resolve DNS and IP**: lookup domain owner and ASN (whois, `whois`, `dig`, `nslookup`).
5. **Check reputation**: VirusTotal URL scan, URLhaus, PhishTank, Google Safe Browsing (prefer automated API or sandbox).
6. **Follow redirects in a controlled sandbox** that captures network traffic and final landing page content.
7. **Inspect final landing page static content**: form fields, login prompts, download triggers, obfuscated JavaScript.

## Tools & commands
- `curl -I` or `curl -L` (use in isolated environment) to follow redirects and inspect headers.
- `wget --max-redirect=0` to detect redirect chains step-by-step.
- `dig`, `host`, `whois` for DNS and registration info.
- Online services: VirusTotal, URLscan.io, Hybrid Analysis, PhishTank.
- Browser devtools in sandbox for JS analysis (network tab, scripts).

## Heuristics: When a URL is suspicious
- Domain age is recent or uses privacy-protected WHOIS.
- Domain uses unusual TLD or misspelled brand name.
- Redirect chain significantly longer than expected or uses multiple third-party services.
- Landing page prompts for credentials but the URL does not belong to expected domain.
- Use of POST forms to external domains or auto-download triggers.

## Example quick checklist
- Extract URL from email HTML.
- Expand shortener and document each redirect.
- Resolve final domain IP and check ASN.
- Submit to reputation services and scan results.
- If safe and necessary for evidence, do a sandbox visit and capture artifacts (JS, network calls, files).
