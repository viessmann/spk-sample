import sys

from pyspark.sql import SparkSession

from spk_sample.func import run_job, total_count, unique_count


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession.builder.appName("WordCount").getOrCreate()

    input_file = sys.argv[1]

    run_job(spark, input_file)
    print(f"Counts: unique {unique_count.value}, total {total_count.value}")
    spark.stop()
