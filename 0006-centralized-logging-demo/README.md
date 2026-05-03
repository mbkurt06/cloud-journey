# Centralized Logging Demo (Loki + Promtail + Grafana)

## Project Overview

This project demonstrates a centralized logging architecture using Docker. It includes Nginx as a reverse proxy, a FastAPI backend service, Promtail for log collection, Loki for log storage, and Grafana for visualization. The goal is to show how logs are generated, collected, stored, and queried in a real-world system.

---

## Architecture

Browser / curl
   │
   ▼
Nginx (Reverse Proxy)
   │
   ▼
Backend (FastAPI)
   │
   ▼
Container Logs (stdout)
   │
   ▼
Promtail (Log Collector)
   │
   ▼
Loki (Log Storage)
   │
   ▼
Grafana (Visualization UI)

---

## Features

- Centralized log collection  
- Aggregation of multiple container logs  
- Real-time log querying via Grafana  
- Separation of infrastructure logs and application logs  
- Label-based log filtering  

---

## Services

- Nginx → Handles incoming HTTP requests  
- Backend → FastAPI service generating application logs  
- Promtail → Collects logs from Docker containers  
- Loki → Stores logs  
- Grafana → Provides UI for log exploration  

---

## How to Run

docker compose up -d --build

---

## Access Points

- Application → http://localhost:8080  
- Grafana → http://localhost:3000  
- Loki API → http://localhost:3100  

---

## Grafana Setup

1. Open Grafana: http://localhost:3000  
2. Login:
   - username: admin  
   - password: admin  
3. Add Data Source:
   - Type: Loki  
   - URL: http://loggingdemo_loki:3100  
4. Go to Explore to query logs  

---

## Example Queries (LogQL)

Backend logs:
{container_name="loggingdemo-backend-service"}

Nginx logs:
{container_name="loggingdemo-nginx-gateway"}

---

## Log Types

Access Logs (Uvicorn):
GET /api/v1/log-demo HTTP/1.1 200 OK

Application Logs:
service=backend-logging-service message=Log demo endpoint was called

---

## Key Concepts Demonstrated

- Centralized logging  
- Container log aggregation  
- Label-based filtering (LogQL)  
- Separation of infrastructure and application logs  
- Real-time log analysis  

---

## Notes

- Logs are collected from container stdout  
- Promtail uses Docker socket for auto-discovery  
- Loki uses label-based indexing (not full-text indexing)  

---

## Next Steps

- Structured logging (JSON format)  
- Correlation IDs (request tracing)  
- Alerting & monitoring integration  
- Security logging  
- SIEM integration (ELK / QRadar)