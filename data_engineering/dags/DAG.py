from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta
from sqlalchemy import create_engine #koneksi ke postgres
import pandas as pd

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
 

from step.load import load_csv_to_postgres 
from step.fetch import fetch_data
from step.cleaning import preprocessing
from step.load_clean import load_csv_clean_to_postgres
from step.push import upload_to_elasticsearch


# create name and set times to Jakarta time     
default_args = {
    'owner': 'Panji', 
    'start_date': datetime(2024, 2, 22, 18, 00) - timedelta(hours=7)
}

with DAG(
    "final_project", 
    description='final',
    schedule_interval='30 06 * * 1', #create schedule to run every 06:30 on monday.
    default_args=default_args, 
    catchup=False
) as dag:
    # Task : 1
    '''  Function to load data raw to postgres'''
    load_csv_task = PythonOperator(
        task_id='load_csv_to_postgres',
        python_callable=load_csv_to_postgres)
    
    #task: 2
    ''' Function to fetch data'''
    ambil_data_pg = PythonOperator(
        task_id='ambil_data_postgres',
        python_callable=fetch_data) #
    

    # Task: 3
    '''  Function to process cleaning data'''
    edit_data = PythonOperator(
        task_id='edit_data',
        python_callable=preprocessing)

    # Task : 4
    '''  Function to load clean data to postgres'''
    load_csv_clean_task = PythonOperator(
        task_id='load_csv_clean_to_postgres',
        python_callable=load_csv_clean_to_postgres)
    
    # Task: 5
    '''  Function to upload data to elasticsearch'''
    upload_data = PythonOperator(
        task_id='upload_data_elastic',
        python_callable=upload_to_elasticsearch)

    #proses untuk menjalankan di airflow
    load_csv_task >> ambil_data_pg >> edit_data >> load_csv_clean_task >> upload_data