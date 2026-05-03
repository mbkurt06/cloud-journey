# Traefik Routing Demo

## Purpose

Demonstrates how to route traffic to multiple services using Traefik with path-based routing.

---

## Architecture

Browser → Traefik → Multiple backend services

---

## Features

- Traefik reverse proxy
- Path-based routing
- Multiple services behind a single entrypoint

---

## Run

```bash
docker compose up -d --build
```

---

## Test

```bash
curl http://localhost/service1
curl http://localhost/service2
```

---

## What I Learned

- Reverse proxy fundamentals
- Path-based routing
- Service exposure via Traefik

---

## Note

Learning project – not production-ready.
