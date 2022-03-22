def reverse_word(word):
    for n in range(len(word) - 1, -1, -1):
        print(word[n], end="")


word = input()

reverse_word(word)