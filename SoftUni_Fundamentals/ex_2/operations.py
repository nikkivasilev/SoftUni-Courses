def operator(n1,n2,n3,n4):
    n2 += n1
    n2 = int(n2 / n3)
    n2 *= n4
    return n2


n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

print(operator(n1,n2,n3,n4))
