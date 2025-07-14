#! /usr/bin/env python3
'''
Load a Bloom Filter from a file and check all strings in a text file containing whitespace-delimited strings
'''
from niemabf import BloomFilter, open_file
from sys import argv
if __name__ == "__main__":
    if len(argv) != 3:
        print("USAGE: %s <input_bloomfilter_pkl> <input_txt>" % argv[0]); exit(1)
    print("Loading Bloom Filter from: %s" % argv[1])
    bf = BloomFilter.load(argv[1])
    print("Loaded Bloom Filter with k = %d hash functions and m = %d bits" % (bf.k, bf.m))
    print("Checking all whitespace-delimited strings from: %s" % argv[2])
    count = 0
    with open_file(argv[2]) as f:
        for s in f.read().strip().split():
            if bf.find(s.strip()):
                count += 1
    print("Found %d word(s)" % count)
