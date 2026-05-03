# Traefik Host-Based Routing Demo

## Purpose

Demonstrates how to route traffic to different services using host-based routing with Traefik.

---

## Architecture

Browser → Traefik → Multiple services (based on host)

---

## Features

- Traefik reverse proxy
- Host-based routing
- Multiple services with domain-style access

---

## Run

```bash
docker compose up -d --build
```

---

## Test

```bash
curl http://service1.localhost
curl http://service2.localhost
```

---

## What I Learned

- Host-based routing
- Domain-style service separation
- Traffic routing strategies

---

## Note

Learning project – not production-ready.
