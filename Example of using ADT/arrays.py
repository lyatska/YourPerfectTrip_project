import ctypes

class DynamicArray:
    """
    A dynamic array class akin to a simplified Python list.
    """
    def __init__(self):
        """
        Creates an empty array.
        """
        self._n = 0                                # count actual elements
        self._capacity = 1                         # default array capacity
        self._A = self._make_array(self._capacity) # low-level array

    def __len__(self):
        """
        Returns number of elements stored in the array.
        """
        return self._n

    def __getitem__(self, k):
        """
        Returns element at index k.
        """
        if not 0 <= k < self._n:
            raise IndexError( 'invalid index' )
        return self._A[k]                          # retrieve from array

    def append(self, obj):
        """
        Adds object to end of the array.
        """
        if self._n == self._capacity:              # not enough room
            self._resize(2 * self._capacity)       # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):                          # nonpublic utitity
        """
        Resizes internal array to capacity c.
        """
        B = self._make_array(c)                    # new (bigger) array
        for k in range(self._n):                   # for each existing value
            B[k] = self._A[k]
        self._A = B                                # use the bigger array
        self._capacity = c

    def _make_array(self, c): # nonpublic utitity
        """
        Returns new array with capacity c.
        """
        return (c * ctypes.py_object)( )            # see ctypes documentation

    def insert(self, k, value):
        """
        Inserts value at index k, shifting subsequent values rightward.
        """
        # (for simplicity, we assume 0 <= k <= n in this verion)
        if self._n == self._capacity: # not enough room
            self._resize(2 * self._capacity) # so double capacity
        for j in range(self._n, k, -1): # shift rightmost first
            self._A[j] = self._A[j - 1]
        self._A[k] = value # store newest element
        self._n += 1

    def remove(self, value):
        """
        Removes first occurrence of value( or  raise ValueError).
        """
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._A[k] == value:               # found a match!
                for j in range(k, self._n - 1):   # shift others to fill gap
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None       # help garbage collection
                self._n -= 1                      # we have one less item

                return  # exit immediately
        raise ValueError( "value not found" )     # only reached if no match

    def __str__(self):
        """
        String representation of the class.
        """
        res = ''
        for i in range(len(self)):
            m = str(self._A[i])
            res += m
        return res