func ='''from pathlib import Path

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
    return count'''

with open('__init__.py', 'w', encoding='utf-8') as f:
    f.write(func)


"""Пример из автотеста"""
code_to_write = '''
import os

def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
    new_names = []

    files = os.listdir('geekbrains')

    filtered_files = [file for file in files if file.endswith(source_ext)]

    filtered_files.sort()

    num = 1

    for file in filtered_files:
        name = os.path.splitext(file)[0]

        if name_range:
            name = name[name_range[0]-1:name_range[1]]

        new_name = desired_name + str(num).zfill(num_digits) + '.' + target_ext

        os.rename(file, new_name)

        new_names.append(new_name)

        num += 1

    return new_names
'''

with open("__init__.py", "w") as init_file:
    init_file.write(code_to_write)


