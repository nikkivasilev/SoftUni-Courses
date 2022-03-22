firs_word = input()
second_word = input()

for i in range(len(firs_word)):
    replacement = second_word[i]
    if firs_word[i] != second_word[i]:
        word = firs_word[0:i] + replacement + firs_word[i + 1:]
        firs_word = word
        print(firs_word)
