from collections import defaultdict
from itertools import product, groupby
from math import pi
from collections import deque
from bisect import bisect, bisect_left, bisect_right
INF = 10 ** 10


def func1(d):
    m = dict()
    m["S"] = (168.75, 191.25)
    m["NNE"] = (11.25, 33.75)
    m["SSW"] = (191.25, 213.75)
    m["NE"] = (33.75, 56.25)
    m["SW"] = (213.75, 236.25)
    m["ENE"] = (56.25, 78.75)
    m["WSW"] = (236.25, 258.75)
    m["E"] = (78.75, 101.25)
    m["W"] = (258.75, 281.25)
    m["ESE"] = (101.25, 123.75)
    m["WNW"] = (281.25, 303.75)
    m["SE"] = (123.75, 146.25)
    m["NW"] = (303.75, 326.25)
    m["SSE"] = (146.25, 168.75)
    m["NNW"] = (326.25, 348.75)

    for a, b in m.items():
        if b[0] <= d / 10 <= b[1]:
            return a
    return "N"


def func2(d):
    m = dict()
    m[0] = (0.0, 0.2)
    m[5] = (8.0, 10.7)
    m[10] = (24.5, 28.4)
    m[1] = (0.3, 1.5)
    m[6] = (10.8, 13.8)
    m[11] = (28.5, 32.6)
    m[2] = (1.6, 3.3)
    m[7] = (13.9, 17.1)
    m[12] = (32.7, 12000)
    m[3] = (3.4, 5.4)
    m[8] = (17.2, 20.7)
    m[4] = (5.5, 7.9)
    m[9] = (20.8, 24.4)

    for a, b in m.items():
        if b[0] <= round(d / 60 + 0.001, 1) <= b[1]:
            return a
    return 0


def main():
    Deg, Dis = map(int, input().split())

    a = func1(Deg)
    b = func2(Dis)
    print("C" if b == 0 else a, b)


if __name__ == '__main__':
    main()
