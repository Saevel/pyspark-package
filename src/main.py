from pyspark.sql import SparkSession
from pyspark.sql.functions import *

from datetime import *

import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--env', default="local", action="store")
args = parser.parse_args()

print('Environment: ' + str(args.env))

f = open('conf/' + args.env + '.json')
config = json.load(f)

spark = SparkSession.\
    builder\
    .config("spark.redis.host", config['redis']['host'])\
    .config("spark.redis.port", config['redis']['port'])\
    .appName("pyspark-package")\
    .getOrCreate()

df = spark.createDataFrame([
    {"name": "Kamil", "surname": "Owczarek"},
    {"name": "Sylwester", "surname": "Lewandowicz"}
]).withColumn("current_date", lit(datetime.now()))\

df.write\
    .format("org.apache.spark.sql.redis")\
    .option("table", "people")\
    .option("key.column", "surname")\
    .save()

df.show()