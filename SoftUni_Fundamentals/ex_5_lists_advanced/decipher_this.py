sentence = input().split(" ")

for current_word in sentence:
    current_word_list = [char for char in current_word]
    current_num_list = []
    for char in current_word:
        if char.isdigit():
            current_num_list.append(char)
    current_num = int("".join(current_num_list))
    first_letter = chr(current_num)

    for char in range(len(current_num_list)):
        current_word_list.remove(current_word_list[0])
    current_word_list.insert(0, first_letter)
    current_word_list[1], current_word_list[-1] = current_word_list[-1], current_word_list[1]
    final_word = ''.join(current_word_list)
    print(final_word, end=" ")



