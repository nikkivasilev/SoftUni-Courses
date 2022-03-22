budget = float(input())
price_of_flour = float(input())

price_of_eggs = price_of_flour * 0.75
price_of_liter_milk  = price_of_flour * 1.25
price_of_needed_milk_per_bread = price_of_liter_milk * 0.25
price_per_bread = price_of_flour + price_of_eggs + price_of_needed_milk_per_bread
total_bread = 0
colored_eggs = 0
every_third = 0
while budget > price_per_bread:
    budget -= price_per_bread
    total_bread += 1
    every_third += 1
    colored_eggs += 3
    if every_third == 3:
        colored_eggs -= (total_bread - 2)
        every_third = 0

money_left = budget
print(f"You made {total_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")