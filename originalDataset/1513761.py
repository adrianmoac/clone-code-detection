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


class Ruiwa():
    def __init__(self, a):
        self.H = h = len(a)
        self.W = w = len(a[0])
        self.R = r = a
        for i in range(h):
            for j in range(1,w):
                r[i][j] += r[i][j-1]

        for i in range(1,h):
            for j in range(w):
                r[i][j] += r[i-1][j]

    def search(self, x1, y1, x2, y2):
        if x1 > x2 or y1 > y2:
            return 0

        r = self.R
        rr = r[y2][x2]
        if x1 > 0 and y1 > 0:
            return rr - r[y1-1][x2] - r[y2][x1-1] + r[y1-1][x1-1]
        if x1 > 0:
            rr -= r[y2][x1-1]
        if y1 > 0:
            rr -= r[y1-1][x2]

        return rr


def main():
    N = I()
    d = [LI() for _ in range(N)]
    rui = Ruiwa(d)
    t = [0] * (N*N+1)
    for i in range(N):
        for j in range(i,N):
            for k in range(N):
                for l in range(k,N):
                    s = (j-i+1) * (l-k+1)
                    tt = rui.search(i,k,j,l)
                    if t[s] < tt:
                        t[s] = tt
    c = t[0]
    for i in range(1,N*N+1):
        if t[i] < c:
            t[i] = c
        else:
            c = t[i]
    r = []
    q = I()
    for _ in range(q):
        p = I()
        r.append(t[p])

    return '\n'.join(map(str,r))


print(main())

