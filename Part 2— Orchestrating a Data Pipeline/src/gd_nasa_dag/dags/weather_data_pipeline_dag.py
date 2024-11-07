from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.docker_operator import DockerOperator


default_args = {
    'owner': 'gnomon digital',
    "description": "nasa pipeline",
    'depends_on_past': False,
    'start_date': datetime.utcnow(),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}


with DAG(
    "gd-nasa-dag",
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    concurrency=1,
    catchup=False,
    max_active_runs=1,
) as dag:
    start_bronze_layer = EmptyOperator(task_id="start_bronze_layer")
    start_silver_layer = EmptyOperator(task_id="start_silver_layer")
    start_gold_layer = EmptyOperator(task_id="start_gold_layer")
    end_dag = EmptyOperator(task_id="end_dag")
    environment_vars = {
        'DB_PORT': '{{ var.value.DB_PORT }}',
        'DB_PASS': '{{ var.value.DB_PASS }}',
        'DB_USER': '{{ var.value.DB_USER }}',
        'DB_HOST': '{{ var.value.DB_HOST }}',
        'DB_NAME': '{{ var.value.DB_NAME }}',
        'DB_SCHEMA': '{{ var.value.DB_SCHEMA }}',
    }
    bronze_layer_data = DockerOperator(
        task_id="bronze_layer_data",
        image="gd-nasa-pipeline:latest",  # local image and tag
        api_version='auto',
        command="--view bronze",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        environment=environment_vars,
    )
    bronze_layer_geo = DockerOperator(
        task_id="bronze_layer_geo",
        image="gd-nasa-pipeline:latest",  # local image and tag
        api_version='auto',
        command="--view bronze --table_name geo_referential",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        environment=environment_vars,
    )
    silver_layer_data = DockerOperator(
        task_id="silver_layer_data",
        image="gd-nasa-pipeline:latest",  # local image and tag
        api_version='auto',
        command="--view silver",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        environment=environment_vars,
    )
    silver_layer_geo = DockerOperator(
        task_id="silver_layer_geo",
        image="gd-nasa-pipeline:latest",  # local image and tag
        api_version='auto',
        command="--view silver --table_name geo_referential",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        environment=environment_vars,
    )
    gold_layer = DockerOperator(
        task_id="gold_layer",
        image="gd-nasa-pipeline:latest",  # local image and tag
        api_version='auto',
        command="--view gold",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        environment=environment_vars,
    )

    (
        start_bronze_layer
        >> [bronze_layer_data, bronze_layer_geo]
        >> start_silver_layer
        >> [silver_layer_data, silver_layer_geo]
        >> start_gold_layer
        >> gold_layer
        >> end_dag
    )
