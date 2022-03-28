num_of_pieces = int(input())

pieces_dict = {}

for current in range(num_of_pieces):
    current_piece = input().split("|")
    piece = current_piece[0]
    composer = current_piece[1]
    key = current_piece[2]
    pieces_dict[piece] = [composer, key]

while True:
    command = input().split("|")

    if command[0] == "Stop":
        break

    elif command[0] == "Add":
        piece = command[1]
        composer = command[2]
        key = command[3]
        if piece not in pieces_dict:
            pieces_dict[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif command[0] == "Remove":
        piece = command[1]
        if piece in pieces_dict:
            print(f"Successfully removed {piece}!")
            del pieces_dict[piece]
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command[0] == "ChangeKey":
        piece = command[1]
        new_key = command[2]
        if piece in pieces_dict:
            print(f"Changed the key of {piece} to {new_key}!")
            pieces_dict[piece][1] = new_key
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")


for item in pieces_dict:
    piece = item
    composer = pieces_dict[item][0]
    key = pieces_dict[item][1]
    print(f"{piece} -> Composer: {composer}, Key: {key}")
