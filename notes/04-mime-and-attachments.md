# 04 — MIME and Attachments: Structure and Common Threats

## Objectives
- Understand MIME structure and common content types.
- Identify risky attachment types and common obfuscation techniques.
- Learn safe methods to extract and analyze attachments.

## MIME basics
- **MIME (Multipurpose Internet Mail Extensions)** defines how messages with multiple parts and attachments are encoded.
- Common `Content-Type` values:
  - `text/plain`, `text/html`
  - `multipart/alternative` (plain + HTML)
  - `multipart/mixed` (attachments + body)
  - `application/octet-stream`, `application/pdf`, `application/msword`, `application/vnd.openxmlformats-officedocument.*`
- `Content-Transfer-Encoding`: `7bit`, `8bit`, `base64`, `quoted-printable` — determine decoding steps.

## Dangerous attachment types
- Office documents with macros (`.doc`, `.docm`, `.xls`, `.xlsm`) — macros remain a top vector.
- Executables (`.exe`, `.bat`, `.scr`) and compressed executables (`.zip`, `.7z`) possibly nested.
- Scripts (`.js`, `.vbs`, `.ps1`) that can run on host systems.
- PDF with embedded JavaScript or malformed structures.
- Archive formats with double extensions or nested archives to hide payload.

## Evasion & obfuscation techniques
- **Double extension** (e.g., `invoice.pdf.exe`) to trick human readers.
- **Password-protected archives** — attackers supply password in email to bypass some scanners.
- **Encoded or embedded payloads** — base64 blobs, steganography, or embedding malicious content in macros.
- **File type mismatches** — content claims one type while header indicates another; e.g., `image/png` with executable content.

## Safe extraction & analysis workflow
1. Save the raw MIME and attachments in a controlled environment.
2. Compute file hashes (MD5, SHA1, SHA256).
3. Use `ripmime`, `munpack`, or `python` `email` libraries to extract attachments.
4. For office macros: use `oletools` (`olevba`) to extract and analyze VBA macros.
5. For PE files: use `pefile`, `strings`, `exiftool` for metadata, and static scanners.
6. For dynamic behavior: run in an instrumented sandbox (e.g., Any.Run, Cuckoo Sandbox) with network controls and capture system calls.
7. Document all findings and preserve original sample.

## Detection & rules
- YARA rules for common macro patterns or embedded payload markers.
- Static scanning for suspicious indicators: auto-exec macros, obfuscated VBA, shell commands, suspicious URLs in macros.
- Gateway-level scanning: disallow risky attachment types or require sandbox detonation before delivery.

## Checklist
- Extract and save attachments separately.
- Record file hashes and file metadata.
- Scan static signatures and run sandbox analysis if safe.
- Inspect macros and scripts for suspicious strings (download URLs, encoded payloads, PowerShell commands).
