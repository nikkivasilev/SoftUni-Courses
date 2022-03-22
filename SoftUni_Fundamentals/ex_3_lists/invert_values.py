def value_inverter(numbers):
    invert_list = list()
    for i in range(len(numbers)):
        current_num = int(numbers[i])
        invert_current = current_num - (current_num * 2)
        invert_list.append(invert_current)
    print(invert_list)


num_list = input().split(" ")
value_inverter(num_list)
