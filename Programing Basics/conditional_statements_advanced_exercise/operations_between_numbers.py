first_number = int(input())
second_number = int(input())
action = input()
result = 0
even_or_odd = ''
if second_number == 0:
    print(f'Cannot divide {first_number} by zero')

elif action == '+':
    result = first_number + second_number
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{first_number} {action} {second_number} = {result} - {even_or_odd}")

elif action == '-':
    result = first_number - second_number
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{first_number} {action} {second_number} = {result} - {even_or_odd}")

elif action == '*':
    result = first_number * second_number
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{first_number} {action} {second_number} = {result} - {even_or_odd}")

elif action == '/':
    result = first_number / second_number
    print(f"{first_number} / {second_number} = {result:.2f}")

elif action == '%':
    result = first_number % second_number
    print(f"{first_number} % {second_number} = {result}")

