# 7. Python Keylogger

### Overview
This project is a Python based keylogger that records keyboard input and stores it in a log file. The program also demonstrates persistence by adding itself to the Windows startup registry.

The project is intended for cybersecurity learning and understanding how certain types of malware operate.

### Features
Keyboard input capture  
Timestamped keystroke logging  
Automatic log file storage  
Startup persistence through Windows registry  
Background execution  

### Technologies
Python  
pynput library  
Windows registry manipulation  
Logging system  

### How It Works
The script listens for keyboard events using the pynput library. Each key press is logged with a timestamp and saved to a file. The program also adds itself to the Windows startup registry so it runs automatically after system reboot.

### Example Log Output

```
2026-03-15 12:42:11: 'h'
2026-03-15 12:42:11: 'e'
2026-03-15 12:42:12: 'l'
2026-03-15 12:42:12: 'l'
2026-03-15 12:42:12: 'o'
```

### Learning Goals
Understanding how keyloggers work  
Event based programming in Python  
Persistence techniques  
System level monitoring  

### Disclaimer
This project is for educational and cybersecurity research purposes only. Running keyloggers on systems without permission may be illegal.

---
