city = input()
sales_volume = float(input())
commissions = 0
condition = True

if city == 'Sofia':
    if 0 <= sales_volume <= 500:
        commissions = sales_volume * 0.05
    elif 500 < sales_volume <= 1000:
        commissions = sales_volume * 0.07
    elif 1000 < sales_volume <= 10000:
        commissions = sales_volume * 0.08
    elif 10000 < sales_volume:
        commissions = sales_volume * 0.12
    else:
        condition = False
elif city == 'Varna':
    if 0 <= sales_volume <= 500:
        commissions = sales_volume * 0.045
    elif 500 < sales_volume <= 1000:
        commissions = sales_volume * 0.075
    elif 1000 < sales_volume <= 10000:
        commissions = sales_volume * 0.1
    elif 10000 < sales_volume:
        commissions = sales_volume * 0.13
    else:
        condition = False

elif city == 'Plovdiv':
    if 0 <= sales_volume <= 500:
        commissions = sales_volume * 0.055
    elif 500 < sales_volume <= 1000:
        commissions = sales_volume * 0.08
    elif 1000 < sales_volume <= 10000:
        commissions = sales_volume * 0.12
    elif 10000 < sales_volume:
        commissions = sales_volume * 0.145
    else:
        condition = False

else:
    condition = False

if condition:
    print(f'{commissions:.2f}')
if not condition:
    print('error')


