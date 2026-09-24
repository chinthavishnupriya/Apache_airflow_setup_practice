from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="etl_ui_practice",
    start_date=datetime(2026, 9, 1),
    schedule=None,
    catchup=False,
) as dag:

    extract = BashOperator(
        task_id="extract",
        bash_command="echo 'Extracting data'",
    )

    transform = BashOperator(
        task_id="transform",
        bash_command="echo 'Transforming data'",
    )

    load = BashOperator(
        task_id="load",
        bash_command="echo 'Loading data'",
    )

    notify = BashOperator(
        task_id="notify",
        bash_command="echo 'ETL completed successfully'",
    )

    extract >> transform >> load >> notify
