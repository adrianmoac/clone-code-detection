#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import math
import itertools
import numpy as np
from collections import OrderedDict, deque
from bisect import bisect_left, bisect_right, insort_left, insort_right
sys.setrecursionlimit(10000)


class EndLoop(Exception):
    pass


def debug_print(L):
    for col in L:
        print(col)


def debug_print_joined(L):
    for col in L:
        print("".join(col))


def transpose_matrix(L):
    transposed = list(map(list, zip(*L)))
    return transposed


def solve():
    N, M = list(map(int, input().split(" ")))
    graph = [[0] * N for _ in range(N)]
    for _ in range(M):
        a, b = list(map(int, input().split(" ")))
        graph[a - 1][b - 1], graph[b - 1][a - 1] = 1, 1

    visited = [False for _ in range(N)]
    cnt = 0
    def dfs(v, G):
        visited[v] = True
        for v2 in range(N):
            if G[v][v2] == 1 and visited[v2] != True:
                dfs(v2, G)

    check = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if check[i][j] == True:
                pass
            elif graph[i][j] == 1 and check[i][j] == False:
                graph[i][j], graph[j][i] = 0, 0
                dfs(0, graph)
                if visited.count(False) == 0:
                    pass
                else:
                    cnt += 1
                graph[i][j], graph[j][i] = 1, 1
                visited = [False for _ in range(N)]
                check[i][j], check[j][i] = True, True

    print(cnt)
    

solve()