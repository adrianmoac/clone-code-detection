import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    n,m,t = LI()
    aa = LI()
    d = collections.defaultdict(list)
    e = collections.defaultdict(list)
    for _ in range(m):
        a,b,c = LI()
        d[a-1].append((b-1,c))
        e[b-1].append((a-1,c))

    f = [inf] * n
    f[0] = 0
    q = []
    heapq.heappush(q, (0, 0))
    v = collections.defaultdict(bool)
    while len(q):
        k, u = heapq.heappop(q)
        if v[u]:
            continue
        v[u] = True

        for uv, ud in d[u]:
            if v[uv]:
                continue
            vd = k + ud
            if f[uv] > vd:
                f[uv] = vd
                heapq.heappush(q, (vd, uv))

    g = [inf] * n
    g[0] = 0
    q = []
    heapq.heappush(q, (0, 0))
    v = collections.defaultdict(bool)
    while len(q):
        k, u = heapq.heappop(q)
        if v[u]:
            continue
        v[u] = True

        for uv, ud in e[u]:
            if v[uv]:
                continue
            vd = k + ud
            if g[uv] > vd:
                g[uv] = vd
                heapq.heappush(q, (vd, uv))

    m = 0
    for i in range(n):
        ti = t - f[i] - g[i]
        if ti < 1:
            continue
        if ti * aa[i] > m:
            m = ti * aa[i]

    return m


print(main())
