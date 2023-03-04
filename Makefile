PYTHON :=
ifeq ($(OS),Windows_NT)
	PYTHON=.venv\Scripts\python
else
	PYTHON=.venv/bin/python
endif

venv:
	test -d .venv || python -m venv .venv/

install: 
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

run: 
	@$(PYTHON) main.py
	

check-venv:
	@if [ -z "$$(which python | grep -o .venv)" ]; then \
		exit 1; \
	fi

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
	cd test/ && pylint *.py

flake8:
	@$(call MESSAGE,$@)
	-flake8

lint: flake8 pylint
