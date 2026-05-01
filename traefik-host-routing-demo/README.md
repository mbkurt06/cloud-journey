# Traefik Host-Based Routing Demo

## Purpose

This project demonstrates a production-like routing architecture using Traefik, Nginx frontend, and FastAPI backend containers.

The main goals are:

- Host-based routing
- Frontend and backend separation
- Traefik Docker provider usage
- Backend API routing
- CORS handling
- Backend scaling with multiple replicas
- Traefik load balancing

---

## Architecture

```bash
Browser
  |
  | app.localhost
  v
Traefik
  |
  v
Frontend Nginx Container


Browser
  |
  | api.localhost
  v
Traefik
  |
  v
Backend API Containers
```

---

## Project Structure

```bash
traefik-host-routing-demo/
├── docker-compose.yml
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

Traefik is the public entry point of the system.

It routes traffic based on the requested hostname:

- app.localhost → frontend
- api.localhost → backend API

### Frontend

The frontend is served by an Nginx container.

It contains a simple user registration form that sends requests to the backend API.

### Backend API

The backend is a FastAPI application.

It exposes:

- GET /
- POST /users

The backend response includes:

- service name
- container instance hostname

This makes load balancing visible during testing.

---

## Routing Rules

### Frontend Route

```yaml
traefik.http.routers.frontend.rule=Host(`app.localhost`)
```

### Backend Route

```yaml
traefik.http.routers.backend-api.rule=Host(`api.localhost`)
```

---

## Docker Socket Note for macOS

On Docker Desktop for macOS, the Docker socket path is:

```bash
/Users/mb/.docker/run/docker.sock
```

It is mounted into the Traefik container as:

```yaml
/Users/mb/.docker/run/docker.sock:/var/run/docker.sock:ro
```

This allows Traefik to read Docker containers and labels.

---

## Run the Project

```bash
docker compose down --remove-orphans
docker compose up -d --build
```

---

## Run with Backend Scaling

```bash
docker compose up -d --build --scale backend_api=2
```

When scaling a service with Docker Compose, do not use a fixed container_name for that service.

---

## Test Frontend

Open in browser:

```bash
http://app.localhost
```

Submit the form.

Expected response:

```json
{
  "message": "User created successfully",
  "service": "backend-api",
  "instance": "container-hostname"
}
```

---

## Test Backend Directly

```bash
curl http://api.localhost/
```

---

## Test Load Balancing

```bash
for i in {1..10}; do curl -s http://api.localhost/; echo; done
```

Expected result:

The instance value should alternate between backend containers.

Example:

```json
{"message":"Backend API is running","service":"backend-api","instance":"backend-container-1"}
{"message":"Backend API is running","service":"backend-api","instance":"backend-container-2"}
```

---

## Traefik Dashboard

Open:

```bash
http://localhost:8080/dashboard/
```

You can inspect:

- routers
- services
- middlewares
- backend targets

---

## Key Concepts Learned

- Traefik as a reverse proxy
- Host-based routing
- Docker provider
- Docker labels
- Frontend/backend separation
- CORS handling
- Backend scaling
- Load balancing between backend replicas
- Why fixed container_name should not be used for scalable services

---

## Compose vs Swarm vs Kubernetes

Docker Compose scaling:

```bash
docker compose up -d --scale backend_api=2
```

Docker Swarm uses:

```yaml
deploy:
  replicas: 2
```

Kubernetes uses:

```yaml
replicas: 2
```

Summary:

- Docker Compose → local multi-container development
- Docker Swarm → Docker-native orchestration
- Kubernetes → industry-standard orchestration

---

## Conclusion

This project shows how a modern container-based routing architecture works.

Traefik handles public traffic, routes requests by hostname, and load balances backend API replicas automatically.

This is a small but realistic foundation for cloud infrastructure, DevOps, and Kubernetes networking concepts.