def sum_numbers(a, b):
    return a + b


def substract(current_sum, c):
    return current_sum - c


a, b, c = int(input()), int(input()), int(input())

result = substract(sum_numbers(a, b), c)
print(result)