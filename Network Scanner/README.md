# 3. Network Scanner

### Overview
This Python script scans a local subnet to identify active devices. It uses ping requests to determine which hosts are reachable.

### Features
Subnet scanning  
Active device detection  
Ping based host discovery  
Simple and lightweight execution  

### Technologies
Python  
Operating system commands  
ICMP ping requests  

### How It Works
The script loops through all possible IP addresses in a subnet and sends a ping request to each address. If the host responds, the script prints the IP as active.

### Example Output

```
Traffic found at 192.168.1.1
Traffic found at 192.168.1.15
Traffic found at 192.168.1.37
```

### Learning Goals
Basic network discovery  
Subnet scanning concepts  
Python system command execution  

---
