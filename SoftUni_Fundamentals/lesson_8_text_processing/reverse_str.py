
string_dict = {}

while True:
    current_str = input()
    reversed_str = ''
    if current_str == "end":
        break
    for ch in reversed(current_str):
        reversed_str += ch
    string_dict[current_str] = reversed_str

for key, value in string_dict.items():
    print(f"{key} = {value}")
