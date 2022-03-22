budget = int(input())
season = input()
total_fishermen = int(input())
boat_rent = 0

if season == 'Spring':
    boat_rent = 3000
elif season == 'Summer' or season == 'Autumn':
    boat_rent = 4200
elif season == 'Winter':
    boat_rent = 2600

if total_fishermen <= 6:
    boat_rent *= 0.9
elif total_fishermen <= 11:
    boat_rent *= 0.85
else:
    boat_rent *= 0.75

if not season == 'Autumn' and total_fishermen % 2 == 0:
    boat_rent *= 0.95

difference = abs(budget - boat_rent)

if budget >= boat_rent:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")