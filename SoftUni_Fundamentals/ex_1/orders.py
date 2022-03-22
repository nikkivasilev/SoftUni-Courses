number_of_orders = int(input())
total = 0


for _ in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    current_total = price_per_capsule * days * capsules_count
    total += current_total
    print(f"The price for the coffee is: ${current_total:.2f}")
print(f"Total: ${total:.2f}")
