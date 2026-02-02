from spark_labs.lab_common import getspark  # adjust to your final package name


sc = getspark().sparkContext
# rdd = sc.parallelize([("a",1),("a",2),("b",1),("c",5)], 2)
# agg = rdd.reduceByKey(lambda a,b: a+b)  # wide-ish but optimized combiner
# print(agg.collect())

rdd = sc.parallelize([("k", i) for i in range(1000)], 4)
bad = rdd.groupByKey().mapValues(sum)
good = rdd.reduceByKey(lambda a,b: a+b)
 
print(bad.take(1))
print(good.take(1))