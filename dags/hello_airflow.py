from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator


def say_hello():
    print("Hello World from Airflow!")


with DAG(
    dag_id="hello_airflow",
    start_date=datetime(2026, 9, 23),
    schedule=None,
    catchup=False,
) as dag:

    hello_task = PythonOperator(
        task_id="hello",
        python_callable=say_hello,
    )
