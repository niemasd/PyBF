# non-standard imports
from numpy import uint8, zeros

class BitArray:
    '''Bit Array class'''
    def __init__(self, m):
        '''
        Initialize a new Bit Array

        Args:
            m (int): The number of bits to use in this Bit Array (must be multiple of 8)
        '''
        if not isinstance(m, int):
            raise TypeError("`m` must be type `int`, but received: `%s`" % type(m))
        if (m < 8) or ((m % 8) != 0):
            raise ValueError("`m` must be a positive multiple of 8, but received: %s" % m)
        self.arr = zeros(m // 8, dtype=uint8, order='C')

    def __len__(self):
        '''
        Return the length (in bits) of this Bit Array

        Returns:
            int: The length (in bits) of this Bit Array
        '''
        return len(self.arr) * 8

    def __str__(self):
        '''
        Return the string representation of this Bit Array

        Returns:
            str: The string representation of this Bit Array
        '''
        return ''.join(str(v) for v in self.arr)
