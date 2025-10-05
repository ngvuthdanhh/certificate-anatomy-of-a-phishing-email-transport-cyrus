#!/usr/bin/env python3
"""
expand_url.py
Usage: python3 expand_url.py "http://short.url/abc"
Performs HEAD requests to follow redirects and prints each redirect step.
Run only in isolated or researcher environment.
"""
import sys
import requests

if len(sys.argv) < 2:
    print("Usage: expand_url.py URL")
    sys.exit(1)

url = sys.argv[1]
session = requests.Session()
session.max_redirects = 10

try:
    resp = session.head(url, allow_redirects=True, timeout=15)
    chain = resp.history + [resp]
    for r in chain:
        print(f"{r.status_code} -> {r.url}")
    print("\nFinal URL:", resp.url)
except requests.exceptions.RequestException as e:
    print("[!] Request error:", e)
