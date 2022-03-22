def updater(current_version):
    current_version = 0
    current_version += 100 * start_version[0]
    current_version += 10 * start_version[1]
    current_version += start_version[2]
    return current_version


start_version = list(map(int, input().split(".")))

new_version = updater(start_version) + 1
string = str(new_version)
print(f"{string[0]}.{string[1]}.{string[2]}")

