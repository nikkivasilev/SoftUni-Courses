list_of_gifts = input().split(' ')

current_command = input().split(' ')

while "No" and "Money" not in current_command:
    if "OutOfStock" in current_command:
        for item in range(len(list_of_gifts)):
            if list_of_gifts[item] == current_command[1]:
                list_of_gifts[item] = 'None'

    elif "Required" in current_command:
        index = int(current_command[2])
        if index in range(len(list_of_gifts)):
            list_of_gifts[index] = current_command[1]

    elif "JustInCase" in current_command:
        list_of_gifts[-1] = current_command[1]

    current_command = input().split(' ')

for item in list_of_gifts:
    if item == 'None':
        list_of_gifts.remove(item)
str1 = ' '.join(str(e) for e in list_of_gifts)
print(str1)
