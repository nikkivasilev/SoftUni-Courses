import re
data = input()
pattern = r"[@#]+(?P<colour>[a-z]{3,})[@#]+[^A-Z-a-z-1-9]*[\/]+(?P<amount>[0-9]+)[\/]+"
matches = re.finditer(pattern, data)
valid_eggs = []
for match in matches:
    colour = match.group("colour")
    amount = match.group("amount")
    print(F"You found {amount} {colour} eggs!")