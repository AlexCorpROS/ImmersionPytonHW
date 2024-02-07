'''import os
import pickle
import json
import csv


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
        dirname = os.path.basename(root)
        dirsize = get_directory_size(root)
        results.append({
            'name' : dirname,
            'type' : 'directory',
            'size' : dirsize,
            'parent_directory' : os.path.dirname(root),

        })
        for file in files:
            filepath = os.path.join(root, file)
            filesize = get_directory_size(filepath)
            results.append({
                'name' : file,
                'type' : 'file',
                'size' : filesize,
                'parent_directory' : os.path.dirname(filepath)
            })
    return results

def save_results_to_json(info: dict, file_name: str):
    with open(file_name, "w") as f:
        json.dump(info, f, indent=2)

def save_results_to_csv(info: dict, file_name: str):
    fieldnames = ['name', 'type', 'size', 'parent_directory']
    with open(file_name, 'w', encoding = 'UTF-8', newline = '') as f:
        writer = csv.DictWriter(f, dialect = 'excel', quoting = csv.QUOTE_MINIMAL, fieldnames = fieldnames)
        writer.writeheader()
        # dict_info = []
        # _dict_info(info, dict_info)
        writer.writerows(info)

def save_results_to_picle(info: dict, file_name: str):
    with open(file_name, "wb") as f:
        pickle.dump(info, f)

def traverse_directory(path):
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

traverse_directory('.')'''

import os
import json
import csv
import pickle

def get_dir_size(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
        for d in dirnames:
            dp = os.path.join(dirpath, d)
            total_size += get_dir_size(dp)
    return total_size

def save_results_to_json(results, file_name):
    with open(file_name, 'w') as f:
        json.dump(results, f)

def save_results_to_csv(results, file_name):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Path', 'Type', 'Size'])
        for result in results:
            writer.writerow([result['Path'], result['Type'], result['Size']])

def save_results_to_pickle(results, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(results, f)

def traverse_directory(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            results.append({'Path': path, 'Type': 'File', 'Size': size})
        for name in dirs:
            path = os.path.join(root, name)
            size = get_dir_size(path)
            results.append({'Path': path, 'Type': 'Directory', 'Size': size})
    return results
