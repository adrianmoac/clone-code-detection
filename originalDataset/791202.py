import re
import doctest

class IO_for_Contest(object):
    @staticmethod
    def my_input():
        #return raw_input()
        return input()

    @staticmethod
    def read_from_input():
        #TODO: impl this for each problem
        pass

    @staticmethod
    def read_line():
        return IO_for_Contest.my_input().strip()

    @staticmethod
    def read_int():
        return int(IO_for_Contest.my_input().strip())

    @staticmethod
    def read_n_int(n):
        return list(map( \
                int, \
                re.split('\s+', IO_for_Contest.my_input().strip())))[ : n]

def solve():
    n, x = IO_for_Contest.read_n_int(2)
    print(think(n, x))

def think(n, x):
    '''
    >>> think(1, 1)
    0
    >>> think(2, 1)
    0
    >>> think(2, 2)
    0
    >>> think(3, 2)
    1
    >>> think(4, 2)
    1
    >>> think(4, 3)
    1
    >>> think(5, 2)
    1
    >>> think(5, 3)
    2
    >>> think(90, 30)
    29
    '''
    if x == 1 or x == n:
        return 0
    return min([x - 1, n - x])

if __name__ == '__main__':
    doctest.testmod()
    solve()
