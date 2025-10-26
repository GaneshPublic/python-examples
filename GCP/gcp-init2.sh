SEB:

http://localhost:7180 - CDM(Cloudera Manager)


Flow:

Spark job:
Create external table if not exists
Load data


Airflow:
	Hive back up jos:
	Save data to load node(insert data local impath)

        Hive delete job:
	delete the table and DB
	delete the data dos -rm -r file

        Hive rest the data:
	load data from local into hive external table



Steps on GCP:
Installing Hive and Dataproc:
1. Follow the steps to configure Dataproc on hive : https://cloud.google.com/architecture/using-apache-hive-on-cloud-dataproc
2. Region change:
NAME: europe-north1-a
REGION: europe-north1
STATUS: UP
NEXT_MAINTENANCE:
TURNDOWN_DATE:
export REGION=europe-north1
      export ZONE=europe-north1-a
      gcloud config set compute/zone ${ZONE}
3. Creating the warehouse bucket:
	export PROJECT=$(gcloud info --format='value(config.project)')
	gsutil mb -l ${REGION} gs://${PROJECT}-warehouse-eu-west
	o/p: Creating gs://assignment-seb-warehouse/...
4. Creating the Cloud SQL instance:
	gcloud sql instances create hive-metastore-eu-west  --database-version="MYSQL_5_7" --activation-policy=ALWAYS  --zone ${ZONE}
	o/p: Creating Cloud SQL instance...done.     
