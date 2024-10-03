import json
import os
import shutil
from pathlib import Path
from lesson_02.job1.bll.get_data_from_api import GetDataFromAPI


def create_dir(raw_dir: str, path: Path) -> None:
    dir_path = Path(__file__).parent.parent / raw_dir
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
    os.makedirs(path, exist_ok=True)


def create_file(path: Path, data: GetDataFromAPI) -> None:
    for number, file  in enumerate(data.purchase_list):
        with open(path/f"sales_{file["purchase_date"]}_{number + 1}.json", "w") as f:
            json.dump(file, f)


def main(raw_dir : str, data: GetDataFromAPI):
    path = Path(__file__).parent.parent / raw_dir / "sales" / data.purchase_list[0]["purchase_date"]
    create_dir(raw_dir=raw_dir, path=path)
    create_file(path=path, data=data)
