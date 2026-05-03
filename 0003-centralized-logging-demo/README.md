# Centralized Logging Demo

## Purpose

Demonstrates how to collect and centralize logs from multiple services using a logging pipeline.

---

## Architecture

Services → Promtail → Loki → Grafana

---

## Features

- Centralized log collection
- Log aggregation with Loki
- Log visualization with Grafana
- Multi-service logging

---

## Run

```bash
docker compose up -d --build
```

---

## Access

Grafana:

```text
http://localhost
