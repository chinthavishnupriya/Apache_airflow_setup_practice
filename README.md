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

The repository contains an organized location for the original Airflow UI screenshots from the practice session.

```text
docs/screenshots/
├── exercise-1/
│   └── hello_workflow screenshots
├── exercise-2/
│   └── daily_sales + weekly_customer_report screenshots
├── exercise-3/
│   └── customer_pipeline screenshots
├── exercise-4/
│   └── etl_ui_practice screenshots
└── mini-project/
    └── customer360 screenshots
```

See [`docs/airflow_practical_outputs.md`](docs/airflow_practical_outputs.md) for the evidence-to-concept mapping.

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

---

## Exercises 1–4 and Customer-360 Mini Project

Completed Airflow exercises and capstone DAGs:

```text
dags/
├── hello_workflow.py
├── daily_sales.py
├── weekly_customer_report.py
├── customer_pipeline.py
├── etl_ui_practice.py
└── customer360.py
```

### Exercise 1

`hello_workflow.py`

Workflow:

```text
start → student_name → course_name → end
```

### Exercise 2

`daily_sales.py` — daily schedule at 09:00.

`weekly_customer_report.py` — weekly schedule on Monday at 08:00.

### Exercise 3

`customer_pipeline.py`

Workflow:

```text
              ┌── validate_data ──┐
start ────────┤                   ├──→ load_data → finish
              └── clean_data ─────┘
```

### Exercise 4

`etl_ui_practice.py`

Workflow:

```text
extract → transform → load → notify
```

Practiced Graph View, task logs, intentional failure, and recovery.

### Exercise 5 — Customer-360 Mini Project

`customer360.py`

Workflow:

```text
                    ┌── ingest_crm ──────────┐
                    ├── ingest_transactions ──┤
start ──────────────┤                         ├──→ process_customer_data
                    └── ingest_support ───────┘
                                                     ↓
                                              spark_processing
                                                     ↓
                                                 load_hive
                                                     ↓
                                                load_hbase
                                                     ↓
                                             notify_downstream
```

All six DAGs were tested locally and the Customer-360 final run completed successfully.

---

## Airflow UI Screenshots

The generated SVG screenshots have been removed. The folders above are reserved for the original Airflow UI screenshots supplied during the practice session.
