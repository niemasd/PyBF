#! /usr/bin/env python3
'''
Load a Hash Set from a file and check all strings in a text file containing whitespace-delimited strings
'''
from niemabf import HashSet, open_file
from sys import argv
if __name__ == "__main__":
    if len(argv) != 3:
        print("USAGE: %s <input_hashset_pkl> <input_txt>" % argv[0]); exit(1)
    print("Loading HashSet from: %s" % argv[1])
    hs = HashSet.load(argv[1])
    print("Loaded Hash Set (NiemaBF v%s, h = %s)" % (hs.niemabf_version, hs.hash_func_key))
    print("Checking all whitespace-delimited strings from: %s" % argv[2])
    count = 0
    with open_file(argv[2]) as f:
        for s in f.read().strip().split():
            if s.strip() in hs:
                count += 1
    print("Found %d word(s)" % count)
