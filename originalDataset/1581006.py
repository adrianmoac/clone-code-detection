# -*- coding: utf-8 -*-
import heapq
import math

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

tmp = input()
N, M, R = [int(a) for a in tmp.split()]
tmp = input()
mokutekis = [int(a) for a in tmp.split()]
Rs = []
for i in range(M):
    tmp = input()
    Rs.append([int(a) for a in tmp.split()])

roots = {}
for a, b, dist in Rs:
    roots[(a, b)], roots[(b, a)] = dist, dist

minimums = {}
for i in range(1, N+1):
    minimums[(i, i)] = 0
for m in mokutekis:
    tmp_mins = {}
    merged = [False for i in range(N+1)]
    merged[m] = True
    merged_num = 1
    now = m
    while merged_num < N:
        minimum = [None, None]
        for i in range(1, N+1):
            if merged[i]:
                continue
            if (now, i) not in roots:
                new_dist = 100000*200+1
            else:
                new_dist = minimums[(m, now)] + roots[(now, i)]
            if (m, i) not in tmp_mins or tmp_mins[(m, i)] > new_dist:
                tmp_mins[(m, i)] = new_dist
                tmp_mins[(i, m)] = new_dist
            if minimum[0] is None or minimum[1] > tmp_mins[(m, i)]:
                minimum = i, tmp_mins[(m, i)]
        minimums[(m, minimum[0])], minimums[(minimum[0], m)] = minimum[1], minimum[1]
        now = minimum[0]
        merged[now] = True
        merged_num += 1

d_min = None
for perm in permutations(range(len(mokutekis))):
    perm = list(perm)
    d = 0
    d_max = None
    for p1, p2 in zip(perm, perm[1:]+[perm[0]]):
        m1, m2 = mokutekis[p1], mokutekis[p2]
        now_d = minimums[(m1, m2)]
        if d_max is None or d_max < now_d:
            d_max = now_d
        d += now_d
    d -= now_d
    if d_min is None or d_min > d:
        d_min = d
print(d_min)
