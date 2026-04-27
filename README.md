# SENTINEL: Cloud-Native Uptime Monitor

A resilient Python-based monitoring tool that tracks website latency (a Golden Signal) and persists logs to the cloud.

## 🛠 Tech Stack
- **Language:** Python 3 (boto3, urllib)
- **Infrastructure:** AWS (S3), Terraform
- **CI/CD:** GitHub Actions (Flake8 Linting)
- **Environment:** Docker & Linux (macOS)

## 🚀 Key SRE Features
- **Fault Tolerance:** Uses try/except blocks to prevent script crashes during network timeouts.
- **Infrastructure as Code:** S3 bucket provisioned via Terraform to ensure repeatable deployments.
- **Persistence:** Logs are automatically offloaded to AWS S3 for long-term observability.
- **Automated Guardrails:** CI/CD pipeline verifies code quality on every push.

## 📈 Service Level Objectives (SLOs)
- **Target:** 95% of monitored sites must return Status 200.
- **Performance:** 90% of requests must have Latency < 500ms.
