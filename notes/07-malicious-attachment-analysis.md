# 07 — Malicious Attachment Analysis: Static and Dynamic Techniques

## Objectives
- Learn the workflow to analyze suspicious attachments using static and dynamic methods.
- Identify common indicators in Office macros, PE files, scripts, and archives.
- Safely perform dynamic detonation and capture observables.

## Attachment triage steps
1. **Collect sample** and record hashes (MD5, SHA1, SHA256).
2. **Determine file type** using file headers (`file` command) rather than extension.
3. **Run quick static scans** with AV engines and YARA rules.
4. **For Office files**: extract macros with `oletools.olevba` and inspect for suspicious commands (PowerShell, Wscript, URL downloads).
5. **For executables**: inspect with `pefile`, `strings`, `routines`, check imports, digital signatures.
6. **For scripts**: look for obfuscated content (base64 blobs, long encoded strings), eval/decode functions.
7. **For archives**: handle nested archives and password-protected archives carefully — password in the email body should be treated as a TTP.

## Static analysis indicators
- Auto-execution macros (AutoOpen, Workbook_Open).
- Use of `CreateObject("WScript.Shell")`, `Shell`, `WScript.Shell.Run`, or `URLDownloadToFile`.
- Embedded URLs or IP addresses encoded in macros.
- Unusual packer signatures or overlay sections in PE files.
- Suspicious imports: `WinExec`, `CreateRemoteThread`, `VirtualAlloc`, `LoadLibrary`, etc.

## Dynamic analysis (sandbox)
- Use an instrumented sandbox with network controls and full logging (process tree, file system, registry, network).
- Capture network IOC: domains, IPs, C2 beacons, HTTP/HTTPS requests, DNS requests.
- Record system changes: persistence mechanisms (services, registry run keys), files dropped, scheduled tasks.
- Snapshot memory if available for deeper analysis (strings, injected modules).

## Safe detonation tips
- Isolate sandbox from production networks and use simulated internet (or use proxy to allow controlled outbound).
- Use different snapshots for repeated runs.
- Ensure the sandbox environment resembles likely victim environment (Office versions, Windows versions) for realistic behavior.
- Be mindful of accidental C2 connections—block or sinkhole known-malicious domains.

## Post-analysis: IOC extraction & reporting
- Extract IOCs: hashes, domains, IPs, mutexes, filenames, registry keys.
- Write a concise report: summary, indicators, TTPs, recommended mitigations.
- Create YARA rules or Snort/Suricata signatures for observed unique behaviors.

## Tools
- `oletools` (`olevba`), `mraptor`, `oledump` for macros/OLE.
- `pefile`, `die`, `r2`/radare2, `Ghidra` for PE reverse engineering.
- Dynamic sandboxes: Cuckoo, Any.Run, commercial sandboxes with good telemetry.
