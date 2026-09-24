from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="daily_sales",
    start_date=datetime(2026, 9, 1),
    schedule="0 9 * * *",
    catchup=False,
) as dag:

    process_sales = BashOperator(
        task_id="process_sales",
        bash_command="echo 'Processing daily sales'",
    )
