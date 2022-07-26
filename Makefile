python=python
mamba=mamba
pkg=ppqm

env:
	${mamba} env create -f ./environment.yml -p ./env

setup-dev:
	pre-commit install

test:
	${python} -m pytest -vrs tests

cov:
	${python} -m pytest -vrs --cov=${pkg} --cov-report html tests

start_jupyter:
	export PYTHONPATH=$$PYTHONPATH:./ & jupyter-lab
