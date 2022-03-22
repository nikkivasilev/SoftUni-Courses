def largest(number):
    number_list = []
    for n in range(len(number)):
        number_list.append(number[n])

    number_list.sort()
    for n in range(len(number_list) - 1, -1, -1):
        print(number_list[n], end="")


num = input()
largest(num)
