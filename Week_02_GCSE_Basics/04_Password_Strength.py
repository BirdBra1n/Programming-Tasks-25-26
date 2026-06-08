"""
TASK: 04 Password Strength

# Skills: Strings, loops, selection
Ask the user to enter a password, and check that they meet these conditions:
- At least 8 characters
- Contains a number
- Contains a captial and lower cased letter
- Extend for one special character
Print a response of weak, medium or strong for how many they pass.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def check_password_strength(password):
    has_length = len(password) >= 8
    has_number = False
    has_upper = False
    has_lower = False
    has_special = False
    
    special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/~`"

    for char in password:
        if char.isdigit():
            has_number = True
        elif char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char in special_characters:
            has_special = True

    score = sum([has_length, has_number, has_upper, has_lower, has_special])

    if score <= 2:
        return "WEAK"
    elif score <= 4:
        return "MEDIUM"
    else:
        return "STRONG"

def main():
    user_password = input("Enter a password to test: ")
    strength = check_password_strength(user_password)
    print(f"Your password strength is: {strength}")

if __name__ == "__main__":
    main()
