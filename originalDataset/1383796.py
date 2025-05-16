import sys
from collections import defaultdict

# sys.stdin = open('d1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_str_list():
    return input().split()


def read_int():
    return int(input())


def read_str():
    return input()


M = 10
inf = 10 ** 20


def solve():
    n, ma, mb = read_int_list()
    p = [read_int_list() for i in range(n)]
    min_c = defaultdict(lambda: inf)
    min_c[(0, 0)] = 0

    for i, (a, b, c) in enumerate(p):
        for u in range(M * i, -1, -1):
            for v in range(M * i, -1, -1):
                if (u, v) in min_c:
                    cost = min_c[(u, v)]
                    if cost + c < min_c[((u + a), (v + b))]:
                        min_c[((u + a), (v + b))] = cost + c

    res = inf
    for u in range(0, M * n + 1):
        for v in range(0, M * n + 1):
            if u == 0 and v == 0:
                continue
            if u * mb == v * ma:
                if (u, v) in min_c:
                    cost = min_c[(u, v)]
                    if cost < res:
                        res = cost
    if res == inf:
        res = -1
    return res


def main():
    res = solve()
    print(res)


main()
