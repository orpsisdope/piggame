run:
    python src/main.py


test:
    pytest tests/ --verbose

coverage:
    pytest --cov=src --cov-report=term-missing


lint:
    pylint src
    flake8 src


doc:
    sphinx-apidoc -o doc/api src
    sphinx-build -b html doc/api doc/api/html
