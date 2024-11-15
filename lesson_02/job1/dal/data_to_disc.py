import json
import os
import shutil
from pathlib import Path
from lesson_02.job1.bll.get_data_from_api import GetDataFromAPI


def create_dir(path: Path) -> None:
    shutil.rmtree(Path(__file__).parents[3] / "storage" )
    os.makedirs(path, exist_ok=True)


def create_file(path: Path, data: GetDataFromAPI) -> None:
    for number, file  in enumerate(data.purchase_list):
        with open(path/f"sales_{file["purchase_date"]}_{number + 1}.json", "w") as f:
            json.dump(file, f)


def main(raw_dir : str, data: GetDataFromAPI):
    path = Path(__file__).parents[3] / "storage"/ raw_dir / "sales" / data.purchase_list[0]["purchase_date"]
    create_dir(path=path)
    create_file(path=path, data=data)