Created [https://sqladmin.googleapis.com/sql/v1beta4/projects/assignment-seb/instances/hive-metastore].
NAME: hive-metastore
DATABASE_VERSION: MYSQL_5_7
LOCATION: europe-north1-a
TIER: db-n1-standard-1
PRIMARY_ADDRESS: 34.88.193.135
PRIVATE_ADDRESS: -
STATUS: RUNNABLE
5. Creating a Dataproc cluster:
	gcloud dataproc clusters create hive-cluster \ --scopes sql-admin \ --image-version 1.4 \ --region ${REGION} \ --initialization-actions gs://goog-dataproc-initialization-actions-${REGION}/cloud-sql-proxy/cloud-sql-proxy.sh \ --properties hive:hive.metastore.warehouse.dir=gs://${PROJECT}-warehouse/datasets \ --metadata "hive-metastore-instance=${PROJECT}:${REGION}:hive-metastore"

Another:
gcloud dataproc clusters create hive-cluster-eu-west  --scopes sql-admin  --image-version 1.4  --region ${REGION}  --initialization-actions gs://goog-dataproc-initialization-actions-${REGION}/cloud-sql-proxy/cloud-sql-proxy.sh  --properties hive:hive.metastore.warehouse.dir=gs://${PROJECT}-warehouse-eu-west/datasets  --metadata "hive-metastore-instance=${PROJECT}:${REGION}:hive-metastore-eu-west"

Waiting on operation [projects/assignment-seb/regions/europe-north1/operations/e225ddda-a1cc-39e4-bff1-b41172000e13].
Waiting for cluster creation operation...done.     
Created [https://dataproc.googleapis.com/v1/projects/assignment-seb/regions/europe-north1/clusters/hive-cluster] Cluster placed in zone [europe-north1-a].

Creating a Hive table:
1. Copy the sample dataset to your warehouse bucket:
	gsutil cp gs://hive-solution/part-00000.parquet gs://${PROJECT}-warehouse-eu-west/datasets/transactions/part-00000.parquet
2. Create an external Hive table for the dataset:
	gcloud dataproc jobs submit hive --cluster hive-cluster-eu-west --region ${REGION} --execute " CREATE EXTERNAL TABLE transactions (SubmissionDate DATE, TransactionAmount DOUBLE, TransactionType STRING) STORED AS PARQUET LOCATION 'gs://${PROJECT}-warehouse-eu-west/datasets/transactions';"
Connecting to jdbc:hive2://hive-cluster-eu-west-m:10000
Connected to: Apache Hive (version 2.3.7)
Driver: Hive JDBC (version 2.3.7)

Querying Hive with the Dataproc Jobs API
1. gcloud dataproc jobs submit hive  --cluster hive-cluster-eu-west  --region ${REGION}  --execute " SELECT * FROM transactions LIMIT 10;"
	o/p: +------------------------------+---------------------------------+-------------------------------+
| transactions.submissiondate  | transactions.transactionamount  | transactions.transactiontype  |
+------------------------------+---------------------------------+-------------------------------+
| 2017-12-03                   | 1167.39                         | debit                         |
| 2017-09-23                   | 2567.87                         | debit                         |
| 2017-12-22                   | 1074.73                         | credit                        |
| 2018-01-21                   | 5718.58                         | debit                         |
| 2017-10-21                   | 333.26                          | debit                         |
| 2017-09-12                   | 2439.62                         | debit                         |
| 2017-08-06                   | 5885.08                         | debit                         |
| 2017-12-05                   | 7353.92                         | authorization                 |
| 2017-09-12                   | 4710.29                         | authorization                 |
| 2018-01-05                   | 9115.27                         | debit                         |
+------------------------------+---------------------------------+-------------------------------+

Querying Hive with Beeline
1. Open an SSH session with the Dataproc's master instance:
	gcloud compute ssh hive-cluster-eu-west-m
2. In the master instance's command prompt, open a Beeline session:
	beeline -u "jdbc:hive2://localhost:10000"
3. Run sample query:
	select * from transaction limit 5;
4. Close the Beeline session: !quit
5. Close the SSH connection: exit

Querying Hive with SparkSQL
1. Open an SSH session with the Dataproc's master instance:
	gcloud compute ssh hive-cluster-m
1. In the master instance's command prompt, open a new PySpark shell session:
	pyspark
3. When the PySpark shell prompt appears, type the following Python code:
>>> from pyspark.sql import HiveContext
>>> hc = HiveContext(sc)
>>> hc.sql("""
... select * from transactions limit 5
... """).show()
ivysettings.xml file not found in HIVE_HOME or HIVE_CONF_DIR,/etc/hive/conf.dist/ivysettings.xml will be used
+--------------+-----------------+---------------+                              
|submissiondate|transactionamount|transactiontype|
+--------------+-----------------+---------------+
|    2017-12-03|          1167.39|          debit|
|    2017-09-23|          2567.87|          debit|
|    2017-12-22|          1074.73|         credit|
|    2018-01-21|          5718.58|          debit|
|    2017-10-21|           333.26|          debit|
+--------------+-----------------+---------------+





SEB assignment:
1. Loading the sample data into hive:
	gcloud compute ssh hive-cluster-eu-west-m
from pyspark.sql import HiveContext
hq = HiveContext(sc)
#df = sc.read.csv("gs://assignment-seb-warehouse/input/green_tripdata_2021-01.csv")
df = hq.read.format("com.databricks.spark.csv").option("header", "true").option("inferschema", "true").option("mode", "DROPMALFORMED").csv("gs://assignment-seb-warehouse-eu-west/input/green_tripdata_2021-01.csv")
df.show()
df.printSchema()
df.createOrReplaceTempView('df_View')
hq.sql("""CREATE EXTERNAL TABLE IF NOT EXISTS green_tripdata
LOCATION "gs://assignment-seb-warehouse-eu-west/input/gree_tripdata_spark_load/"
AS SELECT * FROM df_view
""")


Accessing web interface of Airflow:
Run Airflow CLI commands
        Service account configuration: https://cloud.google.com/composer/docs/how-to/access-control#about-composer-sa
https://cloud.google.com/composer/docs/how-to/access-control#service-account
Creating the cloud composer(For Airflow): https://cloud.google.com/composer/docs/how-to/managing/creating
https://cloud.google.com/composer/docs/how-to/managing/creating#step_1_basic_setup
	Link: https://cloud.google.com/composer/docs/how-to/accessing/airflow-cli#running-commands
	gcloud config set project assignment-seb
       gcloud config set composer/location europe-west3
       gcloud composer environments run example-environment \
    dags list -- --output=json

