import sys

count_of_numbers = int(input())
total_sum = 0
max_num = -sys.maxsize

for num in range(count_of_numbers):
    current_num = int(input())
    total_sum += current_num
    if current_num > max_num:
        max_num = current_num
if max_num == total_sum - max_num:
    print("Yes")
    print(f'Sum = {max_num}')
else:
    diff = abs(max_num - (total_sum - max_num))
    print('No')
    print(f"Diff = {diff}")

