SYSTEM_PYTHON=$(shell echo $(shell which python3) || $(shell which python))
PYTHON_VENV=.venv/bin/python
PYTHON=$(shell if test -f ${PYTHON_VENV}; then echo ${PYTHON_VENV}; else echo ${SYSTEM_PYTHON}; fi)

async_port ?= 8001
async_host ?= localhost

install: requirements.txt
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYTHON) -m pytest -x -s -v
