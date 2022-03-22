import re
data = input()

# user_pattern = r"( |^)[a-zA-Z0-9]+((\.\-\_)[a-zA-Z0-9]+)*"
# host_pattern = r'([a-zA-Z]+(-[a-zA-Z]+)*)(\.[a-zA-Z]+(-[a-zA-Z]+)*)'

matches = re.finditer(r'( |^)([a-zA-Z0-9]+[-._]?[a-zA-Z0-9]+)@[a-zA-Z0-9]+([._-]?[a-zA-Z0-9]+)*\.[a-zA-Z0-9]+\b', data)
# pattern = rf'{user_pattern}@{host_pattern}'
# emails = re.finditer(pattern, data)


for match in matches:
    print(match.group().strip(" "))







