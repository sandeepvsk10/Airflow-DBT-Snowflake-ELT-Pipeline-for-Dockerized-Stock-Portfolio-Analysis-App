from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

with DAG('docker_apps_orchestration', start_date=datetime(2024, 1, 1), schedule_interval=None) as dag:

    # Task to run app1 container
    task_app1 = DockerOperator(
        task_id='run_app1',
        image='app1-image',  # Docker image of app1
        command='python app.py',  # Command to run in the container
        auto_remove=True,  # Remove container once done
        docker_url='unix://var/run/docker.sock',  # Connect to Docker
        network_mode='airflow-net'  # Use the same network
    )

    # Task to run app2 container
    task_app2 = DockerOperator(
        task_id='run_app2',
        image='app2-image',  # Docker image of app2
        command='python app.py',  # Command to run in the container
        auto_remove=True,  # Remove container once done
        docker_url='unix://var/run/docker.sock',  # Connect to Docker
        network_mode='airflow-net'  # Use the same network
    )

    task_app2 = DockerOperator(
        task_id='run_app2',
        image='app2-image',  # Docker image of app2
        command='python app.py',  # Command to run in the container
        auto_remove=True,  # Remove container once done
        docker_url='unix://var/run/docker.sock',  # Connect to Docker
        network_mode='airflow-net'  # Use the same network
    )

    # Set the execution order of tasks
    task_app1 >> task_app2  # app1 runs before app2
