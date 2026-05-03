# Traefik Auth Demo

## Purpose

JWT-based authentication and authorization with Traefik, FastAPI, and a simple frontend.

---

## Architecture

Browser → Traefik → Frontend / Backend

Flow:

User → Login → JWT → Protected API

---

## Features

- Traefik reverse proxy routing
- FastAPI backend
- JWT token generation
- Protected API endpoint
- Bearer token authentication

---

## Run

```bash
docker compose up -d --build
```

---

## Test

Login:

```bash
curl -X POST http://api.auth.localhost/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}'
```

Protected:

```bash
curl http://api.auth.localhost/protected \
  -H "Authorization: Bearer <TOKEN>"
```

---

## What I Learned

- JWT authentication flow
- Stateless auth
- API protection
- Reverse proxy routing with Traefik

---

## Note

Learning project – not production-ready.
