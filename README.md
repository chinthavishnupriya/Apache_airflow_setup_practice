# Apache Airflow Setup & Practice

This repository contains the Apache Airflow practical work completed during the learning sessions.

## Environment

- Apache Airflow 3.3.2
- Python 3.11
- Linux / Ubuntu
- Local Airflow installation with `airflow standalone`
- DAG folder: `~/airflow/dags`

## Completed Practical Work

### Core Airflow
- DAG creation and registration
- PythonOperator
- Task dependencies
- Manual DAG triggering
- Scheduling and cron expressions
- Retries
- Task timeouts
- BashOperator
- Variables
- Connections
- Sensors
- Branching
- Dynamic Task Mapping
- TaskFlow API
- Jinja templating
- Logical dates and data intervals
- Trigger rules
- Task Groups
- Callbacks
- Task testing/debugging
- Pools and task concurrency
- Backfill
- Rerun
- Failure handling and recovery
- Simple ETL workflow

## DAGs

### `hello_airflow.py`
Basic PythonOperator DAG that prints a Hello World message.

### `dependency_demo.py`
Demonstrates a linear dependency:

```
start -> process -> finish
```

### `backfill_test.py`
Used to practice historical DAG runs, backfill creation, task clearing, and rerun verification.

### `failure_recovery.py`
Demonstrates intentional task failure and recovery using:

```python
trigger_rule="all_done"
```

The `fail` task fails intentionally while `recover` succeeds.

### `simple_etl_dag.py`
Demonstrates the basic ETL workflow:

```
extract -> transform -> load
```

All three tasks were executed successfully.

## Verification

The practical DAGs were registered, triggered, and verified using Airflow CLI commands such as:

```bash
airflow dags list
airflow dags trigger <dag_id>
airflow dags list-runs <dag_id>
airflow tasks states-for-dag-run <dag_id> <run_id>
```

## Learning Status

The Airflow material supplied for this practice was completed, including the final Simple ETL exercise.
