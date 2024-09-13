def custom_write(file_name, strings):
    strings_position = {}
    file = open(file_name, 'w', encoding='utf-8')
    for number_str, string in enumerate(strings, 1):
        strings_position[(number_str, file.tell())] = string
        file.write(string + '\n')
    file.close()
    return strings_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
