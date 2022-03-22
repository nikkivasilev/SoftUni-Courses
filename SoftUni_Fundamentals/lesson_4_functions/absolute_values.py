
input_list = input().split(" ")
abs_list = list()

for n in input_list:
    current = abs(float(n))
    abs_list.append(current)
print(abs_list)