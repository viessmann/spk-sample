help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "test - run tests quickly with the default Python"
	@echo "build - package"

all: default

default: clean test build

clean:
	python setup.py clean

test:
	python setup.py nosetests --config=.noserc --nocapture

test-dev:
	python setup.py nosetests --config=.noserc --tests $(test_class)

build: clean
	python setup.py bdist_egg