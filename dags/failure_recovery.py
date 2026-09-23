from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator


def failing_task():
    print("This task will fail")
    raise ValueError("Intentional failure for testing")


def success_task():
    print("Failure was handled successfully")


with DAG(
    dag_id="failure_recovery",
    start_date=datetime(2026, 9, 23),
    schedule=None,
    catchup=False,
) as dag:

    fail = PythonOperator(
        task_id="fail",
        python_callable=failing_task,
    )

    recover = PythonOperator(
        task_id="recover",
        python_callable=success_task,
        trigger_rule="all_done",
    )

    fail >> recover
