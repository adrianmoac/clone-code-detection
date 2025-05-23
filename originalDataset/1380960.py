import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()



def main():
    H,W = LI()
    s = None
    g = None
    a = []
    for i in range(H):
        c = [_ for _ in S()]
        if 's' in c:
            s = (i, c.index('s'))

        if 'g' in c:
            g = (i, c.index('g'))
        a.append([1 if _=='#' else 0 for _ in c])

    x = [1,-1,0,0]
    y = [0,0,1,-1]

    def search(s,g):
        d = collections.defaultdict(lambda: inf)
        d[s] = 0
        q = []
        heapq.heappush(q, (0, s))
        v = collections.defaultdict(bool)
        while len(q):
            k, u = heapq.heappop(q)
            if v[u]:
                continue
            v[u] = True
            if u == g:
                return k

            for ei in range(4):
                ux = u[0]+x[ei]
                uy = u[1]+y[ei]
                if ux < 0 or ux >= H or uy < 0 or uy >= W:
                    continue
                uv = (ux,uy)
                if v[uv]:
                    continue
                vd = k + a[ux][uy]
                if d[uv] > vd:
                    d[uv] = vd
                    heapq.heappush(q, (vd, uv))

        return 3
    if search(s,g) <= 2:
        return 'YES'

    return 'NO'


print(main())






