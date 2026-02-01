# Lab1.py
from spark_labs.lab_common import getspark  # adjust to your final package name

spark = getspark()
sc = spark.sparkContext

rdd = sc.parallelize([1, 2, 3, 4, 5], 2)
mapped = rdd.map(lambda x: x * 10)
filtered = mapped.filter(lambda x: x > 20)

print(filtered.toDebugString())   # lineage
print(filtered.collect())         # action triggers job
