from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator


def start():
    print("Starting workflow")


def process():
    print("Processing data")


def finish():
    print("Workflow completed")


with DAG(
    dag_id="dependency_demo",
    start_date=datetime(2026, 9, 23),
    schedule=None,
    catchup=False,
) as dag:

    start_task = PythonOperator(
        task_id="start",
        python_callable=start,
    )

    process_task = PythonOperator(
        task_id="process",
        python_callable=process,
    )

    finish_task = PythonOperator(
        task_id="finish",
        python_callable=finish,
    )

    start_task >> process_task >> finish_task
