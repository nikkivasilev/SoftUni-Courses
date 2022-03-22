def special(number):
    for n in range(1, number + 1):
        working_number = n
        digit_sum = 0
        while working_number > 0:
            digit_sum += working_number % 10
            working_number = working_number // 10

        is_special = digit_sum == 5 or digit_sum == 7 or digit_sum == 11
        print(f"{n} -> {is_special}")


in_num = int(input())

special(in_num)