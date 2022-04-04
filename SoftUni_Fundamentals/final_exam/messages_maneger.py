maximum_capacity = int(input())

users_dict = {}

while True:
    command = input().split("=")

    if command[0] == "Statistics":
        break
    if command[0] == "Add":
        username = command[1]
        sent = int(command[2])
        received = int(command[3])
        if username not in users_dict:
            users_dict[username] = [sent, received]

    elif command[0] == "Message":
        sender = command[1]
        receiver = command[2]
        if sender in users_dict and receiver in users_dict:
            users_dict[sender][0] += 1
            users_dict[receiver][1] += 1
            if users_dict[sender][0] + users_dict[sender][1] >= maximum_capacity:
                del users_dict[sender]
                print(f"{sender} reached the capacity!")
            if users_dict[receiver][0] + users_dict[receiver][1] >= maximum_capacity:
                del users_dict[receiver]
                print(f"{receiver} reached the capacity!")
    elif command[0] == "Empty":
        username = command[1]
        if username == "All":
            users_dict = {}
        else:
            del users_dict[username]

print(f"Users count: {len(users_dict)}")
for user in users_dict:
    username = user
    number_of_messages = users_dict[username][0] + users_dict[username][1]
    print(f"{username} - {number_of_messages}")