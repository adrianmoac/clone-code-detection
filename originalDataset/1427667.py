import sys
readline = sys.stdin.readline
from heapq import heappush, heappop
from collections import deque

N = int(readline())
edges = [[] for _ in [None]*N]
for _ in [None]*(N-1):
    a,b = map(int, readline().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)


def dijkstra(n, edges, start, stop):
    inf = float("inf")
    vertices = [(inf,None) for _ in [None]*n]
    vertices[start] = (0, None)
    q = [(0, start)]

    while q:
        cost, v = heappop(q)
        if vertices[v][0] < cost:
            continue

        for dest in edges[v]:
            newcost = cost + 1
            if vertices[dest][0] > newcost:
                vertices[dest] = (newcost, v)
                if not dest in stop:
                    heappush(q, (newcost, dest))
    return vertices

def hoge(start, stop):
    dq = deque()
    pop, append = dq.popleft, dq.append
    cnt = 0
    visited = [0]*N
    append(start)
    while dq:
        pos = pop()
        for v in edges[pos]:
            if visited[v] == 0 and v not in stop:
                append(v)
                visited[v] = 1
                cnt += 1
    return cnt

vs = dijkstra(N, edges, 0, {N-1})
path = []
ap = path.append
n = vs[N-1][1]
while n != 0:
    ap(n)
    n = vs[n][1]

import math
x = math.ceil(len(path)/2)
fen_s = set(path[-x:]+[0])
snuke_s = set(path[:-x]+[N-1])
fen = hoge(0, snuke_s)
snuke = hoge(N-1, fen_s)
#print(fen, snuke, path, fen_s, snuke_s)
print("Fennec" if fen > snuke else "Snuke")