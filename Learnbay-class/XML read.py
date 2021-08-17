#!/usr/bin/env python
import os
from pyspark.sql import SparkSession
os.environ['PYSPARK_SUBMIT_ARGS'] = '--jars file:///home/vijay/Documents/jars/spark-xml_2.12-0.11.0.jar pyspark-shell'

spark = SparkSession.builder.appName("readXML").getOrCreate()
empDF = spark.read.format('com.databricks.spark.xml').option("rootTag", "employees").option("rowTag", "employee").load("/home/vijay/Downloads/emp.xml")

