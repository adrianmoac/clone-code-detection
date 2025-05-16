import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**15
mod = 10**9+7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    n,m = LI()
    e = collections.defaultdict(set)
    k = []
    for _ in range(m):
        a,b = LI_()
        e[a].add(b)
        e[b].add(a)
        k.append((a,b))

    # メソッドのみ版
    def search(s):
        d = [inf] * n
        d[s] = 0
        q = []
        heapq.heappush(q, (0, s))
        v = collections.defaultdict(bool)
        while len(q):
            k, u = heapq.heappop(q)
            if v[u]:
                continue
            v[u] = True

            for uv in e[u]:
                ud = 1
                if v[uv]:
                    continue
                vd = k + ud
                if d[uv] > vd:
                    d[uv] = vd
                    heapq.heappush(q, (vd, uv))

        return d

    r = 0
    for a,b in k:
        e[a].remove(b)
        e[b].remove(a)
        d = search(0)
        if max(d) == inf:
            r += 1
        e[a].add(b)
        e[b].add(a)

    return r


print(main())


