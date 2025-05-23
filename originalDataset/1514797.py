import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
gosa = 1.0 / 10**9
mod = 10**9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    n = I()
    a = LI()
    b = []
    c = []
    for i in range(n):
        heapq.heappush(b, a[i])
        heapq.heappush(c, -a[i+n*2])
    sb = sum(b)
    sc = sum(c)
    ba = {}
    ba[n-1] = sb
    for i in range(n):
        t = heapq.heappop(b)
        if a[n+i] > t:
            sb -= t
            heapq.heappush(b, a[n+i])
            sb += a[n+i]
        else:
            heapq.heappush(b, t)
        ba[n+i] = sb

    ca = {}
    ca[n*2-1] = sc
    for i in range(n-1,-1,-1):
        t = heapq.heappop(c)
        if -a[n+i] > t:
            sc -= t
            heapq.heappush(c, -a[n+i])
            sc -= a[n+i]
        else:
            heapq.heappush(c, t)
        ca[n+i-1] = sc


    r = -inf
    for k in ba.keys():
        tr = ba[k] + ca[k]
        if tr > r:
            r = tr

    return r



print(main())

