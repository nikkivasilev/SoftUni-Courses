quantity = int(input())
days = int(input())

christmas_spirit = 0
total_costs = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        christmas_spirit += 5
        total_costs += 2 * quantity
    if day % 3 == 0:
        christmas_spirit += 13
        total_costs += 8 * quantity
    if day % 5 == 0:
        christmas_spirit += 17
        total_costs += 15 * quantity
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        total_costs += 23

if day % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {total_costs}")
print(f"Total spirit: {christmas_spirit}")