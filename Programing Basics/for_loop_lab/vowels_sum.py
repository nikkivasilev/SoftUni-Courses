text = input()

a = 1
e = 2
i = 3
o = 4
u = 5
total_sum = 0
for ch in text:
    if ch == "a":
        total_sum += 1
    elif ch == 'e':
        total_sum += 2
    elif ch == 'i':
        total_sum += 3
    elif ch == 'o':
        total_sum += 4
    elif ch == 'u':
        total_sum += 5

print(total_sum)