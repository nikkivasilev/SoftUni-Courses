type_of_flowers = input()
quantity_of_flowers = int(input())
budget = int(input())
price = quantity_of_flowers

if type_of_flowers == 'Roses':
    price *= 5
    if quantity_of_flowers > 80:
        price *= 0.9
    else:
        price = price
elif type_of_flowers == 'Dahlias':
    price *= 3.80
    if quantity_of_flowers > 90:
        price *= 0.85
    else:
        price = price
elif type_of_flowers == 'Tulips':
    price *= 2.80
    if quantity_of_flowers > 80:
        price *= 0.85
    else:
        price = price
elif type_of_flowers == 'Narcissus':
    price *= 3
    if quantity_of_flowers < 120:
        price *= 1.15
    else:
        price = price
elif type_of_flowers == 'Gladiolus':
    price *= 2.50
    if quantity_of_flowers < 80:
        price *= 1.20
    else:
        price = price

difference = abs(budget - price)
if budget >= price:
    print(f"Hey, you have a great garden with {quantity_of_flowers} {type_of_flowers} and {difference:.2f} leva left.")
else:
    print(f'Not enough money, you need {difference:.2f} leva more.')
