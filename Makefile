.PHONY: run test coverage lint doc uml

run:
	py src/main.py

test:
	pytest tests/ --verbose

coverage:
	pytest --cov=src --cov-report=term-missing

lint:
	pylint src
	flake8 src

doc:
	py -m sphinx.ext.apidoc -o doc/source/api src
	py -m sphinx -b html doc/source doc/build/html

uml:
	pyreverse -o png -p pig_dice src
	mv classes_pig_dice.png doc/uml/class_diagram.png
	mv packages_pig_dice.png doc/uml/package_diagram.png