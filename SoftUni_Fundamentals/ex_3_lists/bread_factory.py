events = input().split('|')
energy = 100
coins = 100
closed_condition = False

for event in events:
    current_event_el = event.split("-")
    command = current_event_el[0]
    number = int(current_event_el[1])

    if command == "rest":
        if energy >= 100:
            energy = 100
            print(f"You gained 0 energy.")
        else:
            energy += number
            print(f"You gained {number} energy.")
        print(f"Current energy: {energy}.")

    elif command == 'order':
        if energy >= 30:
            print(f"You earned {number} coins.")
            energy -= 30
            coins += number
        else:
            energy += 50
            print(f"You had to rest!")

    else:
        if coins >= number:
            print(f"You bought {command}.")
            coins -= number
        else:
            print(f"Closed! Cannot afford {command}.")
            closed_condition = True
            break
if not closed_condition:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
