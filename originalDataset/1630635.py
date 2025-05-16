# -*- coding: utf-8 -*-
"""
http://abc065.contest.atcoder.jp/tasks/arc076_b
TLE
"""
import sys
from sys import stdin
input = stdin.readline
from collections import namedtuple


class DisjointSet(object):
    def __init__(self, size):
        self.rank = []
        self.p = []
        for i in range(size):
            self.makeSet(i)

    def makeSet(self, x):
        self.p.insert(x, x)
        self.rank.insert(x, 0)

    def same(self, x, y):
        return self.findSet(x) == self.findSet(y)

    def unite(self, x, y):
        self.link(self.findSet(x), self.findSet(y))

    def link(self, x, y):
        if self.rank[x] > self.rank[y]:
            self.p[y] = x
        else:
            self.p[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def findSet(self, x):
        if x != self.p[x]:
            self.p[x] = self.findSet(self.p[x])
        return self.p[x]


def kruskal(V, E, es):
    es.sort(key=lambda x: x.c)
    uf = DisjointSet(V)
    res = 0

    for i in range(E):
        e = es[i]
        if not uf.same(e.u, e.v):
            uf.unite(e.u, e.v)
            res += e.c
    return res


edge = namedtuple('edge', ['u', 'v', 'c'])
def main(args):
    N = int(input())
    cities = []
    for i in range(1, N+1):
        x, y = map(int, input().split())
        cities.append([x, y, i])

    es = []
    cities.sort(key=lambda x: x[0])
    prev_x, _, prev_i = cities[0]
    for x, y, i in cities[1:]:
        es.append(edge(prev_i, i, x - prev_x))
#        es.append(edge(i, prev_i, x - prev_x))
        prev_x = x
        prev_i = i

    cities.sort(key=lambda x: x[1])
    _, prev_y, prev_i = cities[0]
    for x, y, i in cities[1:]:
        es.append(edge(prev_i, i, y - prev_y))
#        es.append(edge(i, prev_i, y - prev_y))
        prev_y = y
        prev_i = i

    result = kruskal(N+1, len(es), es)
    print(result)


if __name__ == '__main__':
    main(sys.argv[1:])