from operator import add


def run_job(spark, input_file):
    lines = spark.read.text(input_file).rdd.map(lambda r: r[0])
    counts = lines.flatMap(
        lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(add)
    # sort by word count in descending order
    output = counts.sortBy(lambda x: x[1], ascending=False).collect()

    for (word, count) in output:
        print("%s: %i" % (word, count))
