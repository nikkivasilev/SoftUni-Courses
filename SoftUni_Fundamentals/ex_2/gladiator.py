lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
gladiator_expenses = 0
broken_shields = 0
for lost in range(1, lost_fights_count + 1):

    if lost % 2 == 0:
        gladiator_expenses += helmet_price
    if lost % 3 == 0:
        gladiator_expenses += sword_price
    if lost % 2 == 0 and lost % 3 == 0:
        gladiator_expenses += shield_price
        broken_shields += 1
    if broken_shields == 2:
        gladiator_expenses += armor_price
        broken_shields = 0
print(f"Gladiator expenses: {gladiator_expenses:.2f} aureus")
