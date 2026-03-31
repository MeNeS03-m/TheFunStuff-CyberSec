# 🛡️ Network Intrusion Detection System (NIDS)

A Python-based network intrusion detection system that monitors live traffic in real time and visualizes threats through a sleek web dashboard.

---

## 📸 Dashboard Preview

> Run the tool and open `http://localhost:5000` in your browser.

![Dashboard]

The dashboard features:
- **Live stat cards** — total alerts, port scans, brute force attempts, ARP spoofing
- **Donut chart** — threat type breakdown at a glance
- **Line chart** — alert frequency over time (hourly)
- **Alert table** — last 50 detections with timestamps, type tags, and details
- **Auto-refresh** every 10 seconds

---

## ✅ Features

| Detection | Description |
|---|---|
| ⚡ Port Scan | Detects SYN flood / rapid port scanning |
| 🔨 Brute Force | Detects repeated connection attempts to SSH (22), RDP (3389), FTP (21) |
| 👻 ARP Spoofing | Detects unsolicited ARP replies on local network |

---

## 🛠️ Tech Stack

- **Python 3** — core detection engine
- **Scapy** — live packet capture and analysis
- **Flask** — REST API backend for the dashboard
- **Chart.js** — data visualization
- **Colorama** — colored terminal alerts
- **Threading** — IDS and dashboard run simultaneously

---

## ⚙️ Installation

### 1. Prerequisites

- Python 3.8+
- [Npcap](https://npcap.com/#download) (Windows only — install with "WinPcap API-compatible mode" enabled)

### 2. Clone the repo

```bash
git clone https://github.com/MeNeS03-m/network-ids.git
cd network-ids
```

### 3. Set up virtual environment

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Configure your network interface

Find your interface:
```python
from scapy.arch.windows import get_windows_if_list
for iface in get_windows_if_list(): print(iface['name'], '|', iface['guid'])
```

Update `src/config.py`:
```python
INTERFACE = "\\Device\\NPF_{YOUR-GUID-HERE}"
PORT_SCAN_THRESHOLD   = 10
BRUTE_FORCE_THRESHOLD = 3
LOG_FILE = "logs\\alerts.log"
```

---

## ▶️ Usage

> ⚠️ Must be run as **Administrator** (Scapy requires raw socket access)

```powershell
# Right-click PowerShell → Run as Administrator
venv\Scripts\activate
python main.py
```

Then open your browser at:
```
http://localhost:5000
```

---

## 🧪 Testing

Simulate a port scan against yourself:
```powershell
1..500 | ForEach-Object {
    $client = New-Object Net.Sockets.TcpClient
    try { $client.ConnectAsync("YOUR-IP", $_) | Out-Null } catch {}
    Start-Sleep -Milliseconds 2
}
```

Watch the log live:
```powershell
Get-Content logs\alerts.log -Wait
```

---

## 📁 Project Structure

```
network-ids/
├── main.py               # Entry point — starts IDS + dashboard
├── requirements.txt
├── README.md
├── src/
│   ├── sniffer.py        # Packet capture (Scapy)
│   ├── detector.py       # Threat detection logic
│   ├── alerter.py        # Terminal alerts + file logging
│   ├── dashboard.py      # Flask API (/api/alerts, /api/stats)
│   └── config.py         # Interface, thresholds, log path
├── templates/
│   └── index.html        # Dashboard UI
├── logs/
│   └── alerts.log        # Persistent alert log
└── tests/
```

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes and authorized network monitoring only**. Do not use on networks you do not own or have explicit permission to test.

---
