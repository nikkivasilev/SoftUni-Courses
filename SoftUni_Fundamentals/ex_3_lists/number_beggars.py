numbers_list = list(map(int, input().split(", ")))
number_of_beggars = int(input())

beggars_list = [0] * number_of_beggars

for num in range(len(beggars_list)):
    current_beggar = num
    for n in range(len(numbers_list)):
        current_num = n % number_of_beggars
        if current_num == current_beggar:
            if beggars_list[num] == 0:
                if numbers_list[n] == 0:
                    beggars_list[current_num] = 0
                    break
                beggars_list[current_num] = numbers_list[n]
            else:
                beggars_list[current_num] += numbers_list[n]

print(beggars_list)


# num_string = input()
# beggars = int(input())
#
# num_list = num_string.split(', ')
# result_sum, result_list = 0, []
#
# for n in range(beggars):
#     for i in range(n, len(num_list), beggars):
#         result_sum += int(num_list[i])
#     result_list.append(result_sum)
#     result_sum = 0
#
# print(result_list)
