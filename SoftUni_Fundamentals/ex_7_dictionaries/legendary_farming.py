legendary = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
winner = ''

while winner == '':
    materials = input().split(' ')

    for i in range(0, len(materials), 2):
        value = int(materials[i])
        key = materials[i+1].lower()

        if key in key_materials:
            key_materials[key] += value
            if key_materials[key] >= 250:
                winner = key
                break
        else:
            if key not in junk:
                junk[key] = 0
            junk[key] += value

key_materials[winner] -= 250
winner_item = legendary[winner]

print(f'{winner_item} obtained!')
for key, value in key_materials.items():
    print(f'{key}: {value}')
for key, value in junk.items():
    print(f'{key}: {value}')