import re
import math
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

def think_appr_square_with_tiles(n):
    '''
    >>> a = think_appr_square_with_tiles(26)
    >>> a[0] + a[1]
    1
    >>> a = think_appr_square_with_tiles(41)
    >>> a[0] + a[1]
    4
    >>> a = think_appr_square_with_tiles(100000)
    >>> a[0] + a[1]
    37
    '''
    ceil = int(math.sqrt(n))
    if ceil ** 2 == n:
        #print('path 1')
        return 0, 0 # diff, remain

    diff, remain = n, n
    for i in range(ceil, 0, -1):
        m = n // i
        d = abs(i - m)
        r = n % m
        if diff + remain > d + r:
            #print('{0:d}, {1:d} => {2:d}, {3:d} # {4:d} {5:d} # {6:d}'.format(diff, remain, d, r, n, m, i))
            diff, remain = d, r 
    #print('path 2 {0:d} {1:d}'.format(diff, remain))
    return diff, remain

def solve():
    n = IO_for_Contest.read_int()
    diff, remain = think_appr_square_with_tiles(n)
    print(diff + remain)

if __name__ == '__main__':
    doctest.testmod()
    solve()