# Cloud Journey 🚀

## Project Overview

This project demonstrates how to run a static website using Nginx inside a Docker container.
It covers both development and production approaches using Docker and Docker Compose.

---

## What I Practiced

* Running containers with Docker (`docker run`, `docker ps`, `docker stop`)
* Building custom images using a Dockerfile
* Understanding the difference between image and container
* Port mapping (host → container)
* Using bind mounts for live updates (development)
* Managing services with Docker Compose
* Difference between development and production environments

---

## Project Structure

```
cloud-journey/
├── Dockerfile
├── docker-compose.devyml
├── docker-compose.prod.yml
└── nginx-site/
    └── index.html
```

---

## How to Run

### 🔹 Production (using Dockerfile)

Build and run the container:

```
docker compose -f docker-compose.prod.yml up -d --build
```

Access:
http://localhost:8080

---

### 🔹 Development (live updates with volume)

Run with bind mount:

```
docker compose -f docker-compose.dev.yml up -d
```

Access:
http://localhost:8081

Any change in `index.html` is reflected instantly without rebuilding.

---

## Key Concepts

* **Image vs Container**

  * Image is a static snapshot
  * Container is a running instance

* **Bind Mount vs COPY**

  * Bind mount → live updates (development)
  * COPY → fixed content inside image (production)

* **Docker Compose**

  * Simplifies running multi-container or repeatable setups
  * Replaces manual `docker build` and `docker run`

---

## Notes

This project is part of my cloud and DevOps learning journey.
The goal is to understand infrastructure, containerization, and deployment concepts step by step.
