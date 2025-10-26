"""A liveness prober dag for monitoring composer.googleapis.com/environment/healthy."""
import airflow
import os
from airflow import DAG
from airflow import models
from airflow.operators.bash_operator import BashOperator
from datetime import timedelta
from airflow.providers.google.cloud.transfers.gcs_to_gcs import GCSToGCSOperator

default_args = {
    'start_date': airflow.utils.dates.days_ago(0),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'airflow_monitoring',
    default_args=default_args,
    description='liveness monitoring dag',
    schedule_interval=None,
    dagrun_timeout=timedelta(minutes=20))

# priority_weight has type int in Airflow DB, uses the maximum.
t1 = BashOperator(
    task_id='echo',
    bash_command='echo test',
    dag=dag,
    depends_on_past=False,
    priority_weight=2**31-1)

BUCKET_1_SRC = os.environ.get("GCP_GCS_BUCKET_1_SRC", "assignment-seb-warehouse-eu-west3")
BUCKET_1_DST = os.environ.get("GCP_GCS_BUCKET_1_DST", "assignment-seb-warehouse-eu-west3")
with models.DAG(
        "example_gcs_to_gcs",
        schedule_interval='@once',
        start_date=datetime(2021, 1, 1),
        catchup=False,
        tags=['example'],
) as dag:
    copy_files_with_wildcard = GCSToGCSOperator(
        task_id="copy_files_with_wildcard",
        source_bucket=BUCKET_1_SRC,
        source_object="datasets/input/gree_tripdata_spark_load/*",
        destination_bucket=BUCKET_1_DST,
        destination_object="datasets/input/gree_tripdata_spark_load-backup/",
    )
