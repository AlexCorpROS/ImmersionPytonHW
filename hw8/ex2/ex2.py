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
def get_dir_size():
    pass
    
def save_results_to_json():
    pass
    
def save_results_to_csv():
    pass
    
def save_results_to_pickle():
    pass
    
def traverse_directory():
    pass
    
'''

with open("__init__.py", "w") as init_file:
    init_file.write(code_to_write)
