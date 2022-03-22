number_of_groups = int(input())
max_5 = 0
max_12 = 0
max_25 = 0
max_40 = 0
more_than_41 = 0
total_ppl = 0

for _ in range(number_of_groups):
    people_in_group = int(input())
    if people_in_group <= 5:
        max_5 += people_in_group
    elif people_in_group <= 12:
        max_12 += people_in_group
    elif people_in_group <= 25:
        max_25 += people_in_group
    elif people_in_group <= 40:
        max_40 += people_in_group
    else:
        more_than_41 += people_in_group
    if people_in_group > 0:
        total_ppl += people_in_group

print(f"{max_5 / total_ppl * 100:.2f}%")
print(f"{max_12 / total_ppl * 100:.2f}%")
print(f"{max_25 / total_ppl * 100:.2f}%")
print(f"{max_40 / total_ppl * 100:.2f}%")
print(f"{more_than_41 / total_ppl * 100:.2f}%")
 