# Twine
twine: pybf/__init__.py pybf/BitArray.py pybf/BloomFilter.py pybf/common.py pybf/Hash.py
	python3 setup.py sdist bdist_wheel
	twine upload dist/*.tar.gz
