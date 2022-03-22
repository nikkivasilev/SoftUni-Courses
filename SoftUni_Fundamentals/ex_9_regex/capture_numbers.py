import re

data = ''
while True:
    curr = input()
    if curr == "":
        break
    else:
        data += curr


output = re.finditer(r"\d[0-9]*", data)

for match in output:
    print(match.group(), end=" ")
