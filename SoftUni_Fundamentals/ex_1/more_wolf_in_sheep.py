def wolf_finder(list_input):
    for n in range(len(list_input)):
        if list_input[n] == 'wolf' and n == 0:
            print("Please go away and stop eating my sheep")
        elif list_input[n] == 'wolf':
            print(f"Oi! Sheep number {n}! You are about to be eaten by a wolf!")


list_input = input().split(", ")
list_input.reverse()

wolf_finder(list_input)
