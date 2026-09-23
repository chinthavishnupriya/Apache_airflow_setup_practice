from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator


def process_data():
    print("Processing historical data")


with DAG(
    dag_id="backfill_test",
    start_date=datetime(2026, 9, 20),
    schedule="@daily",
) as dag:

    process = PythonOperator(
        task_id="process_data",
        python_callable=process_data,
    )
