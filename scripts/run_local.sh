#!/bin/bash


make build

spark-submit --py-files dist/spk_sample-1.0.0-py3.6.egg wordcount.py sample.txt
