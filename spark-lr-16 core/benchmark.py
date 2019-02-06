from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import DoubleType
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
import time
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--core", help="The number of core",)
parser.add_argument("--input", help="input ../input/input csv")
args = parser.parse_args()

print(f"{args.input} input({os.path.getsize(args.input)}) running with {args.core} core.")
print("SparkContext starting...")
conf = SparkConf().setAppName("sparklr").setMaster(f"local[{args.core}]")
sc= SparkContext(conf=conf)
sc.setLogLevel("OFF")
sqlContext = SQLContext(sc)

print("Data is loading...")
data = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load(args.input)


data = data.withColumn("Open", data["Open"].cast(DoubleType()))
data = data.withColumn("Date", data["Date"].cast(DoubleType()))
data = data.withColumn("High", data["High"].cast(DoubleType()))
data = data.withColumn("Low", data["Low"].cast(DoubleType()))
data = data.withColumn("Close", data["Close"].cast(DoubleType()))
data = data.withColumn("Adj Close", data["Adj Close"].cast(DoubleType()))
data = data.withColumn("Volume", data["Volume"].cast(DoubleType()))

vectorAssembler = VectorAssembler(inputCols = ['Date','Open','High', 'Low', 'Close', 'Volume'], outputCol = 'features')
vdata=vectorAssembler.setHandleInvalid("skip").transform(data).select(['features','Adj Close'])
splits = vdata.randomSplit([0.7, 0.3])
train_df = splits[0]
test_df = splits[1]

print("MLlib is calling...")
start_time = time.time()
lr = LinearRegression(featuresCol = 'features', labelCol='Adj Close', maxIter=10, regParam=0.3, elasticNetParam=0.8)
lr_model = lr.fit(train_df)
#print("Coefficients: " + str(lr_model.coefficients))
#print("Intercept: " + str(lr_model.intercept))
end_time = time.time()
result_str = f"Core: {args.core} - Input: {args.input} - Size: {(os.path.getsize(args.input)/(1024*1024)):.02f} MB - Elapsed time:{(end_time-start_time):.02f} sec"
print(result_str)

with open(f"result.txt", "a+") as result_file:
	result_file.write(result_str+"\r\n")
