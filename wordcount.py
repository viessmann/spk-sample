import sys

from pyspark.sql import SparkSession

from spk_sample.func import get_counts


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession.builder.appName("WordCount").getOrCreate()

    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])
    output = get_counts(lines)
    for (word, count) in output:
        print("%s: %i" % (word, count))

    spark.stop()
