string = input()
encrypted = [chr(ord(ch) + 3) for ch in string]

print("".join(encrypted))
