from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

with DAG('docker_apps_orchestration', start_date=datetime(2024, 1, 1), schedule_interval=None) as dag:

   
    task_app1 = DockerOperator(
        task_id='run_app1',
        image='app1-image',
        command='python app.py',  
        auto_remove=True,  
        docker_url='unix://var/run/docker.sock', 
        network_mode='airflow-net' 
    )

    
    task_app2 = DockerOperator(
        task_id='run_app2',
        image='app2-image',  
        command='python app.py', 
        auto_remove=True,  
        docker_url='unix://var/run/docker.sock', 
        network_mode='airflow-net' 
    )

    task_app2 = DockerOperator(
        task_id='run_app2',
        image='app2-image', 
        command='python app.py',
        auto_remove=True,  
        docker_url='unix://var/run/docker.sock',  
        network_mode='airflow-net' 
    )

    
    task_app1 >> task_app2  
