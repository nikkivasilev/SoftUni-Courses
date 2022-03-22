command_list = input().split("||")
total_fuel = int(input())
total_ammunition = int(input())

for current_command in command_list:
    if "Titan" in current_command:
        print("You have reached Titan, all passengers are safe.")
        break
    current_list = current_command.split(" ")
    command = current_list[0]
    amount = int(current_list[1])
    if command == "Travel":
        if total_fuel >= amount:
            total_fuel -= amount
            print(f"The spaceship travelled {amount} light-years.")
        else:
            print("Mission failed.")
            break
    elif command == "Enemy":
        if total_ammunition >= amount:
            total_ammunition -= amount
            print(f"An enemy with {amount} armour is defeated.")
        elif total_fuel >= amount * 2:
            total_fuel -= amount * 2
            print(f"An enemy with {amount} armour is outmaneuvered.")
        else:
            print("Mission failed.")
            break
    elif command == "Repair":
        total_fuel += amount
        total_ammunition += amount * 2
        print(f"Ammunitions added: {amount * 2}.")
        print(f"Fuel added: {amount}.")
