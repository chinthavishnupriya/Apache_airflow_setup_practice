from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime


with DAG(
    dag_id="customer_360",
    start_date=datetime(2026, 9, 1),
    schedule=None,
    catchup=False,
) as dag:

    start = BashOperator(
        task_id="start",
        bash_command="echo 'Starting Customer 360'",
    )

    crm = BashOperator(
        task_id="ingest_crm",
        bash_command="echo 'Reading CRM data'",
    )

    transactions = BashOperator(
        task_id="ingest_transactions",
        bash_command="echo 'Reading transaction data'",
    )

    support = BashOperator(
        task_id="ingest_support",
        bash_command="echo 'Reading support data'",
    )

    process = BashOperator(
        task_id="process_customer_data",
        bash_command="echo 'Processing Customer 360 data'",
    )

    spark = BashOperator(
        task_id="spark_processing",
        bash_command="echo 'Running Spark customer processing'",
    )

    hive = BashOperator(
        task_id="load_hive",
        bash_command="echo 'Loading Customer 360 data into Hive'",
    )

    hbase = BashOperator(
        task_id="load_hbase",
        bash_command="echo 'Uploading Customer 360 data to HBase'",
    )

    notify = BashOperator(
        task_id="notify_downstream",
        bash_command="echo 'Customer 360 pipeline completed successfully'",
    )

    start >> [crm, transactions, support]
    [crm, transactions, support] >> process
    process >> spark >> hive >> hbase >> notify
