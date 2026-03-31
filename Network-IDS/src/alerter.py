import logging
import time
from colorama import Fore, Style, init
from src.config import LOG_FILE, ALERT_COOLDOWN

init(autoreset=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.WARNING,
    format="%(asctime)s - %(message)s"
)

# Holder styr på siste varsel per IP for å unngå spam
last_alert = {}

def send_alert(alert_type, src_ip, message):
    now = time.time()
    key = f"{alert_type}_{src_ip}"

    # Ikke varsle samme trussel mer enn hvert 5. sekund
    if key in last_alert and now - last_alert[key] < ALERT_COOLDOWN:
        return

    last_alert[key] = now

    colors = {
        "PORT_SCAN":   Fore.YELLOW,
        "BRUTE_FORCE": Fore.RED,
        "ARP_SPOOF":   Fore.MAGENTA,
    }
    color = colors.get(alert_type, Fore.WHITE)

    print(f"{color}[!] {alert_type} | {message}{Style.RESET_ALL}")
    logging.warning(f"{alert_type} | {message}")
