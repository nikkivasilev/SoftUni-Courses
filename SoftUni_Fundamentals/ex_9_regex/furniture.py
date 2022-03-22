import re


def furniture():
    pattern = r'>>([a-zA-Z]+)<<(\d+|\d+.\d+)!(\d+)'
    total_spend = 0
    product_list = []

    while True:
        data = input()
        if data == "Purchase":
            break

        result = re.match(pattern, data)

        if result is not None:
            prodict = result[1]
            price = float(result[2])
            quantity = float(result[3])
            total_spend += price*quantity
            product_list.append(prodict)
    print('Bought furniture:')

    if total_spend > 0:
        print("\n".join(product_list))
    print(f"Total money spend: {total_spend:.2f}")


furniture()
