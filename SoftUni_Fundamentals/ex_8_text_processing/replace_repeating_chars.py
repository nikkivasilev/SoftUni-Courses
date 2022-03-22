text = input()
new = []
text += " "
for ch in range(len(text) - 1):
    if text[ch] != text[ch + 1]:
        new.append(text[ch])
    else:
        pass
print("".join(new))

