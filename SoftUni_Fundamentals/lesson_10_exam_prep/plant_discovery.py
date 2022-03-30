num_of_lines = int(input())

plants_dict = {}

for _ in range(num_of_lines):
    current = input().split("<->")
    plant = current[0]
    rarity = int(current[1])

    plants_dict[plant] = [rarity, []]

while True:
    command = input().split(": ")

    if command[0] == "Exhibition":
        break
    items = command[1].split(" - ")
    if items[0] not in plants_dict:
        print("error")
        continue
    if command[0] == 'Rate':
        plant = items[0]
        rating = int(items[1])
        plants_dict[plant][1].append(rating)

    elif command[0] == 'Update':
        plant = items[0]
        new_rarity = int(items[1])
        plants_dict[plant][0] = new_rarity
    elif command[0] == 'Reset':
        plant = command[1]
        plants_dict[plant][1] = []
print(f"Plants for the exhibition:")

for current_plant in plants_dict:
    plant = current_plant
    rarity = plants_dict[plant][0]
    if len(plants_dict[plant][1]) > 0:
        average_rating = sum(plants_dict[plant][1]) / len(plants_dict[plant][1])
    else:
        average_rating = 0
    print(f"- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")