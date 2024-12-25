def custom_write(file_name, strings):

    file = open(file_name, 'a', encoding= 'utf-8')
    n = 0
    b = 0
    key = ()
    strings_positions = {}
    for i in info:
        b += file.tell()
        file.write(i + '\n')
        n += 1
        key = (n, b)
        strings_positions[key] = i
    file.close()
    print(strings_positions)




info = ['Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!']


custom_write('test.txt', info)

