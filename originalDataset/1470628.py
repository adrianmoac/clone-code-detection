import sys

# sys.stdin = open('e1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_int():
    return int(input())


def read_str_list():
    return input().split()


def read_str():
    return input()


def ceil_frac(a, b):
    return (a + b - 1) // b


def solve():
    n = read_int()
    a = read_int_list()
    s = sum(a)
    res = 0
    x = s - n * n
    if x > 0:
        res += x
        for j in range(n):
            a[j] += x
        l = 0
        r = 10 ** 20
        while r - l > 1:
            m = (l + r) // 2
            decrements = 0
            for j in range(n):
                if a[j] >= m:
                    decrements += ceil_frac(a[j] - m, n + 1)
            possible = decrements <= x
            if possible:
                r = m
            else:
                l = m
        t = 0
        for j in range(n):
            if a[j] >= r:
                u = ceil_frac(a[j] - r, n + 1)
                a[j] -= u * (n + 1)
                t += u
        for _ in range(x - t):
            j0 = 0
            for j in range(n):
                if a[j] > a[j0]:
                    j0 = j
            a[j0] -= n + 1
    while max(a) >= n:
        for j in range(n):
            a[j] += 1
        j0 = 0
        for j in range(n):
            if a[j] > a[j0]:
                j0 = j
        a[j0] -= n + 1
        res += 1
    return res


def main():
    res = solve()
    print(res)


if __name__ == '__main__':
    main()
