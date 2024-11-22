from flask import Flask, request
from flask import typing as flask_typing

from lesson_02.job1.bll.get_data_from_api import GetDataFromAPI
from lesson_02.job1.dal import data_to_disc
app = Flask(__name__)

@app.route('/', methods=['POST'])
def main() -> flask_typing.ResponseReturnValue:
    input_data: dict = request.json
    for key in ['date', 'raw_dir']:
        try:
            input_data[key]
        except KeyError:
            return {
                "message": f"{key} parameter missed",
            }, 400
    date = input_data.get('date')
    raw_dir = input_data.get('raw_dir')
    data = GetDataFromAPI()
    data.main()
    assert data.status_code == 200, f"Could not get data from API. Status code: {data.status_code}"
    if data.purchase_list[0]["purchase_date"] != date:
        return 'No records for this date'
    data_to_disc.main(raw_dir=raw_dir, data=data)
    return {
               "message": f"Data retrieved successfully from API: date:'{date}, raw_dir:'{raw_dir}'",
           }, 201


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8081)
