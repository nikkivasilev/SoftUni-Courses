import re

text = input()
pattern = r"([#@]{1})(?P<word1>[a-zA-Z]{3,})\1\1(?P<word2>[a-zA-Z]{3,})\1"

matches = re.finditer(pattern, text)
right_matches = []
pairs = 0
condition_pairs = False
condition_mirrored = False
for match in matches:
    condition_pairs = True
    pairs += 1
    first_word = match.group("word1")
    second_word = match.group("word2")
    reversed_second = second_word[::-1]
    if first_word == reversed_second:
        right_matches.append(f"{first_word} <=> {second_word}")
        condition_mirrored = True


if condition_pairs:
    print(f"{pairs} word pairs found!")
else:
    print(f"No word pairs found!")
if condition_mirrored:
    print("The mirror words are:")
    print(", ".join(right_matches))
else:
    print("No mirror words!")
