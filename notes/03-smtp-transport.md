# 03 — SMTP Transport: How Email Moves and Where Attacks Happen

## Objectives
- Understand SMTP basics and the roles of MTA/MDA/MUA.
- Learn typical SMTP session flow and important SMTP commands.
- Identify common weak points and misconfigurations abused by attackers.

## SMTP basics
- SMTP (Simple Mail Transfer Protocol) is the protocol used to transfer mail between MTAs using port 25 (submission may use 587, 465 for SMTPS submission).
- Primary actors:
  - **MUA**: client that submits email (submits to an SMTP submission endpoint).
  - **MTA**: relays and routes messages across networks.
  - **MDA**: final delivery to mailbox storage.

## Typical SMTP session
1. TCP handshake to SMTP port.
2. `EHLO <client>` — extended hello, server advertises supported capabilities (STARTTLS, SIZE, AUTH, etc).
3. `MAIL FROM:<sender>` — envelope sender (used for bounce).
4. `RCPT TO:<recipient>` — recipient address(es).
5. `DATA` — begins message content (headers + body), terminated with a single `.` line.
6. Server responds with status codes (250, 354, 550, etc).
7. `QUIT` ends session.

## Important SMTP extensions & behavior
- **START**
