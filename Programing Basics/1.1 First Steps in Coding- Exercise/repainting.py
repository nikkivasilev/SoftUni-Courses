needed_square_meters_of_plastic = int(input())
needed_liters_of_paint = int(input())
needed_liters_of_conditioner = int(input())
hours_to_complete = int(input())

price_of_square_meter_plastic = 1.50
price_of_liter_paint = 14.50
price_of_liter_conditioner =5

total_price_for_plastic = (needed_square_meters_of_plastic * price_of_square_meter_plastic) \
                          + 2 * price_of_square_meter_plastic
total_price_for_paint = needed_liters_of_paint * price_of_liter_paint\
                        + ((0.1 * needed_liters_of_paint) * price_of_liter_paint)
total_price_for_conditioner = needed_liters_of_conditioner * price_of_liter_conditioner
price_for_bags = 0.40
total_consumatives_price = total_price_for_plastic + total_price_for_conditioner + total_price_for_paint\
                           + price_for_bags

workers_pay = (total_consumatives_price * 0.3) * hours_to_complete

total_price = total_consumatives_price + workers_pay
print(total_price)