from flask import Flask, request
from flask import typing as flask_typing

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

    return {
               "message": f"Data retrieved successfully from API: date:'{date}, raw_dir:'{raw_dir}'",
           }, 201


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8081)