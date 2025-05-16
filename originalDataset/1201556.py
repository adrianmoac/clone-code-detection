#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def hhmm2min(hhmm):
    h = int(hhmm[:2])
    m = int(hhmm[2:4])
    return 60*h + m

def min2hhmm(m):
    h = m // 60
    m = m %  60
    return "{:02d}{:02d}".format(h, m)

def read_memo():
    n = int(input())

    memo = []
    for _ in range(n):
        start, end = map(hhmm2min, input().split("-"))
        memo.append((start, end))

    return memo

def memo2bits(memo):
    bits = [False] * (24*60//5 + 1)

    for start, end in memo:
        min_ = start // 5
        max_ = end   // 5 + (1 if end % 5 else 0)
        bits[min_:max_] = [True] * (max_ - min_)

    return bits

def bits2ranges(bits):
    start = None
    end   = None
    in_range = False

    for i, bit in enumerate(bits):
        if bit:
            if not in_range:
                start    = 5*i
                in_range = True
        else:
            if in_range:
                end      = 5*i
                yield (start, end)
                in_range = False

    if in_range:
        yield (start, 24*60)

def main():
    memo = read_memo()

    bits = memo2bits(memo)

    for start, end in bits2ranges(bits):
        start_hhmm, end_hhmm = map(min2hhmm, (start, end))
        print("{}-{}".format(start_hhmm, end_hhmm))

if __name__ == "__main__": main()
