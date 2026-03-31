from flask import Flask, jsonify, render_template
import os
import re
from datetime import datetime

app = Flask(__name__, template_folder="../templates")

LOG_FILE = "logs/alerts.log"

def parse_logs():
    alerts = []
    if not os.path.exists(LOG_FILE):
        return alerts

    with open(LOG_FILE, "r") as f:
        for line in f.readlines():
            # Format: 2024-01-01 12:00:00,000 - ALERT_TYPE | melding
            match = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),\d+ - (\w+) \| (.+)", line)
            if match:
                alerts.append({
                    "timestamp": match.group(1),
                    "type": match.group(2),
                    "message": match.group(3)
                })
    return alerts

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/alerts")
def get_alerts():
    alerts = parse_logs()
    return jsonify(alerts)

@app.route("/api/stats")
def get_stats():
    alerts = parse_logs()
    stats = {"PORT_SCAN": 0, "BRUTE_FORCE": 0, "ARP_SPOOF": 0}
    for alert in alerts:
        if alert["type"] in stats:
            stats[alert["type"]] += 1
    return jsonify(stats)

def start_dashboard():
    app.run(debug=False, port=5000, use_reloader=False)