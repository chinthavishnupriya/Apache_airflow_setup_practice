from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="customer_pipeline",
    start_date=datetime(2026, 9, 1),
    schedule=None,
    catchup=False,
) as dag:

    start = BashOperator(
        task_id="start",
        bash_command="echo 'Pipeline started'",
    )

    validate = BashOperator(
        task_id="validate_data",
        bash_command="echo 'Validating customer data'",
    )

    clean = BashOperator(
        task_id="clean_data",
        bash_command="echo 'Cleaning customer data'",
    )

    load = BashOperator(
        task_id="load_data",
        bash_command="echo 'Loading customer data'",
    )

    finish = BashOperator(
        task_id="finish",
        bash_command="echo 'Pipeline completed'",
    )

    start >> [validate, clean]
    [validate, clean] >> load
    load >> finish
