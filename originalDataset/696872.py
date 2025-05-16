#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict

MOD = 1000000007

N,A,B = [int(x) for x in input().split()]
As = [int(x) for x in input().split()]

arr = [(x,x) for x in As]
arr.sort()


turn = 0
prev = None

dd = defaultdict(tuple)

cache = {}

while True:
    idx_order = tuple(x[1] for x in arr)
    #print(hash(idx_order))
    # if idx_order in dd:
    #     print("seen!")
    #     if dd[idx_order] == turn - 1:
    #         pass
    #     else:
    # dd[idx_order] = turn

    # process
    ini = arr[0]
    new_arr = [(ini[0]*A, ini[1])] + arr[1:]
    new_arr.sort()

    arr = new_arr

    # print(arr)

    turn += 1
    if turn == B:
        print("\n".join( [str(x[0]%MOD) for x in arr] ))
        break

    enough = 1000
    if enough <= turn < enough + N:
        cache[turn] = arr
        idx_order = tuple(x[1] for x in arr)
        #print("turn, idxes:", turn, idx_order)

    elif turn >= enough + N:
        turn = B

        diff = turn - enough
        v1 = diff % N
        v2 = diff // N

        tmp = [(x[0] * pow(A,v2,MOD)) % MOD for x in cache[enough + v1]]

        print("\n".join(str(x) for x in tmp))
        break
