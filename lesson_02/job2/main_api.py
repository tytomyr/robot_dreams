from flask import Flask, request
from pathlib import Path
from flask import typing as flask_typing
app = Flask(__name__)

@app.route('/', methods=['POST'])
def main() -> flask_typing.ResponseReturnValue:
    input_data: dict = request.json
    for key in ['stg_dir', 'raw_dir']:
        try:
            input_data[key]
        except KeyError:
            return {
                "message": f"{key} parameter missed",
            }, 400
    stg_dir = Path(__file__).parents[3] / "storage"/ f"{input_data.get('stg_dir')}"
    raw_dir = Path(__file__).parents[3] / "storage"/ f"{input_data.get('raw_dir')}"

    return {
               "message": f"Data retrieved successfully",
           }, 201


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8082)
