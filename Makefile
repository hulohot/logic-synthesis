.PHONY: test clean

test:
	echo "Running Python tests"
	python3 -m unittest discover -s tests

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete