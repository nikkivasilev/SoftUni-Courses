def char_sum(number):
    total_sum = 0

    for _ in range(number):
        char = input()
        total_sum += ord(char)
    return total_sum


number = int(input())


print(f"The sum equals: {char_sum(number)}")