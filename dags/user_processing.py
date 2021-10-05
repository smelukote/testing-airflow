from airflow.models import DAG
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from datetime import datetime 

default_args = {
    'start_date=datetime(2021,10,5)'
}

with DAG('user_processing', schedule_interval='@daily', 
         default_args=default_args,
         start_date=datetime(2021,10,5),
         catchup=False) as dag:
    #Define tasks/operators
    creating_table=SqliteOperator(
        task_id='creating_table',
        sql='''
            CREATE TABLE users 
                firstnmae TEXT NOT NULL,
                lastname TEXT NOT NULL,
                country TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL PRIMARY KEY
            );
            '''
            )
          
