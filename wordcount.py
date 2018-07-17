import sys

from pyspark.sql import SparkSession

from spk_sample.func import run_job, total_count, unique_count, check_upper_udf
from spk_sample.schema import output_schema


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession.builder.appName("WordCount").getOrCreate()

    input_file = sys.argv[1]

    output_rdd = run_job(spark, input_file)
    df = spark.createDataFrame(output_rdd, schema=output_schema)
    df = df.withColumn("is_upper", check_upper_udf(df.word))
    df.show()
    print(f"Counts: unique {unique_count.value}, total {total_count.value}")
    spark.stop()
