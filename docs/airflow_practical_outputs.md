# Airflow Practical Outputs

This document records the important CLI commands and verified results from the Apache Airflow practice sessions.

## Environment Verification

### Scheduler

Command:

```bash
airflow jobs check --job-type SchedulerJob
```

Result:

```
Found one alive job.
```

### DAG Processor

Command:

```bash
airflow jobs check --job-type DagProcessorJob
```

Result:

```
Found one alive job.
```

---

## Dependency Demo

Command:

```bash
airflow dags show dependency_demo
```

Verified graph:

```
start -> process -> finish
```

After unpausing and triggering, the DAG run completed successfully.

---

## Backfill

Command:

```bash
airflow backfill create \
  --dag-id backfill_test \
  --from-date 2026-09-20 \
  --to-date 2026-09-22 \
  --dry-run
```

Result: three historical runs were identified.

The actual backfill created runs for:

```
2026-09-20
2026-09-21
2026-09-22
```

All three completed successfully.

Rerun verification:

```bash
airflow tasks states-for-dag-run backfill_test backfill__2026-09-20T00:00:00+00:00
```

Output:

```
process_data | success
```

---

## Failure Recovery

DAG:

```
failure_recovery
```

Run:

```
manual__2026-09-23T09:31:29.989175+00:00
```

Final task states:

```
fail     | failed
recover  | success
```

Final DAG run:

```
success
```

Important configuration:

```python
trigger_rule="all_done"
```

This confirmed that the recovery task ran after the intentional upstream failure.

---

## Simple ETL

DAG:

```
simple_etl_dag
```

Workflow:

```
extract -> transform -> load
```

Trigger:

```bash
airflow dags trigger simple_etl_dag
```

Run:

```
manual__2026-09-23T13:42:04.305701+00:00
```

DAG run result:

```
success
```

Task verification:

```
extract   | success
transform | success
load      | success
```

This is the final verified ETL result.

---

## DAG Registration

Example command:

```bash
airflow dags list | grep simple_etl_dag
```

Verified after Airflow/DAG-processor restart:

```
simple_etl_dag | /home/vishnupriya/airflow/dags/simple_etl_dag.py | airflow | False
```

`False` indicates the DAG was unpaused.

---

## Import Error Check

Command:

```bash
airflow dags list-import-errors
```

Result during the ETL setup:

```
No data found
```

This confirmed that Airflow reported no DAG import errors.

---

## Commands Used Throughout Practice

```bash
airflow dags list
airflow dags show <dag_id>
airflow dags trigger <dag_id>
airflow dags list-runs <dag_id>
airflow dags unpause <dag_id>
airflow dags pause <dag_id>
airflow dags list-import-errors
airflow tasks states-for-dag-run <dag_id> <run_id>
airflow jobs check --job-type SchedulerJob
airflow jobs check --job-type DagProcessorJob
airflow backfill create ...
```

## Final Verified DAG Results

| DAG | Result |
|---|---|
| `dependency_demo` | SUCCESS |
| `backfill_test` | SUCCESS |
| `failure_recovery` | SUCCESS |
| `simple_etl_dag` | SUCCESS |
