snowballz = int(input())
best_snowball = 0
best_snowball_data = ''
for _ in range(snowballz):
    weight = int(input())
    time = int(input())
    quality = int(input())

    result = (weight / time) ** quality
    if result > best_snowball:
        best_snowball = result
        best_snowball_data = f"{weight} : {time} = {int(result)} ({quality})"

print(best_snowball_data)
