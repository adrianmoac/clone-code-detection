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
    H, W = ILI()
    return (H, W)

def solve(H, W):
    ans = INF
    
    if H % 3 == 0 or W % 3 == 0:
        return 0
    else:
        ans = min(ans, H, W)

    if W % 2 == 0:
        for h in range(1, H):
            num_1 = h * W
            num_2 = (H - h) * W // 2
            ans = min(ans, abs(num_1 - num_2))
    else:
        for h in range(1, H):
            num_1 = h * W
            num_2 = (H - h) * (W // 2)
            num_3 = (H - h) * (W // 2 + 1)
            nums = sorted([num_1, num_2, num_3])
            ans = min(ans, (nums[2] - nums[0]))

    if H % 2 == 0:
        for w in range(1, W):
            num_1 = w * H
            num_2 = (W - w) * H // 2
            ans = min(ans, abs(num_1 - num_2))
    else:
        for w in range(1, W):
            num_1 = w * H
            num_2 = (W - w) * (H // 2)
            num_3 = (W - w) * (H // 2 + 1)
            nums = sorted([num_1, num_2, num_3])
            ans = min(ans, (nums[2] - nums[0]))
    
    return ans


def main():
    params = read()
    print(solve(*params))


if __name__ == "__main__":
    main()
