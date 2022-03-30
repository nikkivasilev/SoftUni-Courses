import re
import math
text = input()
emoji_pattern = r"(::|\*\*)([A-Z][a-z]{2,})\1"

matches = re.finditer(emoji_pattern, text)
emojis = []
for match in matches:
    emojis.append(match.group())


threshold_pattern = r"\d"
digits = re.findall(threshold_pattern, text)
digits = [int(digit) for digit in digits]
threshold = 1
for digit in digits:
    threshold *= digit
cool = []
for emoji in emojis:
    current_sum = 0
    for char in emoji:
        current_sum += ord(char)
    if current_sum > threshold:
        cool.append(emoji)

print(f"Cool threshold: {threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for cur in cool:
    print(cur)