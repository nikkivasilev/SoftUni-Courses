vacation_price = float(input())
puzzles = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
miners = int(input())
toy_cars = int(input())

puzzles_price = puzzles * 2.60
talking_dolls_price = talking_dolls * 3
teddy_bears_price = teddy_bears * 4.10
miners_price = miners * 8.20
toy_cars_price = toy_cars * 2

total_price = puzzles_price + talking_dolls_price + teddy_bears_price + miners_price + toy_cars_price
total_toys = puzzles + talking_dolls + teddy_bears + miners + toy_cars
if total_toys >= 50:
    total_price *= 0.75
else:
    total_price = total_price
rent = total_price * 0.1
money_left = total_price - rent
if money_left >= vacation_price:
    money_left -= vacation_price
    print(f'Yes! {money_left:.2f} lv left.')
else:
    money_left = abs(money_left - vacation_price)
    print(f"Not enough money! {money_left:.2f} lv needed.")
