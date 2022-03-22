words = input().split(" ")
palindrome = (input())
palindromes = []

for word in words:
    rev_list = reversed(word)
    rev_word = ''.join(rev_list)
    if rev_word == word:
        palindromes.append(word)


print(palindromes)
palindrome_count = words.count(palindrome)
print(f"Found palindrome {palindrome_count} times")