count = int(input())

even = []
odd = []
negative = []
positive = []

for n in range(count):
    current_num = int(input())
    if current_num == 0:
        even.append(current_num)
        positive.append(current_num)
    elif current_num % 2 == 0:
        even.append(current_num)
    elif current_num % 2 != 0:
        odd.append(current_num)
    if current_num > 0:
        positive.append(current_num)
    if current_num < 0:
        negative.append(current_num)

print(eval(input()))