import os
import time

directory = '.'

for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(os.getcwd())
        file_time = os.path.getatime('module_7_4.py')
        formatted_time = time.strftime('%d.%m.%Y %H:%M', time.localtime(file_time))
        file_size = os.path.getsize('module_7_4.py')
        parent_dir = os.path.dirname(file)
        print(f'Найден файл:{file}, Путь:{file_path}, Размер файла:{file_size} байт, Время изменения:{formatted_time}, Родительская директория:{parent_dir} ')