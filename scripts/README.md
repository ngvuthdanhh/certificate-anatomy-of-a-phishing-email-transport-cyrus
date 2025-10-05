# scripts/ — Utility scripts for email analysis

This folder contains small utilities to support the labs and notes in this repo.

## Files
- `extract_attachments.sh` — extract attachments from a raw .eml file using `munpack`/`ripmime` or `python` fallback.
- `mailparser_extractor.py` — Python script using `mailparser` (or stdlib email) to extract headers, parts, and attachments.
- `headers_to_json.py` — convert raw email headers to a JSON object for easier parsing/enrichment.
- `expand_url.py` — safely expand shortened URLs (HEAD requests) and show redirect chain (use in isolated env).
- `generate_hashes.sh` — compute MD5/SHA1/SHA256 for every file in a folder.
- `yara_scan.py` — run YARA rules against a directory of files and produce a CSV of matches.

## Prerequisites
- Python 3.8+
- Optional Python modules: `mailparser`, `requests`, `python-magic` (install via pip)
- Utilities (optional): `ripmime`, `munpack`, `yara`, `sha256sum`, `md5sum`
- Run scripts in an isolated analysis environment when they may access the internet.

## Usage examples
- `bash extract_attachments.sh sample.eml ./out/`
- `python3 mailparser_extractor.py sample.eml ./out/`
- `python3 expand_url.py "http://bit.ly/xyz"`
- `bash generate_hashes.sh ./out/ > hashes.csv`
- `python3 yara_scan.py rules.yar ./attachments/ matches.csv`

Keep scripts read-only or executable as needed: `chmod +x scripts/*.sh`  
