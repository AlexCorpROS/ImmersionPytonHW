from pathlib import Path

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