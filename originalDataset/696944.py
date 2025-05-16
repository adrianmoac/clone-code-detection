#!/usr/bin/env python

MOD = 1000000007


def read():
    N, A, B = map(int, raw_input().split())
    vList = map(int, raw_input().split())
    return A, B, vList


def mypow(p, n):
    if n == 0:
        return 1
    t = mypow(p, n / 2)
    return t * t % MOD if n % 2 == 0 else t * t * p % MOD


def work((A, B, vList)):

    if A == 1:
        for v in sorted(vList):
            print v
        return

    
    maxIdx = len(vList) - 1
    for i in range(len(vList) - 1, -1, -1):
        if vList[maxIdx] < vList[i]:
            maxIdx = i
    
    while B:
        minV = -1
        minIdx = -1
        for idx, val in enumerate(vList):
            if minV == -1 or minV > val:
                minV = val
                minIdx = idx
        vList[minIdx] *= A
        
        B -= 1
        
        if minIdx == maxIdx:
            vList.sort()
            for i in range(B % len(vList)):
                vList[i] *= A
            vList = vList[B % len(vList):] + vList[:B % len(vList)]
                
            nPow = B / len(vList)
            for i in range(len(vList)):
                vList[i] = vList[i] * mypow(A, nPow) % MOD

            for v in vList:
                print v
            return

    for v in sorted(vList):
        print v % MOD


if __name__ == "__main__":
    work(read())
