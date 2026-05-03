

# Traefik Routing Demo

## Purpose

This project demonstrates how to use Traefik in a container-based environment to implement:

- Reverse proxy
- Path-based routing
- Load balancing
- Docker service discovery

---

## Architecture

```
Client (Browser / curl)
        │
        ▼
     Traefik
        │
        ├── service1 (nginx)
        └── service2 (nginx)
```

---

## How It Works

Traefik acts as the single entry point for all incoming traffic.

Routing rules:

```
/service1 → service1 container
/service2 → service2 container
```

If multiple containers exist for the same service, Traefik automatically performs load balancing.

---

## Project Structure

```
traefik-routing-demo/
├── docker-compose.yml
├── service1/
│   └── index.html
└── service2/
    └── index.html
```

---

## Docker Compose Overview

Traefik is configured as a reverse proxy using Docker provider.

Key configurations:

```
--providers.docker=true
→ Enables Docker service discovery

--providers.docker.exposedbydefault=false
→ Only containers with labels are exposed

--providers.docker.network=traefik-net
→ Ensures correct network communication
```

---

## Routing Configuration

### Service 1

```
traefik.http.routers.service1.rule=PathPrefix(`/service1`)
```

### Service 2

```
traefik.http.routers.service2.rule=PathPrefix(`/service2`)
```

---

## Middleware (StripPrefix)

Incoming request:

```
/service1
```

Forwarded to backend as:

```
/
```

This avoids the need for path rewriting inside nginx.

---

## Run the Project

```bash
docker compose down --remove-orphans
docker compose up -d --force-recreate
```

---

## Testing

```bash
curl http://localhost/service1
curl http://localhost/service2
```

Expected output:

```
Service 1
Service 2
```

---

## Traefik Dashboard

```
http://localhost:8080/dashboard/
```

You can inspect:

- Routers
- Services
- Middlewares

---

## Important Note (macOS)

When using Docker Desktop on macOS, the Docker socket path is:

```
/Users/mb/.docker/run/docker.sock
```

It must be mounted into the Traefik container:

```
/Users/mb/.docker/run/docker.sock:/var/run/docker.sock
```

---

## Concepts Covered

- Traefik reverse proxy
- Docker provider
- Dynamic routing
- Path-based routing
- Middleware (StripPrefix)
- Container networking
- Service discovery
- Basic load balancing

---

## Traefik vs Nginx

| Feature | Traefik | Nginx |
|--------|--------|------|
| Dynamic config | ✔ | ❌ |
| Docker integration | ✔ | ❌ |
| Load balancing | ✔ | ✔ |
| Config complexity | Low | Medium |

---

## Next Steps

- Host-based routing
- Load balancing with multiple replicas
- HTTPS (Let's Encrypt)
- Rate limiting
- Kubernetes Ingress / Gateway API