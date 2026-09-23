# Airflow Practical Outputs

This document records verified Apache Airflow practice results and the corresponding UI evidence supplied during the practice session.

## Environment

- Apache Airflow: 3.3.2
- Python: 3.11.x
- OS: Ubuntu/Linux
- AIRFLOW_HOME: `~/airflow`
- DAG folder: `~/airflow/dags`
- Local UI: `http://localhost:8080`
- Executor: LocalExecutor

## Hello Airflow

The `hello_airflow` DAG was triggered manually and completed successfully.

Verified UI evidence:
- `hello_airflow_run_success.png`
- `hello_airflow_task_logs.png`

The task log shows the Python task output:
`Hello from Airflow!`

## Task Dependencies

DAG:

```
start -> process -> finish
```

The dependency workflow was triggered and completed successfully.

Evidence:
- `dependency_demo_tasks.png`

## Backfill and Rerun

Backfill was tested for:

```
2026-09-20
2026-09-21
2026-09-22
```

All three backfill runs completed successfully.

Rerun verification:

```
airflow tasks states-for-dag-run backfill_test backfill__2026-09-20T00:00:00+00:00
```

Result:

```
process_data | success
```

Evidence:
- `backfill_task_log.png`
- `backfill_run_success.png`
- `backfill_dag_overview.png`

## Failure Handling and Debugging

An intentional task failure was used to verify Airflow failure handling and logs.

Evidence:
- `failure_task_alert.png`
- `failure_task_error.png`

The logs show the task entering the failed state and the intentional exception.

## Failure Recovery

The `failure_recovery` DAG uses:

```python
trigger_rule="all_done"
```

Verified result:

```
fail     | failed
recover  | success
```

The recovery workflow completed successfully.

Evidence:
- `failure_recovery.png`

## Pools and Concurrency

The pool exercise demonstrated tasks running according to the configured pool capacity.

Evidence:
- `pool_running.png`
- `pool_completed.png`

## Dynamic Task Mapping / ETL-Style Workflow

The supplied UI evidence shows mapped extract/transform/load task instances completing successfully.

Evidence:
- `dynamic_etl_mapped_tasks.png`

## Other Airflow Features

Additional supplied evidence covers:

- Airflow home/health: `airflow_home.png`
- DAG list: `dag_list.png`
- BashOperator and logical-date output: `bash_operator_output.png`
- TaskFlow API output: `taskflow_output.png`

## Final Simple ETL Verification

The final `simple_etl_dag` was also verified from the terminal:

```
extract   | success
transform | success
load      | success
```

DAG run:

```
manual__2026-09-23T13:42:04.305701+00:00
```

### Missing screenshot

A dedicated UI screenshot of this final `simple_etl_dag` run was **not included in the screenshots supplied in the conversation**.

To capture it:

```
Airflow UI
  -> DAGs
  -> simple_etl_dag
  -> latest successful run
  -> Task Instances
```

Capture the page showing `extract`, `transform`, and `load` as **Success**, then save it as:

```
docs/screenshots/simple_etl_final.png
```

## Import and Service Checks

Useful verification commands used during practice:

```bash
airflow dags list-import-errors
airflow jobs check --job-type SchedulerJob
airflow jobs check --job-type DagProcessorJob
```

The DAG import check returned:

```
No data found
```

Scheduler and DAG processor health were also verified during troubleshooting.

## Final Verified DAG Results

| DAG | Result |
|---|---|
| `dependency_demo` | SUCCESS |
| `backfill_test` | SUCCESS |
| `failure_recovery` | SUCCESS |
| `simple_etl_dag` | SUCCESS |
