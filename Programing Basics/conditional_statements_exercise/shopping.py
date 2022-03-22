peters_budget = float(input())
video_cards = int(input())
procesors = int(input())
ram_storage = int(input())

videocard_price = 250
procesor_price = (videocard_price * video_cards) * 0.35
ram_price = (videocard_price * video_cards) * 0.10

total_price = (video_cards * videocard_price) + (procesors * procesor_price) + (ram_price * ram_storage)
if video_cards > procesors:
    total_price = total_price - (total_price * 0.15)
else:
    total_price = total_price

money_left = peters_budget - total_price
if money_left >= 0:
    print(f"You have {money_left:.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(money_left):.2f} leva more!")
