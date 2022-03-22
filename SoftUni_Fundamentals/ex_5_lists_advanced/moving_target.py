def shoot(index, power):
    if 0 <= index <= len(targets):
        target_value = targets[index]
        current_target = targets[index]
        current_target -= power
        if current_target <= 0:
            targets.remove(target_value)
        else:
            targets[index] = current_target


def add(index, value):
    if 0 <= index <= len(targets):
        targets.insert(index, value)
    else:
        print("Invalid placement!")


def strike(index, radius):
    indices = []
    strike_index = targets[index]
    indices.append(strike_index)
    minus_index = index
    next_index = index
    condition = True
    for _ in range(radius):
        minus_index -= 1
        if minus_index in range(len(targets)):
            indices.append(targets[minus_index])
        next_index += 1
        if next_index in range(len(targets)):
            indices.append(targets[next_index])
        else:
            condition = False
            break
    if condition:
        for target in indices:
            if target in targets:
                targets.remove(target)
    else:
        print("Strike missed!")
    return targets


targets = list(map(int, input().split(" ")))

current_command = input().split(" ")
while current_command[0] != "End":
    command = current_command[0]
    index = int(current_command[1])
    power = int(current_command[2])
    if command == "Shoot":
        shoot(index, power)
    elif command == "Add":
        add(index, power)
    elif command == "Strike":
        strike(index, power)
    current_command = input().split(" ")

print("|".join(map(str, targets)))
