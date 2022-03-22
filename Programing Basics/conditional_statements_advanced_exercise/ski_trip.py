days_spend = int(input())
type_of_room = input()
score = input()

nights_spend = days_spend - 1
price = nights_spend

if type_of_room == 'room for one person':
    price *= 18.00
elif type_of_room == 'apartment':
    price *= 25.00
    if days_spend < 10:
        price *= 0.7
    elif days_spend < 15:
        price *= 0.65
    elif days_spend > 15:
        price *= 0.5
elif type_of_room == 'president apartment':
    price *= 35.00
    if days_spend < 10:
        price *= 0.9
    elif days_spend < 15:
        price *= 0.85
    elif days_spend > 15:
        price *= 0.8

if score == 'positive':
    price += price * 0.25
elif score == 'negative':
    price *= 0.9
print(f"{price:.2f}")
