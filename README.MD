# SIGMA5+ LAB – Config Management

## Ansible Tasks

### 1. Common Tasks (All Targets)
- Create default user for all targets

### 2. iPerf Servers
- Install iPerf3 (client/server)
- Install pip (client/server)
- Install and configure Telegraf (server)
- Create iPerf bash scripts for TCP and UDP (server)
- Create systemd service for:
  - `iperf3-tcp`
  - `iperf3-udp` (client)
- Configure Telegraf YAML file

### 3. Grafana-Prometheus Server
- Install Grafana
- Install Prometheus
- Configure Prometheus YAML file

---

### ✅ Test Phase
Ensure all services are installed, configured, and running as expected.