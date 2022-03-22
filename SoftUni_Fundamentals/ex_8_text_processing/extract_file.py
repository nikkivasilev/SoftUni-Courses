splitter = '\ '
splitter = splitter.strip(' ')
data_list = input().split(splitter)
useful_info = [item for item in data_list if '.' in item]
output_item = ''.join(useful_info)
output = output_item.split(".")
print(f'File name: {output[0]}')
print(f'File extension: {output[1]}')
