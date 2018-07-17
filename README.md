# spk-sample
Sample Spark app to to demonstrate Python packaging and deployment in Spark cluster (Databricks, HDInsight, Local) 

# Run on local

`./scripts/run_local.sh`

# Build

`make build`

# Run on Databricks

First setup [Databricks CLI](https://docs.azuredatabricks.net/user-guide/dev-tools/databricks-cli.html)

* Copy egg package and main file (wordcount.py) & files to Databricks filesystem: 

`dbfs cp dist/spk_sample-1.0.0-py3.6.egg dbfs:/spk_sample/dist/spk_sample-1.0.0-py3.6.egg`

`dbfs cp wordcount.py dbfs:/spk_sample/wordcount.py`

`dbfs cp wordcount.py dbfs:/spk_sample/sample.txt`

* Run Spark submit from Jobs UI with following parameters:

`["--py-files","dbfs:/spk_sample/dist/spk_sample-1.0.0-py3.6.egg","dbfs:/spk_sample/wordcount.py", "dbfs:/spk_sample/sample.txt"]`

## Limitations

* With `spark-submit`, Databricks always creates new cluster. You cannot run this job on already running cluster.
