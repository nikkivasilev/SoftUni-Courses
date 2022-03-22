budget = float(input())
season = input()
destination = ''
cost = budget
place_to_stay = ''

if budget <= 100:
    destination = "Bulgaria"
    if season == 'summer':
        cost *= 0.3
    elif season == 'winter':
        cost *= 0.7
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        cost *= 0.4
    if season == 'winter':
        cost *= 0.8
else:
    destination = 'Europe'
    cost *= 0.9

if season == "summer" and destination != "Europe":
    place_to_stay = 'Camp'
elif season == 'winter' or destination == 'Europe':
    place_to_stay = 'Hotel'
print(f"Somewhere in {destination}")
print(f'{place_to_stay} - {cost:.2f}')

