number_of_lines = int(input())
opening_bracelet = 0
closing_bracelet = 0
total_opening_bracelet = 0
total_closing_bracelet = 0
is_balanced = True
for _ in range(number_of_lines):
    current_input = input()
    if current_input == '(':
        opening_bracelet += 1
        closing_bracelet = 0
        total_opening_bracelet += 1
        if opening_bracelet == 2:
            is_balanced = False
    if current_input == ')':
        closing_bracelet += 1
        opening_bracelet = 0
        total_closing_bracelet += 1
        if closing_bracelet == 2:
            is_balanced = False
if int(total_opening_bracelet / total_closing_bracelet) != 1:
    is_balanced = False
if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")