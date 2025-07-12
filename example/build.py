#! /usr/bin/env python3
'''
Build a Bloom Filter from a file containing whitespace-delimited strings
'''
from pybf import BloomFilter, open_file
from sys import argv
if __name__ == "__main__":
    if len(argv) != 5:
        print("USAGE: %s <k> <m> <input_txt> <output_bf>" % argv[0]); exit(1)
    bf = BloomFilter(int(argv[1]), int(argv[2]))
    with open_file(argv[3]) as f:
        for s in f.read().strip().split():
            bf.insert(s.strip())
    print(len(bf)) # TODO DELETE
