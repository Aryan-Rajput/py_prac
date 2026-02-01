# Lab1.py
from spark_labs.lab_common import getspark  # adjust to your final package name


sc = getspark().sparkContext
rdd = sc.parallelize([("a",1),("a",2),("b",1),("c",5)], 2)
agg = rdd.reduceByKey(lambda a,b: a+b)  # wide-ish but optimized combiner
print(agg.collect())