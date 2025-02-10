.PHONY: test

test:
	pytest -xv test.py cgc.py
	flake8 cgc.py
	pylint cgc.py

seqs.fa:
	./genseq.py -n 1000
