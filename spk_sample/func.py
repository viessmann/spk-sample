from operator import add

from pyspark.accumulators import Accumulator, AddingAccumulatorParam

unique_count = Accumulator('unique', 0, AddingAccumulatorParam(0))
total_count = Accumulator('total', 0, AddingAccumulatorParam(0))


def get_sort_param(x):
    unique_count.add(1)
    total_count.add(x[1])
    return x[1]


def run_job(spark, input_file):
    lines = spark.read.text(input_file).rdd.map(lambda r: r[0])
    counts = lines.flatMap(
        lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(add)
    # sort by word count in descending order
    output = counts.sortBy(get_sort_param, ascending=False).collect()

    for (word, count) in output:
        print("%s: %i" % (word, count))
