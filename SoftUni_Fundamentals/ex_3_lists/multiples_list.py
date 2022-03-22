def multiples(factor, count):
    multiples_list = list()
    new_num = factor
    for i in range(count):
        multiples_list.append(new_num)
        new_num += factor
    print(multiples_list)


factor = int(input())
count = int(input())
multiples(factor, count)

