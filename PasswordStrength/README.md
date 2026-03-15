# 5. Password Strength Checker

### Overview
Password Strength Checker is a Python script that analyzes passwords and evaluates their strength based on common security guidelines.

The program assigns a score and provides suggestions for improving weak passwords.

### Features
Password strength scoring  
Length verification  
Digit detection  
Uppercase character detection  
Special character detection  
User feedback suggestions  

### Technologies
Python  
String processing  
Conditional logic  

### How It Works
The password is analyzed using several checks. Each successful check increases the overall score. If a requirement is missing, the script suggests improvements.

### Example Output

Strong password:

```
Wow! Your password got a score 5 of 5, and thats strong! Nothing to worry about.
```

Weak password:

```
Your password got a score 2 of 5. Here are some suggestions to improve it:
Password should contain at least one digit.
Password should contain at least one special character.
Password should contain at least one uppercase letter.
```

### Learning Goals
Password security fundamentals  
Validation logic in Python  
User feedback systems  

---
