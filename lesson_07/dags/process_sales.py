import os

import pendulum
import requests

from airflow import DAG
from airflow.decorators import task
from airflow.example_dags.plugins.workday import AfterWorkdayTimetable

BASE_DIR = "/home/tytomyr/rd_/robot_dreams/storage"

if not BASE_DIR:
    print("BASE_DIR environment variable must be set")
    exit(1)

JOB1_PORT = 8081
JOB2_PORT = 8082

RAW_DIR = os.path.join(BASE_DIR, "raw", "sales", "2022-08-09")
STG_DIR = os.path.join(BASE_DIR, "stg", "sales", "2022-08-09")

with DAG(
    dag_id="process_sales",
    start_date=pendulum.datetime(2022, 8, 9, tz="UTC"),
    end_date=pendulum.datetime(2022, 8, 11, tz="UTC"),
    schedule="0 1 * * *",
) as dag:

    @task(task_id="extract_data_from_api")
    def extract_data_from_api():
        resp = requests.post(
            url=f'http://localhost:{JOB1_PORT}/',
            json={
                "date": "2022-08-09",
                "raw_dir": RAW_DIR
            }
        )
        assert resp.status_code == 201


    @task(task_id="convert_to_avro")
    def convert_to_avro():
        resp = requests.post(
            url=f'http://localhost:{JOB2_PORT}/',
            json={
                "raw_dir": RAW_DIR,
                "stg_dir": STG_DIR
            }
        )
        assert resp.status_code == 201


    extract_data_from_api() >> convert_to_avro()
