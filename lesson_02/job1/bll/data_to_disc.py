import json
import os
import shutil
from pathlib import Path
from get_data_from_api import GetDataFromAPI

def create_dir(path: Path = None) -> None:
    if os.path.exists(path):
        if os.listdir(path):
            shutil.rmtree(path)
    os.makedirs(path, exist_ok=True)


def create_file(path : Path = None, data: GetDataFromAPI = None) -> None:
    for number, file  in enumerate(data.purchase_list):
        with open(path/f"sales_{file["purchase_date"]}_{number}.json", "w") as f:
            json.dump(file, f)


def data_to_disc(raw_dir : str = "raw_directory") -> None:
    path = Path(__file__).parent.parent / raw_dir
    data = GetDataFromAPI()
    data.main()
    assert data.status_code == 200, f"Could not get data from API. Status code: {data.status_code}"
    create_dir(path)
    create_file(path, data)




if __name__ == '__main__':
    data_to_disc()