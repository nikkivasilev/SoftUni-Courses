def upper(word):
    upper_list = []
    for n in range(len(word)):
        if word[n].isupper():
            upper_list.append(n)
    return upper_list


input = input()
print(upper(input))
