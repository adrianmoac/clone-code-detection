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


solution = {}
choice = {}


def solve(x, y):
    if (x, y) in solution:
        return solution[(x, y)]
    for j in range(2, x + 1, 2):
        i = j // 2
        if not solve(x - 2 * i, y + i):
            res = True
            solution[(x, y)] = res
            choice[x, y] = x - 2 * i, y + i
            return res
    for j in range(2, y + 1, 2):
        i = j // 2
        if not solve(x + i, y - 2 * i):
            res = True
            solution[(x, y)] = res
            choice[x, y] = x + i, y - 2 * i
            return res
    res = False
    solution[(x, y)] = res
    return res


def solve2(x, y):
    return abs(x - y) >= 2


def test(N):
    for x in range(N):
        for y in range(N):
            if solve(x, y):
                print(x, y, '     ', choice[x, y])


def main():
    x, y = read_int_list()
    res = solve2(x, y)
    if res:
        print('Alice')
    else:
        print('Brown')


# test(10)
main()
