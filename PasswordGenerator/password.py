import random
import string

def generate_password(length, numbers=True, special_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    chars = letters

    if numbers:
        chars += digits

    if special_chars:
        chars += special

    password = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(password) < length:
        new_char = random.choice(chars)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True 

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_chars:
            meets_criteria = meets_criteria and has_special

    print(f"Your password is: {password}")


generate_password(10)