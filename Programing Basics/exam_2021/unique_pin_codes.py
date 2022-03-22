max_n1 = int(input())
max_n2 = int(input())
max_n3 = int(input())
nx = 0
ny = 0
nz = 0

for n1 in range(2, max_n1 + 1):
    if n1 % 2 == 0:
        nx = n1
    for n2 in range(2, max_n2 + 1):
        if n2 == 2 or n2 == 3 or n2 == 5 or n2 == 7:
            ny = n2
        for n3 in range(2, max_n3 + 1):
            if n3 % 2 == 0:
                nz = n3
                print(f"{nx} {ny} {nz}")

