def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short, it should be at least 8 characters long.")
    
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")
    
    if any(char.isalpha() for char in password):
        score += 1
    else:
        feedback.append("Password should contain at least one letter.")
    
    if any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    
    if len(feedback) == 0:
        print(f"Wow! Your password got a score {score} of 5, and thats strong! Nothing to worry about.")
    else:
        print(f"Your password got a score {score} of 5. Here are some suggestions to improve it:")
        for line in feedback:
            print(f"- {line}")
    return "Password is strong."
    
check_password_strength("examplepassword123")