test:
	#!/bin/bash
	source env/bin/activate
	python -m pytest test

docs:
	#!/bin/bash
	source env/bin/activate
	cd doc
	python -m sphinx doc-in docs
	touch docs/.nojekyll


upload:
	python setup.py bdist_wheel
	twine upload dist/*.whl dist/*.gz
	
	
register:
	python setup.py register
