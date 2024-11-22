import os
import shutil
from pathlib import Path

def convert_files(stg_dir: Path = None, raw_dir: Path = None) -> None:
    print(stg_dir, raw_dir)
    directory = raw_dir
    new_directory = stg_dir

    files = [f.name for f in directory.iterdir() if f.is_file()]
    os.makedirs(new_directory, exist_ok=True)

    for file in files:
        base_name = os.path.basename(file).rsplit(".", 1)[0]
        new_file = os.path.join(new_directory, f"{base_name}.avro")
        shutil.copy(directory/file, new_file)

if __name__ == "__main__":
    convert_files()