numbers = int(input())
left_sum = 0
right_sum = 0
for _ in range(numbers):
    total_left = int(input())
    left_sum += total_left
for _ in range(numbers):
    total_right = int(input())
    right_sum += total_right

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")
