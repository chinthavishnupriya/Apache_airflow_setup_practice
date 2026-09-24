from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="hello_workflow",
    start_date=datetime(2026, 9, 1),
    schedule=None,
    catchup=False,
) as dag:

    start = BashOperator(
        task_id="start",
        bash_command="echo 'Starting Airflow workflow'",
    )

    student = BashOperator(
        task_id="student_name",
        bash_command="echo 'Student: Chintan'",
    )

    course = BashOperator(
        task_id="course_name",
        bash_command="echo 'Course: Data Engineering'",
    )

    end = BashOperator(
        task_id="end",
        bash_command="echo 'Workflow completed'",
    )

    start >> student >> course >> end
