# import libraries
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from sqlalchemy import create_engine #koneksi ke postgres
import pandas as pd

def load_csv_clean_to_postgres():
    # load csv to postgres
    database = "airflow_finalproject"
    username = "airflow_finalproject"
    password = "airflow_finalproject"
    host = "postgres"

    # Create URL connection to PostgreSQL
    postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"
    engine = create_engine(postgres_url)
    conn = engine.connect()

    # save from csv to PostgreSQL
    df = pd.read_csv('/opt/airflow/dags/bank-additional-full_clean.csv')
    df.to_sql('table_finalproject_clean', conn, index=False, if_exists='replace')  # Menggunakan if_exists='replace' agar tabel digantikan jika sudah ada
    
