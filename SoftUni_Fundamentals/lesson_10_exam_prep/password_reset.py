string = input()
original = string

while True:
    command = input().split(" ")
    if command[0] == "Done":
        break

    elif command[0] == "TakeOdd":
        if len(string) > 1:
            string = string[1::2]
        print(string)
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        substring = string[index: index + length]
        string = string.replace(substring, "")
        print(string)
    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]

        if substring in string:
            while substring in string:
                string = string.replace(substring, substitute)
            print(string)
        else:
            print("Nothing to replace!")
    condition = True
if condition:

    print(f"Your password is: {string}")