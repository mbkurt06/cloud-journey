# Cloud Journey

## Purpose

This repository documents my structured journey into Cloud, DevOps, and Security.

The goal is to learn by building real, hands-on projects that reflect production-like environments.

---

## Approach

- Learn by building real systems
- Focus on practical, production-relevant setups
- Keep projects simple but meaningful
- Progress step by step with a structured roadmap

---

## Project List

### 0001 – Static Website with Nginx
- Containerized static site
- Basic Docker usage

### 0002 – User Management API
- Basic CRUD operations
- Backend service structure

### 0003 – Centralized Logging
- Log aggregation with Loki
- Log collection with Promtail
- Visualization via Grafana

### 0004 – Monitoring (Prometheus & Grafana)
- Metrics collection
- Service monitoring
- Dashboard visualization

### 0005 – Traefik Routing (Path-based)
- Reverse proxy setup
- Path-based routing
- Multiple services behind one entrypoint

### 0006 – Traefik Routing (Host-based)
- Domain-based routing
- Service separation using hostnames

### 0007 – HTTPS with Traefik
- TLS termination
- HTTP → HTTPS redirection
- Secure traffic handling

### 0008 – Authentication (JWT)
- Login flow
- JWT token generation
- Protected API endpoints
- Bearer token authorization

---

## Technologies Used

- Docker / Docker Compose
- Traefik
- Nginx
- FastAPI
- Prometheus
- Grafana
- Loki / Promtail

---

## What I’m Learning

- Networking fundamentals
- Reverse proxy and traffic routing
- Containerization
- API design
- Authentication and security basics
- Observability (monitoring & logging)

---

## Next Steps

- External authentication providers (Keycloak)
- Rate limiting and API protection
- CI/CD pipelines
- Kubernetes

---

## Notes

This repository focuses on learning through practical implementation.

Each project is intentionally simple but designed to reflect real-world concepts.

---

## Conclusion

This repository represents a structured path toward becoming a Cloud / DevOps Engineer with strong security fundamentals through hands-on experience.  -H "Content-Type: application/json" \
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

## Why It Matters

Authentication is a core part of modern applications.

In real-world systems, this is usually handled by external identity providers such as Keycloak or Auth0.

---

## Note

Learning project – not production-ready.
