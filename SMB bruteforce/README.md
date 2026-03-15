# 6. SMB Bruteforce Tool

### Overview
This project is a batch script that attempts to discover valid SMB credentials using a password wordlist.

The script iterates through each password and attempts authentication against a target system.

### Features
Wordlist based password testing  
Automated password attempts  
SMB authentication testing  
Success detection and reporting  

### Technologies
Windows Batch scripting  
SMB protocol  
Windows networking commands  

### How It Works
The script requests the target IP, username, and password list from the user. It then attempts to authenticate using each password from the list until a successful login occurs.

### Example Output

```
[ATTEMPT 12] password123
[ATTEMPT 13] admin123
Password Found!: admin123
```

### Learning Goals
Understanding brute force attacks  
Batch scripting automation  
Basic SMB authentication mechanisms  

### Disclaimer
This tool should only be used in authorized penetration testing environments.

---
