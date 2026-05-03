# Traefik HTTPS Demo

## Purpose

Demonstrates HTTPS setup using Traefik with TLS termination and automatic HTTP to HTTPS redirection.

---

## Architecture

Browser → Traefik (HTTPS) → Frontend / Backend

---

## Features

- HTTPS with Traefik
- TLS termination
- HTTP → HTTPS redirect
- Secure routing

---

## Run

```bash
docker compose up -d --build
```

---

## Test

```bash
curl -I http://secure.localhost
```

Expected:

308 Permanent Redirect → HTTPS

---

## What I Learned

- TLS basics
- HTTPS setup with Traefik
- Secure traffic routing

---

## Why It Matters

HTTPS ensures secure communication and is mandatory for production systems.

---

## Note

Learning project – not production-ready.
