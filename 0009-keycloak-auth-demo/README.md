# 0009-keycloak-auth-demo

Production-like authentication & authorization demo using Keycloak, FastAPI, Traefik, PostgreSQL, Prometheus, Grafana, Loki and Docker Compose.

## Project Goal

The purpose of this project is to understand how modern authentication systems work in containerized environments.

This demo includes:

- Identity Provider (Keycloak)
- JWT Authentication
- Protected API endpoints
- Reverse proxy routing with Traefik
- PostgreSQL persistence
- Monitoring with Prometheus & Grafana
- Centralized logging with Loki & Promtail

---

## Architecture

```text
User
 ↓
Traefik Reverse Proxy
 ↓
Keycloak Authentication
 ↓
JWT Token
 ↓
FastAPI Backend API
 ↓
Protected Endpoints
```

Monitoring & Logging:

```text
Backend API
 ├── Prometheus (/metrics)
 ├── Grafana Dashboards
 └── Loki Logs
```

---

## Technologies

- Keycloak
- FastAPI
- PostgreSQL
- Docker Compose
- Traefik
- Prometheus
- Grafana
- Loki
- Promtail

---

## Features

### Authentication
- JWT-based authentication
- Keycloak Identity Provider
- Protected API endpoints
- Token validation

### Monitoring
- Prometheus metrics collection
- Grafana dashboards
- FastAPI `/metrics` endpoint

### Logging
- Centralized container logging
- Loki log aggregation
- Promtail log collection

### Persistence
- PostgreSQL persistent storage
- Data survives `docker compose down`

---

## Project Structure

```text
0009-keycloak-auth-demo/
│── backend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
│── frontend/
│
│── prometheus/
│   └── prometheus.yml
│
│── grafana/
│
│── loki/
│
│── promtail/
│
│── docker-compose.yml
│── README.md
```

---

## Run Project

### Start project

```bash
docker compose up -d --build
```

### Check containers

```bash
docker ps
```

### Get JWT token

```bash
TOKEN=$(curl -s -X POST "http://keycloak.localhost/realms/cloud-journey/protocol/openid-connect/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=backend-api" \
  -d "username=testuser" \
  -d "password=test123" \
  -d "grant_type=password" | jq -r '.access_token')
```

### Test protected endpoint

```bash
curl http://api.auth.localhost/protected \
  -H "Authorization: Bearer $TOKEN"
```

Expected response:

```json
{
  "message": "Protected endpoint",
  "user": "testuser"
}
```

---

## Monitoring URLs

```text
Traefik Dashboard:
http://localhost:8080

Grafana:
http://localhost:3000

Prometheus:
http://localhost:9090

Keycloak:
http://keycloak.localhost
```

---

## Validation Tests

### Backend Health Check

```bash
curl http://api.auth.localhost/
```

Expected:

```json
{
  "message": "Backend API is running"
}
```

### Unauthorized Access Test

```bash
curl http://api.auth.localhost/protected
```

Expected:

```json
{
  "detail": "Not authenticated"
}
```

### Authorized Access Test

```bash
curl http://api.auth.localhost/protected \
  -H "Authorization: Bearer $TOKEN"
```

Expected:

```json
{
  "message": "Protected endpoint",
  "user": "testuser"
}
```

### Metrics Test

```bash
curl http://api.auth.localhost/metrics | head
```

Expected:

```text
# HELP python_gc_objects_collected_total
# TYPE python_gc_objects_collected_total counter
```

### Logging Test

Generate traffic:

```bash
curl http://api.auth.localhost/
curl http://api.auth.localhost/protected
```

Open:

```text
Grafana → Explore → Loki
```

Query example:

```logql
{job="containerlogs"}
```

Expected:
- Backend logs visible
- `/metrics`
- `/protected`
- HTTP status codes

---

## Learning Outcomes

This project helped practice:

- Identity & Access Management (IAM)
- Authentication vs Authorization
- JWT flow
- Reverse proxy integration
- Monitoring & observability
- Centralized logging
- Secure API architecture
- Production-like container architecture

---

## Next Project

```text
0010-keycloak-rbac-demo
```

Goal:

- Role-Based Access Control (RBAC)
- Admin / Developer / Viewer roles
- Role-protected endpoints
- Authorization concepts