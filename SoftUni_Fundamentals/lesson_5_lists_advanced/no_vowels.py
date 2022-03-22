vowels = ["a", "e", "i", "o", "u"]
text = input()
no_vowels = [ch for ch in text if ch not in vowels]

print("".join(no_vowels))
