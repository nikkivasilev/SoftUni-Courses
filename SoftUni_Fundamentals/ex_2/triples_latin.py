def latin_triples(num_of_letters):
    for i in range(0, num_of_letters):
        for k in range(0, num_of_letters):
            for j in range(0, num_of_letters):
                print(F"{chr(97 + i)}{chr(97 + k)}{chr(97 + j)}")


num_of_letters = int(input())
latin_triples(num_of_letters)