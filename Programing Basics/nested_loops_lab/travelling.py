
destination = ''
destination_price = 0
current_total = 0
destination = input()
while destination != 'End':
    destination_price = float(input())
    while destination_price != "End":
        current_input = float(input())
        current_total += current_input
        if current_total >= destination_price:
            print(f"Going to {destination}!")
            break
    destination = input()
    destination_price = 0
    current_total = 0