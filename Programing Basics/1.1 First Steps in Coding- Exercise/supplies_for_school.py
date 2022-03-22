number_of_pens = int(input())
number_of_markers = int(input())
number_of_detegrent = int(input())
percent_discount = int(input())
price_per_pen = 5.80
price_per_marker = 7.20
price_per_liter_detegrent = 1.20
needed_sum = number_of_pens * price_per_pen + number_of_markers * price_per_marker \
             + number_of_detegrent * price_per_liter_detegrent
percent_discount /= 100
needed_sum = needed_sum - (needed_sum * percent_discount)
print(needed_sum)
