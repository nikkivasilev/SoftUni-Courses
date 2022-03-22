month = input()
total_stay = int(input())

price_of_studio = total_stay
price_of_apartment = total_stay

if month == "May" or month == "October":
    price_of_studio *= 50
    price_of_apartment *= 65
    if 7 < total_stay < 14:
        price_of_studio *= 0.95
    elif total_stay > 14:
        price_of_studio *= 0.7
    else:
        price_of_studio = price_of_studio
elif month == "June" or month == 'September':
    price_of_studio *= 75.20
    price_of_apartment *= 68.70
    if total_stay > 14:
        price_of_studio *= 0.8
elif month == 'July' or month == 'August':
    price_of_studio *= 76
    price_of_apartment *= 77
if total_stay > 14:
    price_of_apartment *= 0.9

print(f'Apartment: {price_of_apartment:.2f} lv.')
print(f'Studio: {price_of_studio:.2f} lv.')
