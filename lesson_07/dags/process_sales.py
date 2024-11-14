import pendulum

from airflow import DAG
from airflow.example_dags.plugins.workday import AfterWorkdayTimetable


with DAG(
    dag_id="example_after_workday_timetable_dag",
    start_date=pendulum.datetime(2021, 3, 10, tz="UTC"),
    schedule=AfterWorkdayTimetable(),
    tags=["example", "timetable"],
) as dag:

    def extract_data_from_api():
        pass

    def convert_to_avro():
        pass
