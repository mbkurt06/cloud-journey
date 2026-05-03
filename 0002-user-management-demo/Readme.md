# User Management Demo

## Purpose

Demonstrates a basic backend service for managing users with simple CRUD operations.

---

## Architecture

Browser → Backend API

---

## Features
ll
- User creation
- Basic API endpoints
- Simple data handling
- Backend service structure

---

## Run

```bash
docker compose up -d --build
```

---

## Test

Create user:

```bash
curl -X POST http://localhost/users \
  -H "Content-Type: application/json" \
  -d '{"name":"test","email":"test@test.com"}'
```

---

## What I Learned

- API design basics
- CRUD operations
- Backend structure
- Request handling

---

## Note

Learning project – not production-ready.
