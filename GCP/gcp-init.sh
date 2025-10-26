#PROJECT config
export REGION=europe-west3
export ZONE=europe-west3-a
gcloud config set compute/zone ${ZONE}
export PROJECT=$(gcloud info --format='value(config.project)')
export HIVEMETASTORE=hive-metastore3

#BUcket create
gsutil mb -l ${REGION} gs://${PROJECT}-warehouse-eu-west3

#Creating the Cloud SQL instance:
gcloud sql instances create ${HIVEMETASTORE} \
	--database-version="MYSQL_5_7" \
	--activation-policy=ALWAYS  \
	--zone ${ZONE}

#Creating a Dataproc cluster:
#gcloud dataproc clusters create hive-cluster-eu-west3 --scopes sql-admin --image-version 1.4 --region ${REGION} --initialization-actions gs://goog-dataproc-initialization-actions-${REGION}/cloud-sql-proxy/cloud-sql-proxy.sh  --properties hive:hive.metastore.warehouse.dir=gs://${PROJECT}-warehouse-eu-west3/datasets  --metadata "hive-metastore-instance=${PROJECT}:${REGION}:hive-metastore-eu-west3"

gcloud dataproc clusters create hive-cluster \
    --scopes sql-admin \
    --image-version 1.4 \
    --region ${REGION} \
    --initialization-actions gs://goog-dataproc-initialization-actions-${REGION}/cloud-sql-proxy/cloud-sql-proxy.sh \
    --properties hive:hive.metastore.warehouse.dir=gs://${PROJECT}-warehouse-eu-west3/datasets \
    --metadata "hive-metastore-instance=${PROJECT}:${REGION}:${HIVEMETASTORE}"

gsutil cp gs://hive-solution/part-00000.parquet gs://${PROJECT}-warehouse-eu-west/datasets/transactions/part-00000.parquet

gcloud dataproc jobs submit hive \
	--cluster hive-cluster \
	--region ${REGION} \ 
	--execute " CREATE EXTERNAL TABLE transactions (SubmissionDate DATE, TransactionAmount DOUBLE, TransactionType STRING) STORED AS PARQUET LOCATION 'gs://${PROJECT}-warehouse-eu-west3/datasets/transactions';"

gcloud dataproc jobs submit hive \
    --cluster hive-cluster \
    --region ${REGION} \
    --execute "
      SELECT *
      FROM transactions
      LIMIT 10;"


