number_of_lines = int(input())
users_dict = {}
for _ in range(number_of_lines):
    command = input().split(" ")
    current_command = command[0]
    username = command[1]
    if current_command == 'register':
        license_plate_num = command[2]
        if username in users_dict:
            print(f"ERROR: already registered with plate number {license_plate_num}")
        else:
            users_dict[username] = license_plate_num
            print(f"{username} registered {license_plate_num} successfully")

    elif current_command == 'unregister':
        if username not in users_dict:
            print(f"ERROR: user {username} not found")
        else:
            del users_dict[username]
            print(f'{username} unregistered successfully')

for key, value in users_dict.items():
    print(f'{key} => {value}')
