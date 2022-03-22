def building_builder():
    budget = float(input())
    initial_capital = float(input())
    number_of_investors = int(input())
    total = initial_capital
    we_building = False
    for investor in range(1, number_of_investors + 1):
        investors_money = float(input())
        total += investors_money
        print(f"Investor {investor} gave us {investors_money:.2f}.")
        if total >= budget:
            diff = abs(total - budget)
            print(f'We will manage to build it. Start now! Extra money - {diff:.2f}.')
            we_building = True
            break
    if not we_building:
        diff = abs(total - budget)
        print(f"Project can not start. We need {diff:.2f} more.")


building_builder()