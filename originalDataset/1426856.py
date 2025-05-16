# coding: utf-8


import sys
sys.setrecursionlimit(int(1e6))


class Graph(object):
    def __init__(self, N):
        self.N = N
        self.paths = [None] * (N + 1)
        for i in range(1, N + 1):
            self.paths[i] = set()

    def path(self, n1, n2):
        self.paths[n1].add(n2)
        self.paths[n2].add(n1)

    def dfs(self, n, f):
        # fからNへの最短経路を探す
        if n == self.N:
            return [n]
        for nn in self.paths[n]:
            if nn != f:
                path = self.dfs(nn, n)
                if path is not None:
                    path.append(n)
                    return path
        return None

    def region(self, start, block, f):
        # startからblockを経由せず行ける範囲のnode数
        s = 1
        for nn in self.paths[start]:
            if nn != f and nn != block:
                s += self.region(nn, block, start)
        return s


def main():
    N = int(input())
    graph = Graph(N)
    for i in range(N-1):
        n1, n2 = map(int, input().split())
        graph.path(n1, n2)
    path = graph.dfs(1, None)
    l = len(path)
    fb = path[l // 2]
    sb = path[l // 2 - 1]
    fr = graph.region(1, sb, None)
    sr = graph.region(N, fb, None)
    # print(fr)
    # print(sr)
    if fr > sr:
        print("Fennec")
    else:
        print("Snuke")


main()
