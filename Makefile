.PHONY: test

deps:
	pip install -r requirements.txt
	pip install -r test_requirements.txt

test:
	PYTHONPATH=. py.test --verbose -s

run: main.py
	python3 main.py

lint:
	flake8 hello_world test
