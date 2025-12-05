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
	pyreverse -o png -p pig_dice -d doc/uml src
	py -c "import shutil, pathlib; d = pathlib.Path('doc/uml'); shutil.move(str(d/'classes_pig_dice.png'), str(d/'class_diagram.png'))"
	py -c "import shutil, pathlib; d = pathlib.Path('doc/uml'); shutil.move(str(d/'packages_pig_dice.png'), str(d/'package_diagram.png'))"
