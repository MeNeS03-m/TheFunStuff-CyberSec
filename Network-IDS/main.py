import threading
from src.sniffer import start_sniffing
from src.detector import analyze_packet
from src.alerter import send_alert
from src.dashboard import start_dashboard
from src.config import INTERFACE

def packet_callback(packet):
    analyze_packet(packet, send_alert)

if __name__ == "__main__":
    print("=" * 50)
    print("  🛡️  Network Intrusion Detection System")
    print("=" * 50)
    print("  📊 Dashboard: http://localhost:5000")
    print("=" * 50)

    # Start dashboard i egen tråd
    dashboard_thread = threading.Thread(target=start_dashboard, daemon=True)
    dashboard_thread.start()

    # Start IDS
    start_sniffing(packet_callback, INTERFACE)