number = int(input())
is_prime = True
for num in range(number):
    if num * num == number or num + num == number:
        is_prime = False
print(is_prime)