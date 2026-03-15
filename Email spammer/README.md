## 1. Email Automation Script

### Overview
This Python script automatically sends multiple emails using the SMTP protocol. The script includes timestamped messages, configurable limits, and logging of sent emails.

### Features
Automated email sending  
Configurable email limit  
Customizable subject lines  
Timestamped messages  
Logging of sent emails  
Adjustable delay between emails

### Technologies
Python  
SMTP protocol  
MIME email formatting  

### How It Works
The script connects to an SMTP server, authenticates using provided credentials, and sends emails to a specified recipient. After each email is sent, the action is recorded in a log file.

### Example Output

```
[+] Email #1 sent at 2026-03-15 14:20:31
```

Log file example:

```
[2026-03-15 14:20:31] Email #1 sent to recipient@email.com
```

### Learning Goals
Understanding SMTP communication  
Automation with Python  
Logging and error handling  

### Disclaimer
This project is intended for educational and testing purposes only.

---
