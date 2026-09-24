from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="weekly_customer_report",
    start_date=datetime(2026, 9, 1),
    schedule="0 8 * * 1",
    catchup=False,
) as dag:

    generate_report = BashOperator(
        task_id="generate_report",
        bash_command='echo "Generating weekly customer report"',
    )
