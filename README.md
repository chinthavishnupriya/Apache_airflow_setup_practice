# Apache Airflow Setup & Practice

A practical Apache Airflow learning repository documenting setup, concepts, DAG development, debugging, execution, backfill/rerun, failure recovery, pools, and ETL workflow verification.

## Environment

| Component | Version / Configuration |
|---|---|
| Apache Airflow | 3.3.2 |
| Python | 3.11.x |
| OS | Ubuntu / Linux |
| Airflow mode | `airflow standalone` |
| AIRFLOW_HOME | `~/airflow` |
| DAG folder | `~/airflow/dags` |
| Web UI / API | `http://localhost:8080` |
| Executor | LocalExecutor |

---

## Core Concepts Practiced

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
- Task testing and debugging
- Pools and task concurrency
- Backfill
- Rerun
- Failure handling and recovery
- Simple ETL workflow

---

## DAG Practice Files

```text
dags/
├── hello_airflow.py
├── dependency_demo.py
├── backfill_test.py
├── failure_recovery.py
└── simple_etl_dag.py
```

### Simple ETL

Workflow:

```text
EXTRACT
   ↓
TRANSFORM
   ↓
LOAD
```

Implementation:

```python
extract_task >> transform_task >> load_task
```

Verified final result:

```text
extract   | success
transform | success
load      | success
```

---

## Actual Airflow UI Evidence

The repository documentation maps the original Airflow UI screenshots supplied during the practice session to the corresponding concepts.

Screenshots are stored under:

```text
docs/screenshots/
```

Evidence includes:

- Airflow home/health
- Hello Airflow successful run and task logs
- Task dependency execution
- Backfill and rerun
- Pool/concurrency execution
- DAG listing
- Failure debugging logs
- Failure recovery
- Dynamic task mapping / ETL-style execution
- BashOperator
- TaskFlow API

See [`docs/airflow_practical_outputs.md`](docs/airflow_practical_outputs.md) for the evidence-to-concept mapping and final verification results.

> **Screenshot note:** The actual PNG screenshots supplied in the practice conversation are prepared for upload separately. A dedicated screenshot for the final `simple_etl_dag` run is still missing; the exact Airflow UI location is documented in `docs/airflow_practical_outputs.md`.

---

## Important Commands

```bash
airflow dags list
airflow dags show <dag_id>
airflow dags trigger <dag_id>
airflow dags list-runs <dag_id>
airflow tasks states-for-dag-run <dag_id> <run_id>
airflow dags unpause <dag_id>
airflow dags pause <dag_id>
airflow dags list-import-errors
airflow jobs check --job-type SchedulerJob
airflow jobs check --job-type DagProcessorJob
```

Backfill:

```bash
airflow backfill create --dag-id backfill_test --from-date 2026-09-20 --to-date 2026-09-22
```

---

## Troubleshooting Performed

During practice, real Airflow troubleshooting situations were handled:

- DAG not appearing in the DAG list
- DAG processor restart
- Scheduler health verification
- DAG pause/unpause
- DAG run stuck in queued state
- Import-error verification
- Task-state inspection
- Failure log inspection
- Intentional failure and recovery

---

## Final Verified Results

```text
dependency_demo   -> SUCCESS
backfill_test     -> SUCCESS
failure_recovery  -> SUCCESS
simple_etl_dag    -> SUCCESS
```

All documented DAGs were developed and verified locally with Apache Airflow 3.3.2.