
my_dict = {}

while True:
    command = input()
    if command == "stop":
        break
    command_value = int(input())

    if command == "stop":
        break

    if command not in my_dict.keys():
        my_dict[command] = command_value
    else:
        my_dict[command] += command_value

for key, value in my_dict.items():
    print(f"{key} -> {value}")