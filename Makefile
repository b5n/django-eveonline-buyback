build:
	python3 -m pip install --upgrade setuptools wheel
	python3 setup.py sdist bdist_wheel

testpypi:
	python3 -m pip install --upgrade twine
	twine upload --repository testpypi dist/*

pypi:
	python3 -m pip install --upgrade twine
	twine upload dist/*

clean:
	rm -rf build dist *.egg-info
	find . -type d -name '__pycache__' -exec rm -rf {} +
