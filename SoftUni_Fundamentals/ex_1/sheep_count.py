def sheep_count(count):
    for sheep in range(1, count + 1):
        current_sheep = f"{sheep} sheep..."
        print(current_sheep, end="")


count = (int(input()))
sheep_count(count)
