import os

subnet = "192.168.1."

for i in range (1, 255):
    ip = subnet + str(i)

    res = os.system(f'ping -n 1 -w 200 {ip} > nul')

    if res == 0:
        print(f'Traffic found at {ip}')