class DisjointSet(object):
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.num = n  # number of disjoint sets

    def union(self, x, y):
        self._link(self.find_set(x), self.find_set(y))

    def _link(self, x, y):
        if x == y:
            return
        self.num -= 1
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def find_set(self, x):
        xp = self.parent[x]
        if xp != x:
            self.parent[x] = self.find_set(xp)
        return self.parent[x]

def read_data():
    N = int(input())
    xs = []
    ys = []
    for i in range(N):
        x, y = map(int, input().split())
        xs.append((x, i))
        ys.append((y, i))
    return N, xs, ys

def add_edges(xs):
    es = []
    prev_x, prev_i = xs[0]
    for x, i in xs[1:]:
        es.append((x - prev_x, prev_i, i))
        prev_x = x
        prev_i = i
    return es

def solve(N, xs, ys):
    xs.sort()
    ys.sort()
    es = add_edges(xs)
    es.extend(add_edges(ys))
    es.sort()
    ds = DisjointSet(N)
    cost = 0
    for d, i, j in es:
        if ds.find_set(i) == ds.find_set(j):
            continue
        ds.union(i, j)
        cost += d
    return cost

N, xs, ys = read_data()
print(solve(N, xs, ys))
