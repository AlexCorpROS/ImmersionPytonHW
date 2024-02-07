from os import path


def get_file_info(file_path):
    full_name = path.basename(file_path)
    if full_name == "file":
        name = ""
        extension = ".file"
    else:
        name, extension = path.splitext(full_name)
    _path = file_path[0:-len(full_name)]
    return _path, name, extension

# def get_file_info(file_path):
#     file_name = file_path.split("/")[-1]
#     file_extension = file_name.split(".")[-1]
#     path = file_path[:-len(file_name)]
#     return (path, file_name[:-len(file_extension)-1], "." + file_extension)

print(get_file_info(file_path = 'file_in_current_directory.txt'))