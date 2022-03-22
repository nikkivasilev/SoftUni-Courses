number_of_cities = int(input())
total_profit = 0

for current_city in range(1, number_of_cities + 1):
    city_name = input()
    owner_income = float(input())
    owner_expenses = float(input())
    if current_city % 3 == 0:
        if current_city % 5 != 0:
            owner_expenses *= 1.5
    if current_city % 5 == 0:
        owner_income -= 0.1 * owner_income
    current_profit = owner_income - owner_expenses
    total_profit += current_profit
    print(f"In {city_name} Burger Bus earned {current_profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")