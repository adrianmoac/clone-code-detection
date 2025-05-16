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
    R,G,B = LI()
    r = inf

    def f(n, ik):
        rr = {}
        for i in range(-600, 601):
            k = abs(i)
            if i <= 0:
                rr[i+ik] = (k+k+n-1) * n // 2
                continue
            nk = n-k
            rk = min(n,k)
            rr[i+ik] = (k+k-rk+1) * rk // 2
            if nk > 0:
                rr[i+ik] += (nk-1) * nk // 2
        return rr

    rr = f(R,-100)
    gr = f(G,0)
    br = f(B,100)

    c = inf
    for k,v in sorted(rr.items()):
        if v > c:
            rr[k] = c
        else:
            c = v

    c = inf
    for k,v in sorted(br.items(), reverse=True):
        if v > c:
            br[k] = c
        else:
            c = v

    for k in range(-250,251):
        tr = gr[k]
        tr += rr[k-G]
        tr += br[k+B]
        if tr < r:
            r = tr

    return r



print(main())

