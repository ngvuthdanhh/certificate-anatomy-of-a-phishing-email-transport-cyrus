#!/usr/bin/env python3
"""
headers_to_json.py
Usage: python3 headers_to_json.py headers.txt headers.json
Converts raw headers (as plain text) into a JSON mapping of header -> list(values)
"""
import sys, json
if len(sys.argv) < 3:
    print("Usage: headers_to_json.py headers.txt headers.json")
    sys.exit(1)

infile = sys.argv[1]
outfile = sys.argv[2]
headers = {}
with open(infile, 'r', encoding='utf-8') as f:
    key=None
    for line in f:
        line=line.rstrip('\n')
        if not line:
            continue
        if line[0].isspace() and key:
            # continuation
            headers[key][-1] += ' ' + line.strip()
        else:
            if ':' in line:
                k,v = line.split(':',1)
                key=k.strip()
                val=v.strip()
                headers.setdefault(key,[]).append(val)
            else:
                # malformed line - append to last header if exists
                if key:
                    headers[key][-1] += ' ' + line.strip()

with open(outfile,'w',encoding='utf-8') as out:
    json.dump(headers,out,indent=2)
print(f"[+] written {outfile}")
