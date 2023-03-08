PYTHON = python

# ---------------------------------------------------------
# run the code
#
run: 
	@$(PYTHON) main.py

# ---------------------------------------------------------
# Setup a venv and install packages.
#
venv:
	test -d .venv || python -m venv .venv/
	@printf "Now activate the Python virtual environment.\n"
	@printf "On Unix and Mac, do:\n"
	@printf ". .venv/bin/activate\n"
	@printf "On Windows (bash terminal), do:\n"
	@printf ". .venv/Scripts/activate\n"
	@printf "Type 'deactivate' to deactivate.\n"


install: 
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

installed:
	$(PYTHON) -m pip list

check-venv:
	@if [ -z "$$(which python | grep -o .venv)" ]; then \
		exit 1; \
	fi

activate-w:
	. .venv/Scripts/activate

activate-m:
	. .venv/bin/activate

# ---------------------------------------------------------
# Work with unit test and code coverage.
#


test:
	$(PYTHON) -m unittest discover -p 'test_*.py' -v -b

coverage:
	coverage run -m unittest
	coverage report -m

# ---------------------------------------------------------
# Work with static code linters.
#
pylint:
	@$(call MESSAGE,$@)
	cd app/ && pylint *.py

flake8:
	@$(call MESSAGE,$@)
	cd app/ && flake8

lint: flake8 pylint


# ---------------------------------------------------------
# Cleanup generated and installed files.
#
clean:
	@$(call MESSAGE,$@)
	rm -f .coverage *.pyc
	rm -rf __pycache__
	rm -rf htmlcov

clean-doc: clean
	@$(call MESSAGE,$@)
	rm -rf doc

clean-all: clean clean-doc
	@$(call MESSAGE,$@)
	rm -rf .venv

# Work with generating documentation.
#
.PHONY: pydoc
pydoc:
	@$(call MESSAGE,$@)
	install -d doc/pydoc
	python -m pydoc -w app
	mv *.html doc/pydoc

pdoc:
	@$(call MESSAGE,$@)
	pdoc  --output-dir doc/pdoc app/*.py

pyreverse:
	@$(call MESSAGE,$@)
	install -d doc/pyreverse
	pyreverse app/*.py
	dot -Tpng classes.dot -o doc/pyreverse/classes.png
	dot -Tpng packages.dot -o doc/pyreverse/packages.png
	rm -f classes.dot packages.dot
