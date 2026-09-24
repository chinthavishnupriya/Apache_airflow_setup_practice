# Apache Airflow Setup & Practice

A practical Apache Airflow learning repository documenting setup, DAG development, scheduling, dependencies, UI troubleshooting, failure recovery, and an end-to-end Customer-360 workflow.

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

## Practical Exercises

The repository follows the supplied Airflow practical exercise sheet.

### Exercise 1 — First Workflow

File: `dags/exercises/exercise_1/hello_workflow.py`

Workflow: `start → student_name → course_name → end`

### Exercise 2 — Cron to Airflow Scheduling

- `dags/exercises/exercise_2/daily_sales.py` — daily at 09:00
- `dags/exercises/exercise_2/weekly_customer_report.py` — Monday at 08:00

### Exercise 3 — Dependencies and Parallel Execution

File: `dags/exercises/exercise_3/customer_pipeline.py`

Workflow:
```text
              ┌── validate_data ──┐
start ────────┤                   ├──→ load_data → finish
              └── clean_data ─────┘
```

The failure scenario was also tested by intentionally failing `clean_data`.

### Exercise 4 — Airflow UI and Failure Investigation

File: `dags/exercises/exercise_4/etl_ui_practice.py`

Workflow: `extract → transform → load → notify`

Practiced Graph View, Tree View, task logs, intentional failure, downstream impact, and recovery.

### Exercise 5 — Customer-360 Mini Capstone

- `dags/exercises/exercise_5/customer360.py` — BashOperator version
- `dags/exercises/exercise_5/customer360_taskflow.py` — TaskFlow API version

Workflow:
```text
CRM ───────────────┐
Transactions ─────┼──→ Process → Spark → Hive → HBase → Notify
Support ──────────┘
```

The TaskFlow version was tested successfully and demonstrates automatic XCom data passing through task return values.

## Repository Structure

```text
dags/
├── exercises/
│   ├── exercise_1/
│   │   └── hello_workflow.py
│   ├── exercise_2/
│   │   ├── daily_sales.py
│   │   └── weekly_customer_report.py
│   ├── exercise_3/
│   │   └── customer_pipeline.py
│   ├── exercise_4/
│   │   └── etl_ui_practice.py
│   └── exercise_5/
│       ├── customer360.py
│       └── customer360_taskflow.py
├── backfill_test.py
├── dependency_demo.py
├── failure_recovery.py
├── hello_airflow.py
├── hello_three.py
├── pool_test.py
├── simple_etl_dag.py
└── test_debug.py
```

## Core Airflow Concepts Practiced

- DAG creation and registration
- Task dependencies
- Sequential and parallel execution
- BashOperator
- Scheduling and cron expressions
- Retries and task timeouts
- Variables and Connections
- Sensors and Branching
- Dynamic Task Mapping
- TaskFlow API
- XCom through TaskFlow return values
- Jinja templating
- Logical dates and data intervals
- Trigger rules and Task Groups
- Callbacks
- Task testing and debugging
- Pools and task concurrency
- Backfill and rerun
- Failure handling and recovery
- Airflow Graph View, Tree View, and Logs

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

Test a DAG:

```bash
airflow dags test <dag_id> 2026-09-24
```

## Verification

The exercise DAGs were tested locally with Apache Airflow 3.3.2. The Customer-360 TaskFlow test completed with a successful DAG run.

## UI Evidence

The original Airflow UI screenshots were captured during the practical session. The `docs/screenshots/` area is reserved for practice evidence. Generated SVG screenshots are not presented as the original Airflow UI screenshots.
