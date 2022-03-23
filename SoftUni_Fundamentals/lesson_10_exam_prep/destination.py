import re

text = input()
regex = r"([=/])([A-Z][A-Za-z]{2,})\1"

matches = re.finditer(regex, text)

cities = []
points = 0

for match in matches:
    cities.append(match[2])
    points += len(match[2])
output = ", ".join(cities)

print(f"Destinations: {output}")
print(f"Travel Points: {points}")
