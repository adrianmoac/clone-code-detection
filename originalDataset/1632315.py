# -*- coding: utf-8 -*-
"""
http://abc062.contest.atcoder.jp/tasks/arc074_a

"""
import sys
from sys import stdin
from math import ceil
input = stdin.readline


def main(args):
    H, W = map(int, input().split())

    p1 = -1
    p2 = -1
    p3 = -1
    min_diff = H * W

    for i in range(1, (H//2)+1):
        p1 = i * W              #  横に割る
        reH = H - i
        # 残りを横に割った場合
        p2 = ceil(reH / 2) * W
        p3 = (H * W) - p1 - p2
        diff = max(p1, p2, p3) - min(p1, p2, p3)
        if diff < min_diff:
            min_diff = diff

        # 残りを縦に割った場合
        p2 = ceil(W / 2) * reH
        p3 = (H * W) - p1 - p2
        diff = max(p1, p2, p3) - min(p1, p2, p3)
        if diff < min_diff:
            min_diff = diff

    # HとWを入れ替えて同じ計算
    temp = H
    H = W
    W = temp
    for i in range(1, (H//2)+1):
        p1 = i * W              #  横に割る
        reH = H - i
        # 残りを横に割った場合
        p2 = ceil(reH / 2) * W
        p3 = (H * W) - p1 - p2
        diff = max(p1, p2, p3) - min(p1, p2, p3)
        if diff < min_diff:
            min_diff = diff

        # 残りを縦に割った場合
        p2 = ceil(W / 2) * reH
        p3 = (H * W) - p1 - p2
        diff = max(p1, p2, p3) - min(p1, p2, p3)
        if diff < min_diff:
            min_diff = diff

    print(min_diff)

if __name__ == '__main__':
    main(sys.argv[1:])