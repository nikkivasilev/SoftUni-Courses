vacation_price = float(input())
budget = float(input())
days = 0
enough_money = False
days_spending = 0
while vacation_price > budget:
    command = input()
    current_sum = float(input())
    days += 1
    if command == "spend":
        days_spending += 1
        budget -= current_sum
        if budget < 0:
            budget = 0
        if days_spending >= 5:
            break
    elif command == 'save':
        days_spending = 0
        budget += current_sum
        if budget >= vacation_price:
            enough_money = True
            break
if enough_money:
    print(f"You saved the money for {abs(days)} days.")
else:
    print(f"You can't save the money.")
    print(abs(days))
