from airflow.sdk import dag, task
from datetime import datetime

@dag(
    dag_id="customer_360_taskflow",
    start_date=datetime(2026, 9, 1),
    schedule=None,
    catchup=False,
)
def customer_360_taskflow():

    @task
    def ingest_crm():
        print("Reading CRM data")
        return "CRM data"

    @task
    def ingest_transactions():
        print("Reading transaction data")
        return "Transaction data"

    @task
    def ingest_support():
        print("Reading support data")
        return "Support data"

    @task
    def process_customer_data(crm, transactions, support):
        print("Processing Customer 360 data")
        print(f"CRM: {crm}")
        print(f"Transactions: {transactions}")
        print(f"Support: {support}")
        return "Processed Customer 360 data"

    @task
    def spark_processing(data):
        print("Running Spark customer processing")
        print(data)
        return "Spark processed data"

    @task
    def load_hive(data):
        print("Loading Customer 360 data into Hive")
        print(data)
        return "Hive load completed"

    @task
    def load_hbase(data):
        print("Uploading Customer 360 data to HBase")
        print(data)
        return "HBase load completed"

    @task
    def notify(data):
        print("Customer 360 pipeline completed successfully")
        print(data)

    crm = ingest_crm()
    transactions = ingest_transactions()
    support = ingest_support()
    processed = process_customer_data(crm, transactions, support)
    spark = spark_processing(processed)
    hive = load_hive(spark)
    hbase = load_hbase(hive)
    notify(hbase)

customer_360_taskflow()
