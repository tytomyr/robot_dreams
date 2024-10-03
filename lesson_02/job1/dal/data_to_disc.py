import json
import os
import shutil
from pathlib import Path
from lesson_02.job1.bll.get_data_from_api import GetDataFromAPI

def create_file(raw_dir: str, data: GetDataFromAPI = None) -> None:
    path = Path(__file__).parent.parent / raw_dir
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path/"sales", exist_ok=True)
    for number, file  in enumerate(data.purchase_list):
        with open(path/"sales"/f"sales_{file["purchase_date"]}_{number + 1}.json", "w") as f:
            json.dump(file, f)


def main(raw_dir : str, data: GetDataFromAPI):
    create_file(raw_dir, data)
