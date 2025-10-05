#!/usr/bin/env bash
# extract_attachments.sh
# Usage: ./extract_attachments.sh sample.eml output_dir
# Requires: ripmime or munpack (optional). Falls back to python email module if neither installed.

set -euo pipefail

EML="$1"
OUTDIR="${2:-./extracted}"
mkdir -p "$OUTDIR"

command -v ripmime >/dev/null 2>&1
if [ $? -eq 0 ]; then
  echo "[*] Using ripmime to extract attachments..."
  ripmime -i "$EML" -d "$OUTDIR"
  exit 0
fi

command -v munpack >/dev/null 2>&1
if [ $? -eq 0 ]; then
  echo "[*] Using munpack to extract attachments..."
  (cd "$OUTDIR" && munpack -t "$EML")
  exit 0
fi

# Fallback: use python to extract attachments (no external deps)
echo "[*] ripmime/munpack not found — using python fallback."
python3 - <<PY
import sys, os
from email import policy
from email.parser import BytesParser

eml = "$EML"
out = "$OUTDIR"
with open(eml,'rb') as f:
    msg = BytesParser(policy=policy.default).parse(f)

count = 0
for part in msg.iter_attachments():
    filename = part.get_filename()
    if not filename:
        filename = f'part-{count}.bin'
    path = os.path.join(out, filename)
    with open(path, 'wb') as fh:
        fh.write(part.get_payload(decode=True))
    print(f"[+] extracted: {path}")
    count += 1

if count == 0:
    print("[!] No attachments found.")
PY
