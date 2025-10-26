#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""
Example Airflow DAG for Google Cloud Storage to Google Cloud Storage transfer operators.
"""

import os
from datetime import datetime

from airflow import models
from airflow.providers.google.cloud.operators.gcs import GCSSynchronizeBucketsOperator
from airflow.providers.google.cloud.transfers.gcs_to_gcs import GCSToGCSOperator

BUCKET_1_SRC = os.environ.get("GCP_GCS_BUCKET_1_SRC", "assignment-seb-warehouse-eu-west3")
BUCKET_1_DST = os.environ.get("GCP_GCS_BUCKET_1_DST", "assignment-seb-warehouse-eu-west3")


with models.DAG(
        "example_gcs_to_gcs",
        schedule_interval='@once',
        start_date=datetime(2021, 1, 1),
        catchup=False,
        tags=['example'],
) as dag:
    # [START howto_synch_bucket]
    sync_bucket = GCSSynchronizeBucketsOperator(
        task_id="sync_bucket", source_bucket=BUCKET_1_SRC, destination_bucket=BUCKET_1_DST
    )
    # [END howto_synch_bucket]

    # [START howto_operator_gcs_to_gcs_wildcard]
    copy_files_with_wildcard_f1 = GCSToGCSOperator(
        task_id="copy_files_with_wildcard_f1",
        source_bucket=BUCKET_1_SRC,
        source_object="datasets/input/fhvhv_tripdata_2021-01_spark_load/*",
        destination_bucket=BUCKET_1_DST,
        destination_object="datasets/input/fhvhv_tripdata_2021-01_spark_load-backup/",
    )
    # [END howto_operator_gcs_to_gcs_wildcard]

    # [START howto_operator_gcs_to_gcs_wildcard]
    copy_files_with_wildcard_f2 = GCSToGCSOperator(
        task_id="copy_files_with_wildcard_f2",
        source_bucket=BUCKET_1_SRC,
        source_object="datasets/input/fhvhv_tripdata_2021-03_spark_load/*",
        destination_bucket=BUCKET_1_DST,
        destination_object="datasets/input/fhvhv_tripdata_2021-03_spark_load-backup/",
    )
    # [END howto_operator_gcs_to_gcs_wildcard]