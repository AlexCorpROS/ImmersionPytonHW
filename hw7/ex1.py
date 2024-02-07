'''Напишите функцию группового переименования файлов в папке test_folder под названием rename_files.
Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
f. Папка test_folder доступна из текущей директории'''

import os
from pathlib import Path
import shutil


'''def rename_files(desired_name: str, num_digits: int = 2, source_ext: str = None, target_ext: str = None, range_original: range = (0, 0),
                 path: str = None):
    if target_ext is None:
         target_ext = source_ext
    w_path = Path.cwd() if path is None else Path(path)
    count = 0
    for p in w_path.iterdir():
        if p.is_file() and p.suffix == f'.{source_ext}':
            file_name = f'{p.stem[range_original[0]:range_original[1]]}{desired_name}{count:03}.{target_ext}'
            p.rename(Path(p.parent,  file_name))
            count += 1
    return count


rename_files(desired_name="new", num_digits=3, source_ext="doc", target_ext="txt")'''

def rename_files(desired_name: str, num_digits: int = 2, source_ext: str = None, target_ext: str = None, range_original: range = (0, 0),
                 path: str = None):
    if target_ext is None:
         target_ext = source_ext
    w_path = Path(Path.cwd() / 'test_folder') if path is None else Path(path)
    count = 1
    for p in w_path.iterdir():
        if p.is_file() and p.suffix == f'.{source_ext}':
            file_name = f'{p.stem[range_original[0]:range_original[1]]}{desired_name}{str(count).zfill(num_digits)}.{target_ext}'
            p.rename(Path(p.parent,  file_name))
            count += 1
    return count

if __name__ == '__main__':
    import os
    import shutil

    # Создать тестовую папку
    folder_name = "test_folder"
    folder_path = os.path.join(os.getcwd(), folder_name)
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path)

    # Заполнить тестовую папку
    file_name = "test1.txt"
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "w") as file:
        file.write("This is a test file.\n")
        file.close()

# Заполнить тестовую папку
    for i in range(10):
        file_name = f"test{i}.txt"
        file_path = os.path.join(folder_path, file_name)

        with open(file_path, "w") as file:
            file.write("This is a test file.\n")
            file.close()

    file_name = "test.doc"
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "w") as file:
        file.write("This is a test file.\n")
        file.close()



rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")