from operator import add

def get_counts(lines):
    counts = lines.flatMap(
        lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(add)
    # sort by word count in descending order
    return counts.sortBy(lambda x: x[1], ascending=False).collect()
