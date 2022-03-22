text_list = input().split('>')
result = []
to_add = 0
for item in text_list:
    if not item[0].isdigit():
        result.append(item)
    if item[0].isdigit():
        index = int(item[0]) + to_add
        if len(item) >= index:
            item = item[index:]
            if item == '':
                result.append('>')
            else:
                result.append(f'>{item}')
        else:
            result.append('>')
            to_add = index - len(item[0])

result = ''.join(result)
print(result)