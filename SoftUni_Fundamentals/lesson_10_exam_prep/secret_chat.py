secret_message = input()


while True:
    command = input().split(":|:")

    if command[0] == "Reveal":
        break
    current_command = command[0]

    if current_command == "InsertSpace":
        index = int(command[1])
        secret_message = secret_message[:index] + " " + secret_message[index:]
        print(secret_message)
    elif current_command == "Reverse":
        substring = command[1]
        if substring in secret_message:
            replacement = substring[::-1]
            secret_message = secret_message.replace(substring, "")
            secret_message = secret_message + replacement
            print(secret_message)
        else:
            print("error")
    elif current_command == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        while substring in secret_message:
            secret_message = secret_message.replace(substring, replacement)
        print(secret_message)

print(f"You have a new text message: {secret_message}")
