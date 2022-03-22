substrings = input().split(", ")
strings = input()
result = [el for el in substrings if el in strings]

print(result)
