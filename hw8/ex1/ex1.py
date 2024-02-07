'''Путь к файлу или директории: Абсолютный путь к файлу или директории. Тип объекта: Это файл или директория.
Размер: Для файлов - размер в байтах, для директорий - размер, учитывая все вложенные файлы и директории в байтах. Важные детали:
Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.
Для файлов сохраните их размер в байтах.
Для директорий, помимо их размера, учтите размер всех файлов и директорий, находящихся внутри данной директории, и вложенных директорий.
Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.
Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. Форматы файлов должны быть выбираемыми.
Для обхода файловой системы вы можете использовать модуль os.
Вам необходимо написать функцию traverse_directory(directory), которая будет выполнять обход директории и возвращать результаты в виде списка словарей. После этого результаты должны быть сохранены в трех различных файлах (JSON, CSV и Pickle) с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.'''

import os
import pickle
import json
import csv
from pathlib import Path

def get_directory_size(path):
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath,filename)
                total_size += os.path.getsize(filepath)
        return total_size


def get_directory_info(path):
    results = []
    for root, dirs, files in os.walk(path):
        dirname = str(Path(root).resolve())
        dirsize = get_directory_size(root)
        results.append({
            'Path' : dirname,
            'Type' : 'directory',
            'Size' : dirsize,
            'parent_directory' : os.path.dirname(root),

        })
        for file in files:
            filepath = os.path.join(root, file)
            filesize = get_directory_size(filepath)
            results.append({
                'Path' : file,
                'Type' : 'file',
                'Size' : filesize,
                'parent_directory' : os.path.dirname(filepath)
            })
    return results

def save_results_to_json(info: dict, file_name: str):
    with open(file_name, "w") as f:
        json.dump(info, f, indent=4)

def save_results_to_csv(info: dict, file_name: str):
    fieldnames = ['Path', 'Type', 'Size', 'parent_directory']
    with open(file_name, 'w', encoding = 'UTF-8', newline = '') as f:
        writer = csv.DictWriter(f, dialect = 'excel', quoting = csv.QUOTE_MINIMAL, fieldnames = fieldnames)
        # writer.writeheader()
        writer.writerows(info)

def save_results_to_picle(info: dict, file_name: str):
    with open(file_name, "wb") as f:
        pickle.dump(info, f)

def traverse_directory(path = '.'):
    results  = get_directory_info(path)

    json_output_file = 'output.json'
    save_results_to_json(results, json_output_file)
    print(f'Save results to {json_output_file}')

    csv_output_file = 'output.csv'
    save_results_to_csv(results, csv_output_file)
    print(f'Save results to {csv_output_file}')

    picle_output_file = 'output.picle'
    save_results_to_picle(results, picle_output_file)
    print(f'Save results to {picle_output_file}')

directory = 'geekbrains'
results = traverse_directory(directory)
print(results)

