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
    n = I()
    e = collections.defaultdict(list)
    for _ in range(n-1):
        a,b = LI()
        e[a].append(b)
        e[b].append(a)

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

            for uv in e[u]:
                ud = 1
                if v[uv]:
                    continue
                vd = k + ud
                if d[uv] > vd:
                    d[uv] = vd
                    heapq.heappush(q, (vd, uv))

        return d

    ad = search(1)
    bd = search(n)
    t = -1
    for i in range(2,n):
        if ad[i] <= bd[i]:
            t += 1
        else:
            t -= 1

    if t >= 0:
        return 'Fennec'

    return 'Snuke'


print(main())



