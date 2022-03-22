data = input()
data_list = [ch for ch in data]
power = 0
for ch in range(len(data)):
    if data[ch] == ">":
        power += 1 + ch + int(data[ch + 1])
        current_cicle = ch + 1
        while current_cicle < power:

            if data[current_cicle] == ">":
                power += 1 + int(data[current_cicle + 1])

            else:
                data_list[current_cicle] = " "
            current_cicle += 1
        power = 0
        current_cicle = 0


output_list = [item for item in data_list if item != " "]

print("".join(output_list))

