from collections import defaultdict

N, K, L = map(int, input().split())


class UnionFind(object):

    def __init__(self, n):
        self.n = n
        self.par = list(range(n))
        self.rank = [1] * n

    def is_same(self, a, b):
        return self.root(a) == self.root(b)

    def root(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.par[y] = x
        elif self.rank[x]  < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            self.rank[x] += 1

load_uf = UnionFind(N)
rail_uf = UnionFind(N)

for k in range(K):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    load_uf.unite(p, q)

for l in range(L):
    r, s = map(int, input().split())
    r -= 1
    s -= 1
    rail_uf.unite(r, s)

ans = []
d = defaultdict(int)
for i in range(N):
    lp = load_uf.root(i)
    rp = rail_uf.root(i)
    d[lp, rp] += 1

for i in range(N):
    lp = load_uf.par[i]
    rp = rail_uf.par[i]
    if i == N-1:
        print(d[lp, rp])
    else:
        print(d[lp, rp], end=' ')

#     print(rd[rp])
#     print(ld[lp])
#     ans.append(len(ld[lp] & rd[rp]))
# print(str(ans).replace(',', '')[1:-1])
