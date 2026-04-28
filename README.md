# SENTINEL: Cloud-Native Uptime & Observability Monitor

A resilient Python-based monitoring tool that tracks website latency (a Golden Signal), persists logs to AWS S3, and exposes real-time metrics for Prometheus/Grafana dashboards.

## 🛠 Tech Stack
* **Language**: Python 3 (`boto3`, `urllib`, `prometheus_client`)
* **Infrastructure**: AWS (S3), Terraform
* **Environment**: Docker, Linux/macOS
* **Observability**: Prometheus, Grafana

## 🚀 Key SRE Features
* **Live Observability**: Exposes a local `/metrics` endpoint serving real-time latency Histograms formatted for Prometheus scraping.
* **Fault Tolerance**: Implements strict `try/except` blocks to prevent script crashes during network timeouts or DNS failures.
* **Infrastructure as Code (IaC)**: AWS S3 bucket provisioned via Terraform to ensure repeatable, idempotent deployments.
* **Data Persistence**: Automated offloading of raw `monitor.log` data to AWS S3 for disaster recovery and historical auditing.
* **Security & Isolation**: Uses Python Virtual Environments (`venv`), Docker containerization, and `.env` files to ensure no AWS secrets are hardcoded or leaked.

## 📈 Service Level Objectives (SLOs)
* **Availability Target**: 95% of monitored sites must return HTTP Status 200.
* **Performance Target**: 90% of requests must have a Latency < 500ms.

## 🏗 System Architecture
1. **Docker Container** runs the Python monitoring loop.
2. **Boto3 SDK** securely connects to the **AWS Cloud** to persist logs to an **S3 Bucket**.
3. **Prometheus Client** opens an internal server on Port 8000 to stream live metrics.

## 💻 Quick Start Guide

**1. Clone the repository and navigate to the directory:**
```bash
git clone [https://github.com/YOUR_USERNAME/sentinel-monitor.git](https://github.com/YOUR_USERNAME/sentinel-monitor.git)
cd sentinel-monitor
