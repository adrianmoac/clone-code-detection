# coding: utf-8
import array, bisect, collections, copy, heapq, itertools, math, random, re, string, sys, time

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
MOD = 10 ** 9 + 7


def II(): return int(input())
def ILI(): return list(map(int, input().split()))
def IAI(LINE): return [ILI() for __ in range(LINE)]
def IDI(): return {key: value for key, value in ILI()}


def read():
    N = II()
    a = ILI()
    return (N, a)


def solve(N, a):
    count = [0] * 9
    for ele in a:
        if 1 <= ele <= 399:
            count[0] = 1
        elif 400 <= ele <= 799:
            count[1] = 1
        elif 800 <= ele <= 1199:
            count[2] = 1
        elif 1200 <= ele <= 1599:
            count[3] = 1
        elif 1600 <= ele <= 1999:
            count[4] = 1
        elif 2000 <= ele <= 2399:
            count[5] = 1
        elif 2400 <= ele <= 2799:
            count[6] = 1
        elif 2800 <= ele <= 3199:
            count[7] = 1
        elif ele >= 3200:
            count[8] += 1

    num_else = sum(count[0: 8])
    ans_max = sum(count)
    if num_else == 0:
        ans_min = 1
    else:
        ans_min = num_else
    
    ans = (ans_min, ans_max)
    return ans


def main():
    params = read()
    ans = solve(*params)
    print("{} {}".format(ans[0], ans[1]))


if __name__ == "__main__":
    main()
