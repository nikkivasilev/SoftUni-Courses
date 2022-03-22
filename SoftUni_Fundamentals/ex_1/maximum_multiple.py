def maximum(divisor, boundary):
    max = (boundary // divisor) * divisor
    return max


divisor = int(input())
boundary = int(input())

print(maximum(divisor, boundary))
