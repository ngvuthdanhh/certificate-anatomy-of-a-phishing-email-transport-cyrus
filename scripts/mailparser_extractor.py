#!/usr/bin/env python3
"""
mailparser_extractor.py
Usage: python3 mailparser_extractor.py sample.eml outdir

- Extracts full headers to headers.txt
- Saves plain and html bodies to body.txt / body.html
- Extracts attachments into outdir/attachments/
Dependencies: prefers `mailparser` (pip install mailparser) but will fall back to stdlib.
"""
import sys
import os
import hashlib

def write_hashes(path, outfh):
    with open(path,'rb') as f:
        data=f.read()
    outfh.write(f"{path},{hashlib.md5(data).hexdigest()},{hashlib.sha1(data).hexdigest()},{hashlib.sha256(data).hexdigest()}\n")

def main():
    if len(sys.argv) < 3:
        print("Usage: mailparser_extractor.py sample.eml outdir")
        sys.exit(1)
    eml = sys.argv[1]
    outdir = sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    attachments_dir = os.path.join(outdir,'attachments')
    os.makedirs(attachments_dir, exist_ok=True)

    try:
        import mailparser
        m = mailparser.parse_from_file(eml)
        # headers
        with open(os.path.join(outdir,'headers.txt'),'w',encoding='utf-8') as hf:
            for k,v in m.headers.items():
                hf.write(f"{k}: {v}\n")
        # body
        with open(os.path.join(outdir,'body.txt'),'w',encoding='utf-8') as bf:
            bf.write(m.body or "")
        if m.body_html:
            with open(os.path.join(outdir,'body.html'),'w',encoding='utf-8') as hf:
                hf.write(m.body_html)
        # attachments
        hashes_file = os.path.join(outdir,'attachment_hashes.csv')
        with open(hashes_file,'w') as hf:
            hf.write("path,md5,sha1,sha256\n")
            for att in m.attachments:
                filename = att['filename'] or f"attachment-{att['content_id'] or 'noname'}"
                path = os.path.join(attachments_dir, filename)
                with open(path,'wb') as fh:
                    fh.write(att['payload'])
                write_hashes(path, open(hashes_file,'a'))
                print(f"[+] saved attachment: {path}")
        print("[*] Done using mailparser.")
        return
    except Exception:
        pass

    # Fallback: stdlib parsing
    from email import policy
    from email.parser import BytesParser
    with open(eml,'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)
    with open(os.path.join(outdir,'headers.txt'),'w',encoding='utf-8') as hf:
        for k,v in msg.items():
            hf.write(f"{k}: {v}\n")
    # body parts
    text_parts=[]
    html_parts=[]
    for part in msg.walk():
        ctype = part.get_content_type()
        if part.get_content_disposition() == 'attachment':
            filename = part.get_filename() or 'unknown.bin'
            path = os.path.join(attachments_dir, filename)
            with open(path,'wb') as fh:
                fh.write(part.get_payload(decode=True))
            print(f"[+] saved attachment: {path}")
        elif ctype == 'text/plain':
            text_parts.append(part.get_payload(decode=True).decode(part.get_content_charset('utf-8'), errors='replace'))
        elif ctype == 'text/html':
            html_parts.append(part.get_payload(decode=True).decode(part.get_content_charset('utf-8'), errors='replace'))
    with open(os.path.join(outdir,'body.txt'),'w',encoding='utf-8') as bf:
        bf.write("\n\n".join(text_parts))
    if html_parts:
        with open(os.path.join(outdir,'body.html'),'w',encoding='utf-8') as hf:
            hf.write("\n\n".join(html_parts))
    # write hashes for attachments
    with open(os.path.join(outdir,'attachment_hashes.csv'),'w') as hf:
        hf.write("path,md5,sha1,sha256\n")
        for fname in os.listdir(attachments_dir):
            write_hashes(os.path.join(attachments_dir,fname), hf)

if __name__ == "__main__":
    main()
