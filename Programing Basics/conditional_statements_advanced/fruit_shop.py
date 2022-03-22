type_of_fruit = input()
day_of_week = input()
quantity = float(input())
price = 0
condition = True
if day_of_week == "Workday":
    condition = False

if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' \
        or day_of_week == 'Friday':
    if type_of_fruit == "banana":
        price = quantity * 2.50
    elif type_of_fruit == "apple":
        price = quantity * 1.20
    elif type_of_fruit == "orange":
        price = quantity * 0.85
    elif type_of_fruit == "grapefruit":
        price = quantity * 1.45
    elif type_of_fruit == "kiwi":
        price = quantity * 2.70
    elif type_of_fruit == "pineapple":
        price = quantity * 5.50
    elif type_of_fruit == "grapes":
        price = quantity * 3.85
    else:
        condition = False

elif day_of_week == 'Saturday' or 'Sunday':
    if type_of_fruit == 'banana':
        price = quantity * 2.70
    elif type_of_fruit == "apple":
        price = quantity * 1.25
    elif type_of_fruit == "orange":
        price = quantity * 0.90
    elif type_of_fruit == "grapefruit":
        price = quantity * 1.60
    elif type_of_fruit == "kiwi":
        price = quantity * 3.00
    elif type_of_fruit == "pineapple":
        price = quantity * 5.60
    elif type_of_fruit == "grapes":
        price = quantity * 4.20
    else:
        condition = False
else:
    condition = False

if condition:
    print(f"{price:.2f}")
else:
    print('error')
