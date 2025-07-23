#! /usr/bin/env python3
'''
Build a Hash Set from a file containing whitespace-delimited strings
'''
from niemabf import HashSet, open_file
from sys import argv
if __name__ == "__main__":
    if len(argv) != 3:
        print("USAGE: %s <input_txt> <output_hashset_pkl>" % argv[0]); exit(1)
    print("Creating empty Hash Set...")
    hs = HashSet()
    print("Inserting all whitespace-delimited strings from: %s" % argv[1])
    num_inserts = 0
    with open_file(argv[1]) as f:
        for s in f.read().strip().split():
            hs.insert(s.strip())
            num_inserts += 1
    print("Successfully inserted %d strings" % num_inserts)
    print("Dumping Hash Set to: %s" % argv[2])
    hs.dump(argv[2])
