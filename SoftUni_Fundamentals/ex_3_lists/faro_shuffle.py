starting_string = input()
shuffles = int(input())

first_char = starting_string[0]
last_char = starting_string[-1]

starting_list = starting_string.split(" ")

changeable_list = starting_list
first_list = []
second_list = []

half = int(len(starting_list) / 2)

for n in range(shuffles):
    first_list = changeable_list[1:half]
    second_list = changeable_list[half:-1]
    changeable_list = []
    for num in range(len(second_list)):
        if num == 0:
            changeable_list.append(starting_list[0])
        changeable_list.append(second_list[num])
        changeable_list.append(first_list[num])
        if num == (len(second_list) - 1):
            changeable_list.append(starting_list[-1])

print(changeable_list)
