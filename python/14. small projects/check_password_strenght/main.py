def check_password_strength(password: str) -> str:
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|`~"

    if len(password) < 8:
        return "Weak"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    score = sum([has_upper, has_lower, has_digit, has_special])

    if score == 4:
        return "Strong"
    elif score == 3:
        return "Medium"
    else:
        return "Weak"


password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"Password strength: {strength}")
