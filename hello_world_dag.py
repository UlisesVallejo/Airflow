from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def my_first_dag():
    print("Hello world,i made my first DAG")
    
with DAG(dag_id="my_first_dag",
         start_date=datetime(2022,3,14),
         schedule_interval="@hourly",
         catchup=False) as dag:
    
    task1 = PythonOperator(
        task_id="my_first_dag",
        python_callable=my_first_dag
    )
    
task1