'''Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

Пример использования.
На входе:
file_path = "C:/Users/User/Documents/example.txt"

На выходе:
('C:/Users/User/Documents/', 'example', '.txt')'''

"""import os

file_path = 'C:/Users/User/Documents/example.txt'

def get_file_info(path):
    filepath, file_extens = os.path.splitext(path)
    dirname, filename = os.path.split(filepath)
    return (dirname, filename, file_extens)"""

'''def get_file_info(**path):
    *filepath, file_extension = path.split('/')
    filename, file_extens = file_extension.split('.')
    file_extens = '.'+ file_extens
    filepath = '/'.join(filepath)+'/'
    return (filepath, filename, file_extens)'''


def get_file_info(**path):
    path = path['file_path']
    *filepath, file_extension = path.split('/')
    print(file_extension)
    if '.' in file_extension:
        *filename, file_extens = file_extension.split('.')
        filename = '.'.join(filename)
        file_extens = '.'+ file_extens
    else:
        filename = ''
        file_extens = '.' + file_extension
    if len(filepath) < 1:
        filepath = ''
    else:
        filepath = '/'.join(filepath)+'/'
    return (filepath, filename, file_extens)

print(get_file_info(file_path = 'file_in_current_directory.txt'))

