# User Management Demo (Docker + Nginx + Load Balancing)

## Demo

This project simulates a real-world backend architecture with load balancing using Docker and Nginx.

---

## Project Overview

This project demonstrates a real-world web architecture using Docker.

It includes:

* Nginx as a reverse proxy and load balancer
* Two backend API instances
* PostgreSQL database
* A simple frontend (HTML + JavaScript)

The goal is to simulate how modern applications handle traffic, routing, and scaling.

---

## Architecture

The following diagram shows how requests flow through the system:

```
Browser
   │
   ▼
Nginx (Reverse Proxy + Load Balancer)
   │
   ├── backend-1 (API)
   └── backend-2 (API)
         │
         ▼
     PostgreSQL
```

---

## Features

* Create user
* Sign in
* Get user information
* Delete user
* Load balancing between multiple backend instances
* Single entry point via Nginx

---

## API Endpoints

The backend exposes the following REST endpoints:

```
POST   /api/v1/users
POST   /api/v1/auth/signin
GET    /api/v1/users/me?email=...
DELETE /api/v1/users/me?email=...
```

---

## Technologies Used

* Docker & Docker Compose
* Nginx (reverse proxy & load balancing)
* FastAPI (Python backend)
* PostgreSQL
* HTML + JavaScript (frontend)

---

## Key Concepts Demonstrated

* Container-based architecture
* Reverse proxy pattern
* Load balancing (multiple backend instances)
* Service-to-service communication via Docker network
* Health checks and service readiness

---

## Load Balancing Behavior

Each backend response includes:

```json
{
  "served_by": "backend-1"
}
```

or

```json
{
  "served_by": "backend-2"
}
```

This allows observing how traffic is distributed across instances.

---

## Important Notes

### Database ID Behavior

User IDs may not be sequential (e.g., 1 → 3).
This is expected due to PostgreSQL sequence behavior and failed insert attempts.

---

### Internal Networking

Backend services are not exposed externally.

All traffic flows through Nginx:

```
Frontend → Nginx → Backend → Database
```

---

## How to Run

```bash
docker compose up -d --build
```

Open in browser:

```
http://localhost:8080
```

---

## Learning Goals

* Understanding container communication
* Implementing reverse proxy routing
* Observing load balancing in practice
* Connecting backend services to a database

---

## Next Steps

Planned improvements to extend this project:

* Centralized logging (Loki / ELK)
* Authentication (JWT)
* HTTPS setup (TLS)
* Kubernetes deployment (container orchestration)
