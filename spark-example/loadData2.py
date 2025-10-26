#from pyspark.sql import HiveContext
#from pyspark.sql import SparkContext

#sqlContext = HiveContext(sc)
#data = [('First', 1), ('Second', 2), ('Third', 3), ('Fourth', 4), ('Fifth', 5)]
#df = sqlContext.createDataFrame(data)
#df.show()
#df.write.saveAsTable('example')
#df_ex = sqlContext.sql('SELECT * FROM example')
#df_ex.show()

from pyspark.sql import HiveContext
from pyspark.sql import SparkSession
#from os.path import expanduser, join, abspath

# warehouse_location points to the default location for managed databases and tables
#warehouse_location = abspath('gs://assignment-seb-warehouse-eu-west/datasets')

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL Hive load") \
    .enableHiveSupport() \
    .getOrCreate()

#hq = HiveContext(sc)
df1 = spark.read.format("com.databricks.spark.csv")\
    .option("header", "true")\
    .option("inferschema", "true")\
    .option("mode", "DROPMALFORMED") \
    .csv("gs://assignment-seb-warehouse-eu-west3/datasets/input/fhvhv_tripdata_2021-01.csv")

#    .csv("gs://assignment-seb-warehouse-eu-west3/datasets/input/green_tripdata_2021-01.csv")

df2 = spark.read.format("com.databricks.spark.csv") \
    .option("header", "true") \
    .option("inferschema", "true") \
    .option("mode", "DROPMALFORMED") \
    .csv("gs://assignment-seb-warehouse-eu-west3/datasets/input/fhvhv_tripdata_2021-03.csv")


#df1.show()
df1.printSchema()
df1.createOrReplaceTempView('df1_View')
spark.sql("""DROP TABLE IF EXISTS fhvhv_tripdata1""")
spark.sql("""CREATE EXTERNAL TABLE IF NOT EXISTS fhvhv_tripdata1
LOCATION "gs://assignment-seb-warehouse-eu-west3/datasets/input/fhvhv_tripdata_2021-01_spark_load/"
AS SELECT * FROM df1_view
""")

#df2.show()
df2.printSchema()
df2.createOrReplaceTempView('df2_View')
spark.sql("""DROP TABLE IF EXISTS fhvhv_tripdata3""")
spark.sql("""CREATE EXTERNAL TABLE IF NOT EXISTS fhvhv_tripdata3
LOCATION "gs://assignment-seb-warehouse-eu-west3/datasets/input/fhvhv_tripdata_2021-03_spark_load/"
AS SELECT * FROM df2_view
""")