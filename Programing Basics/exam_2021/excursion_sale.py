total_sea = int(input())
total_mountain = int(input())
everything_sold = False
sea_price = 680
mountain_price = 499
total_money_earned = 0
current_packet = input()
while current_packet != "Stop":
    if current_packet == "sea":
        if total_sea == 0:
            pass
        else:
            total_money_earned += 680
            total_sea -= 1
    elif current_packet == "mountain":
        if total_mountain == 0:
            pass
        else:
            total_money_earned += 499
            total_mountain -= 1
    if total_sea == 0 and total_mountain == 0:
        everything_sold = True
        break
    current_packet = input()

if everything_sold:
    print(f"Good job! Everything is sold.")
    print(f"Profit: {total_money_earned} leva.")
else:
    print(f"Profit: {total_money_earned} leva.")