from scapy.all import sniff

def start_sniffing(packet_callback, interface):
    print(f"[*] Lytter på grensesnitt: {interface}")
    sniff(iface=interface, prn=packet_callback, store=False)