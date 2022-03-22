input_num = int(input())
output_num = input()
bin_num = bin(input_num)

one = []
zero = []
for char in str(bin_num):
    if char == "0":
        zero.append(char)
    elif char == '1':
        one.append(char)

zero.remove("0")

if output_num == "1":
    print(len(one))

else:
    print(len(zero))

