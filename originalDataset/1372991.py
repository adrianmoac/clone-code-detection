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


def solve(n, r):
    for a0 in range(2):
        for a1 in range(2):
            a = [a0, a1] + [-1] * (n - 2)
            for i in range(2, n):
                if r[i - 1] == 'o':
                    t = a[i - 2]
                else:
                    t = 1 - a[i - 2]
                if a[i - 1] == 1:
                    t = 1 - t
                a[i] = t

            ok = True
            for i in range(-1, n - 1):
                if a[i - 1] != a[i + 1]:
                    s = 1
                else:
                    s = 0
                if a[i] == 1:
                    s = 1 - s
                if s == 1:
                    expected = 'x'
                else:
                    expected = 'o'
                ok &= r[i] == expected
            if ok:
                l = map(lambda j: 'SW'[j], a)
                res = ''.join(l)
                return res
    return -1


def main():
    n = read_int()
    r = read_str()
    res = solve(n, r)
    print(res)


main()
