def password_validator(password):
    nums = 0
    is_valid = True
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    for chars in password:
        if chars.isnumeric():
            nums += 1
    if nums < 2:
        print(f"Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print("Password is valid")


current_password = input()
password_validator(current_password)