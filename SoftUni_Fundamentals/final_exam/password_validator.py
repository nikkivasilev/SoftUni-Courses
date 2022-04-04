import re
password = input()
password_list = [ch for ch in password]
allowed = r"[A-Z-a-z_0-9]+"
while True:
    command = input().split(" ")

    if command[0] == "Complete":
        break

    if command[0] == "Make":
        action = command[1]
        index = int(command[2])
        char_to_replace = password_list[index]
        if action == "Upper":
            password = password[:index] + char_to_replace.upper() + password[index + 1:]
            print(password)
        elif action == "Lower":
            password = password[:index] + char_to_replace.lower() + password[index + 1:]
            print(password)
    elif command[0] == "Insert":
        index = int(command[1])
        char = command[2]
        password = password[:index] + char + password[index:]
        print(password)
    elif command[0] == "Replace":
        char = command[1]
        value = int(command[2])
        if char not in password:
            continue
        else:
            new_char = ord(char) + value
            while char in password:
                password = password.replace(char, chr(new_char))
            print(password)
    elif command[0] == "Validation":
        if len(password) < 8:
            print(f"Password must be at least 8 characters long!")
        all_char = []
        upper = []
        lower = []
        digit = []
        for ch in password:
            if ch == "_":
                all_char.append(ch)
            if ch.isalnum():
                all_char.append(ch)
            if ch.isupper():
                upper.append(ch)
            if ch.islower():
                lower.append(ch)
            if ch.isdigit():
                digit.append(ch)

        if len(all_char) < len(password):
            print("Password must consist only of letters, digits and _!")
        if len(upper) < 1:
            print("Password must consist at least one uppercase letter!")
        if len(lower) < 1:
            print("Password must consist at least one lowercase letter!")
        if len(digit) < 1:
            print("Password must consist at least one digit!")
