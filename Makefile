python=python
mamba=mamba
pkg=ppqm

env:
	${mamba} env create -f ./environment.yml -p ./env
	./env/bin/python -m pip setup.py install --editable

setup-dev:
	pre-commit install

test:
	${python} -m pytest -vrs tests

cov:
	${python} -m pytest -vrs --cov=${pkg} --cov-report html tests

start-jupyter:
	PYTHONPATH=$$PYTHONPATH:`pwd`/src ${python} -m jupyterlab --no-browser --ip $$(hostname -I | awk '{print $$1}') --port 8888
