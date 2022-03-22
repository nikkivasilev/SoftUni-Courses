numbers = list(map(int, input().split(", ")))
even_index_numbers = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_index_numbers.append(i)

print(even_index_numbers)
