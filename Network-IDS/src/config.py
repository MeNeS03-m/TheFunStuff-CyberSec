# Nettverksgrensesnitt å lytte på (f.eks. "eth0", "Wi-Fi")
INTERFACE = "\\Device\\NPF_{A55E7837-6B91-457B-8CA4-E524920B267E}"

PORT_SCAN_THRESHOLD   = 15   # antall SYN-pakker per sekund
BRUTE_FORCE_THRESHOLD = 5    # antall forsøk per sekund mot SSH/RDP/FTP
ALERT_COOLDOWN        = 8    # sekunder mellom like varsler fra samme IP

# Loggfil
LOG_FILE = "logs/alerts.log"