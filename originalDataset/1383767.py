import sys

# sys.stdin = open('d1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_str_list():
    return input().split()


def read_int():
    return int(input())


def read_str():
    return input()


def solve():
    M = 10
    n, ma, mb = read_int_list()
    p = [read_int_list() for i in range(n)]
    min_c = {(0, 0, 0): 0}

    for i in range(1, n + 1):
        a, b, c = p[i - 1]
        for u in range(0, M * (i - 1) + 1):
            for v in range(0, M * (i - 1) + 1):
                if (i - 1, u, v) in min_c:
                    cost = min_c[(i - 1, u, v)]
                    cc = cost + c
                    uu = u + a
                    vv = v + b
                    if (i, uu, vv) not in min_c:
                        min_c[(i, uu, vv)] = cc
                    if cc < min_c[(i, uu, vv)]:
                        min_c[(i, uu, vv)] = cc
                        
                    cc = cost
                    uu = u
                    vv = v
                    if (i, uu, vv) not in min_c:
                        min_c[(i, uu, vv)] = cc
                    if cc < min_c[(i, uu, vv)]:
                        min_c[(i, uu, vv)] = cc

    inf = 10 ** 20
    res = inf
    for u in range(0, M * n + 1):
        for v in range(0, M * n + 1):
            if u == 0 and v == 0:
                continue
            if u * mb == v * ma:
                if (n, u, v) in min_c:
                    cost = min_c[(n, u, v)]
                    if cost < res:
                        res = cost
    if res == inf:
        res = -1
    return res


def main():
    res = solve()
    print(res)


main()
