# Apache Airflow Setup & Practice

A practical Apache Airflow learning repository documenting the setup, concepts, DAG development, debugging, execution, and verification completed during the practice sessions.

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

## 1. Airflow Setup

Airflow was installed in a Python virtual environment and run locally using:

```bash
airflow standalone
```

The Airflow scheduler and DAG processor were verified during troubleshooting with:

```bash
airflow jobs check --job-type SchedulerJob
airflow jobs check --job-type DagProcessorJob
```

Example verification:

```
Found one alive job.
```

---

# 2. Core Concepts Practiced

The following Airflow concepts were practiced and verified:

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

# 3. DAG Practice Files

## 3.1 Hello Airflow

File:

```
dags/hello_airflow.py
```

Purpose:

- Create a basic DAG.
- Use `PythonOperator`.
- Execute a simple Python function.

---

## 3.2 Task Dependencies

File:

```
dags/dependency_demo.py
```

Workflow:

```
start
  ↓
process
  ↓
finish
```

The dependency was verified using:

```bash
airflow dags show dependency_demo
```

The DAG graph showed:

```
start -> process -> finish
```

The DAG was then unpaused and triggered successfully.

---

# 4. Backfill and Rerun

File:

```
dags/backfill_test.py
```

The DAG was configured with:

```python
schedule="@daily"
```

Backfill was tested for:

- 2026-09-20
- 2026-09-21
- 2026-09-22

Dry run:

```bash
airflow backfill create \
  --dag-id backfill_test \
  --from-date 2026-09-20 \
  --to-date 2026-09-22 \
  --dry-run
```

The dry run showed three historical runs.

Actual backfill:

```bash
airflow backfill create \
  --dag-id backfill_test \
  --from-date 2026-09-20 \
  --to-date 2026-09-22 \
  --reprocess-behavior none \
  --max-active-runs 1
```

The three backfill runs completed successfully.

The task state for the rerun target was verified with:

```bash
airflow tasks states-for-dag-run \
  backfill_test \
  backfill__2026-09-20T00:00:00+00:00
```

Output:

```
process_data | success
```

---

# 5. Failure Handling and Recovery

File:

```
dags/failure_recovery.py
```

The DAG intentionally contains a failing task:

```python
raise ValueError("Intentional failure for testing")
```

The recovery task uses:

```python
trigger_rule="all_done"
```

Workflow:

```
fail
  ↓
recover
```

The DAG was first diagnosed when its run remained queued because the DAG was paused. The DAG was unpaused and the run completed.

Final DAG run:

```
SUCCESS
```

Task-state verification:

```bash
airflow tasks states-for-dag-run \
  failure_recovery \
  manual__2026-09-23T09:31:29.989175+00:00
```

Final output:

```
fail     | failed
recover  | success
```

This demonstrates that the recovery task can execute after the upstream task fails when `all_done` is used.

---

# 6. Simple ETL

File:

```
dags/simple_etl_dag.py
```

This was the final practical exercise.

Workflow:

```
extract
   ↓
transform
   ↓
load
```

The DAG was registered, unpaused, triggered, and verified.

Trigger:

```bash
airflow dags trigger simple_etl_dag
```

The run completed with:

```
success
```

Task-state verification:

```bash
airflow tasks states-for-dag-run \
  simple_etl_dag \
  manual__2026-09-23T13:42:04.305701+00:00
```

Final task states:

```
extract   | success
transform | success
load      | success
```

Therefore the complete ETL pipeline executed successfully.

---

# 7. Useful Verification Commands

List DAGs:

```bash
airflow dags list
```

Check import errors:

```bash
airflow dags list-import-errors
```

Show a DAG graph:

```bash
airflow dags show <dag_id>
```

Trigger a DAG:

```bash
airflow dags trigger <dag_id>
```

List DAG runs:

```bash
airflow dags list-runs <dag_id>
```

Check task states:

```bash
airflow tasks states-for-dag-run <dag_id> <run_id>
```

Pause/unpause:

```bash
airflow dags pause <dag_id>
airflow dags unpause <dag_id>
```

Check scheduler:

```bash
airflow jobs check --job-type SchedulerJob
```

Check DAG processor:

```bash
airflow jobs check --job-type DagProcessorJob
```

---

# 8. Troubleshooting Performed

During practice, several real Airflow troubleshooting situations were handled.

### DAG not appearing

Checked:

```bash
ls -l ~/airflow/dags/<dag_file>.py
airflow dags list-import-errors
airflow jobs check --job-type DagProcessorJob
```

The DAG processor was restarted when required and Airflow was restarted using:

```bash
airflow standalone
```

### DAG run stuck in queued state

Checked:

- DAG pause state
- Scheduler health
- DAG processor health
- Executor configuration
- Task states

A paused DAG was identified and unpaused:

```bash
airflow dags unpause failure_recovery
```

The queued run then completed successfully.

---

# 9. Repository Structure

```
Apache_airflow_setup_practice/
│
├── README.md
│
└── dags/
    ├── hello_airflow.py
    ├── dependency_demo.py
    ├── backfill_test.py
    ├── failure_recovery.py
    └── simple_etl_dag.py
```

---

# 10. Learning Status

The supplied Airflow practical material was completed through the final Simple ETL exercise.

Additional Airflow concepts were also practiced beyond the basic PDF material, including XCom, Variables, Connections, Sensors, Branching, Dynamic Task Mapping, TaskFlow API, Jinja templating, Logical Dates, Trigger Rules, Task Groups, Callbacks, Debugging, Pools, Backfill/Rerun, and Failure Recovery.

## Final verified practical result

```
dependency_demo   -> SUCCESS
backfill_test     -> SUCCESS
failure_recovery  -> SUCCESS
simple_etl_dag    -> SUCCESS
```

All documented DAGs were developed and verified locally with Apache Airflow 3.3.2.
