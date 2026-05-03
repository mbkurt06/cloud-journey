# Docker Nginx Static Site

## Purpose

Demonstrates how to serve a static website using Nginx inside a Docker container.

---

## Architecture

Browser → Nginx container → Static HTML files

---

## Project Structure

0001-docker-nginx-static-site/
├── docker-compose.yml
├── README.md
└── nginx-site/
    └── index.html

---

## Run

docker compose up -d

---

## Access

http://localhost:8080

---

## What I Learned

- Basic Docker Compose usage
- Running Nginx in a container
- Serving static files with bind mounts
- Mapping host ports to container ports

---

## Note

Learning project – not production-ready.
