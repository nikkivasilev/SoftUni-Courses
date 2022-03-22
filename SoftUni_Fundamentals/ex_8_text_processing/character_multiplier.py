string = input().split()
word1 = string[0]
word2 = string[1]
total_sum = 0
if len(word1) <= len(word2):
    for ch in range(len(word1)):
        total_sum += ord(word1[ch]) * ord(word2[ch])
    if len(word1) < len(word2):

        diff = len(word2) - len(word1)
        for char in range(len(word2) - diff, len(word2)):
            total_sum += ord(word2[char])

elif len(word1) > len(word2):
    for ch in range(len(word2)):
        total_sum += ord(word1[ch]) * ord(word2[ch])
    diff = len(word1) - len(word2)
    for char in range(len(word1) - diff, len(word1)):
        total_sum += ord(word1[char])

print(total_sum)
