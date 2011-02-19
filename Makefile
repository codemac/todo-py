clean:
	find . -name '*.pyc' -exec rm -v '{}' \;
test:
	python -m unittest discover t
