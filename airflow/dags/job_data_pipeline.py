from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import psycopg2


def fetch_and_save_jobs():
    url = "https://remotive.com/api/remote-jobs"
    response = requests.get(url)
    jobs = response.json()["jobs"][:10]

    conn = psycopg2.connect(
        host="postgres",
        database="airflow",
        user="airflow",
        password="airflow"
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id SERIAL PRIMARY KEY,
            title TEXT,
            company TEXT,
            location TEXT,
            url TEXT
        )
    """)

    for job in jobs:
        cur.execute("""
            INSERT INTO jobs (title, company, location, url)
            VALUES (%s, %s, %s, %s)
        """, (
            job["title"],
            job["company_name"],
            job["candidate_required_location"],
            job["url"]
        ))

    conn.commit()
    cur.close()
    conn.close()


with DAG(
    dag_id="job_data_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    task = PythonOperator(
        task_id="fetch_and_store_jobs",
        python_callable=fetch_and_save_jobs
    )