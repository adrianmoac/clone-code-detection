#!/usr/bin/python

import os
import sys
import itertools

def solve(f):
    l, x, y, s, d = f.read_int_list()
    ans = float((d-s)%l)/(x+y)
    if y > x:
        ans = min(ans, float((s-d)%l)/(y-x))

    return ans

class Reader(object):
    def __init__(self, filename=None):
        self.test_mode = filename is not None
        self.cases = 1
        self.buffer = []
        if self.test_mode:
            with open(filename) as f:
                blank_flg = False
                for line in f:
                    line = line.strip()
                    if line:
                        self.buffer.append(line)
                        blank_flg = False
                    else:
                        if not blank_flg: self.cases += 1
                        blank_flg = True

    def __readline(self):
        return self.buffer.pop(0) if self.test_mode else raw_input()

    def read_int(self):
        return int(self.__readline())
    def read_float(self):
        return float(self.__readline())
    def read_long(self):
        return long(self.__readline())
    def read_str(self):
        return self.__readline()

    def read_int_list(self):
        return [int(item) for item in self.__readline().split()]
    def read_float_list(self):
        return [float(item) for item in self.__readline().split()]
    def read_long_list(self):
        return [long(item) for item in self.__readline().split()]
    def read_str_list(self):
        return self.__readline().split()

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv)>1 else None
    f = Reader(filename)
    if f.test_mode:
        for c in xrange(f.cases):
            print "Case #%d"%(c+1)
            print solve(f)
    else:
        print solve(f)
