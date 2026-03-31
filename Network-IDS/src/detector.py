from scapy.all import IP, TCP, ARP, ICMP
from collections import defaultdict
import time
from src.config import PORT_SCAN_THRESHOLD, BRUTE_FORCE_THRESHOLD

port_scan_tracker = defaultdict(list)
brute_force_tracker = defaultdict(list)

def analyze_packet(packet, alert_callback):
    now = time.time()

    # --- Vis all IP-trafikk (for debugging) ---
    if packet.haslayer(IP):
        src = packet[IP].src
        dst = packet[IP].dst
        proto = packet[IP].proto
        print(f"[>] Pakke fanget: {src} -> {dst} (proto={proto})")

    # --- Port Scan deteksjon ---
    if packet.haslayer(TCP) and packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_port = packet[TCP].dport
        flags = packet[TCP].flags

        if flags == "S":
            port_scan_tracker[src_ip].append(now)
            port_scan_tracker[src_ip] = [
                t for t in port_scan_tracker[src_ip] if now - t < 1
            ]
            if len(port_scan_tracker[src_ip]) > PORT_SCAN_THRESHOLD:
                alert_callback("PORT_SCAN", src_ip,
                               f"Mulig port scan fra {src_ip}")

        if dst_port in [22, 3389, 21, 80, 443]:
            brute_force_tracker[src_ip].append(now)
            brute_force_tracker[src_ip] = [
                t for t in brute_force_tracker[src_ip] if now - t < 1
            ]
            if len(brute_force_tracker[src_ip]) > BRUTE_FORCE_THRESHOLD:
                alert_callback("BRUTE_FORCE", src_ip,
                               f"Mulig brute force fra {src_ip} mot port {dst_port}")

    # --- ARP Spoofing deteksjon ---
    if packet.haslayer(ARP):
        if packet[ARP].op == 2:
            alert_callback("ARP_SPOOF", packet[ARP].psrc,
                           f"Mistenkelig ARP reply fra {packet[ARP].psrc}")