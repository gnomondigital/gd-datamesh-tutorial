from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

# A DAG represents a workflow, a collection of tasks
with DAG(dag_id="demo", start_date=datetime(2022, 1, 1),
         schedule="0 0 * * *") as dag:

    # Tasks are represented as operators
    hello = BashOperator(task_id="hello", bash_command="echo hello")
    start = BashOperator(task_id="start", bash_command="echo start")
    end = BashOperator(task_id="end", bash_command="echo end")

    @task()
    def airflow():
        print("airflow")

    @task()
    def training():
        print("100 push ups")

    # Set dependencies between tasks
    start >> hello >> airflow() >> training() >> end
