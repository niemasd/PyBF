# PyBF imports
from pybf.BitArray import BitArray
from pybf.common import PYBF_VERSION
from pybf.Hash import HASH_FUNCTIONS

class BloomFilter:
    '''Bloom Filter class'''
    def __init__(self, k, m, hash_func='mmh3'):
        '''
        Initialize a new Bloom Filter

        Args:
            k (int): The number of hash functions to use in this Bloom Filter (must be positive)
            m (int): The number of bits to use in this Bloom Filter (must be multiple of 8)
            hash_func (str): The hash function to use in this Bloom Filter
        '''
        if not isinstance(k, int):
            raise TypeError("`k` must be type `int`, but received: `%s`" % type(k))
        if k < 1:
            raise ValueError("`k` must be positive, but received: %s" % k)
        if hash_func not in HASH_FUNCTIONS:
            raise ValueError("Invalid hash function (%s). Options: %s" % (hash_func, ', '.join(sorted(HASH_FUNCTIONS.keys()))))
        self.pybf_version = PYBF_VERSION
        self.k = k
        self.bits = BitArray(m)
        self.hash_func_key = hash_func
        self.hash_func = HASH_FUNCTIONS[hash_func]

    def insert(self, x):
        '''
        Insert an element into this Bloom Filter

        Args:
            x (object): The element to insert
        '''
        pass # TODO
