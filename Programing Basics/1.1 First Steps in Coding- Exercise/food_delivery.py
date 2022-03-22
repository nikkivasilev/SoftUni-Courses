quantity_of_chicken_menus = int(input())
quantity_of_fish_menus = int(input())
quantity_of_vegan_menus = int(input())

price_of_chicken_menu = 10.35
price_of_fish_menu = 12.40
price_of_vegan_menu = 8.15
price_of_delivery = 2.50

price_for_the_meal = price_of_chicken_menu * quantity_of_chicken_menus + price_of_fish_menu * quantity_of_fish_menus \
                     + quantity_of_vegan_menus * price_of_vegan_menu
price_for_dessert = price_for_the_meal * 0.2
total_price = price_for_the_meal + price_for_dessert + price_of_delivery
print(total_price)