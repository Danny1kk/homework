def custom_write(file_name, strings):
    strings_positions = {}
    line_number = 1

    file = open(file_name, 'w', encoding= 'utf_8')

    for line in strings:
        position = file.tell()
        file.write(line + '\n')
        strings_positions[(line_number, position)] = line
        line_number += 1

    file.close()
    return strings_positions


# Пример выполняемого кода:
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
