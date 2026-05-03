# Traefik HTTPS Demo

## Purpose

This project demonstrates how to use Traefik as an HTTPS reverse proxy in a containerized environment.

The project covers:

- HTTPS entrypoint
- TLS termination
- HTTP to HTTPS redirect
- Frontend HTTPS routing
- Backend HTTPS routing
- Local self-signed TLS behavior

---

## Architecture

```bash
Browser
  |
  | https://secure.localhost
  v
Traefik :443
  |
  v
Frontend Nginx Container


Browser / curl
  |
  | https://api.secure.localhost
  v
Traefik :443
  |
  v
Backend FastAPI Container
```

---

## Project Structure

```bash
traefik-https-demo/
├── docker-compose.yml
├── traefik/
│   ├── traefik.yml
│   ├── dynamic.yml
│   └── acme.json
├── frontend/
│   └── index.html
└── backend/
    ├── Dockerfile
    ├── requirements.txt
    └── app.py
```

---

## Services

### Traefik

Traefik is the single entry point for HTTP and HTTPS traffic.

It listens on:

- Port 80 for HTTP
- Port 443 for HTTPS
- Port 8080 for the Traefik dashboard

### Frontend

The frontend is served by an Nginx container.

Route:

```bash
https://secure.localhost
```

### Backend API

The backend is a FastAPI application.

Routes:

```bash
https://api.secure.localhost/
https://api.secure.localhost/health
```

---

## HTTPS Behavior

HTTP traffic is automatically redirected to HTTPS.

Example:

```bash
curl -I http://secure.localhost
```

Expected result:

```bash
HTTP/1.1 308 Permanent Redirect
Location: https://secure.localhost/
```

---

## Run the Project

```bash
docker compose down --remove-orphans
docker compose up -d --build
```

---

## Test Frontend

Open in browser:

```bash
https://secure.localhost
```

Because this is a local self-signed TLS setup, the browser may show a certificate warning.

---

## Test Backend API

```bash
curl -k https://api.secure.localhost/
curl -k https://api.secure.localhost/health
```

Expected output:

```json
{"message":"HTTPS Backend API is running","instance":"container-hostname"}
{"status":"ok","service":"https-backend-api"}
```

The `-k` option is used because the local certificate is self-signed.

---

## Traefik Dashboard

```bash
http://localhost:8080/dashboard/
```

You can inspect:

- Routers
- Services
- Middlewares
- TLS-enabled routes

---

## Key Concepts Learned

- HTTPS reverse proxy
- TLS termination
- HTTP to HTTPS redirect
- Traefik secure entrypoint
- Frontend and backend HTTPS routing
- Local self-signed certificate behavior
- Difference between local TLS and production Let’s Encrypt certificates

---

## Important Note

This project uses local HTTPS behavior.

For production, a real domain and a certificate resolver such as Let’s Encrypt should be used.

Example production concepts:

- ACME
- Let’s Encrypt
- DNS challenge
- HTTP challenge
- Certificate storage with `acme.json`

---

## Conclusion

This project demonstrates how Traefik can terminate HTTPS traffic and securely route requests to frontend and backend services.

It is a foundation for production-ready routing, cloud deployment, and Kubernetes ingress concepts.