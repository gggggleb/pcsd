build:
		pip wheel .
		rm -r pcsd.egg-info/ build/
		mkdir package
		mv *.whl package
test:
		python pcsd_test.py
install:
		pip install .