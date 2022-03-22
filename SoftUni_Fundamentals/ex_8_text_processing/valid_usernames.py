input_names = input().split(", ")

for name in input_names:
    if 3 <= len(name) <= 16:
        if " " not in name:
            if name.isalnum():
                print(name)
            elif "-" in name or '_' in name:

                    print(name)