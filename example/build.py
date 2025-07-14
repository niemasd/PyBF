#! /usr/bin/env python3
'''
Build a Bloom Filter from a file containing whitespace-delimited strings
'''
from niemabf import BloomFilter, open_file
from sys import argv
if __name__ == "__main__":
    if len(argv) != 5:
        print("USAGE: %s <k> <m> <input_txt> <output_bloomfilter_pkl>" % argv[0]); exit(1)
    k = int(argv[1]); m = int(argv[2])
    print("Creating empty Bloom Filter with k = %d hash functions and m = %d bits..." % (k, m))
    bf = BloomFilter(k, m)
    print("Inserting all whitespace-delimited strings from: %s" % argv[3])
    with open_file(argv[3]) as f:
        for s in f.read().strip().split():
            bf.insert(s.strip())
    print("Successfully inserted %d strings" % len(bf))
    print("Dumping Bloom Filter to: %s" % argv[4])
    bf.dump(argv[4])
