def calc_price(product,quality):
    if product == 'coffee':
        return quality * 1.5
    elif product == 'coke':
        return  quality * 1.4
    elif product == 'water':
        return  quality * 1
    elif product == 'snacks':
        return  quality * 2

current_product = input()
current_qualiry = int(input())

final_price = calc_price(current_product, current_qualiry)
print(f"{final_price:.2f}")