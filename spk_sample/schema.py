from pyspark.sql.types import *

output_schema = StructType([
    StructField("word", StringType(), True),
    StructField("count", IntegerType(), True)
])
