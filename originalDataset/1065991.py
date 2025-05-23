import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI(): return list(map(int, input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()


def main():
    n,a,b = LI()
    r = 0
    x = LI()

    t = x[0]
    x.sort()
    i = x.index(t)
    if i == n-1 or i == 0:
        for j in range(n-1):
            if (x[j+1] - x[j]) * a < b:
                r += (x[j+1] - x[j]) * a
            else:
                r += b
        return r

    if (x[i+1]-x[0])*a < b:
        r += ((t - x[0]) + (x[i+1] - x[0]))*a
        for j in range(i+2,n):
            if (x[j] - x[j-1]) * a < b:
                r += (x[j] - x[j-1]) * a
            else:
                r += b
        return r
    if (x[-1]-x[i-1])*a < b:
        r += ((x[-1] - t) + (x[-1] - x[i-1]))*a
        for j in range(i-1):
            if (x[j+1] - x[j]) * a < b:
                r += (x[j+1] - x[j]) * a
            else:
                r += b
        return r

    for j in range(i+2,n):
        if (x[j] - x[j-1]) * a < b:
            r += (x[j] - x[j-1]) * a
        else:
            r += b
    for j in range(i-1):
        if (x[j+1] - x[j]) * a < b:
            r += (x[j+1] - x[j]) * a
        else:
            r += b
    r += b

    return r


print(main())
