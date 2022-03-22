import re

data = input()

maches = re.finditer(r"(?<=\s_)[A-Za-z0-9]+\b", data)
m = []
for mach in maches:
    m.append(mach.group())

print(",".join(m))

