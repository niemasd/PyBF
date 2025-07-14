# Twine
twine: niemabf/__init__.py niemabf/BitArray.py niemabf/BloomFilter.py niemabf/common.py niemabf/Hash.py
	python3 setup.py sdist bdist_wheel
	twine upload dist/*.tar.gz
