# 🚀 monitoring-demo (Prometheus + Grafana + Nginx)

## 🎯 Project Goal
This project demonstrates a basic monitoring stack using:
- Prometheus (metrics collection)
- Grafana (visualization)
- Nginx (demo service)
- Nginx Exporter (application metrics)
- cAdvisor (container metrics)

Goal: understand how metrics are collected, processed, and visualized in a containerized environment.

---

## 🧠 Architecture
Nginx → nginx-exporter → Prometheus → Grafana  
                        ↑  
                     cAdvisor  

---

## 📁 Project Structure
```
monitoring-demo/
├── docker-compose.yml
├── nginx/
│   └── default.conf
├── prometheus/
│   └── prometheus.yml
```

---

## ⚙️ Services
**Nginx**
- Demo web server
- Exposes `/status` endpoint

**Nginx Exporter**
- Converts Nginx metrics into Prometheus format

**Prometheus**
- Scrapes metrics every 5 seconds
- Stores time-series data

**Grafana**
- Connects to Prometheus
- Visualizes metrics

**cAdvisor**
- Provides container-level metrics

---

## ▶️ Run
```bash
docker compose up -d
```

---

## 🧪 Test
```bash
curl http://localhost:8080
curl http://localhost:8080/status
curl http://localhost:9113/metrics
```

---

## 🔍 Prometheus
URL: http://localhost:9090

Example queries:
```promql
nginx_http_requests_total
nginx_connections_active
nginx_up
rate(nginx_http_requests_total[1m])
```

---

## 📊 Grafana
URL: http://localhost:3000  
Login: `admin / admin`

Data source:
```
http://monitoringdemo_prometheus:9090
```

---

## 📈 Dashboard Panels
**Application Metrics**
- Request Rate (RPS)
- Active Connections
- Total Requests
- Nginx Status

**Container Metrics**
- CPU Usage
- Memory Usage

---

## 🧠 Key Concepts
- Prometheus uses pull model
- Exporters expose metrics
- Counters require `rate()`
- Grafana only visualizes
- Metrics → “How much?”
- Logs → “What happened?”

---

## ⚠️ Limitation
On Docker Desktop for macOS:
- cAdvisor may expose only container IDs
- Container names may not appear as labels
- Container IDs change after restart

In production (Linux/Kubernetes), proper labels are available.

---

## 🎯 Conclusion
This project demonstrates:
- Monitoring architecture
- Metrics collection
- Real-time visualization
ti