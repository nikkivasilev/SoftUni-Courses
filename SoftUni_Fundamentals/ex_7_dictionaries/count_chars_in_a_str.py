word = input()

my_dict = {}

for ch in word:
    if ch not in my_dict and ch != " ":
        my_dict[ch] = 1
    elif ch != " ":
        my_dict[ch] += 1

for key, value in my_dict.items():
    print(f"{key} -> {value}")
