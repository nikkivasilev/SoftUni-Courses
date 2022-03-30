import re
pattern = r"([@][#]+)(?P<barcode>[A-Z][A-Z-a-z0-9]{4,}[A-Z])([@][#]+)"

count = int(input())

for _ in range(count):
    current_barcode = input()
    checker = re.match(pattern, current_barcode)

    if checker:
        barcode = checker.group("barcode")
        numbers = [num for num in barcode if num.isdigit()]
        product_group = ''
        if len(numbers) > 0:
            product_group = "".join(numbers)
        else:
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")