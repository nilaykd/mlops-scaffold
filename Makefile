install:
	pip install --upgrade pip &&\
			pip install -r requirements.txt

lint:
	pylint --disable=R,C hello.py

test:
	python -m pytest -vv --cov=hello test_hello.py

# Code formatting for Black's strict style (PEP 8 + Black's rules)
format:
	black *.py