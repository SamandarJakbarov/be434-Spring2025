.PHONY: test

test:
	pytest -xv test.py blastomatic.py
	flake8 blastomatic.py
	pylint blastomatic.py

taxdump:
	wget ftp://ftp.ncbi.nih.gov/pub/taxonomy/gi_taxid_nucl.dmp.gz
