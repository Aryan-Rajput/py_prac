import os, sys

# Prevent picking up mismatched local Spark/Hadoop installs
os.environ.pop("SPARK_HOME", None)
os.environ.pop("HADOOP_HOME", None)

# Use JDK 17 explicitly
os.environ["JAVA_HOME"] = r"C:\Program Files\Eclipse Adoptium\jdk-17.0.11.9-hotspot"
os.environ["PATH"] = rf"{os.environ['JAVA_HOME']}\bin;" + os.environ["PATH"]

# Make both driver and executors use the SAME Python (your venv 3.11)
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
os.environ["PYSPARK_PYTHON"] = sys.executable

# Optional hardening against broken global env
os.environ.pop("PYTHONHOME", None)

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window

def getspark(app="GSSparkLabs"):
    return (
        SparkSession.builder
        .appName(app)
        .master("local[*]")
        # Belt & suspenders
        .config("spark.pyspark.driver.python", sys.executable)
        .config("spark.pyspark.python", sys.executable)
        .config("spark.sql.shuffle.partitions", "8")
        .getOrCreate()
    )
    
print("lab_common.py loaded with Python311 for driver & workers")

def getspark(app="GSSparkLabs"):
    return (
        SparkSession.builder
        .appName(app)
        .master("local[*]")
        # Double-ensure via Spark conf (belt & suspenders)
        .config("spark.pyspark.driver.python", sys.executable)
        .config("spark.pyspark.python", sys.executable)
        .config("spark.sql.shuffle.partitions", "8")
        .getOrCreate()
    )


def getspark(app="GSSparkLabs"):
    return (
        SparkSession.builder
        .appName(app)
        .master("local[*]")
        .config("spark.sql.shuffle.partitions", "8")
        .getOrCreate()
    )
 
def makesampledata(spark):
    users = [
        (1, "Asha", "IN", "2026-01-01"),
        (2, "Ravi", "IN", "2026-01-02"),
        (3, "Mina", "US", "2026-01-02"),
        (4, "John", "US", "2026-01-03"),
        (5, None,  "IN", "2026-01-03"),
    ]
    txns = [
        (101, 1, 100.0, "2026-01-10"),
        (102, 1, 120.0, "2026-01-11"),
        (103, 2,  10.0, "2026-01-11"),
        (104, 2,  10.0, "2026-01-11"),  # duplicate-ish
        (105, 99, 99.0,  "2026-01-12"),  # missing user
        (106, 3, 5000.0, "2026-01-13"),
    ]
    usersdf = spark.createDataFrame(users, "userid INT, name STRING, country STRING, signupdt STRING") \
                    .withColumn("signupdt", F.todate("signupdt"))
    txnsdf = spark.createDataFrame(txns, "txnid INT, userid INT, amount DOUBLE, txndt STRING") \
                   .withColumn("txndt", F.todate("txndt"))
    return usersdf, txnsdf



print("lab_common.py loaded")