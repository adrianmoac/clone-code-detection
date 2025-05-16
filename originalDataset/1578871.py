import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
gosa = 1.0 / 10**10
mod = 10**9+7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    n,m,R = LI()
    t = LI()
    e = collections.defaultdict(list)
    for _ in range(m):
        a,b,c = LI()
        e[a].append((b,c))
        e[b].append((a,c))

    # メソッドのみ版
    def search(s):
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

            for uv, ud in e[u]:
                if v[uv]:
                    continue
                vd = k + ud
                if d[uv] > vd:
                    d[uv] = vd
                    heapq.heappush(q, (vd, uv))

        return d
    td = {}
    for i in t:
        td[i] = search(i)

    r = inf
    for ta in itertools.permutations(t):
        tr = 0
        for i in range(1,R):
            tr += td[ta[i-1]][ta[i]]
        if tr < r:
            r = tr

    return r

print(main())



