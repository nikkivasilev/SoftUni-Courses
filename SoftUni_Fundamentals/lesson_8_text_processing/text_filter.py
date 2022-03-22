filters = input().split(", ")
text = input()

for word in filters:
    while word in text:
        stars = '*' * len(word)
        text = text.replace(word, stars)

print(text)