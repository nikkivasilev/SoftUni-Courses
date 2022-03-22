num_of_str = int(input())
keyword = input()
all_list = []
filtered_list = []
for n in range(num_of_str):
    current_str = input()
    all_list.append(current_str)
    if keyword in current_str:
        filtered_list.append(current_str)

print(all_list)
print(filtered_list)
